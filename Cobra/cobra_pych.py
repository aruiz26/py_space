# based of spiderRobot example

import pychrono.core as chrono
import pychrono.irrlicht as chronoirr


print("Load Cobra SW")

# Utility class to use ChLinkMotorRotationAngle given the markers from the CAD
class CobraRobotMotor(chrono.ChLinkMotorRotationAngle):
    def __init__(self):
        super().__init__()
        self.bodylist = []

    def Initialize(self, mark1, mark2):
        body1 = mark1.GetBody()
        body2 = mark2.GetBody()
        self.bodylist.append([body1, body2])
        frame = mark1.GetAbsFrame()
        super().Initialize(body1, body2, frame)

    def SetMotorFunction(self, rotfun):
        super().SetAngleFunction(rotfun)

# ---------------------------------------------------------------------
#
#  Create the simulation system and add items
#
 
mysystem = chrono.ChSystemNSC()
mysystem.SetCollisionSystemType(chrono.ChCollisionSystem.Type_BULLET)
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.05)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.005)

# Import model items from Solidworks and add to system 
parts = chrono.ImportSolidWorksSystem('cobra_assem_4_2.py')
 
for ib in parts:
    mysystem.Add(ib)
    print(ib)
    
# Retrieve objects from their name as saved from the SolidWorks interface
bbody    = mysystem.SearchBody('Assem6^cobra_assem_4_2-1')
bbody.SetFixed(False)
# FrontRight Asembly
b1arm = mysystem.SearchBody('arm_assembly-2')
b1hub = mysystem.SearchBody('hub_assem-1')
b1wheel = mysystem.SearchBody('wheel_grouser-1')











 
# ---------------------------------------------------------------------
#
#  Create an Irrlicht application to visualize the system
#

# Create the Irrlicht visualization
vis = chronoirr.ChVisualSystemIrrlicht()
vis.AttachSystem(mysystem)
vis.SetWindowSize(1280,720)
vis.SetWindowTitle('Cobra')
vis.Initialize()
vis.AddLogo(chrono.GetChronoDataFile('logo_pychrono_alpha.png'))
vis.AddSkyBox()
vis.AddCamera(chrono.ChVector3d(5, 5, -7.5), chrono.ChVector3d(-1.0, 0, -2.5))
vis.AddLightWithShadow(chrono.ChVector3d(10,20,10), chrono.ChVector3d(0,2.6,0), 50, 10, 40, 60, 512)


# ---------------------------------------------------------------------
#
#  Run the simulation
#

solver = chrono.ChSolverBB()
solver.SetMaxIterations(200)
solver.SetTolerance(1e-6)
mysystem.SetSolver(solver)

while(vis.Run()):
    vis.BeginScene()
    vis.Render()
    mysystem.DoStepDynamics(0.001)
    vis.EndScene()

print('Done')
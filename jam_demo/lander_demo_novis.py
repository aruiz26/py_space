# based of spiderRobot example SW_ex/demo_SW_spider_robot.py
# and pychrono_ex/scm__singlewheel.py


# =============================================================================
# This demo: Drops lander, exports kinematics data to 'output.csv'
# No Visualization is used
# =============================================================================


import pychrono.core as chrono
import pychrono.irrlicht as chronoirr
import pychrono.vehicle as veh
import math
import sys
import csv
import numpy as np



print("Loading Cobra SW...")

# ---------------------------------------------------------------------
#
#  Create the simulation system and add items
#
 

# mysystem = chrono.ChSystemNSC()
mysystem = chrono.ChSystemSMC()
mysystem.SetCollisionSystemType(chrono.ChCollisionSystem.Type_BULLET)
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.05)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.005)
mysystem.SetGravitationalAcceleration(chrono.ChVector3d(0,-9.81,0))

# Import model items from Solidworks and add to system 
parts = chrono.ImportSolidWorksSystem('./lander2.py')


for ib in parts:
    mysystem.Add(ib)
    # print(ib.GetName())
    
# Retrieve objects from their name as saved from the SolidWorks interface
bbody    = mysystem.SearchBody('lander2-1')
bbody.SetFixed(False)

# bbody.SetRot(chrono.ChQuaterniond(1, 1, 0, 0)) # quat(mag, xdir, ydir, zdir)
bbody.SetRot(chrono.QuatFromAngleX(3.14/2)) # quat(mag, xdir, ydir, zdir)
bbody.SetPos(chrono.ChVector3d(0.5,1.5,0) )

# Create a floor
mymat = chrono.ChContactMaterialSMC()
mymat.SetRestitution(0.0)

# mfloor = chrono.ChBodyEasyBox(.2, 0.05, 1, 1000, True, True, mymat)
# mfloor.SetFixed(True)
# mfloor.SetPos(chrono.ChVector3d(0,-0.2,0))
# mfloor.GetVisualShape(0).SetColor(chrono.ChColor(0.4, 0.4, 0.4))
# mysystem.Add(mfloor)

terrain = veh.SCMTerrain(mysystem)
terrain.SetPlane(chrono.ChCoordsysd(chrono.ChVector3d(0,0,0), chrono.QuatFromAngleX(-math.pi/2)))
terrain.Initialize(4.0, 4.0, 0.04)


terrain.SetSoilParameters(0.2e6,  # Bekker Kphi
                           0,      # Bekker Kc
                           1.1,    # Bekker n exponent
                           0,      # Mohr cohesive limit (Pa)
                           30,     # Mohr friction limit (degrees)
                           0.01,   # Janosi shear coefficient (m)
                           4e7,    # Elastic stiffness (Pa/m), before plastic yield, must be > Kphi
                           3e4     # Damping (Pa s/m), proportional to negative vertical speed (optional)
)

# Set terrain visualization mode
terrain.SetPlotType(veh.SCMTerrain.PLOT_PRESSURE, 0, 30000.2)

 
# ---------------------------------------------------------------------
#
#  Create an Irrlicht application to visualize the system
#

# Create the Irrlicht visualization
# =============================================================================
# vis = chronoirr.ChVisualSystemIrrlicht()
# vis.AttachSystem(mysystem)
# vis.SetWindowSize(1280,720)
# vis.SetWindowTitle('Cobra')
# vis.Initialize()
# vis.AddLogo(chrono.GetChronoDataFile('logo_pychrono_alpha.png'))
# vis.AddSkyBox()
# vis.AddCamera(chrono.ChVector3d(2, 2, -2), chrono.ChVector3d(0.0, 0, 0.0))
# vis.AddLightWithShadow(chrono.ChVector3d(10,20,10), chrono.ChVector3d(0,2.6,0), 50, 10, 40, 60, 512)
# =============================================================================


# ---------------------------------------------------------------------
#
#  Run the simulation
#

solver = chrono.ChSolverBB()
solver.SetMaxIterations(200)
solver.SetTolerance(1e-6)
mysystem.SetSolver(solver)


# sys.exit()

# Data export
csv_filename = 'output.csv'
# Create a new CSV file and write a header (optional)
headers = ['t', 'x', 'y', 'z', 'dx', 'dy', 'dz', 'ddx', 'ddy', 'ddz']
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # header = [f'val{i+1}' for i in range(9)]
    writer.writerow(headers)

dt = 1/100000
T = 1
print(dt)
while(True):
    # vis.BeginScene()
    # vis.Render()
    mysystem.DoStepDynamics(dt)
    
    t = mysystem.GetChTime()
    pos = bbody.GetPos()
    dtpos = bbody.GetPosDt()
    ddtpos = bbody.GetPosDt2()
    
    # var1 = np.random.rand(3)  # 1x3 array
    # var2 = np.random.rand(3)
    # var3 = np.random.rand(3)
    
    var1 = np.array([pos.x, pos.y, pos.z])
    var2 = np.array([dtpos.x, dtpos.y, dtpos.z])
    var3 = np.array([ddtpos.x, ddtpos.y, ddtpos.z])

    combined = np.concatenate(([t], var1, var2, var3))  # 1x9 array

    # Append the data row to the CSV
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(combined)
    
    if(mysystem.GetChTime()>T):
        sys.exit()

print('Done')




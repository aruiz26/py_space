import pychrono.core as chrono
import pychrono.vehicle as veh
import pychrono.irrlicht as chronoirr


# Create Chrono system
sys = chrono.ChSystemSMC()
sys.SetCollisionSystemType(chrono.ChCollisionSystem.Type_BULLET)
sys.SetGravitationalAcceleration(chrono.ChVector3d(0, 0, -9.81))
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.0025)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.0025)


chrono.SetChronoDataPath(chrono.GetChronoDataPath())


# Import your exported assembly
exported_items = []
from cobra_assem_4_2 import exported_items  # replace with your exported file name
for item in exported_items:
    sys.Add(item)


# Optional: name and identify wheels/steering links
FL_wheel = sys.SearchBody("wheel_grouser-1")

RL_wheel = sys.SearchBody("wheel_grouser-3")
# RL_wheel = sys.SearchBody("wheel_grouser-3")
# RL_wheel = sys.SearchBody("wheel_grouser-3")
FL_arm = sys.SearchBody("arm_assembly-1")
RL_arm = sys.SearchBody("hub_assem-3")
steering_link_FL = sys.SearchLink("Concentric6")

print(FL_wheel)
print(steering_link_FL)

# Create a floor
mymat = chrono.ChContactMaterialSMC()
mymat.SetRestitution(0.0)


mfloor = chrono.ChBodyEasyBox(2, 0.01, 1, 1000, True, True, mymat)
mfloor.SetFixed(True)
mfloor.SetPos(chrono.ChVector3d(0,-0.15,0))
mfloor.GetVisualShape(0).SetColor(chrono.ChColor(0.4, 0.4, 0.4))
sys.Add(mfloor)


# Create visualization
vis = chronoirr.ChVisualSystemIrrlicht()
vis.AttachSystem(sys)
vis.SetWindowSize(1024,768)
vis.SetWindowTitle('Vehicle SCM Simulation')
vis.Initialize()
vis.AddSkyBox()
vis.AddCamera(chrono.ChVector3d(0, 1, 1))
vis.AddTypicalLights()


# Define motion functions 
period = 1/4
mfunc   = chrono.ChFunctionSine(10, 40,  2)
# mfunc   = chrono.ChFunctionConst(5)
mfunc2   = chrono.ChFunctionConst(-15)
print(mfunc)

# print(FL_wheel.getPos)


# Apply torques/steering
motor_torque = 5.0
steering_angle = 0.3  # radians

# Motor set ups
motorFL = chrono.ChLinkMotorRotationTorque()
motorFL.Initialize(FL_wheel, FL_arm, chrono.ChFramed())
# motorFL.SetMotorFunction(mfunc)
motorFL.SetTorqueFunction(mfunc)
sys.Add(motorFL)

# motorRL = chrono.ChLinkMotorRotationTorque()
# motorRL.Initialize(RL_wheel, RL_arm, chrono.ChFramed())
# motorRL.SetTorqueFunction(mfunc2)
# sys.Add(motorRL)




# Simulation loop
step_size = 1e-3
while vis.Run():
    # apply_controls()
    #torque_fun = chrono.ChFunction_Const(5)  # constant torque of 5 Nm
    # motor.SetTorqueFunction(chrono.ChFunction_(5))

    vis.BeginScene()
    vis.Render()
    vis.EndScene()
    sys.DoStepDynamics(step_size)


print('Hello')
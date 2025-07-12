# based of spiderRobot example SW_ex/demo_SW_spider_robot.py
# and pychrono_ex/scm__singlewheel.py
import pychrono.core as chrono
import pychrono.irrlicht as chronoirr
import pychrono.vehicle as veh
import math
import sys
import time
import csv
import numpy as np

print("Loading Cobra SW...")

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

def control(speed=0, steering=0):
    temp_fun1 = chrono.ChFunctionConst(steering)
    temp_fun2 = chrono.ChFunctionConst(-steering)
    
    temp_fun3 = chrono.ChFunctionConst(speed)
    temp_fun4 = chrono.ChFunctionConst(-speed)
    
    motorFR_steer.SetMotorFunction(temp_fun1)
    motorRR_steer.SetMotorFunction(temp_fun2)
    motorFL_steer.SetMotorFunction(temp_fun1)
    motorRL_steer.SetMotorFunction(temp_fun2)
    # Drive actuation
    motorFR_drive.SetMotorFunction(temp_fun3)
    motorRR_drive.SetMotorFunction(temp_fun4)
    motorFL_drive.SetMotorFunction(temp_fun3)
    motorRL_drive.SetMotorFunction(temp_fun4)
    
    
# ---------------------------------------------------------------------
#
#  Create the simulation system and add items
#

SWexportfilename = './cobra2.py'
chassisPartName = 'Assem6^cobra_4_1_pyMarkers-1'

# mysystem = chrono.ChSystemNSC()
mysystem = chrono.ChSystemSMC()
mysystem.SetGravitationalAcceleration(chrono.ChVector3d(0, -9.81, 0))
mysystem.SetCollisionSystemType(chrono.ChCollisionSystem.Type_BULLET)
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.05)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.005)

# Import model items from Solidworks and add to system 
# A list of minor differences of SW export
######### cobra_4.py - does not include collision shapes
######### cobra_4_2.py - includes manual addition of collison shape
parts = chrono.ImportSolidWorksSystem(SWexportfilename)

for item in parts:
    mysystem.Add(item)
    # print(item.GetName())
    
# Retrieve objects from their name as saved from the SolidWorks interface
bbody    = mysystem.SearchBody(chassisPartName)
bbody.SetFixed(False)

# Front Right Assembly
b1arm = mysystem.SearchBody('arm_assembly-2')
b1hub = mysystem.SearchBody('hub_assem-1')
b1wheel = mysystem.SearchBody('wheel_grouser-1')
# m1_steer_arm = b1arm.SearchMarker('steer_arm_1')
# m1_steer_hub = mysystem.SearchMarker('steer_hub_1')
# m1_drive_hub = mysystem.SearchMarker('drive_hub_1')
# m1_drive_wheel = mysystem.SearchMarker('drive_wheel_1')
# Rear Right Assembly
b2arm = mysystem.SearchBody('arm_assembly-3')
b2hub = mysystem.SearchBody('hub_assem-4')
b2wheel = mysystem.SearchBody('wheel_grouser-3')
# m2_steer_arm = mysystem.SearchMarker('steer_arm_2')
# m2_steer_hub = mysystem.SearchMarker('steer_hub_2')
# m2_drive_hub = mysystem.SearchMarker('drive_hub_2')
# m2_drive_wheel = mysystem.SearchMarker('drive_wheel_2')
# Front Left Assembly
b3arm = mysystem.SearchBody('arm_assembly-1')
b3hub = mysystem.SearchBody('hub_assem-3')
b3wheel = mysystem.SearchBody('wheel_grouser-2')
# m3_steer_arm = mysystem.SearchMarker('steer_arm_3')
# m3_steer_hub = mysystem.SearchMarker('steer_hub_3')
# m3_drive_hub = mysystem.SearchMarker('drive_hub_3')
# m3_drive_wheel = mysystem.SearchMarker('drive_wheel_3')
# Rear Left Assembly
b4arm = mysystem.SearchBody('arm_assembly-4')
b4hub = mysystem.SearchBody('hub_assem-2')
b4wheel = mysystem.SearchBody('wheel_grouser-4')
# m4_steer_arm = mysystem.SearchMarker('steer_arm_4')
# m4_steer_hub = mysystem.SearchMarker('steer_hub_4')
# m4_drive_hub = mysystem.SearchMarker('drive_hub_4')
# m4_drive_wheel = mysystem.SearchMarker('drive_wheel_4')




# IF WHEEL COLLISIONS ARE ENABLED
b1wheel.GetCollisionModel().SetFamily(1)
b3wheel.GetCollisionModel().SetFamily(2)
b2wheel.GetCollisionModel().SetFamily(3)
b4wheel.GetCollisionModel().SetFamily(4)

b1wheel.GetCollisionModel().DisallowCollisionsWith(2)
b1wheel.GetCollisionModel().DisallowCollisionsWith(3)
b1wheel.GetCollisionModel().DisallowCollisionsWith(4)

b3wheel.GetCollisionModel().DisallowCollisionsWith(3)
b3wheel.GetCollisionModel().DisallowCollisionsWith(4)

b2wheel.GetCollisionModel().DisallowCollisionsWith(4)


# STEERING ACTUATION SETUP
motorFR_steer = chrono.ChLinkMotorRotationAngle()
jointFR_steer = mysystem.SearchLink('Concentric5')
frameFR_steer = jointFR_steer.GetVisualModelFrame()
motorFR_steer.Initialize(b1arm, b1hub, frameFR_steer)
mysystem.Add(motorFR_steer)

motorRR_steer = chrono.ChLinkMotorRotationAngle()
jointRR_steer = mysystem.SearchLink('Concentric7')
frameRR_steer = jointRR_steer.GetVisualModelFrame()
motorRR_steer.Initialize(b2arm, b2hub, frameRR_steer)
mysystem.Add(motorRR_steer)

motorFL_steer = chrono.ChLinkMotorRotationAngle()
jointFL_steer = mysystem.SearchLink('Concentric8')
frameFL_steer = jointFL_steer.GetVisualModelFrame()
motorFL_steer.Initialize(b3arm, b3hub, frameFL_steer)
mysystem.Add(motorFL_steer)

motorRL_steer = chrono.ChLinkMotorRotationAngle()
jointRL_steer = mysystem.SearchLink('Concentric9')
frameRL_steer = jointRL_steer.GetVisualModelFrame()
motorRL_steer.Initialize(b4arm, b4hub, frameRL_steer)
mysystem.Add(motorRL_steer)

# DRIVE ACTUATION SETUP
motorFR_drive = chrono.ChLinkMotorRotationSpeed()
jointFR_drive = mysystem.SearchLink('Concentric6')
frameFR_drive = jointFR_drive.GetVisualModelFrame()
motorFR_drive.Initialize(b1hub, b1wheel, frameFR_drive)
mysystem.Add(motorFR_drive)

motorRR_drive = chrono.ChLinkMotorRotationSpeed()
jointRR_drive = mysystem.SearchLink('Concentric11')
frameRR_drive = jointRR_drive.GetVisualModelFrame()
motorRR_drive.Initialize(b2hub, b2wheel, frameRR_drive)
mysystem.Add(motorRR_drive)

motorFL_drive = chrono.ChLinkMotorRotationSpeed()
jointFL_drive = mysystem.SearchLink('Concentric12')
frameFL_drive = jointFL_drive.GetVisualModelFrame()
motorFL_drive.Initialize(b3hub, b3wheel, frameFL_drive)
mysystem.Add(motorFL_drive)

motorRL_drive = chrono.ChLinkMotorRotationSpeed()
jointRL_drive = mysystem.SearchLink('Concentric10')
frameRL_drive = jointRL_drive.GetVisualModelFrame()
motorRL_drive.Initialize(b4hub, b4wheel, frameRL_drive)
mysystem.Add(motorRL_drive)

print(dir( b1wheel.GetAppliedTorque() ))

appT = [getattr(wheel.getAppliedTorque(), comp) for wheel in [b1wheel, b2wheel, b3wheel, b4wheel], 
        for comp in ['x', 'y', 'z']]
print(appT)

sys.exit()

# sys.exit()
# Create a floor
mymat = chrono.ChContactMaterialSMC()
mymat.SetRestitution(0.0)

# mfloor = chrono.ChBodyEasyBox(.2, 0.05, 1, 1000, True, True, mymat)
# mfloor.SetFixed(True)
# mfloor.SetPos(chrono.ChVector3d(0,-0.2,0))
# mfloor.GetVisualShape(0).SetColor(chrono.ChColor(0.4, 0.4, 0.4))
# mysystem.Add(mfloor)

terrain = veh.SCMTerrain(mysystem)

terrain.SetPlane(chrono.ChCoordsysd(chrono.ChVector3d(4,-0.2,0.4), chrono.QuatFromAngleX(-math.pi/2)))
# terrain.Initialize(12.0, 5.0, 0.01)
terrain.Initialize(8.0, 2.5, 0.01*(5))


terrain.SetSoilParameters(0.2e8,  # Bekker Kphi
                           0,      # Bekker Kc
                           1.1,    # Bekker n exponent
                           0,      # Mohr cohesive limit (Pa)
                           30,     # Mohr friction limit (degrees)
                           0.01,   # Janosi shear coefficient (m)
                           4e7,    # Elastic stiffness (Pa/m), before plastic yield, must be > Kphi
                           3e4     # Damping (Pa s/m), proportional to negative vertical speed (optional)
)

# enabling moving patches
# terrain.AddMovingPatch(b1wheel, chrono.ChVector3d(0,0,0), chrono.ChVector3d(0.5, 1, 1))
# terrain.AddMovingPatch(b3wheel, chrono.ChVector3d(0,0,0), chrono.ChVector3d(0.5, 1, 1))

# Set terrain visualization mode
terrain.SetPlotType(veh.SCMTerrain.PLOT_PRESSURE, 0, 30000.2)

 
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
vis.AddCamera(chrono.ChVector3d(2, 2, -2), chrono.ChVector3d(0.0, 0, 0.0))
vis.AddLightWithShadow(chrono.ChVector3d(10,20,10), chrono.ChVector3d(0,2.6,0), 50, 10, 40, 60, 512)


# ---------------------------------------------------------------------
#
#  Run the simulation
#
solver = chrono.ChSolverBB()
solver.SetMaxIterations(200)
solver.SetTolerance(1e-6)
mysystem.SetSolver(solver)

# sim time counter variables
last_displayed_time = -1  # Initialize before the loop
start_time = time.perf_counter() # Counter for real time
tf1, tf2 = 0, 0 # recalls last time
dt1, dt2 = 0, 0
rtf = 0
t = 0



# Data export
csv_filename = 'output_04_straight21s_60rpm.csv'
# Create a new CSV file and write a header (optional)
headers = ['t', 'x', 'y', 'z', 'dx', 'dy', 'dz', 'ddx', 'ddy', 'ddz', 'speed_set', 'steering_set',
           'q0', 'q1', 'q2', 'q3']
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # header = [f'val{i+1}' for i in range(9)]
    writer.writerow(headers)

while(vis.Run() ):
# while (True):
    vis.BeginScene()
    vis.Render()
        
    # Get current simulation time, rounded to 2 decimals
    current_time = mysystem.GetChTime()
    dt1 = current_time - tf1
    tf1 = current_time
    rounded_time = round(current_time, 2)
    # Real elapsed time
    elapsed_t = time.perf_counter() - start_time
    dt2 = elapsed_t - tf2
    tf2 = elapsed_t
    if current_time>0:
        rtf = dt2/dt1
    
    # Only display if it changed, to 2 decimal points (eg. 0.01, 0.02,...)
    if rounded_time != last_displayed_time:
        #print(f"Simulation time: {rounded_time:.2f} s", f"Real time: {elapsed_t::2f} s")
        print(f"Simulation time: {rounded_time:.2f} s, Real time: {elapsed_t:.2f} s, RTF: {rtf:.2f}")
        last_displayed_time = rounded_time
        
        
        x1 = b1wheel.GetAppliedTorque()
        print(x1)
    
    t = current_time
    if t<1:
        speed_t = 0
        steering_t = 0
    else:
        speed_t = 60*(1/60)*(2*math.pi) # RPM*(1min/60s)*(2pirad/1rev)
        steering_t = 30*(math.pi/180)*math.sin( (t - 1)*(2*math.pi)*(1/4)) # 30deg(pi/180deg), 1rev every 4 seconds
        steering_t = 0
    
 

    control(speed = speed_t, steering = steering_t)
   
    mysystem.DoStepDynamics(0.001)
    
    # data export ready
    pos = bbody.GetPos()
    dtpos = bbody.GetPosDt()
    ddtpos = bbody.GetPosDt2()
    qrot = bbody.GetRot()
    wheels_cont_tor = np.array([b1wheel.GetContactTorque(), ])
    
    var1 = np.array([pos.x, pos.y, pos.z])
    var2 = np.array([dtpos.x, dtpos.y, dtpos.z])
    var3 = np.array([ddtpos.x, ddtpos.y, ddtpos.z])
    var4 = np.array([qrot.e0, qrot.e1, qrot.e2, qrot.e3])
    
    combined = np.concatenate(([t], var1, var2, var3, [speed_t], [steering_t], var4, np.array(x1)))  # 1x9 array

    # Append the data row to the CSV
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(combined)
    
    vis.EndScene()
    
    if t>21:
        input("Pause as t=9s. Press Enter to END")
        sys.exit()
    

print('Done')
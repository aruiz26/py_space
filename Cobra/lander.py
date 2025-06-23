# PyChrono model automatically generated using Chrono::SolidWorks add-in
# Assembly: C:\Users\alexi\Desktop\SW\lander.SLDASM


import pychrono as chrono 
import builtins 

# Some global settings 
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'lander_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0 = chrono.ChBodyAuxRef()
body_0.SetName('SLDW_GROUND')
body_0.SetFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('lander-2')
body_1.SetPos(chrono.ChVector3d(0.0705847248419493,0.295322093743468,0.408784346445812))
body_1.SetRot(chrono.ChQuaterniond(0.707106781186541,0.707106781186554,0,0))
body_1.SetMass(5.90093826070148)
body_1.SetInertiaXX(chrono.ChVector3d(0.122011094006681,0.0876410484879871,0.0987019365245219))
body_1.SetInertiaXY(chrono.ChVector3d(-4.36798959568082e-08,-3.06898866825394e-08,2.44793908703231e-08))
body_1.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(5.77240685410432e-08,4.89163302585042e-08,-0.0513572622531015),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Collision Model

body_1.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_1 = chrono.ChContactMaterialNSC()

# Triangle mesh collision shape 
body_1_1_collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_1_1_collision.obj', False, True) 
mr = chrono.ChMatrix33d()
mr[0,0]=1; mr[1,0]=0; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
mr[0,2]=0; mr[1,2]=0; mr[2,2]=1 
body_1_1_collision_mesh.Transform(chrono.ChVector3d(0, 0, 0), mr) 
collshape = chrono.ChCollisionShapeTriangleMesh(mat_1,body_1_1_collision_mesh,False,False,sphereswept_r)
body_1.GetCollisionModel().AddShape(collshape)
body_1.EnableCollision(True)

exported_items.append(body_1)




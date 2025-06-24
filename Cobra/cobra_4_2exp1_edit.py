# PyChrono model automatically generated using Chrono::SolidWorks add-in
# Assembly: C:\Users\alexi\Box\0MyFiles_BOX\03_sbel_cad\Cobra_CAD\cobra_4_1_py.SLDASM


import pychrono as chrono 
import builtins 

# Some global settings 
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

# =============================================================================
# sphereswept_r = 0.01
# chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.03)
# chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.03)
# chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.02)
# =============================================================================

# Enable or disable wheel contact
ENABLE_wheel1_contact = True # FR - wheel_grouser-1
ENABLE_wheel2_contact = True # FL - wheel_grouser-2
ENABLE_wheel3_contact = True # RR - wheel_grouser-3
ENABLE_wheel4_contact = True # RL - wheel_grouser-4

shapes_dir = 'cobra_4_2exp1_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0 = chrono.ChBodyAuxRef()
body_0.SetName('SLDW_GROUND')
body_0.SetFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('wheel_grouser-1')
body_1.SetPos(chrono.ChVector3d(0.67919613249864,0.162900702624963,0.564258946844999))
body_1.SetRot(chrono.ChQuaterniond(0.51607057398506,0.580804059344094,0.418162284117186,-0.470614610332116))
body_1.SetMass(25.7732862791227)
body_1.SetInertiaXX(chrono.ChVector3d(0.198804848043728,0.331455610706199,0.194424903578368))
body_1.SetInertiaXY(chrono.ChVector3d(0.0296599053323516,-0.00351307165898384,-0.0164615648792474))
body_1.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0270700245615144,-0.000185466324721263,0.0154474354006911),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0290351109510424,-0.000185466335892559,0.0154474354087597), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_2_shape = chrono.ChVisualShapeModelFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_1.AddVisualShape(body_1_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.00253511095104253,-0.000185466335892559,0.0154474354087597), chrono.ChQuaterniond(0.669230211120907,0.228321975558784,-0.669230211120907,-0.228321975558784)))

if(ENABLE_wheel1_contact):
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
    body_1_1_collision_mesh.Transform(chrono.ChVector3d(-0.0290351109510424, -0.000185466335892559, 0.0154474354087597), mr) 
    collshape = chrono.ChCollisionShapeTriangleMesh(mat_1,body_1_1_collision_mesh,False,False,sphereswept_r)
    body_1.GetCollisionModel().AddShape(collshape)
    body_1.EnableCollision(True)

exported_items.append(body_1)



# Rigid body part
body_2 = chrono.ChBodyAuxRef()
body_2.SetName('Assem6^cobra_4_1_py-1')
body_2.SetPos(chrono.ChVector3d(0.357296158663475,-0.167031516408032,0))
body_2.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_2.SetMass(8.40829630556841)
body_2.SetInertiaXX(chrono.ChVector3d(0.300679202818509,0.139983722497611,0.378573662340627))
body_2.SetInertiaXY(chrono.ChVector3d(-0.0381026245199455,2.45385522116201e-06,8.96463617500081e-06))
body_2.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.156780185103172,0.514832406020355,0.253737426526277),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837842,0.654713829730607,0.366455907357322), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,-3.81260211858883E-16,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837841,0.654713829730607,0.141055907358348), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,3.8126021208526E-16,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612741,0.307876329730607,0.367553348962111), chrono.ChQuaterniond(0.707106781186548,-2.53822826583835E-16,-0.707106781186547,-2.53822826252613E-16)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612742,0.305113829730607,0.367553348962111), chrono.ChQuaterniond(-0.5,0.5,0.5,0.5)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612742,0.317813829730607,0.367553348962111), chrono.ChQuaterniond(-0.5,0.5,0.5,0.5)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.167497262836957,0.317813829730607,0.141055907357911), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.164734762836957,0.305113829730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186548,3.81260211858883E-16,0.707106781186547,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.177434762836957,0.307876329730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186548,3.81260211858883E-16,0.707106781186547,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612743,0.317813829730607,0.141055907358865), chrono.ChQuaterniond(0.5,0.499999999999999,0.5,-0.5)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612743,0.305113829730607,0.141055907358865), chrono.ChQuaterniond(0.707106781186547,-3.8126021208526E-16,0.707106781186548,3.4863055968421E-32)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612743,0.307876329730607,0.141055907358865), chrono.ChQuaterniond(0.707106781186547,-3.8126021208526E-16,0.707106781186548,3.4863055968421E-32)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.317813829730607,0.36645590735784), chrono.ChQuaterniond(0.5,0.499999999999999,-0.500000000000001,0.5)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.305113829730607,0.36645590735784), chrono.ChQuaterniond(0.707106781186547,-3.81260211858883E-16,-0.707106781186548,-7.62520423717767E-16)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.307876329730607,0.36645590735784), chrono.ChQuaterniond(0.707106781186547,-3.81260211858883E-16,-0.707106781186548,-7.62520423717767E-16)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.317813829730607,0.156518407360262), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,1.74315279842105E-32,1.93528837224682E-48)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.305113829730607,0.153755907360262), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.307876329730607,0.166455907360262), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371612741,0.654713829730607,0.366455907357323), chrono.ChQuaterniond(0.707106781186547,0.707106781186548,-3.81260211858883E-16,-3.4863055968421E-32)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617163,0.317813829730607,0.156518407360262), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,1.74315279842105E-32,1.93528837224682E-48)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617163,0.305113829730607,0.153755907360262), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617163,0.307876329730607,0.166455907360262), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762836078,0.654713829730607,0.366455907359236), chrono.ChQuaterniond(-0.5,-0.5,0.500000000000001,-0.5)))

# Visualization shape 
body_2_23_shape = chrono.ChVisualShapeModelFile() 
body_2_23_shape.SetFilename(shapes_dir +'body_2_23.obj') 
body_2.AddVisualShape(body_2_23_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762836078,0.343213829730607,0.328355907358351), chrono.ChQuaterniond(3.81260211858883E-16,-0.707106781186547,0.707106781186548,3.81260211858883E-16)))

# Visualization shape 
body_2_24_shape = chrono.ChVisualShapeModelFile() 
body_2_24_shape.SetFilename(shapes_dir +'body_2_24.obj') 
body_2.AddVisualShape(body_2_24_shape, chrono.ChFramed(chrono.ChVector3d(-0.0379652371644393,0.365438829731491,0.253755907358352), chrono.ChQuaterniond(-5.39183362404072E-16,1,7.75060634674567E-18,-6.52099496614874E-17)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762836079,0.654713829730607,0.141055907358352), chrono.ChQuaterniond(-0.5,-0.5,0.500000000000001,-0.5)))

# Visualization shape 
body_2_26_shape = chrono.ChVisualShapeModelFile() 
body_2_26_shape.SetFilename(shapes_dir +'body_2_26.obj') 
body_2.AddVisualShape(body_2_26_shape, chrono.ChFramed(chrono.ChVector3d(-0.0229652371644389,0.359088829731491,0.317255907358351), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.317813829730607,0.350993407358351), chrono.ChQuaterniond(0.707106781186548,-0.707106781186547,-1.9063010604263E-16,-5.71890317901514E-16)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.330513829730607,0.353755907358351), chrono.ChQuaterniond(-5.81233805195342E-16,1,-2.69591681202036E-16,5.39183362564145E-16)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.327751329730607,0.341055907358351), chrono.ChQuaterniond(-5.81233805195342E-16,1,-2.69591681202036E-16,5.39183362564145E-16)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283556,0.368613829731492,0.350993407358352), chrono.ChQuaterniond(-5.23184691419221E-16,1.30533127109691E-15,0.707106781186548,-0.707106781186547)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283556,0.355913829731492,0.353755907358351), chrono.ChQuaterniond(5.53061150371959E-16,1.30683382441082E-15,1,2.90599267418406E-16)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283556,0.358676329731492,0.341055907358352), chrono.ChQuaterniond(5.53061150371959E-16,1.30683382441082E-15,1,2.90599267418406E-16)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283556,0.358676329731492,0.166455907358351), chrono.ChQuaterniond(3.29143574404111E-14,7.71242404223993E-16,1,6.87057791361391E-16)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.355913829731492,0.153755907358351), chrono.ChQuaterniond(2.38487553120783E-14,-2.27580538441475E-14,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.368613829731492,0.156518407358351), chrono.ChQuaterniond(2.38487553120783E-14,-2.27580538441475E-14,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835541,0.327751329730622,0.166455907358351), chrono.ChQuaterniond(-4.49815360045584E-16,1,-3.31597768161896E-14,-2.05642184200826E-29)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835541,0.330513829730622,0.153755907358351), chrono.ChQuaterniond(0.707106781186547,0.707106781186548,-2.34475030493601E-14,-2.34475030493601E-14)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283554,0.317813829730622,0.156518407358351), chrono.ChQuaterniond(0.707106781186547,0.707106781186548,-2.34475030493601E-14,-2.34475030493601E-14)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.360263829731491,0.307095907358351), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.360263829731491,0.200415907358351), chrono.ChQuaterniond(-6.12323399573674E-17,-9.3664216290059E-25,1,6.70601807553831E-16)))

# Visualization shape 
body_2_41_shape = chrono.ChVisualShapeModelFile() 
body_2_41_shape.SetFilename(shapes_dir +'body_2_41.obj') 
body_2.AddVisualShape(body_2_41_shape, chrono.ChFramed(chrono.ChVector3d(0.327034762835561,0.368613829731491,0.253755907358351), chrono.ChQuaterniond(-2.55140024536113E-16,1.2612018732277E-16,0.707106781186548,-0.707106781186547)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616935,0.317813829730607,0.350993407356446), chrono.ChQuaterniond(5.71890317788325E-16,-1.90630105929442E-16,0.707106781186548,-0.707106781186547)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616935,0.305113829730607,0.353755907356446), chrono.ChQuaterniond(2.69591681202037E-16,-5.39183362404072E-16,1,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616935,0.307876329730607,0.341055907356446), chrono.ChQuaterniond(2.69591681202037E-16,-5.39183362404072E-16,1,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.136572262834165,0.317813829730607,0.141055907357911), chrono.ChQuaterniond(0.5,0.499999999999999,-0.5,0.5)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834165,0.305113829730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186547,-3.81260211858884E-16,-0.707106781186548,-3.4863055968421E-32)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.126634762834165,0.307876329730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186547,-3.81260211858884E-16,-0.707106781186548,-3.4863055968421E-32)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836957,0.317813829730607,0.141055907357911), chrono.ChQuaterniond(0.5,0.500000000000001,-0.5,0.5)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836957,0.305113829730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186548,3.8126021208526E-16,-0.707106781186547,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836957,0.307876329730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186548,3.8126021208526E-16,-0.707106781186547,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.167497262836957,0.317813829730607,0.366455907358794), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.164734762836957,0.305113829730607,0.366455907358794), chrono.ChQuaterniond(0.707106781186548,5.71890317788325E-16,0.707106781186547,1.90630105929442E-16)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.177434762836957,0.307876329730607,0.366455907358794), chrono.ChQuaterniond(0.707106781186548,5.71890317788325E-16,0.707106781186547,1.90630105929442E-16)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.3298347628374,0.317813829730607,0.350993407356443), chrono.ChQuaterniond(1.3738309013483E-16,-1.17756934401283E-16,0.707106781186548,-0.707106781186547)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.3298347628374,0.305113829730607,0.353755907356443), chrono.ChQuaterniond(8.47409175530384E-33,-1.80411241501588E-16,1,-3.41856075107737E-17)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.3298347628374,0.307876329730607,0.341055907356443), chrono.ChQuaterniond(8.47409175530384E-33,-1.80411241501588E-16,1,-3.41856075107737E-17)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.136572262834165,0.317813829730607,0.366455907358794), chrono.ChQuaterniond(0.5,0.5,-0.5,0.5)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834165,0.305113829730607,0.366455907358794), chrono.ChQuaterniond(0.707106781186548,-3.81260211858883E-16,-0.707106781186547,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.126634762834165,0.307876329730607,0.366455907358794), chrono.ChQuaterniond(0.707106781186548,-3.81260211858883E-16,-0.707106781186547,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.136572262834165,0.667413829730607,0.366455907358794), chrono.ChQuaterniond(0.500000000000001,-0.499999999999999,0.5,0.500000000000001)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834165,0.680113829730607,0.366455907358794), chrono.ChQuaterniond(9.53150529647208E-16,-0.707106781186547,-5.71890317788325E-16,0.707106781186548)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.126634762834165,0.677351329730607,0.366455907358794), chrono.ChQuaterniond(9.53150529647208E-16,-0.707106781186547,-5.71890317788325E-16,0.707106781186548)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.167497262836957,0.667413829730607,0.366455907358794), chrono.ChQuaterniond(-0.5,0.5,0.5,0.5)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.164734762836957,0.680113829730607,0.366455907358794), chrono.ChQuaterniond(1.39452223873684E-31,0.707106781186547,-3.81260211858883E-16,0.707106781186548)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.177434762836957,0.677351329730607,0.366455907358794), chrono.ChQuaterniond(1.39452223873684E-31,0.707106781186547,-3.81260211858883E-16,0.707106781186548)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.167497262836958,0.667413829730607,0.141055907357911), chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.500000000000001)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.164734762836958,0.680113829730607,0.141055907357911), chrono.ChQuaterniond(-1.90630105929442E-16,0.707106781186547,-5.71890317788325E-16,0.707106781186548)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.177434762836957,0.677351329730607,0.141055907357911), chrono.ChQuaterniond(-1.90630105929442E-16,0.707106781186547,-5.71890317788325E-16,0.707106781186548)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.019365237161274,0.677351329730607,0.367553348962111), chrono.ChQuaterniond(-6.99327703394595E-16,0.707106781186548,4.44452932513277E-16,-0.707106781186547)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.032065237161274,0.680113829730607,0.367553348962111), chrono.ChQuaterniond(0.499999999999999,0.500000000000001,0.5,-0.5)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.029302737161274,0.667413829730607,0.367553348962111), chrono.ChQuaterniond(0.499999999999999,0.500000000000001,0.5,-0.5)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.667413829730608,0.156518407360262), chrono.ChQuaterniond(3.81260211858883E-16,3.81260211858883E-16,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.680113829730608,0.153755907360262), chrono.ChQuaterniond(5.39183362404072E-16,0,-8.08775043606108E-16,1)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.677351329730608,0.166455907360262), chrono.ChQuaterniond(5.39183362404072E-16,0,-8.08775043606108E-16,1)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612741,0.667413829730608,0.141055907358866), chrono.ChQuaterniond(0.5,-0.5,-0.499999999999999,-0.500000000000001)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612741,0.680113829730608,0.141055907358866), chrono.ChQuaterniond(-1.90630105929442E-16,0.707106781186548,-1.33441074173247E-15,0.707106781186547)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612741,0.677351329730608,0.141055907358866), chrono.ChQuaterniond(-1.90630105929442E-16,0.707106781186548,-1.33441074173247E-15,0.707106781186547)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616918,0.667413829730608,0.350993407356447), chrono.ChQuaterniond(0.707106781186548,-0.707106781186547,5.71890317788325E-16,-9.53150529647208E-16)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616918,0.680113829730608,0.353755907356447), chrono.ChQuaterniond(-8.08775043606108E-16,1,-1.07836672480814E-15,2.69591681202036E-16)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616918,0.677351329730608,0.341055907356447), chrono.ChQuaterniond(-8.08775043606108E-16,1,-1.07836672480814E-15,2.69591681202036E-16)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.136572262834165,0.667413829730607,0.141055907357911), chrono.ChQuaterniond(0.500000000000001,-0.5,0.499999999999999,0.5)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834165,0.680113829730607,0.141055907357911), chrono.ChQuaterniond(-9.53150529647208E-16,0.707106781186548,5.71890317788325E-16,-0.707106781186547)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.126634762834165,0.677351329730607,0.141055907357911), chrono.ChQuaterniond(-9.53150529647208E-16,0.707106781186548,5.71890317788325E-16,-0.707106781186547)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836957,0.667413829730607,0.141055907357911), chrono.ChQuaterniond(0.5,-0.499999999999999,0.5,0.5)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836957,0.680113829730607,0.141055907357911), chrono.ChQuaterniond(9.53150529647208E-16,-0.707106781186547,1.90630106155817E-16,0.707106781186548)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836957,0.677351329730607,0.141055907357911), chrono.ChQuaterniond(9.53150529647208E-16,-0.707106781186547,1.90630106155817E-16,0.707106781186548)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.667413829730607,0.36645590735784), chrono.ChQuaterniond(0.5,-0.5,0.499999999999999,0.5)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.680113829730607,0.36645590735784), chrono.ChQuaterniond(-1.90630105929441E-16,0.707106781186548,5.71890317788325E-16,-0.707106781186547)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.677351329730607,0.36645590735784), chrono.ChQuaterniond(-1.90630105929441E-16,0.707106781186548,5.71890317788325E-16,-0.707106781186547)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617162,0.667413829730608,0.156518407360262), chrono.ChQuaterniond(3.81260211858883E-16,3.81260211858883E-16,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617162,0.680113829730608,0.153755907360262), chrono.ChQuaterniond(5.39183362404072E-16,0,-8.08775043606108E-16,1)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617162,0.677351329730608,0.166455907360262), chrono.ChQuaterniond(5.39183362404072E-16,0,-8.08775043606108E-16,1)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.3298347628374,0.667413829730607,0.350993407356444), chrono.ChQuaterniond(0.707106781186548,-0.707106781186547,4.99017146260166E-16,-4.99017146260166E-16)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.3298347628374,0.680113829730607,0.353755907356444), chrono.ChQuaterniond(-8.42960651116882E-16,1,-7.05716816097846E-16,-1.07481255273164E-31)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.3298347628374,0.677351329730607,0.341055907356444), chrono.ChQuaterniond(-8.42960651116882E-16,1,-7.05716816097846E-16,-1.07481255273164E-31)))

# Visualization shape 
body_2_96_shape = chrono.ChVisualShapeModelFile() 
body_2_96_shape.SetFilename(shapes_dir +'body_2_96.obj') 
body_2.AddVisualShape(body_2_96_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371621581,0.692813829731486,0.141055907357469), chrono.ChQuaterniond(0.707106781186548,-3.8126021208526E-16,0.707106781186547,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.029302737161274,0.692813829732003,0.341055907358352), chrono.ChQuaterniond(0.707106781186547,-4.96290709266116E-17,1.36224676550161E-16,-0.707106781186548)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.032065237161274,0.692813829732003,0.353755907358352), chrono.ChQuaterniond(0.5,-0.5,0.5,-0.5)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612739,0.692813829732003,0.350993407358352), chrono.ChQuaterniond(0.5,-0.5,0.5,-0.5)))

# Visualization shape 
body_2_23_shape = chrono.ChVisualShapeModelFile() 
body_2_23_shape.SetFilename(shapes_dir +'body_2_23.obj') 
body_2.AddVisualShape(body_2_23_shape, chrono.ChFramed(chrono.ChVector3d(-0.044765237161274,0.692813829731486,0.179155907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_96_shape = chrono.ChVisualShapeModelFile() 
body_2_96_shape.SetFilename(shapes_dir +'body_2_96.obj') 
body_2.AddVisualShape(body_2_96_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371621581,0.692813829731486,0.366455907358352), chrono.ChQuaterniond(0.707106781186548,3.81260211858883E-16,0.707106781186547,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.692813829731979,0.341055907358375), chrono.ChQuaterniond(0.707106781186547,2.32369780257537E-14,-2.33633634667313E-14,0.707106781186548)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.692813829731978,0.353755907358375), chrono.ChQuaterniond(0.500000000000016,-0.499999999999983,-0.500000000000017,0.499999999999984)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.692813829731978,0.350993407358375), chrono.ChQuaterniond(0.500000000000016,-0.499999999999983,-0.500000000000017,0.499999999999984)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.019365237161274,0.692813829732003,0.156518407358353), chrono.ChQuaterniond(-0.5,-0.5,0.5,0.5)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.032065237161274,0.692813829732003,0.153755907358353), chrono.ChQuaterniond(0.707106781186547,2.97341532496038E-17,-2.97341532496038E-17,-0.707106781186548)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.029302737161274,0.692813829732003,0.166455907358353), chrono.ChQuaterniond(0.707106781186547,2.97341532496038E-17,-2.97341532496038E-17,-0.707106781186548)))

# Visualization shape 
body_2_23_shape = chrono.ChVisualShapeModelFile() 
body_2_23_shape.SetFilename(shapes_dir +'body_2_23.obj') 
body_2.AddVisualShape(body_2_23_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837842,0.692813829731486,0.179155907358353), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.692813829732003,0.166455907358353), chrono.ChQuaterniond(6.31927204887826E-17,0.707106781186548,-0.707106781186547,-6.31927204887825E-17)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.692813829732003,0.153755907358353), chrono.ChQuaterniond(0.5,0.5,-0.5,-0.5)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.692813829732003,0.156518407358353), chrono.ChQuaterniond(0.5,0.5,-0.5,-0.5)))

# Visualization shape 
body_2_96_shape = chrono.ChVisualShapeModelFile() 
body_2_96_shape.SetFilename(shapes_dir +'body_2_96.obj') 
body_2.AddVisualShape(body_2_96_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371621585,0.292413829728693,0.141055907357469), chrono.ChQuaterniond(0.707106781186548,-3.8126021208526E-16,0.707106781186547,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612743,0.292413829729211,0.341055907358352), chrono.ChQuaterniond(0.707106781186547,-4.96290709266116E-17,1.36224676550161E-16,-0.707106781186548)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612743,0.292413829729211,0.353755907358352), chrono.ChQuaterniond(0.5,-0.5,0.5,-0.5)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612743,0.292413829729211,0.350993407358352), chrono.ChQuaterniond(0.5,-0.5,0.5,-0.5)))

# Visualization shape 
body_2_23_shape = chrono.ChVisualShapeModelFile() 
body_2_23_shape.SetFilename(shapes_dir +'body_2_23.obj') 
body_2.AddVisualShape(body_2_23_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371612743,0.292413829728693,0.179155907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_96_shape = chrono.ChVisualShapeModelFile() 
body_2_96_shape.SetFilename(shapes_dir +'body_2_96.obj') 
body_2.AddVisualShape(body_2_96_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371621584,0.292413829728693,0.366455907358352), chrono.ChQuaterniond(0.707106781186548,3.81260211858883E-16,0.707106781186547,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.292413829729186,0.341055907358375), chrono.ChQuaterniond(0.707106781186547,2.32369780257537E-14,-2.33633634667313E-14,0.707106781186548)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.292413829729186,0.353755907358375), chrono.ChQuaterniond(0.500000000000016,-0.499999999999983,-0.500000000000017,0.499999999999984)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.292413829729186,0.350993407358375), chrono.ChQuaterniond(0.500000000000016,-0.499999999999983,-0.500000000000017,0.499999999999984)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612743,0.292413829729211,0.156518407358353), chrono.ChQuaterniond(-0.5,-0.5,0.5,0.5)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612743,0.292413829729211,0.153755907358353), chrono.ChQuaterniond(0.707106781186547,2.97341532496038E-17,-2.97341532496038E-17,-0.707106781186548)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612743,0.292413829729211,0.166455907358353), chrono.ChQuaterniond(0.707106781186547,2.97341532496038E-17,-2.97341532496038E-17,-0.707106781186548)))

# Visualization shape 
body_2_23_shape = chrono.ChVisualShapeModelFile() 
body_2_23_shape.SetFilename(shapes_dir +'body_2_23.obj') 
body_2.AddVisualShape(body_2_23_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837842,0.292413829728693,0.179155907358353), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.292413829729211,0.166455907358353), chrono.ChQuaterniond(6.31927204887826E-17,0.707106781186548,-0.707106781186547,-6.31927204887825E-17)))

# Visualization shape 
body_2_4_shape = chrono.ChVisualShapeModelFile() 
body_2_4_shape.SetFilename(shapes_dir +'body_2_4.obj') 
body_2.AddVisualShape(body_2_4_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.292413829729211,0.153755907358353), chrono.ChQuaterniond(0.5,0.5,-0.5,-0.5)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.292413829729211,0.156518407358353), chrono.ChQuaterniond(0.5,0.5,-0.5,-0.5)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371612745,0.654713829730607,0.141055907358347), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,3.8126021208526E-16,-3.4863055968421E-32)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837411,0.324323829726142,0.123355907345341), chrono.ChQuaterniond(-2.42051107587712E-15,3.16604287669643E-15,0.707106781186551,-0.707106781186544)))

# Visualization shape 
body_2_130_shape = chrono.ChVisualShapeModelFile() 
body_2_130_shape.SetFilename(shapes_dir +'body_2_130.obj') 
body_2.AddVisualShape(body_2_130_shape, chrono.ChFramed(chrono.ChVector3d(0.202834762834166,0.540813829733399,0.122640907358352), chrono.ChQuaterniond(0,0,1,0)))

# Visualization shape 
body_2_130_shape = chrono.ChVisualShapeModelFile() 
body_2_130_shape.SetFilename(shapes_dir +'body_2_130.obj') 
body_2.AddVisualShape(body_2_130_shape, chrono.ChFramed(chrono.ChVector3d(0.101234762834166,0.540813829733399,0.384870907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_132_shape = chrono.ChVisualShapeModelFile() 
body_2_132_shape.SetFilename(shapes_dir +'body_2_132.obj') 
body_2.AddVisualShape(body_2_132_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762834166,0.634476329733399,0.253449907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_130_shape = chrono.ChVisualShapeModelFile() 
body_2_130_shape.SetFilename(shapes_dir +'body_2_130.obj') 
body_2.AddVisualShape(body_2_130_shape, chrono.ChFramed(chrono.ChVector3d(0.101234762834166,0.629713829733399,0.384870907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_130_shape = chrono.ChVisualShapeModelFile() 
body_2_130_shape.SetFilename(shapes_dir +'body_2_130.obj') 
body_2.AddVisualShape(body_2_130_shape, chrono.ChFramed(chrono.ChVector3d(0.202834762834166,0.629713829733399,0.122640907358352), chrono.ChQuaterniond(0,0,1,0)))

# Visualization shape 
body_2_132_shape = chrono.ChVisualShapeModelFile() 
body_2_132_shape.SetFilename(shapes_dir +'body_2_132.obj') 
body_2.AddVisualShape(body_2_132_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762834166,0.545576329733399,0.253449907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_130_shape = chrono.ChVisualShapeModelFile() 
body_2_130_shape.SetFilename(shapes_dir +'body_2_130.obj') 
body_2.AddVisualShape(body_2_130_shape, chrono.ChFramed(chrono.ChVector3d(0.101234762834166,0.451913829733399,0.384870907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_137_shape = chrono.ChVisualShapeModelFile() 
body_2_137_shape.SetFilename(shapes_dir +'body_2_137.obj') 
body_2.AddVisualShape(body_2_137_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834166,0.426513829733399,0.347405907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_137_shape = chrono.ChVisualShapeModelFile() 
body_2_137_shape.SetFilename(shapes_dir +'body_2_137.obj') 
body_2.AddVisualShape(body_2_137_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834166,0.426513829733399,0.153755907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_130_shape = chrono.ChVisualShapeModelFile() 
body_2_130_shape.SetFilename(shapes_dir +'body_2_130.obj') 
body_2.AddVisualShape(body_2_130_shape, chrono.ChFramed(chrono.ChVector3d(0.202834762834166,0.451913829733399,0.122640907358352), chrono.ChQuaterniond(0,0,1,0)))

# Visualization shape 
body_2_132_shape = chrono.ChVisualShapeModelFile() 
body_2_132_shape.SetFilename(shapes_dir +'body_2_132.obj') 
body_2.AddVisualShape(body_2_132_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762834166,0.456676329733399,0.253449907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.043740031618308,0.324323829727827,0.385076107359235), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,-3.87555566842849E-15,-3.85864489921714E-15)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837403,0.399323829727772,0.384155907361403), chrono.ChQuaterniond(3.08604551201541E-15,2.79804846673445E-15,0.707106781186544,0.707106781186551)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617139,0.324323829728002,0.123355907357452), chrono.ChQuaterniond(0.70710678118655,-0.707106781186545,2.56160942495213E-15,-3.25179140527763E-15)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837402,0.324323829726021,0.384155907359311), chrono.ChQuaterniond(3.03943339214823E-15,2.84466058660162E-15,0.707106781186544,0.707106781186551)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617132,0.399323829727808,0.123355907359389), chrono.ChQuaterniond(0.70710678118655,-0.707106781186545,2.59350884430325E-15,-3.28368045020259E-15)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0437400316183114,0.399323829727813,0.385076107359236), chrono.ChQuaterniond(4.39389193448936E-16,5.79964487832136E-17,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_2_3_shape = chrono.ChVisualShapeModelFile() 
body_2_3_shape.SetFilename(shapes_dir +'body_2_3.obj') 
body_2.AddVisualShape(body_2_3_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837411,0.399323829726145,0.123355907345068), chrono.ChQuaterniond(0.707106781186551,-0.707106781186544,2.50389615269494E-15,-3.01391408471168E-15)))

# Visualization shape 
body_2_148_shape = chrono.ChVisualShapeModelFile() 
body_2_148_shape.SetFilename(shapes_dir +'body_2_148.obj') 
body_2.AddVisualShape(body_2_148_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.706085329733399,0.141157299661483), chrono.ChQuaterniond(0.500020607772399,-0.499979391378206,-0.499979391378206,0.500020607772398)))

# Visualization shape 
body_2_149_shape = chrono.ChVisualShapeModelFile() 
body_2_149_shape.SetFilename(shapes_dir +'body_2_149.obj') 
body_2.AddVisualShape(body_2_149_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.757456829733399,0.141157299661483), chrono.ChQuaterniond(-0.0731636374323121,0.0731636374323132,0.703311511463926,0.703311511463927)))

# Visualization shape 
body_2_149_shape = chrono.ChVisualShapeModelFile() 
body_2_149_shape.SetFilename(shapes_dir +'body_2_149.obj') 
body_2.AddVisualShape(body_2_149_shape, chrono.ChFramed(chrono.ChVector3d(-0.027117460658095,0.7574568297334,0.366157299661484), chrono.ChQuaterniond(-0.0731636374323121,0.0731636374323132,0.703311511463926,0.703311511463927)))

# Visualization shape 
body_2_151_shape = chrono.ChVisualShapeModelFile() 
body_2_151_shape.SetFilename(shapes_dir +'body_2_151.obj') 
body_2.AddVisualShape(body_2_151_shape, chrono.ChFramed(chrono.ChVector3d(-0.0271174606580948,0.8073043297334,0.366157299661484), chrono.ChQuaterniond(-0.0435546902795118,0.0435546902795129,0.705764117077835,0.705764117077835)))

# Visualization shape 
body_2_149_shape = chrono.ChVisualShapeModelFile() 
body_2_149_shape.SetFilename(shapes_dir +'body_2_149.obj') 
body_2.AddVisualShape(body_2_149_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.757456829733399,0.366157299661484), chrono.ChQuaterniond(-0.0731636374323121,0.0731636374323132,0.703311511463926,0.703311511463927)))

# Visualization shape 
body_2_151_shape = chrono.ChVisualShapeModelFile() 
body_2_151_shape.SetFilename(shapes_dir +'body_2_151.obj') 
body_2.AddVisualShape(body_2_151_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.710606529733399,0.141157299661483), chrono.ChQuaterniond(-0.277117631253953,-0.277117631253952,0.650542710702533,-0.650542710702532)))

# Visualization shape 
body_2_151_shape = chrono.ChVisualShapeModelFile() 
body_2_151_shape.SetFilename(shapes_dir +'body_2_151.obj') 
body_2.AddVisualShape(body_2_151_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.710606529733399,0.366157299661483), chrono.ChQuaterniond(-0.277117631253953,-0.277117631253952,0.650542710702533,-0.650542710702532)))

# Visualization shape 
body_2_151_shape = chrono.ChVisualShapeModelFile() 
body_2_151_shape.SetFilename(shapes_dir +'body_2_151.obj') 
body_2.AddVisualShape(body_2_151_shape, chrono.ChFramed(chrono.ChVector3d(-0.027117460658095,0.7106065297334,0.366157299661483), chrono.ChQuaterniond(-0.277117631253953,-0.277117631253952,0.650542710702533,-0.650542710702532)))

# Visualization shape 
body_2_148_shape = chrono.ChVisualShapeModelFile() 
body_2_148_shape.SetFilename(shapes_dir +'body_2_148.obj') 
body_2.AddVisualShape(body_2_148_shape, chrono.ChFramed(chrono.ChVector3d(-0.027117460658095,0.7060853297334,0.366157299661483), chrono.ChQuaterniond(0.500020607772399,-0.499979391378206,-0.499979391378206,0.500020607772398)))

# Visualization shape 
body_2_148_shape = chrono.ChVisualShapeModelFile() 
body_2_148_shape.SetFilename(shapes_dir +'body_2_148.obj') 
body_2.AddVisualShape(body_2_148_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.706085329733399,0.366157299661483), chrono.ChQuaterniond(0.500020607772399,-0.499979391378206,-0.499979391378206,0.500020607772398)))

# Visualization shape 
body_2_151_shape = chrono.ChVisualShapeModelFile() 
body_2_151_shape.SetFilename(shapes_dir +'body_2_151.obj') 
body_2.AddVisualShape(body_2_151_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.807304329733399,0.141157299661483), chrono.ChQuaterniond(-0.0435546902795118,0.0435546902795129,0.705764117077835,0.705764117077835)))

# Visualization shape 
body_2_151_shape = chrono.ChVisualShapeModelFile() 
body_2_151_shape.SetFilename(shapes_dir +'body_2_151.obj') 
body_2.AddVisualShape(body_2_151_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.807304329733399,0.366157299661484), chrono.ChQuaterniond(-0.0435546902795118,0.0435546902795129,0.705764117077835,0.705764117077835)))

# Visualization shape 
body_2_160_shape = chrono.ChVisualShapeModelFile() 
body_2_160_shape.SetFilename(shapes_dir +'body_2_160.obj') 
body_2.AddVisualShape(body_2_160_shape, chrono.ChFramed(chrono.ChVector3d(0.147534762837843,0.808256829733399,0.253755907359236), chrono.ChQuaterniond(0.707106781186548,-3.81260211858883E-16,-0.707106781186547,-7.62520423717767E-16)))

# Visualization shape 
body_2_161_shape = chrono.ChVisualShapeModelFile() 
body_2_161_shape.SetFilename(shapes_dir +'body_2_161.obj') 
body_2.AddVisualShape(body_2_161_shape, chrono.ChFramed(chrono.ChVector3d(0.265188762837843,0.869606829733399,0.253755907359236), chrono.ChQuaterniond(1.11022302462516E-16,8.08775043606109E-16,1,2.69591681202036E-16)))

# Visualization shape 
body_2_151_shape = chrono.ChVisualShapeModelFile() 
body_2_151_shape.SetFilename(shapes_dir +'body_2_151.obj') 
body_2.AddVisualShape(body_2_151_shape, chrono.ChFramed(chrono.ChVector3d(-0.027117460658095,0.7106065297334,0.141157299661483), chrono.ChQuaterniond(-0.277117631253953,-0.277117631253952,0.650542710702533,-0.650542710702532)))

# Visualization shape 
body_2_163_shape = chrono.ChVisualShapeModelFile() 
body_2_163_shape.SetFilename(shapes_dir +'body_2_163.obj') 
body_2.AddVisualShape(body_2_163_shape, chrono.ChFramed(chrono.ChVector3d(0.265634762837843,0.864606829733399,0.253755907359236), chrono.ChQuaterniond(-1.16879339985135E-31,8.08775043606108E-16,1,2.69591681202036E-16)))

# Visualization shape 
body_2_151_shape = chrono.ChVisualShapeModelFile() 
body_2_151_shape.SetFilename(shapes_dir +'body_2_151.obj') 
body_2.AddVisualShape(body_2_151_shape, chrono.ChFramed(chrono.ChVector3d(-0.0271174606580948,0.8073043297334,0.141157299661483), chrono.ChQuaterniond(-0.0435546902795118,0.0435546902795129,0.705764117077835,0.705764117077835)))

# Visualization shape 
body_2_148_shape = chrono.ChVisualShapeModelFile() 
body_2_148_shape.SetFilename(shapes_dir +'body_2_148.obj') 
body_2.AddVisualShape(body_2_148_shape, chrono.ChFramed(chrono.ChVector3d(-0.027117460658095,0.7060853297334,0.141157299661483), chrono.ChQuaterniond(0.500020607772399,-0.499979391378206,-0.499979391378206,0.500020607772398)))

# Visualization shape 
body_2_149_shape = chrono.ChVisualShapeModelFile() 
body_2_149_shape.SetFilename(shapes_dir +'body_2_149.obj') 
body_2.AddVisualShape(body_2_149_shape, chrono.ChFramed(chrono.ChVector3d(-0.027117460658095,0.7574568297334,0.141157299661483), chrono.ChQuaterniond(-0.0731636374323121,0.0731636374323132,0.703311511463926,0.703311511463927)))

exported_items.append(body_2)



# Rigid body part
body_3 = chrono.ChBodyAuxRef()
body_3.SetName('arm_assembly-4')
body_3.SetPos(chrono.ChVector3d(0.312530921501762,0.149292313319778,0.115855907357467))
body_3.SetRot(chrono.ChQuaterniond(4.92844550549504e-16,-2.77555756156281e-16,1,4.44029194545789e-15))
body_3.SetMass(0.364051497440596)
body_3.SetInertiaXX(chrono.ChVector3d(0.00408204363389774,0.00104054206771477,0.00318444113837038))
body_3.SetInertiaXY(chrono.ChVector3d(4.23413299037235e-11,-6.11651643754802e-10,0.000719823333564849))
body_3.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-1.59228715578873e-08,0.0724885111288461,0.0511378350659033),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999995,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.92925761838102E-17,1.44170911143914E-17,0.707106781186547)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.92925761838102E-17,1.44170911143914E-17,0.707106781186547)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.00500000000000006,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.92925761838102E-17,1.44170911143914E-17,0.707106781186547)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_3.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(-4.92844550549504E-16,-2.77555756156281E-16,1,4.44029194545789E-15)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.92925761838102E-17,1.44170911143914E-17,0.707106781186547)))

# Visualization shape 
body_3_6_shape = chrono.ChVisualShapeModelFile() 
body_3_6_shape.SetFilename(shapes_dir +'body_3_6.obj') 
body_3.AddVisualShape(body_3_6_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.0558,0.12551), chrono.ChQuaterniond(0.878355111664487,5.53303520153522E-17,0.478008679641767,4.48614121768739E-18)))

# Visualization shape 
body_3_7_shape = chrono.ChVisualShapeModelFile() 
body_3_7_shape.SetFilename(shapes_dir +'body_3_7.obj') 
body_3.AddVisualShape(body_3_7_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.05261,0.12551), chrono.ChQuaterniond(0.707106781186548,3.94589586905534E-17,0.707106781186547,-3.90456642436136E-17)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_3.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-1.44170911167254E-17,1.40037966721206E-17,-0.707106781186547)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_3.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-1.44170911167254E-17,1.40037966721206E-17,-0.707106781186547)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_3.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(-0.00500000000000006,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-1.44170911167254E-17,1.40037966721206E-17,-0.707106781186547)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_3.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999995,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-1.44170911167254E-17,1.40037966721206E-17,-0.707106781186547)))

# Visualization shape 
body_3_12_shape = chrono.ChVisualShapeModelFile() 
body_3_12_shape.SetFilename(shapes_dir +'body_3_12.obj') 
body_3.AddVisualShape(body_3_12_shape, chrono.ChFramed(chrono.ChVector3d(-5.55111512312578E-17,0.14679,0.12551), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

exported_items.append(body_3)



# Rigid body part
body_4 = chrono.ChBodyAuxRef()
body_4.SetName('hub_assem-3')
body_4.SetPos(chrono.ChVector3d(0.596289661401382,0.111007899961958,0.115855478526423))
body_4.SetRot(chrono.ChQuaterniond(0.00129962045144908,-0.106401479115183,0.994322390821007,0.000139071129855213))
body_4.SetMass(1.5598908069349)
body_4.SetInertiaXX(chrono.ChVector3d(0.00436080523071917,0.00230048447927596,0.00414454522173494))
body_4.SetInertiaXY(chrono.ChVector3d(0.000728725428031433,0.000534309901548285,-0.000448361570726465))
body_4.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0870481233327875,0.072850189784672,0.0857992020333657),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0713531392165593,0.0218992234984526,0.132196545530042), chrono.ChQuaterniond(0.666388969328945,-0.233706445072318,0.668133245007216,0.234318172586962)))

# Visualization shape 
body_4_2_shape = chrono.ChVisualShapeModelFile() 
body_4_2_shape.SetFilename(shapes_dir +'body_4_2.obj') 
body_4.AddVisualShape(body_4_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.128151564600374,0.165433452720356,0.0755948276627572), chrono.ChQuaterniond(-0.00101730857317258,0.627854897824528,0.778329312645782,-0.000820632295209721)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.10393587812052,-0.00766152532301641,0.132281719647764), chrono.ChQuaterniond(0.674333044626005,-0.209685254219403,0.676098113951778,0.210234106175032)))

# Visualization shape 
body_4_4_shape = chrono.ChVisualShapeModelFile() 
body_4_4_shape.SetFilename(shapes_dir +'body_4_4.obj') 
body_4.AddVisualShape(body_4_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961426426015956,0.0165247077633607,0.14576139357698), chrono.ChQuaterniond(0.999999145822587,4.72100700412701E-15,0.00130704020480689,1.29104006833423E-17)))

# Visualization shape 
body_4_5_shape = chrono.ChVisualShapeModelFile() 
body_4_5_shape.SetFilename(shapes_dir +'body_4_5.obj') 
body_4.AddVisualShape(body_4_5_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961949241651302,0.0165247077633611,0.125761461911144), chrono.ChQuaterniond(0.994322390821007,0.000139071129845418,0.00129962045145291,0.106401479115182)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.113244780633865,0.0353364251146471,0.132306053929816), chrono.ChQuaterniond(0.672485001165168,-0.215538590789487,0.674245233230107,0.216102763875997)))

exported_items.append(body_4)



# Rigid body part
body_5 = chrono.ChBodyAuxRef()
body_5.SetName('wheel_grouser-3')
body_5.SetPos(chrono.ChVector3d(0.317288608205122,0.162573185304428,0.564880796408194))
body_5.SetRot(chrono.ChQuaterniond(0.438765292178574,0.554513316683604,0.438765292178579,-0.554513316683599))
body_5.SetMass(25.7732862791227)
body_5.SetInertiaXX(chrono.ChVector3d(0.192475111227948,0.331949143225572,0.200261107874774))
body_5.SetInertiaXY(chrono.ChVector3d(-2.9543199204016e-11,2.12324673475255e-11,-0.032953669737147))
body_5.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0270700245615144,-0.000185466324721263,0.0154474354006911),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_5.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0290351109510424,-0.00018546633589267,0.0154474354087597), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_2_shape = chrono.ChVisualShapeModelFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_5.AddVisualShape(body_1_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.00253511095104242,-0.00018546633589267,0.0154474354087597), chrono.ChQuaterniond(0.669230211120907,0.228321975558784,-0.669230211120907,-0.228321975558784)))

if ENABLE_wheel3_contact: 
    # Collision Model
    
    body_5.AddCollisionModel(chrono.ChCollisionModel())
    
    # Collision material 
    mat_5 = chrono.ChContactMaterialNSC()
    
    # Triangle mesh collision shape 
    body_1_1_collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_1_1_collision.obj', False, True) 
    mr = chrono.ChMatrix33d()
    mr[0,0]=1; mr[1,0]=0; mr[2,0]=0 
    mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
    mr[0,2]=0; mr[1,2]=0; mr[2,2]=1 
    body_1_1_collision_mesh.Transform(chrono.ChVector3d(-0.0290351109510424, -0.00018546633589267, 0.0154474354087597), mr) 
    collshape = chrono.ChCollisionShapeTriangleMesh(mat_5,body_1_1_collision_mesh,False,False,sphereswept_r)
    body_5.GetCollisionModel().AddShape(collshape)
    body_5.EnableCollision(True)

exported_items.append(body_5)



# Rigid body part
body_6 = chrono.ChBodyAuxRef()
body_6.SetName('arm_assembly-3')
body_6.SetPos(chrono.ChVector3d(0.313556127045162,0.149292313319782,0.391655907359236))
body_6.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_6.SetMass(0.364051497440596)
body_6.SetInertiaXX(chrono.ChVector3d(0.00408204363389774,0.00104054206771479,0.00318444113837037))
body_6.SetInertiaXY(chrono.ChVector3d(-4.23413272333361e-11,-6.11651642364871e-10,-0.000719823333564868))
body_6.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-1.59228715578811e-08,0.0724885111288461,0.0511378350659033),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_6.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_6.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_6.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_6.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(-6.12303176911189E-17,-8.14015851325628E-17,1,1.65030317669818E-27)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_6.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_6_shape = chrono.ChVisualShapeModelFile() 
body_3_6_shape.SetFilename(shapes_dir +'body_3_6.obj') 
body_6.AddVisualShape(body_3_6_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.0558,0.12551), chrono.ChQuaterniond(0.878355111664487,0,0.478008679641768,0)))

# Visualization shape 
body_3_7_shape = chrono.ChVisualShapeModelFile() 
body_3_7_shape.SetFilename(shapes_dir +'body_3_7.obj') 
body_6.AddVisualShape(body_3_7_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.05261,0.12551), chrono.ChQuaterniond(0.707106781186548,0,0.707106781186547,0)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_6.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_6.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_6.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_6.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_12_shape = chrono.ChVisualShapeModelFile() 
body_3_12_shape.SetFilename(shapes_dir +'body_3_12.obj') 
body_6.AddVisualShape(body_3_12_shape, chrono.ChFramed(chrono.ChVector3d(0,0.14679,0.12551), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

exported_items.append(body_6)



# Rigid body part
body_7 = chrono.ChBodyAuxRef()
body_7.SetName('arm_assembly-1')
body_7.SetPos(chrono.ChVector3d(0.687130921500886,0.149292313318114,0.115855907357466))
body_7.SetRot(chrono.ChQuaterniond(4.16660120460961e-16,-2.63677968348465e-16,1,4.76768293758141e-15))
body_7.SetMass(0.364051497440596)
body_7.SetInertiaXX(chrono.ChVector3d(0.00408204363389774,0.00104054206771477,0.00318444113837038))
body_7.SetInertiaXY(chrono.ChVector3d(4.23413295729475e-11,-6.11651643544938e-10,0.000719823333564847))
body_7.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-1.59228715578904e-08,0.0724885111288461,0.0511378350659033),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_7.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.00500000000000012,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-5.39835192531853E-17,2.48277311480301E-17,0.707106781186548)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_7.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.00500000000000012,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-5.39835192531853E-17,2.48277311480301E-17,0.707106781186548)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_7.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.00499999999999989,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-5.39835192531853E-17,2.48277311480301E-17,0.707106781186548)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_7.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(-4.16660120460961E-16,-2.63677968348465E-16,1,4.76768293758141E-15)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_7.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.00499999999999989,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-5.39835192531853E-17,2.48277311480301E-17,0.707106781186548)))

# Visualization shape 
body_3_6_shape = chrono.ChVisualShapeModelFile() 
body_3_6_shape.SetFilename(shapes_dir +'body_3_6.obj') 
body_7.AddVisualShape(body_3_6_shape, chrono.ChFramed(chrono.ChVector3d(1.11022302462516E-16,-0.0558,0.12551), chrono.ChQuaterniond(0.878355111664487,2.57785531505459E-17,0.478008679641767,2.71383757603969E-17)))

# Visualization shape 
body_3_7_shape = chrono.ChVisualShapeModelFile() 
body_3_7_shape.SetFilename(shapes_dir +'body_3_7.obj') 
body_7.AddVisualShape(body_3_7_shape, chrono.ChFramed(chrono.ChVector3d(1.11022302462516E-16,-0.05261,0.12551), chrono.ChQuaterniond(0.707106781186548,3.73835945085112E-17,0.707106781186547,-1.86871695855872E-18)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_7.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(0.00500000000000012,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.48277311503641E-17,-1.06871463972545E-17,-0.707106781186547)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_7.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(-0.00499999999999989,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.48277311503641E-17,-1.06871463972545E-17,-0.707106781186547)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_7.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(-0.00499999999999989,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.48277311503641E-17,-1.06871463972545E-17,-0.707106781186547)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_7.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(0.00500000000000012,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.48277311503641E-17,-1.06871463972545E-17,-0.707106781186547)))

# Visualization shape 
body_3_12_shape = chrono.ChVisualShapeModelFile() 
body_3_12_shape.SetFilename(shapes_dir +'body_3_12.obj') 
body_7.AddVisualShape(body_3_12_shape, chrono.ChFramed(chrono.ChVector3d(1.11022302462516E-16,0.14679,0.12551), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

exported_items.append(body_7)



# Rigid body part
body_8 = chrono.ChBodyAuxRef()
body_8.SetName('hub_assem-4')
body_8.SetPos(chrono.ChVector3d(0.404397387144667,0.111007899963626,0.391656336190281))
body_8.SetRot(chrono.ChQuaterniond(0.994322390821008,-0.000139071129845742,-0.00129962045144819,-0.106401479115182))
body_8.SetMass(1.5598908069349)
body_8.SetInertiaXX(chrono.ChVector3d(0.00455731911417192,0.0021027534296609,0.00414576238789726))
body_8.SetInertiaXY(chrono.ChVector3d(0.000296279277479677,0.000301244020441806,0.000626930626183415))
body_8.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0870481233327876,0.072850189784672,0.0857992020333657),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_8.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0713531392165592,0.0218992234984526,0.132196545530042), chrono.ChQuaterniond(0.666388969328945,-0.233706445072318,0.668133245007217,0.234318172586962)))

# Visualization shape 
body_4_2_shape = chrono.ChVisualShapeModelFile() 
body_4_2_shape.SetFilename(shapes_dir +'body_4_2.obj') 
body_8.AddVisualShape(body_4_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.128151564600374,0.165433452720356,0.0755948276627572), chrono.ChQuaterniond(-0.00101730857317254,0.627854897824528,0.778329312645782,-0.000820632295209681)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_8.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.10393587812052,-0.00766152532301645,0.132281719647764), chrono.ChQuaterniond(0.674333044626005,-0.209685254219402,0.676098113951778,0.210234106175032)))

# Visualization shape 
body_4_4_shape = chrono.ChVisualShapeModelFile() 
body_4_4_shape.SetFilename(shapes_dir +'body_4_4.obj') 
body_8.AddVisualShape(body_4_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961426426015955,0.0165247077633606,0.14576139357698), chrono.ChQuaterniond(0.999999145822587,4.70120440901168E-15,0.00130704020480687,1.46320688999867E-17)))

# Visualization shape 
body_4_5_shape = chrono.ChVisualShapeModelFile() 
body_4_5_shape.SetFilename(shapes_dir +'body_4_5.obj') 
body_8.AddVisualShape(body_4_5_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961949241651301,0.0165247077633611,0.125761461911144), chrono.ChQuaterniond(0.994322390821008,0.000139071129845742,0.00129962045144819,0.106401479115182)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_8.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.113244780633865,0.0353364251146472,0.132306053929817), chrono.ChQuaterniond(0.672485001165168,-0.215538590789487,0.674245233230107,0.216102763875997)))

exported_items.append(body_8)



# Rigid body part
body_9 = chrono.ChBodyAuxRef()
body_9.SetName('wheel_grouser-4')
body_9.SetPos(chrono.ChVector3d(0.297099942835025,0.146845729409912,-0.0573689816914894))
body_9.SetRot(chrono.ChQuaterniond(-0.0126184239327423,0.70699418341133,0.0126184239327361,0.70699418341133))
body_9.SetMass(25.7732862791227)
body_9.SetInertiaXX(chrono.ChVector3d(0.192475111227948,0.192662630844764,0.339547620255583))
body_9.SetInertiaXY(chrono.ChVector3d(-1.26613318004633e-11,3.41073019707029e-11,0.00525156969192117))
body_9.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0270700245615144,-0.000185466324721263,0.0154474354006911),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_9.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0290351109510424,-0.000185466335892698,0.0154474354087596), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_2_shape = chrono.ChVisualShapeModelFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_9.AddVisualShape(body_1_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.00253511095104248,-0.00018546633589267,0.0154474354087596), chrono.ChQuaterniond(0.669230211120907,0.228321975558784,-0.669230211120907,-0.228321975558784)))

if ENABLE_wheel4_contact:
    # Collision Model
    
    body_9.AddCollisionModel(chrono.ChCollisionModel())
    
    # Collision material 
    mat_9 = chrono.ChContactMaterialNSC()
    
    # Triangle mesh collision shape 
    body_1_1_collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_1_1_collision.obj', False, True) 
    mr = chrono.ChMatrix33d()
    mr[0,0]=1; mr[1,0]=0; mr[2,0]=0 
    mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
    mr[0,2]=0; mr[1,2]=0; mr[2,2]=1 
    body_1_1_collision_mesh.Transform(chrono.ChVector3d(-0.0290351109510424, -0.000185466335892698, 0.0154474354087596), mr) 
    collshape = chrono.ChCollisionShapeTriangleMesh(mat_9,body_1_1_collision_mesh,False,False,sphereswept_r)
    body_9.GetCollisionModel().AddShape(collshape)
    body_9.EnableCollision(True)

exported_items.append(body_9)



# Rigid body part
body_10 = chrono.ChBodyAuxRef()
body_10.SetName('arm_assembly-2')
body_10.SetPos(chrono.ChVector3d(0.687130921500877,0.149292313319744,0.391655907359234))
body_10.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_10.SetMass(0.364051497440596)
body_10.SetInertiaXX(chrono.ChVector3d(0.00408204363389774,0.00104054206771479,0.00318444113837037))
body_10.SetInertiaXY(chrono.ChVector3d(-4.23413272323965e-11,-6.1165164236322e-10,-0.000719823333564868))
body_10.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-1.59228715578904e-08,0.0724885111288461,0.0511378350659033),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_10.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_10.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.14239,0.0907100000000001), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_10.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_10.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(-6.12303176911189E-17,-8.14015851325628E-17,1,1.65030317669818E-27)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_10.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.0907100000000001), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_6_shape = chrono.ChVisualShapeModelFile() 
body_3_6_shape.SetFilename(shapes_dir +'body_3_6.obj') 
body_10.AddVisualShape(body_3_6_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.0558,0.12551), chrono.ChQuaterniond(0.878355111664487,0,0.478008679641768,0)))

# Visualization shape 
body_3_7_shape = chrono.ChVisualShapeModelFile() 
body_3_7_shape.SetFilename(shapes_dir +'body_3_7.obj') 
body_10.AddVisualShape(body_3_7_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.05261,0.12551), chrono.ChQuaterniond(0.707106781186548,0,0.707106781186547,0)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_10.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.17059,0.0907100000000001), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_10.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.0907100000000001), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_10.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_8_shape = chrono.ChVisualShapeModelFile() 
body_3_8_shape.SetFilename(shapes_dir +'body_3_8.obj') 
body_10.AddVisualShape(body_3_8_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_12_shape = chrono.ChVisualShapeModelFile() 
body_3_12_shape.SetFilename(shapes_dir +'body_3_12.obj') 
body_10.AddVisualShape(body_3_12_shape, chrono.ChFramed(chrono.ChVector3d(0,0.14679,0.12551), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

exported_items.append(body_10)



# Rigid body part
body_11 = chrono.ChBodyAuxRef()
body_11.SetName('wheel_grouser-2')
body_11.SetPos(chrono.ChVector3d(0.671685810617397,0.14725641722072,-0.0573689816914893))
body_11.SetRot(chrono.ChQuaterniond(-0.00321429673581218,0.707099475531197,0.0032142967358056,0.707099475531197))
body_11.SetMass(25.7732862791227)
body_11.SetInertiaXX(chrono.ChVector3d(0.192475111227948,0.19248728252612,0.339722968574226))
body_11.SetInertiaXY(chrono.ChVector3d(-1.35640248668858e-11,3.37585270965709e-11,0.00133873121615276))
body_11.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0270700245615144,-0.000185466324721263,0.0154474354006911),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_11.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0290351109510424,-0.00018546633589267,0.0154474354087597), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_2_shape = chrono.ChVisualShapeModelFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_11.AddVisualShape(body_1_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.00253511095104248,-0.00018546633589267,0.0154474354087597), chrono.ChQuaterniond(0.669230211120907,0.228321975558784,-0.669230211120907,-0.228321975558784)))

if ENABLE_wheel2_contact: 
    # Collision Model
    
    body_11.AddCollisionModel(chrono.ChCollisionModel())
    
    # Collision material 
    mat_11 = chrono.ChContactMaterialNSC()
    
    # Triangle mesh collision shape 
    body_1_1_collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_1_1_collision.obj', False, True) 
    mr = chrono.ChMatrix33d()
    mr[0,0]=1; mr[1,0]=0; mr[2,0]=0 
    mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
    mr[0,2]=0; mr[1,2]=0; mr[2,2]=1 
    body_1_1_collision_mesh.Transform(chrono.ChVector3d(-0.0290351109510424, -0.00018546633589267, 0.0154474354087597), mr) 
    collshape = chrono.ChCollisionShapeTriangleMesh(mat_11,body_1_1_collision_mesh,False,False,sphereswept_r)
    body_11.GetCollisionModel().AddShape(collshape)
    body_11.EnableCollision(True)

exported_items.append(body_11)



# Rigid body part
body_12 = chrono.ChBodyAuxRef()
body_12.SetName('hub_assem-1')
body_12.SetPos(chrono.ChVector3d(0.802019600302532,0.111007899963583,0.413216984927633))
body_12.SetRot(chrono.ChQuaterniond(0.988771085504673,0.0109519028540781,-0.104930674119787,-0.105836430034996))
body_12.SetMass(1.5598908069349)
body_12.SetInertiaXX(chrono.ChVector3d(0.00465607158005443,0.00215899285401024,0.0039907704976654))
body_12.SetInertiaXY(chrono.ChVector3d(0.000436954311009607,0.000173291619565753,0.000637494334735008))
body_12.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0870481233327876,0.072850189784672,0.0857992020333657),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_12.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0713531392165592,0.0218992234984526,0.132196545530042), chrono.ChQuaterniond(0.666388969328945,-0.233706445072318,0.668133245007217,0.234318172586962)))

# Visualization shape 
body_4_2_shape = chrono.ChVisualShapeModelFile() 
body_4_2_shape.SetFilename(shapes_dir +'body_4_2.obj') 
body_12.AddVisualShape(body_4_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.128151564600374,0.165433452720356,0.0755948276627572), chrono.ChQuaterniond(-0.00101730857317255,0.627854897824528,0.778329312645782,-0.000820632295209674)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_12.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.10393587812052,-0.00766152532301645,0.132281719647764), chrono.ChQuaterniond(0.674333044626005,-0.209685254219402,0.676098113951778,0.210234106175032)))

# Visualization shape 
body_4_4_shape = chrono.ChVisualShapeModelFile() 
body_4_4_shape.SetFilename(shapes_dir +'body_4_4.obj') 
body_12.AddVisualShape(body_4_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961426426015954,0.0165247077633607,0.14576139357698), chrono.ChQuaterniond(0.999999145822587,4.70110463547454E-15,0.0013070402048069,4.33681239434921E-19)))

# Visualization shape 
body_4_5_shape = chrono.ChVisualShapeModelFile() 
body_4_5_shape.SetFilename(shapes_dir +'body_4_5.obj') 
body_12.AddVisualShape(body_4_5_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961949241651301,0.0165247077633611,0.125761461911144), chrono.ChQuaterniond(0.994322390821007,0.000139071129845386,0.00129962045145289,0.106401479115182)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_12.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.113244780633865,0.0353364251146471,0.132306053929816), chrono.ChQuaterniond(0.672485001165168,-0.215538590789487,0.674245233230107,0.216102763875997)))

exported_items.append(body_12)



# Rigid body part
body_13 = chrono.ChBodyAuxRef()
body_13.SetName('hub_assem-2')
body_13.SetPos(chrono.ChVector3d(0.221689661402257,0.11100789996362,0.115855478526423))
body_13.SetRot(chrono.ChQuaterniond(0.00129962045144924,-0.106401479115182,0.994322390821007,0.00013907112985486))
body_13.SetMass(1.5598908069349)
body_13.SetInertiaXX(chrono.ChVector3d(0.00436080523071917,0.00230048447927596,0.00414454522173494))
body_13.SetInertiaXY(chrono.ChVector3d(0.000728725428031431,0.000534309901548283,-0.000448361570726464))
body_13.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0870481233327875,0.072850189784672,0.0857992020333657),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_13.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0713531392165592,0.0218992234984526,0.132196545530042), chrono.ChQuaterniond(0.666388969328945,-0.233706445072318,0.668133245007216,0.234318172586962)))

# Visualization shape 
body_4_2_shape = chrono.ChVisualShapeModelFile() 
body_4_2_shape.SetFilename(shapes_dir +'body_4_2.obj') 
body_13.AddVisualShape(body_4_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.128151564600374,0.165433452720356,0.0755948276627571), chrono.ChQuaterniond(-0.00101730857317256,0.627854897824528,0.778329312645782,-0.000820632295209695)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_13.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.10393587812052,-0.00766152532301644,0.132281719647764), chrono.ChQuaterniond(0.674333044626005,-0.209685254219403,0.676098113951778,0.210234106175032)))

# Visualization shape 
body_4_4_shape = chrono.ChVisualShapeModelFile() 
body_4_4_shape.SetFilename(shapes_dir +'body_4_4.obj') 
body_13.AddVisualShape(body_4_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961426426015956,0.0165247077633606,0.14576139357698), chrono.ChQuaterniond(0.999999145822587,4.70059926117162E-15,0.00130704020480688,1.24585519117578E-17)))

# Visualization shape 
body_4_5_shape = chrono.ChVisualShapeModelFile() 
body_4_5_shape.SetFilename(shapes_dir +'body_4_5.obj') 
body_13.AddVisualShape(body_4_5_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961949241651301,0.0165247077633611,0.125761461911144), chrono.ChQuaterniond(0.994322390821007,0.000139071129845377,0.00129962045145291,0.106401479115182)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_13.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.113244780633865,0.0353364251146471,0.132306053929816), chrono.ChQuaterniond(0.672485001165168,-0.215538590789487,0.674245233230107,0.216102763875997)))

exported_items.append(body_13)




# # Mate constraint: Parallel27 [MateParallel] type:3 align:0 flip:False
# #   Entity 0: C::E name: body_0 , SW name: Assem6^cobra_4_1_py-1/Frame Assy-1 ,  SW ref.type:4 (4)
# #   Entity 1: C::E name: body_0 , SW name: cobra_4_1_py ,  SW ref.type:4 (4)
# link_1 = chrono.ChLinkMateParallel()
# cA = chrono.ChVector3d(0.357296158663475,-0.167031516408032,0)
# dA = chrono.ChVector3d(0,1,0)
# cB = chrono.ChVector3d(0,0,0)
# dB = chrono.ChVector3d(0,1,0)
# link_1.Initialize(body_2,body_0,False,cA,cB,dA,dB)
# link_1.SetName("Parallel27")
# exported_items.append(link_1)


# # Mate constraint: Parallel28 [MateParallel] type:3 align:0 flip:False
# #   Entity 0: C::E name: body_0 , SW name: Assem6^cobra_4_1_py-1/Frame Assy-1 ,  SW ref.type:4 (4)
# #   Entity 1: C::E name: body_0 , SW name: cobra_4_1_py ,  SW ref.type:4 (4)
# link_2 = chrono.ChLinkMateParallel()
# cA = chrono.ChVector3d(0.357296158663475,-0.167031516408032,0)
# dA = chrono.ChVector3d(1,0,0)
# cB = chrono.ChVector3d(0,0,0)
# dB = chrono.ChVector3d(1,0,0)
# link_2.Initialize(body_2,body_0,False,cA,cB,dA,dB)
# link_2.SetName("Parallel28")
# exported_items.append(link_2)


# # Mate constraint: Coincident230 [MateCoincident] type:0 align:0 flip:False
# #   Entity 0: C::E name: body_0 , SW name: Assem6^cobra_4_1_py-1/Frame Assy-1 ,  SW ref.type:4 (4)
# #   Entity 1: C::E name: body_0 , SW name: cobra_4_1_py ,  SW ref.type:4 (4)
# link_3 = chrono.ChLinkMateDistanceZ()
# cA = chrono.ChVector3d(0.357296158663475,-0.167031516408032,0)
# cB = chrono.ChVector3d(0,0,0)
# dA = chrono.ChVector3d(0,0,1)
# dB = chrono.ChVector3d(0,0,1)
# link_3.Initialize(body_2,body_0,False,cA,cB,dB)
# link_3.SetDistance(0)
# link_3.SetName("Coincident230")
# exported_items.append(link_3)

# link_4 = chrono.ChLinkMateParallel()
# cA = chrono.ChVector3d(0.357296158663475,-0.167031516408032,0)
# dA = chrono.ChVector3d(0,0,1)
# cB = chrono.ChVector3d(0,0,0)
# dB = chrono.ChVector3d(0,0,1)
# link_4.Initialize(body_2,body_0,False,cA,cB,dA,dB)
# link_4.SetName("Coincident230")
# exported_items.append(link_4)


# Mate constraint: Coincident199 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_12 , SW name: hub_assem-1/Strut-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: arm_assembly-2/DS3225MG Servo 25Kg 4.8-6.8V-1 ,  SW ref.type:2 (2)
link_5 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.687130921500877,0.296082313319736,0.517165907359238)
cB = chrono.ChVector3d(0.687130921500877,0.296082313319744,0.517165907359234)
dA = chrono.ChVector3d(-2.77448691191756e-15,1,1.91343252006759e-14)
dB = chrono.ChVector3d(1.62803170264902e-16,-1,-3.30081589457431e-27)
link_5.Initialize(body_12,body_10,False,cA,cB,dB)
link_5.SetDistance(0)
link_5.SetName("Coincident199")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.687130921500877,0.296082313319736,0.517165907359238)
dA = chrono.ChVector3d(-2.77448691191756e-15,1,1.91343252006759e-14)
cB = chrono.ChVector3d(0.687130921500877,0.296082313319744,0.517165907359234)
dB = chrono.ChVector3d(1.62803170264902e-16,-1,-3.30081589457431e-27)
link_6.SetFlipped(True)
link_6.Initialize(body_12,body_10,False,cA,cB,dA,dB)
link_6.SetName("Coincident199")
exported_items.append(link_6)


# Mate constraint: Concentric5 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_12 , SW name: hub_assem-1/Strut-2 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_10 , SW name: arm_assembly-2/bearings-1 ,  SW ref.type:1 (1)
link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.687130921500878,0.0930823133197361,0.517165907359234)
dA = chrono.ChVector3d(2.86499527680382e-15,-1,-1.91151438418258e-14)
cB = chrono.ChVector3d(0.687130921500877,0.100582313319744,0.517165907359234)
dB = chrono.ChVector3d(0,1,0)
link_7.SetFlipped(True)
link_7.Initialize(body_12,body_10,False,cA,cB,dA,dB)
link_7.SetName("Concentric5")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.687130921500878,0.0930823133197361,0.517165907359234)
cB = chrono.ChVector3d(0.687130921500877,0.100582313319744,0.517165907359234)
dA = chrono.ChVector3d(2.86499527680382e-15,-1,-1.91151438418258e-14)
dB = chrono.ChVector3d(0,1,0)
link_8.Initialize(body_12,body_10,False,cA,cB,dA,dB)
link_8.SetName("Concentric5")
exported_items.append(link_8)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: wheel_grouser-1/wheel_hub_2-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_12 , SW name: hub_assem-1/Wheel Hub_n2-1 ,  SW ref.type:1 (1)
link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.681895980770343,0.147582313319746,0.5418672817248)
dA = chrono.ChVector3d(0.207324385367696,1.86062103224582e-14,-0.978272252101585)
cB = chrono.ChVector3d(0.67857879060446,0.147582313319735,0.557519637758426)
dB = chrono.ChVector3d(-0.207324385367694,-2.86923262926564e-14,0.978272252101586)
link_9.SetFlipped(True)
link_9.Initialize(body_1,body_12,False,cA,cB,dA,dB)
link_9.SetName("Concentric6")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.681895980770343,0.147582313319746,0.5418672817248)
cB = chrono.ChVector3d(0.67857879060446,0.147582313319735,0.557519637758426)
dA = chrono.ChVector3d(0.207324385367696,1.86062103224582e-14,-0.978272252101585)
dB = chrono.ChVector3d(-0.207324385367694,-2.86923262926564e-14,0.978272252101586)
link_10.Initialize(body_1,body_12,False,cA,cB,dA,dB)
link_10.SetName("Concentric6")
exported_items.append(link_10)


# Mate constraint: Coincident200 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: wheel_grouser-1/wheel_hub_2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: hub_assem-1/Wheel Hub_n2-1 ,  SW ref.type:2 (2)
link_11 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.67857879060446,0.147582313319746,0.557519637758426)
cB = chrono.ChVector3d(0.67857879060446,0.147582313319735,0.557519637758426)
dA = chrono.ChVector3d(0.207324385367696,1.86062103224582e-14,-0.978272252101585)
dB = chrono.ChVector3d(-0.207324385367694,-2.86923262926564e-14,0.978272252101586)
link_11.Initialize(body_1,body_12,False,cA,cB,dB)
link_11.SetDistance(0)
link_11.SetName("Coincident200")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.67857879060446,0.147582313319746,0.557519637758426)
dA = chrono.ChVector3d(0.207324385367696,1.86062103224582e-14,-0.978272252101585)
cB = chrono.ChVector3d(0.67857879060446,0.147582313319735,0.557519637758426)
dB = chrono.ChVector3d(-0.207324385367694,-2.86923262926564e-14,0.978272252101586)
link_12.SetFlipped(True)
link_12.Initialize(body_1,body_12,False,cA,cB,dA,dB)
link_12.SetName("Coincident200")
exported_items.append(link_12)


# Mate constraint: Concentric7 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: arm_assembly-3/bearings-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: hub_assem-4/Strut-2 ,  SW ref.type:2 (2)
link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.313556127045162,0.100582313319782,0.517165907359236)
dA = chrono.ChVector3d(0,-1,0)
cB = chrono.ChVector3d(0.313556127045162,0.0930823133197815,0.517165907359236)
dB = chrono.ChVector3d(-9.25185853854297e-17,1,0)
link_13.SetFlipped(True)
link_13.Initialize(body_6,body_8,False,cA,cB,dA,dB)
link_13.SetName("Concentric7")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.313556127045162,0.100582313319782,0.517165907359236)
cB = chrono.ChVector3d(0.313556127045162,0.0930823133197815,0.517165907359236)
dA = chrono.ChVector3d(0,-1,0)
dB = chrono.ChVector3d(-9.25185853854297e-17,1,0)
link_14.Initialize(body_6,body_8,False,cA,cB,dA,dB)
link_14.SetName("Concentric7")
exported_items.append(link_14)


# Mate constraint: Coincident201 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: arm_assembly-3/DS3225MG Servo 25Kg 4.8-6.8V-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: hub_assem-4/Strut-2 ,  SW ref.type:2 (2)
link_15 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.313556127045162,0.296082313319782,0.517165907359236)
cB = chrono.ChVector3d(0.313556127045162,0.296082313319782,0.517165907359236)
dA = chrono.ChVector3d(1.62803170264902e-16,-1,-3.30081589457431e-27)
dB = chrono.ChVector3d(0,1,0)
link_15.Initialize(body_6,body_8,False,cA,cB,dB)
link_15.SetDistance(0)
link_15.SetName("Coincident201")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.313556127045162,0.296082313319782,0.517165907359236)
dA = chrono.ChVector3d(1.62803170264902e-16,-1,-3.30081589457431e-27)
cB = chrono.ChVector3d(0.313556127045162,0.296082313319782,0.517165907359236)
dB = chrono.ChVector3d(0,1,0)
link_16.SetFlipped(True)
link_16.Initialize(body_6,body_8,False,cA,cB,dA,dB)
link_16.SetName("Coincident201")
exported_items.append(link_16)


# Mate constraint: Concentric8 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: arm_assembly-1/bearings-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: hub_assem-3/Strut-2 ,  SW ref.type:2 (2)
link_17 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.687130921500886,0.100582313318115,-0.00965409264253404)
dA = chrono.ChVector3d(5.55111512312546e-16,-1,-9.5604786859114e-15)
cB = chrono.ChVector3d(0.687130921500886,0.0930823133181158,-0.00965409264253275)
dB = chrono.ChVector3d(-1.06622989799674e-15,1,1.87023790551577e-14)
link_17.SetFlipped(True)
link_17.Initialize(body_7,body_4,False,cA,cB,dA,dB)
link_17.SetName("Concentric8")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateGeneric()
link_18.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.687130921500886,0.100582313318115,-0.00965409264253404)
cB = chrono.ChVector3d(0.687130921500886,0.0930823133181158,-0.00965409264253275)
dA = chrono.ChVector3d(5.55111512312546e-16,-1,-9.5604786859114e-15)
dB = chrono.ChVector3d(-1.06622989799674e-15,1,1.87023790551577e-14)
link_18.Initialize(body_7,body_4,False,cA,cB,dA,dB)
link_18.SetName("Concentric8")
exported_items.append(link_18)


# Mate constraint: Coincident202 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: arm_assembly-1/DS3225MG Servo 25Kg 4.8-6.8V-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: hub_assem-3/Strut-2 ,  SW ref.type:2 (2)
link_19 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.687130921500886,0.296082313318115,-0.00965409264253217)
cB = chrono.ChVector3d(0.687130921500886,0.296082313318116,-0.00965409264252895)
dA = chrono.ChVector3d(3.92308342047645e-16,-1,-9.5604786859081e-15)
dB = chrono.ChVector3d(-1.15874848338217e-15,1,1.87023790551577e-14)
link_19.Initialize(body_7,body_4,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Coincident202")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.687130921500886,0.296082313318115,-0.00965409264253217)
dA = chrono.ChVector3d(3.92308342047645e-16,-1,-9.5604786859081e-15)
cB = chrono.ChVector3d(0.687130921500886,0.296082313318116,-0.00965409264252895)
dB = chrono.ChVector3d(-1.15874848338217e-15,1,1.87023790551577e-14)
link_20.SetFlipped(True)
link_20.Initialize(body_7,body_4,False,cA,cB,dA,dB)
link_20.SetName("Coincident202")
exported_items.append(link_20)


# Mate constraint: Concentric9 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: arm_assembly-4/bearings-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_13 , SW name: hub_assem-2/Strut-2 ,  SW ref.type:2 (2)
link_21 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.312530921501762,0.100582313319779,-0.0096540926425338)
dA = chrono.ChVector3d(6.10622663543809e-16,-1,-8.88087613422183e-15)
cB = chrono.ChVector3d(0.312530921501762,0.0930823133197779,-0.00965409264253275)
dB = chrono.ChVector3d(-3.90616302234214e-17,1,1.80776617633716e-14)
link_21.SetFlipped(True)
link_21.Initialize(body_3,body_13,False,cA,cB,dA,dB)
link_21.SetName("Concentric9")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateGeneric()
link_22.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.312530921501762,0.100582313319779,-0.0096540926425338)
cB = chrono.ChVector3d(0.312530921501762,0.0930823133197779,-0.00965409264253275)
dA = chrono.ChVector3d(6.10622663543809e-16,-1,-8.88087613422183e-15)
dB = chrono.ChVector3d(-3.90616302234214e-17,1,1.80776617633716e-14)
link_22.Initialize(body_3,body_13,False,cA,cB,dA,dB)
link_22.SetName("Concentric9")
exported_items.append(link_22)


# Mate constraint: Coincident203 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: arm_assembly-4/DS3225MG Servo 25Kg 4.8-6.8V-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_13 , SW name: hub_assem-2/Strut-2 ,  SW ref.type:2 (2)
link_23 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.312530921501762,0.296082313319779,-0.00965409264253206)
cB = chrono.ChVector3d(0.312530921501762,0.296082313319778,-0.00965409264252908)
dA = chrono.ChVector3d(4.47819493278907e-16,-1,-8.88087613421853e-15)
dB = chrono.ChVector3d(-1.31580215608851e-16,1,1.80776617633716e-14)
link_23.Initialize(body_3,body_13,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Coincident203")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.312530921501762,0.296082313319779,-0.00965409264253206)
dA = chrono.ChVector3d(4.47819493278907e-16,-1,-8.88087613421853e-15)
cB = chrono.ChVector3d(0.312530921501762,0.296082313319778,-0.00965409264252908)
dB = chrono.ChVector3d(-1.31580215608851e-16,1,1.80776617633716e-14)
link_24.SetFlipped(True)
link_24.Initialize(body_3,body_13,False,cA,cB,dA,dB)
link_24.SetName("Coincident203")
exported_items.append(link_24)


# Mate constraint: Concentric10 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: wheel_grouser-4/wheel_hub_2-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_13 , SW name: hub_assem-2/Wheel Hub_n2-1 ,  SW ref.type:1 (1)
link_25 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.312530921501762,0.147582313319778,-0.0349040926425318)
dA = chrono.ChVector3d(-1.34468347783088e-16,-8.79609957776578e-15,1)
cB = chrono.ChVector3d(0.312530921501762,0.147582313319778,-0.0509040926425318)
dB = chrono.ChVector3d(1.58383786951885e-16,8.67599275199803e-15,-1)
link_25.SetFlipped(True)
link_25.Initialize(body_9,body_13,False,cA,cB,dA,dB)
link_25.SetName("Concentric10")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateGeneric()
link_26.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.312530921501762,0.147582313319778,-0.0349040926425318)
cB = chrono.ChVector3d(0.312530921501762,0.147582313319778,-0.0509040926425318)
dA = chrono.ChVector3d(-1.34468347783088e-16,-8.79609957776578e-15,1)
dB = chrono.ChVector3d(1.58383786951885e-16,8.67599275199803e-15,-1)
link_26.Initialize(body_9,body_13,False,cA,cB,dA,dB)
link_26.SetName("Concentric10")
exported_items.append(link_26)


# Mate constraint: Coincident204 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: wheel_grouser-4/wheel_hub_2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_13 , SW name: hub_assem-2/Wheel Hub_n2-1 ,  SW ref.type:2 (2)
link_27 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.312530921501762,0.147582313319778,-0.0509040926425318)
cB = chrono.ChVector3d(0.312530921501762,0.147582313319778,-0.0509040926425318)
dA = chrono.ChVector3d(-1.34468347783088e-16,-8.79609957776578e-15,1)
dB = chrono.ChVector3d(1.58383786951885e-16,8.67599275199803e-15,-1)
link_27.Initialize(body_9,body_13,False,cA,cB,dB)
link_27.SetDistance(0)
link_27.SetName("Coincident204")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.312530921501762,0.147582313319778,-0.0509040926425318)
dA = chrono.ChVector3d(-1.34468347783088e-16,-8.79609957776578e-15,1)
cB = chrono.ChVector3d(0.312530921501762,0.147582313319778,-0.0509040926425318)
dB = chrono.ChVector3d(1.58383786951885e-16,8.67599275199803e-15,-1)
link_28.SetFlipped(True)
link_28.Initialize(body_9,body_13,False,cA,cB,dA,dB)
link_28.SetName("Coincident204")
exported_items.append(link_28)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_5 , SW name: wheel_grouser-3/wheel_hub_2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: hub_assem-4/Wheel Hub_n2-1 ,  SW ref.type:2 (2)
link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.313556127045162,0.14758231331978,0.617256527792802)
dA = chrono.ChVector3d(4.16622924069702e-17,9.67379006382285e-15,-1)
cB = chrono.ChVector3d(0.313556127045162,0.147582313319781,0.558415907359236)
dB = chrono.ChVector3d(4.16622923990423e-17,9.67379006382442e-15,-1)
link_29.Initialize(body_5,body_8,False,cA,cB,dA,dB)
link_29.SetName("Concentric11")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.313556127045162,0.14758231331978,0.617256527792802)
cB = chrono.ChVector3d(0.313556127045162,0.147582313319781,0.558415907359236)
dA = chrono.ChVector3d(4.16622924069702e-17,9.67379006382285e-15,-1)
dB = chrono.ChVector3d(4.16622923990423e-17,9.67379006382442e-15,-1)
link_30.Initialize(body_5,body_8,False,cA,cB,dA,dB)
link_30.SetName("Concentric11")
exported_items.append(link_30)


# Mate constraint: Coincident205 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: wheel_grouser-3/wheel_hub_2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: hub_assem-4/Wheel Hub_n2-1 ,  SW ref.type:2 (2)
link_31 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.313556127045162,0.147582313319781,0.558415907359236)
cB = chrono.ChVector3d(0.313556127045162,0.147582313319781,0.558415907359236)
dA = chrono.ChVector3d(4.16622924069702e-17,9.67379006382285e-15,-1)
dB = chrono.ChVector3d(-4.16622923990423e-17,-9.67379006382442e-15,1)
link_31.Initialize(body_5,body_8,False,cA,cB,dB)
link_31.SetDistance(0)
link_31.SetName("Coincident205")
exported_items.append(link_31)

link_32 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.313556127045162,0.147582313319781,0.558415907359236)
dA = chrono.ChVector3d(4.16622924069702e-17,9.67379006382285e-15,-1)
cB = chrono.ChVector3d(0.313556127045162,0.147582313319781,0.558415907359236)
dB = chrono.ChVector3d(-4.16622923990423e-17,-9.67379006382442e-15,1)
link_32.SetFlipped(True)
link_32.Initialize(body_5,body_8,False,cA,cB,dA,dB)
link_32.SetName("Coincident205")
exported_items.append(link_32)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_11 , SW name: wheel_grouser-2/wheel_hub_2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: hub_assem-3/Wheel Hub_n2-1 ,  SW ref.type:2 (2)
link_33 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.687130921500886,0.147582313318116,-0.109744713076098)
dA = chrono.ChVector3d(2.24108596615843e-16,-9.30125282518174e-15,1)
cB = chrono.ChVector3d(0.687130921500886,0.147582313318116,-0.0509040926425318)
dB = chrono.ChVector3d(2.23581514261285e-16,-9.30072390235511e-15,1)
link_33.Initialize(body_11,body_4,False,cA,cB,dA,dB)
link_33.SetName("Concentric12")
exported_items.append(link_33)

link_34 = chrono.ChLinkMateGeneric()
link_34.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.687130921500886,0.147582313318116,-0.109744713076098)
cB = chrono.ChVector3d(0.687130921500886,0.147582313318116,-0.0509040926425318)
dA = chrono.ChVector3d(2.24108596615843e-16,-9.30125282518174e-15,1)
dB = chrono.ChVector3d(2.23581514261285e-16,-9.30072390235511e-15,1)
link_34.Initialize(body_11,body_4,False,cA,cB,dA,dB)
link_34.SetName("Concentric12")
exported_items.append(link_34)


# Mate constraint: Coincident206 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_11 , SW name: wheel_grouser-2/wheel_hub_2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: hub_assem-3/Wheel Hub_n2-1 ,  SW ref.type:2 (2)
link_35 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.687130921500886,0.147582313318116,-0.0509040926425318)
cB = chrono.ChVector3d(0.687130921500886,0.147582313318116,-0.0509040926425318)
dA = chrono.ChVector3d(2.24108596615843e-16,-9.30125282518174e-15,1)
dB = chrono.ChVector3d(-2.23581514261285e-16,9.30072390235511e-15,-1)
link_35.Initialize(body_11,body_4,False,cA,cB,dB)
link_35.SetDistance(0)
link_35.SetName("Coincident206")
exported_items.append(link_35)

link_36 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.687130921500886,0.147582313318116,-0.0509040926425318)
dA = chrono.ChVector3d(2.24108596615843e-16,-9.30125282518174e-15,1)
cB = chrono.ChVector3d(0.687130921500886,0.147582313318116,-0.0509040926425318)
dB = chrono.ChVector3d(-2.23581514261285e-16,9.30072390235511e-15,-1)
link_36.SetFlipped(True)
link_36.Initialize(body_11,body_4,False,cA,cB,dA,dB)
link_36.SetName("Coincident206")
exported_items.append(link_36)


# Mate constraint: Concentric25 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Assem6^cobra_4_1_py-1/5537T868_T-Slotted Framing-2 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_6 , SW name: arm_assembly-3/Steering Arm-1 ,  SW ref.type:1 (1)
link_37 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.313556127045163,0.232292313319782,0.387901107359236)
dA = chrono.ChVector3d(5.38482581824738e-16,8.15634772288052e-16,-1)
cB = chrono.ChVector3d(0.313556127045162,0.232292313319782,0.379155907359236)
dB = chrono.ChVector3d(1.22460635382238e-16,-2.44327250170582e-17,1)
link_37.SetFlipped(True)
link_37.Initialize(body_2,body_6,False,cA,cB,dA,dB)
link_37.SetName("Concentric25")
exported_items.append(link_37)

link_38 = chrono.ChLinkMateGeneric()
link_38.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.313556127045163,0.232292313319782,0.387901107359236)
cB = chrono.ChVector3d(0.313556127045162,0.232292313319782,0.379155907359236)
dA = chrono.ChVector3d(5.38482581824738e-16,8.15634772288052e-16,-1)
dB = chrono.ChVector3d(1.22460635382238e-16,-2.44327250170582e-17,1)
link_38.Initialize(body_2,body_6,False,cA,cB,dA,dB)
link_38.SetName("Concentric25")
exported_items.append(link_38)


# Mate constraint: Concentric26 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Assem6^cobra_4_1_py-1/5537T868_T-Slotted Framing-4 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_3 , SW name: arm_assembly-4/Steering Arm-1 ,  SW ref.type:2 (2)
link_39 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.312530921501761,0.232292313319777,0.118055907359389)
dA = chrono.ChVector3d(-9.65870286624315e-16,-8.73511389791494e-15,1)
cB = chrono.ChVector3d(0.312530921501762,0.232292313319778,0.128355907357467)
dB = chrono.ChVector3d(0,-2.44327250137578e-17,-1)
link_39.SetFlipped(True)
link_39.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_39.SetName("Concentric26")
exported_items.append(link_39)

link_40 = chrono.ChLinkMateGeneric()
link_40.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.312530921501761,0.232292313319777,0.118055907359389)
cB = chrono.ChVector3d(0.312530921501762,0.232292313319778,0.128355907357467)
dA = chrono.ChVector3d(-9.65870286624315e-16,-8.73511389791494e-15,1)
dB = chrono.ChVector3d(0,-2.44327250137578e-17,-1)
link_40.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_40.SetName("Concentric26")
exported_items.append(link_40)


# Mate constraint: Concentric27 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Assem6^cobra_4_1_py-1/5537T868_T-Slotted Framing-6 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_7 , SW name: arm_assembly-1/Steering Arm-1 ,  SW ref.type:1 (1)
link_41 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.687130921500886,0.232292313318113,0.118055907345068)
dA = chrono.ChVector3d(-7.21274276511585e-16,-9.36784210960477e-15,1)
cB = chrono.ChVector3d(0.687130921500886,0.232292313318114,0.128355907357466)
dB = chrono.ChVector3d(0,-2.44327250137578e-17,-1)
link_41.SetFlipped(True)
link_41.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_41.SetName("Concentric27")
exported_items.append(link_41)

link_42 = chrono.ChLinkMateGeneric()
link_42.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.687130921500886,0.232292313318113,0.118055907345068)
cB = chrono.ChVector3d(0.687130921500886,0.232292313318114,0.128355907357466)
dA = chrono.ChVector3d(-7.21274276511585e-16,-9.36784210960477e-15,1)
dB = chrono.ChVector3d(0,-2.44327250137578e-17,-1)
link_42.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_42.SetName("Concentric27")
exported_items.append(link_42)


# Mate constraint: Concentric28 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Assem6^cobra_4_1_py-1/5537T868_T-Slotted Framing-8 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_10 , SW name: arm_assembly-2/Steering Arm-1 ,  SW ref.type:1 (1)
link_43 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.687130921500877,0.23229231331974,0.386980907361403)
dA = chrono.ChVector3d(4.07289327359778e-16,8.80349115125891e-15,-1)
cB = chrono.ChVector3d(0.687130921500877,0.232292313319744,0.379155907359233)
dB = chrono.ChVector3d(1.22460635382238e-16,-2.44327250170582e-17,1)
link_43.SetFlipped(True)
link_43.Initialize(body_2,body_10,False,cA,cB,dA,dB)
link_43.SetName("Concentric28")
exported_items.append(link_43)

link_44 = chrono.ChLinkMateGeneric()
link_44.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.687130921500877,0.23229231331974,0.386980907361403)
cB = chrono.ChVector3d(0.687130921500877,0.232292313319744,0.379155907359233)
dA = chrono.ChVector3d(4.07289327359778e-16,8.80349115125891e-15,-1)
dB = chrono.ChVector3d(1.22460635382238e-16,-2.44327250170582e-17,1)
link_44.Initialize(body_2,body_10,False,cA,cB,dA,dB)
link_44.SetName("Concentric28")
exported_items.append(link_44)


# Mate constraint: Coincident231 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Assem6^cobra_4_1_py-1/Frame Assy-1/Vertical Tubes-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: arm_assembly-1/Steering Arm-1 ,  SW ref.type:2 (2)
link_45 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.680797837899402,0.138082313322575,0.128355907357469)
cB = chrono.ChVector3d(0.724630921500886,0.149292313318114,0.128355907357466)
dA = chrono.ChVector3d(-5.39183362724218e-16,-3.20145585429192e-25,-1)
dB = chrono.ChVector3d(0,-2.03744416706092e-17,1)
link_45.Initialize(body_2,body_7,False,cA,cB,dB)
link_45.SetDistance(0)
link_45.SetName("Coincident231")
exported_items.append(link_45)

link_46 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.680797837899402,0.138082313322575,0.128355907357469)
dA = chrono.ChVector3d(-5.39183362724218e-16,-3.20145585429192e-25,-1)
cB = chrono.ChVector3d(0.724630921500886,0.149292313318114,0.128355907357466)
dB = chrono.ChVector3d(0,-2.03744416706092e-17,1)
link_46.SetFlipped(True)
link_46.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_46.SetName("Coincident231")
exported_items.append(link_46)


# Mate constraint: Parallel23 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Assem6^cobra_4_1_py-1/Frame Assy-1/Vertical Tubes-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: arm_assembly-1/Steering Arm-1 ,  SW ref.type:2 (2)
link_47 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.699830921501316,0.138082313322575,0.134722823758348)
dA = chrono.ChVector3d(1,5.39183362724218e-16,6.47020035448468e-14)
cB = chrono.ChVector3d(0.712130921500886,-0.069491939941944,0.128355907357466)
dB = chrono.ChVector3d(1,0,-2.77988306607176e-16)
link_47.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_47.SetName("Parallel23")
exported_items.append(link_47)


# Mate constraint: Coincident232 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Assem6^cobra_4_1_py-1/Frame Assy-1/Vertical Tubes-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: arm_assembly-4/Steering Arm-1 ,  SW ref.type:2 (2)
link_48 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.306197837900287,0.138082313322575,0.128355907357469)
cB = chrono.ChVector3d(0.350030921501762,0.149292313319778,0.128355907357467)
dA = chrono.ChVector3d(-5.39183362724217e-16,-1.07836672559671e-15,-1)
dB = chrono.ChVector3d(0,-2.03744416706092e-17,1)
link_48.Initialize(body_2,body_3,False,cA,cB,dB)
link_48.SetDistance(0)
link_48.SetName("Coincident232")
exported_items.append(link_48)

link_49 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.306197837900287,0.138082313322575,0.128355907357469)
dA = chrono.ChVector3d(-5.39183362724217e-16,-1.07836672559671e-15,-1)
cB = chrono.ChVector3d(0.350030921501762,0.149292313319778,0.128355907357467)
dB = chrono.ChVector3d(0,-2.03744416706092e-17,1)
link_49.SetFlipped(True)
link_49.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_49.SetName("Coincident232")
exported_items.append(link_49)


# Mate constraint: Parallel24 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Assem6^cobra_4_1_py-1/Frame Assy-1/Vertical Tubes-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: arm_assembly-4/Steering Arm-1 ,  SW ref.type:2 (2)
link_50 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.299830921501316,0.138082313322575,0.147388990960262)
dA = chrono.ChVector3d(-1,-5.39183362724218e-16,9.86076131526265e-32)
cB = chrono.ChVector3d(0.287530921501762,-0.0694919399402803,0.128355907357467)
dB = chrono.ChVector3d(-1,0,0)
link_50.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_50.SetName("Parallel24")
exported_items.append(link_50)


# Mate constraint: Coincident233 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Assem6^cobra_4_1_py-1/Frame Assy-1/Vertical Tubes-4 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: arm_assembly-3/Steering Arm-1 ,  SW ref.type:2 (2)
link_51 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.302980521498521,0.138082313322575,0.379155907359236)
cB = chrono.ChVector3d(0.276056127045162,0.149292313319782,0.379155907359236)
dA = chrono.ChVector3d(-1.07836672480815e-15,-1.07836672480814e-15,1)
dB = chrono.ChVector3d(-1.22460635382238e-16,-2.03744416673088e-17,-1)
link_51.Initialize(body_2,body_6,False,cA,cB,dB)
link_51.SetDistance(0)
link_51.SetName("Coincident233")
exported_items.append(link_51)

link_52 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.302980521498521,0.138082313322575,0.379155907359236)
dA = chrono.ChVector3d(-1.07836672480815e-15,-1.07836672480814e-15,1)
cB = chrono.ChVector3d(0.276056127045162,0.149292313319782,0.379155907359236)
dB = chrono.ChVector3d(-1.22460635382238e-16,-2.03744416673088e-17,-1)
link_52.SetFlipped(True)
link_52.Initialize(body_2,body_6,False,cA,cB,dA,dB)
link_52.SetName("Coincident233")
exported_items.append(link_52)


# Mate constraint: Parallel25 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Assem6^cobra_4_1_py-1/Frame Assy-1/Vertical Tubes-4 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: arm_assembly-3/Steering Arm-1 ,  SW ref.type:2 (2)
link_53 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.299830921501316,0.138082313322575,0.372788990959236)
dA = chrono.ChVector3d(-1,5.39183362404073e-16,-1.07836672512829e-15)
cB = chrono.ChVector3d(0.288556127045162,-0.0694919399402763,0.379155907359236)
dB = chrono.ChVector3d(-1,-1.6280317026535e-16,4.00448941989414e-16)
link_53.Initialize(body_2,body_6,False,cA,cB,dA,dB)
link_53.SetName("Parallel25")
exported_items.append(link_53)


# Mate constraint: Coincident234 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Assem6^cobra_4_1_py-1/Frame Assy-1/Vertical Tubes-3 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: arm_assembly-2/Steering Arm-1 ,  SW ref.type:2 (2)
link_54 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.693464005100432,0.138082313322575,0.379155907359236)
cB = chrono.ChVector3d(0.649630921500877,0.149292313319744,0.379155907359233)
dA = chrono.ChVector3d(4.6841850577209e-25,4.6841850577209e-25,1)
dB = chrono.ChVector3d(-1.22460635382238e-16,-2.03744416673088e-17,-1)
link_54.Initialize(body_2,body_10,False,cA,cB,dB)
link_54.SetDistance(0)
link_54.SetName("Coincident234")
exported_items.append(link_54)

link_55 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.693464005100432,0.138082313322575,0.379155907359236)
dA = chrono.ChVector3d(4.6841850577209e-25,4.6841850577209e-25,1)
cB = chrono.ChVector3d(0.649630921500877,0.149292313319744,0.379155907359233)
dB = chrono.ChVector3d(-1.22460635382238e-16,-2.03744416673088e-17,-1)
link_55.SetFlipped(True)
link_55.Initialize(body_2,body_10,False,cA,cB,dA,dB)
link_55.SetName("Coincident234")
exported_items.append(link_55)


# Mate constraint: Parallel26 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Assem6^cobra_4_1_py-1/Frame Assy-1/Vertical Tubes-3 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: arm_assembly-2/Steering Arm-1 ,  SW ref.type:2 (2)
link_56 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.699830921501316,0.138082313322575,0.376006307360117)
dA = chrono.ChVector3d(1,-5.39183362404072e-16,0)
cB = chrono.ChVector3d(0.712130921500877,-0.0694919399403139,0.379155907359233)
dB = chrono.ChVector3d(1,1.6280317026535e-16,-1.22460635382238e-16)
link_56.Initialize(body_2,body_10,False,cA,cB,dA,dB)
link_56.SetName("Parallel26")
exported_items.append(link_56)


# Auxiliary marker (coordinate system feature)
marker_0_1 = chrono.ChMarker()
marker_0_1.SetName('steer_arm_1')
body_0.AddMarker(marker_0_1)
marker_0_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.687130921500877,0.10058231331977,0.51716590735925),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_2 = chrono.ChMarker()
marker_0_2.SetName('steer_arm_2')
body_0.AddMarker(marker_0_2)
marker_0_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.313556127045162,0.100582313319782,0.517165907359236),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_3 = chrono.ChMarker()
marker_0_3.SetName('steer_arm_3')
body_0.AddMarker(marker_0_3)
marker_0_3.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.687130921500887,0.100582313318148,-0.00965409264251317),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_4 = chrono.ChMarker()
marker_0_4.SetName('steer_arm_4')
body_0.AddMarker(marker_0_4)
marker_0_4.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.312530921501761,0.1005823133198,-0.00965409264250541),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_5 = chrono.ChMarker()
marker_0_5.SetName('steer_hub_1')
body_0.AddMarker(marker_0_5)
marker_0_5.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.687130921500887,0.0930823133196226,0.517165907359258),chrono.ChQuaterniond(-0.445161660139419,0.445161660139409,0.549391569230832,0.549391569230841)))

# Auxiliary marker (coordinate system feature)
marker_0_6 = chrono.ChMarker()
marker_0_6.SetName('steer_hub_2')
body_0.AddMarker(marker_0_6)
marker_0_6.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.313556127045162,0.0930823133197815,0.517165907359236),chrono.ChQuaterniond(-0.5,0.5,0.5,0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_7 = chrono.ChMarker()
marker_0_7.SetName('steer_hub_3')
body_0.AddMarker(marker_0_7)
marker_0_7.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.687130921500887,0.0930823133181391,-0.00965409264253714),chrono.ChQuaterniond(0.500000000000007,-0.499999999999997,-0.499999999999993,-0.500000000000002)))

# Auxiliary marker (coordinate system feature)
marker_0_8 = chrono.ChMarker()
marker_0_8.SetName('steer_hub_4')
body_0.AddMarker(marker_0_8)
marker_0_8.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.31253092150176,0.0930823133197879,-0.00965409264253692),chrono.ChQuaterniond(0.500000000000007,-0.499999999999998,-0.499999999999993,-0.500000000000002)))

# Auxiliary marker (coordinate system feature)
marker_0_9 = chrono.ChMarker()
marker_0_9.SetName('drive_hub_1')
body_0.AddMarker(marker_0_9)
marker_0_9.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.678578790604469,0.147582313319621,0.557519637758449),chrono.ChQuaterniond(0.99455322937025,9.65503809338631E-15,-0.104229909091423,4.26459017704533E-16)))

# Auxiliary marker (coordinate system feature)
marker_0_10 = chrono.ChMarker()
marker_0_10.SetName('drive_hub_2')
body_0.AddMarker(marker_0_10)
marker_0_10.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.313556127045162,0.147582313319781,0.558415907359236),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_11 = chrono.ChMarker()
marker_0_11.SetName('drive_hub_3')
body_0.AddMarker(marker_0_11)
marker_0_11.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.687130921500887,0.147582313318139,-0.050904092642536),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_12 = chrono.ChMarker()
marker_0_12.SetName('drive_hub_4')
body_0.AddMarker(marker_0_12)
marker_0_12.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.31253092150176,0.147582313319788,-0.0509040926425358),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_13 = chrono.ChMarker()
marker_0_13.SetName('drive_wheel_1')
body_0.AddMarker(marker_0_13)
marker_0_13.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.678578790604459,0.147582313319741,0.557519637758417),chrono.ChQuaterniond(0.991087846823857,-0.0086934126166222,-0.103866734454707,0.0829518289662404)))

# Auxiliary marker (coordinate system feature)
marker_0_14 = chrono.ChMarker()
marker_0_14.SetName('drive_wheel_2')
body_0.AddMarker(marker_0_14)
marker_0_14.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.313556127045162,0.147582313319781,0.558415907359236),chrono.ChQuaterniond(0.999650404071471,4.83872123341665E-15,-3.02512959443703E-16,0.0264399251085184)))

# Auxiliary marker (coordinate system feature)
marker_0_15 = chrono.ChMarker()
marker_0_15.SetName('drive_wheel_3')
body_0.AddMarker(marker_0_15)
marker_0_15.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.687130921500886,0.147582313318139,-0.050904092642536),chrono.ChQuaterniond(0.999816178919164,4.65191995946034E-15,2.28667013718492E-17,0.0191731158521873)))

# Auxiliary marker (coordinate system feature)
marker_0_16 = chrono.ChMarker()
marker_0_16.SetName('drive_wheel_4')
body_0.AddMarker(marker_0_16)
marker_0_16.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.31253092150176,0.147582313319788,-0.0509040926425359),chrono.ChQuaterniond(0.999472744354863,4.39354786867565E-15,-2.09998822109536E-16,0.0324689588955277)))

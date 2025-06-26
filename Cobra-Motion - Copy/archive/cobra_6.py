# PyChrono model automatically generated using Chrono::SolidWorks add-in
# Assembly: C:\Users\ruiza\Box\0MyFiles_BOX\03_sbel_cad\Cobra_CAD\cobra_assem_4_2.SLDASM


import pychrono as chrono 
import builtins 

# Some global settings 
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'cobra_6_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0 = chrono.ChBodyAuxRef()
body_0.SetName('SLDW_GROUND')
body_0.SetFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('hub_assem-2')
body_1.SetPos(chrono.ChVector3d(-0.31057651221722,0.0152569187836753,0.115855478526423))
body_1.SetRot(chrono.ChQuaterniond(0.00129962045144924,-0.106401479115182,0.994322390821007,0.00013907112985486))
body_1.SetMass(1.5598908069349)
body_1.SetInertiaXX(chrono.ChVector3d(0.00436080523071917,0.00230048447927596,0.00414454522173494))
body_1.SetInertiaXY(chrono.ChVector3d(0.000728725428031431,0.000534309901548283,-0.000448361570726464))
body_1.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0870481233327876,0.072850189784672,0.0857992020333658),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.128151564600374,0.165433452720356,0.0755948276627571), chrono.ChQuaterniond(-0.00101730857317256,0.627854897824528,0.778329312645782,-0.000820632295209695)))

# Visualization shape 
body_1_2_shape = chrono.ChVisualShapeModelFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_1.AddVisualShape(body_1_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961949241651301,0.0165247077633611,0.125761461911144), chrono.ChQuaterniond(0.994322390821007,0.000139071129845377,0.00129962045145291,0.106401479115182)))

# Visualization shape 
body_1_3_shape = chrono.ChVisualShapeModelFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_1.AddVisualShape(body_1_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0713531392165592,0.0218992234984526,0.132196545530042), chrono.ChQuaterniond(0.666388969328945,-0.233706445072318,0.668133245007216,0.234318172586962)))

# Visualization shape 
body_1_3_shape = chrono.ChVisualShapeModelFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_1.AddVisualShape(body_1_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.10393587812052,-0.00766152532301644,0.132281719647764), chrono.ChQuaterniond(0.674333044626005,-0.209685254219403,0.676098113951778,0.210234106175032)))

# Visualization shape 
body_1_3_shape = chrono.ChVisualShapeModelFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_1.AddVisualShape(body_1_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.113244780633865,0.0353364251146471,0.132306053929816), chrono.ChQuaterniond(0.672485001165168,-0.215538590789487,0.674245233230107,0.216102763875997)))

# Visualization shape 
body_1_6_shape = chrono.ChVisualShapeModelFile() 
body_1_6_shape.SetFilename(shapes_dir +'body_1_6.obj') 
body_1.AddVisualShape(body_1_6_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961426426015955,0.0165247077633606,0.14576139357698), chrono.ChQuaterniond(0.999999145822587,4.70059926117162E-15,0.00130704020480688,1.24585519117578E-17)))

exported_items.append(body_1)



# Rigid body part
body_2 = chrono.ChBodyAuxRef()
body_2.SetName('wheel_grouser-2')
body_2.SetPos(chrono.ChVector3d(0.13941963699792,0.0515054360407698,-0.0573689816914893))
body_2.SetRot(chrono.ChQuaterniond(-0.00321429673581218,0.707099475531197,0.0032142967358056,0.707099475531197))
body_2.SetMass(25.7732862791227)
body_2.SetInertiaXX(chrono.ChVector3d(0.192475111227948,0.19248728252612,0.339722968574226))
body_2.SetInertiaXY(chrono.ChVector3d(-1.35640248939885e-11,3.37585270969547e-11,0.00133873121615276))
body_2.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0270700245615144,-0.000185466324721263,0.0154474354006911),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0290351109510424,-0.000185466335892677,0.0154474354087597), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_2_shape = chrono.ChVisualShapeModelFile() 
body_2_2_shape.SetFilename(shapes_dir +'body_2_2.obj') 
body_2.AddVisualShape(body_2_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.00253511095104247,-0.000185466335892677,0.0154474354087597), chrono.ChQuaterniond(0.669230211120907,0.228321975558784,-0.669230211120907,-0.228321975558784)))

# Collision Model

body_2.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_2 = chrono.ChContactMaterialNSC()

# Triangle mesh collision shape 
body_2_1_collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_2_1_collision.obj', False, True) 
mr = chrono.ChMatrix33d()
mr[0,0]=1; mr[1,0]=0; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
mr[0,2]=0; mr[1,2]=0; mr[2,2]=1 
body_2_1_collision_mesh.Transform(chrono.ChVector3d(-0.0290351109510424, -0.000185466335892677, 0.0154474354087597), mr) 
collshape = chrono.ChCollisionShapeTriangleMesh(mat_2,body_2_1_collision_mesh,False,False,sphereswept_r)
body_2.GetCollisionModel().AddShape(collshape)
body_2.EnableCollision(True)

exported_items.append(body_2)



# Rigid body part
body_3 = chrono.ChBodyAuxRef()
body_3.SetName('wheel_grouser-4')
body_3.SetPos(chrono.ChVector3d(-0.235166230784452,0.0510947482299669,-0.0573689816914892))
body_3.SetRot(chrono.ChQuaterniond(-0.0126184239327423,0.70699418341133,0.0126184239327361,0.70699418341133))
body_3.SetMass(25.7732862791227)
body_3.SetInertiaXX(chrono.ChVector3d(0.192475111227948,0.192662630844764,0.339547620255583))
body_3.SetInertiaXY(chrono.ChVector3d(-1.26613317598088e-11,3.41073019698932e-11,0.00525156969192117))
body_3.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0270700245615144,-0.000185466324721263,0.0154474354006911),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_3.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0290351109510424,-0.000185466335892677,0.0154474354087597), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_2_shape = chrono.ChVisualShapeModelFile() 
body_2_2_shape.SetFilename(shapes_dir +'body_2_2.obj') 
body_3.AddVisualShape(body_2_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.00253511095104248,-0.00018546633589267,0.0154474354087597), chrono.ChQuaterniond(0.669230211120907,0.228321975558784,-0.669230211120907,-0.228321975558784)))

# Collision Model

body_3.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_3 = chrono.ChContactMaterialNSC()

# Triangle mesh collision shape 
body_2_1_collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_2_1_collision.obj', False, True) 
mr = chrono.ChMatrix33d()
mr[0,0]=1; mr[1,0]=0; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
mr[0,2]=0; mr[1,2]=0; mr[2,2]=1 
body_2_1_collision_mesh.Transform(chrono.ChVector3d(-0.0290351109510424, -0.000185466335892677, 0.0154474354087597), mr) 
collshape = chrono.ChCollisionShapeTriangleMesh(mat_3,body_2_1_collision_mesh,False,False,sphereswept_r)
body_3.GetCollisionModel().AddShape(collshape)
body_3.EnableCollision(True)

exported_items.append(body_3)



# Rigid body part
body_4 = chrono.ChBodyAuxRef()
body_4.SetName('arm_assembly-1')
body_4.SetPos(chrono.ChVector3d(0.154864747881409,0.0535413321381585,0.115855907357468))
body_4.SetRot(chrono.ChQuaterniond(4.16660120460961e-16,-2.63677968348465e-16,1,4.76768293758141e-15))
body_4.SetMass(0.364051497440596)
body_4.SetInertiaXX(chrono.ChVector3d(0.00408204363389774,0.00104054206771477,0.00318444113837038))
body_4.SetInertiaXY(chrono.ChVector3d(4.23413295717627e-11,-6.11651643539437e-10,0.000719823333564847))
body_4.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-1.59228715578904e-08,0.0724885111288461,0.0511378350659033),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.00500000000000003,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.48277311503641E-17,-1.06871463972545E-17,-0.707106781186547)))

# Visualization shape 
body_4_2_shape = chrono.ChVisualShapeModelFile() 
body_4_2_shape.SetFilename(shapes_dir +'body_4_2.obj') 
body_4.AddVisualShape(body_4_2_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(-4.16660120460961E-16,-2.63677968348465E-16,1,4.76768293758141E-15)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_4.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.00500000000000003,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-5.39835192531853E-17,2.48277311480301E-17,0.707106781186548)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.48277311503641E-17,-1.06871463972545E-17,-0.707106781186547)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_4.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999998,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-5.39835192531853E-17,2.48277311480301E-17,0.707106781186548)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_4.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999995,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-5.39835192531853E-17,2.48277311480301E-17,0.707106781186548)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999998,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.48277311503641E-17,-1.06871463972545E-17,-0.707106781186547)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_4.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.00500000000000003,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-5.39835192531853E-17,2.48277311480301E-17,0.707106781186548)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.48277311503641E-17,-1.06871463972545E-17,-0.707106781186547)))

# Visualization shape 
body_4_10_shape = chrono.ChVisualShapeModelFile() 
body_4_10_shape.SetFilename(shapes_dir +'body_4_10.obj') 
body_4.AddVisualShape(body_4_10_shape, chrono.ChFramed(chrono.ChVector3d(-2.77555756156289E-17,0.14679,0.12551), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_4_11_shape = chrono.ChVisualShapeModelFile() 
body_4_11_shape.SetFilename(shapes_dir +'body_4_11.obj') 
body_4.AddVisualShape(body_4_11_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.0558,0.12551), chrono.ChQuaterniond(0.878355111664487,2.57785531505459E-17,0.478008679641767,2.71383757603969E-17)))

# Visualization shape 
body_4_12_shape = chrono.ChVisualShapeModelFile() 
body_4_12_shape.SetFilename(shapes_dir +'body_4_12.obj') 
body_4.AddVisualShape(body_4_12_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.05261,0.12551), chrono.ChQuaterniond(0.707106781186548,3.73835945085112E-17,0.707106781186547,-1.86871695855872E-18)))

exported_items.append(body_4)



# Rigid body part
body_5 = chrono.ChBodyAuxRef()
body_5.SetName('arm_assembly-2')
body_5.SetPos(chrono.ChVector3d(0.1548647478814,0.0535413321397893,0.391655907359235))
body_5.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_5.SetMass(0.364051497440596)
body_5.SetInertiaXX(chrono.ChVector3d(0.00408204363389774,0.00104054206771479,0.00318444113837037))
body_5.SetInertiaXY(chrono.ChVector3d(-4.23413272324216e-11,-6.11651642362796e-10,-0.000719823333564868))
body_5.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-1.59228715578969e-08,0.0724885111288461,0.0511378350659033),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_5.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.0907100000000001), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_4_2_shape = chrono.ChVisualShapeModelFile() 
body_4_2_shape.SetFilename(shapes_dir +'body_4_2.obj') 
body_5.AddVisualShape(body_4_2_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(-6.12303176911189E-17,-8.14015851325628E-17,1,1.65030317669818E-27)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_5.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.0907100000000001), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_5.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999998,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_5.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999998,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_5.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999998,0.14239,0.0907100000000001), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_5.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999998,0.17059,0.0907100000000001), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_5.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_5.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_4_10_shape = chrono.ChVisualShapeModelFile() 
body_4_10_shape.SetFilename(shapes_dir +'body_4_10.obj') 
body_5.AddVisualShape(body_4_10_shape, chrono.ChFramed(chrono.ChVector3d(0,0.14679,0.12551), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_4_11_shape = chrono.ChVisualShapeModelFile() 
body_4_11_shape.SetFilename(shapes_dir +'body_4_11.obj') 
body_5.AddVisualShape(body_4_11_shape, chrono.ChFramed(chrono.ChVector3d(2.77555756156289E-17,-0.0558,0.12551), chrono.ChQuaterniond(0.878355111664487,0,0.478008679641768,0)))

# Visualization shape 
body_4_12_shape = chrono.ChVisualShapeModelFile() 
body_4_12_shape.SetFilename(shapes_dir +'body_4_12.obj') 
body_5.AddVisualShape(body_4_12_shape, chrono.ChFramed(chrono.ChVector3d(2.77555756156289E-17,-0.05261,0.12551), chrono.ChQuaterniond(0.707106781186548,0,0.707106781186547,0)))

exported_items.append(body_5)



# Rigid body part
body_6 = chrono.ChBodyAuxRef()
body_6.SetName('wheel_grouser-3')
body_6.SetPos(chrono.ChVector3d(-0.214977565414353,0.0668222041244843,0.564880796408194))
body_6.SetRot(chrono.ChQuaterniond(0.438765292178574,0.554513316683604,0.438765292178579,-0.554513316683599))
body_6.SetMass(25.7732862791227)
body_6.SetInertiaXX(chrono.ChVector3d(0.192475111227948,0.331949143225572,0.200261107874774))
body_6.SetInertiaXY(chrono.ChVector3d(-2.95431991923235e-11,2.12324674004656e-11,-0.032953669737147))
body_6.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0270700245615144,-0.000185466324721263,0.0154474354006911),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_6.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0290351109510425,-0.000185466335892698,0.0154474354087597), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_2_shape = chrono.ChVisualShapeModelFile() 
body_2_2_shape.SetFilename(shapes_dir +'body_2_2.obj') 
body_6.AddVisualShape(body_2_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.00253511095104253,-0.000185466335892698,0.0154474354087597), chrono.ChQuaterniond(0.669230211120907,0.228321975558784,-0.669230211120907,-0.228321975558784)))

# Collision Model

body_6.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_6 = chrono.ChContactMaterialNSC()

# Triangle mesh collision shape 
body_2_1_collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_2_1_collision.obj', False, True) 
mr = chrono.ChMatrix33d()
mr[0,0]=1; mr[1,0]=0; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
mr[0,2]=0; mr[1,2]=0; mr[2,2]=1 
body_2_1_collision_mesh.Transform(chrono.ChVector3d(-0.0290351109510425, -0.000185466335892698, 0.0154474354087597), mr) 
collshape = chrono.ChCollisionShapeTriangleMesh(mat_6,body_2_1_collision_mesh,False,False,sphereswept_r)
body_6.GetCollisionModel().AddShape(collshape)
body_6.EnableCollision(True)

exported_items.append(body_6)



# Rigid body part
body_7 = chrono.ChBodyAuxRef()
body_7.SetName('wheel_grouser-1')
body_7.SetPos(chrono.ChVector3d(0.146929958879163,0.0671497214450013,0.564258946844999))
body_7.SetRot(chrono.ChQuaterniond(0.51607057398506,0.580804059344094,0.418162284117186,-0.470614610332116))
body_7.SetMass(25.7732862791227)
body_7.SetInertiaXX(chrono.ChVector3d(0.198804848043728,0.331455610706199,0.194424903578368))
body_7.SetInertiaXY(chrono.ChVector3d(0.0296599053323516,-0.00351307165898384,-0.0164615648792474))
body_7.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0270700245615144,-0.000185466324721263,0.0154474354006911),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_7.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0290351109510425,-0.00018546633589267,0.0154474354087597), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_2_shape = chrono.ChVisualShapeModelFile() 
body_2_2_shape.SetFilename(shapes_dir +'body_2_2.obj') 
body_7.AddVisualShape(body_2_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.00253511095104253,-0.00018546633589267,0.0154474354087597), chrono.ChQuaterniond(0.669230211120907,0.228321975558784,-0.669230211120907,-0.228321975558784)))

# Collision Model

body_7.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_7 = chrono.ChContactMaterialNSC()

# Triangle mesh collision shape 
body_2_1_collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_2_1_collision.obj', False, True) 
mr = chrono.ChMatrix33d()
mr[0,0]=1; mr[1,0]=0; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
mr[0,2]=0; mr[1,2]=0; mr[2,2]=1 
body_2_1_collision_mesh.Transform(chrono.ChVector3d(-0.0290351109510425, -0.00018546633589267, 0.0154474354087597), mr) 
collshape = chrono.ChCollisionShapeTriangleMesh(mat_7,body_2_1_collision_mesh,False,False,sphereswept_r)
body_7.GetCollisionModel().AddShape(collshape)
body_7.EnableCollision(True)

exported_items.append(body_7)



# Rigid body part
body_8 = chrono.ChBodyAuxRef()
body_8.SetName('hub_assem-1')
body_8.SetPos(chrono.ChVector3d(0.269753426683056,0.0152569187836265,0.413216984927633))
body_8.SetRot(chrono.ChQuaterniond(0.988771085504673,0.0109519028540781,-0.104930674119787,-0.105836430034996))
body_8.SetMass(1.5598908069349)
body_8.SetInertiaXX(chrono.ChVector3d(0.00465607158005443,0.00215899285401024,0.0039907704976654))
body_8.SetInertiaXY(chrono.ChVector3d(0.000436954311009608,0.000173291619565752,0.000637494334735007))
body_8.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0870481233327876,0.072850189784672,0.0857992020333658),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_8.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.128151564600374,0.165433452720356,0.0755948276627572), chrono.ChQuaterniond(-0.00101730857317255,0.627854897824528,0.778329312645782,-0.000820632295209674)))

# Visualization shape 
body_1_2_shape = chrono.ChVisualShapeModelFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_8.AddVisualShape(body_1_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961949241651301,0.0165247077633611,0.125761461911144), chrono.ChQuaterniond(0.994322390821007,0.000139071129845386,0.00129962045145289,0.106401479115182)))

# Visualization shape 
body_1_3_shape = chrono.ChVisualShapeModelFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_8.AddVisualShape(body_1_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0713531392165592,0.0218992234984526,0.132196545530042), chrono.ChQuaterniond(0.666388969328945,-0.233706445072318,0.668133245007217,0.234318172586962)))

# Visualization shape 
body_1_3_shape = chrono.ChVisualShapeModelFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_8.AddVisualShape(body_1_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.10393587812052,-0.00766152532301644,0.132281719647764), chrono.ChQuaterniond(0.674333044626005,-0.209685254219402,0.676098113951778,0.210234106175032)))

# Visualization shape 
body_1_3_shape = chrono.ChVisualShapeModelFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_8.AddVisualShape(body_1_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.113244780633865,0.0353364251146471,0.132306053929816), chrono.ChQuaterniond(0.672485001165168,-0.215538590789487,0.674245233230107,0.216102763875997)))

# Visualization shape 
body_1_6_shape = chrono.ChVisualShapeModelFile() 
body_1_6_shape.SetFilename(shapes_dir +'body_1_6.obj') 
body_8.AddVisualShape(body_1_6_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961426426015955,0.0165247077633606,0.14576139357698), chrono.ChQuaterniond(0.999999145822587,4.70110463547454E-15,0.0013070402048069,4.33681239434921E-19)))

exported_items.append(body_8)



# Rigid body part
body_9 = chrono.ChBodyAuxRef()
body_9.SetName('arm_assembly-3')
body_9.SetPos(chrono.ChVector3d(-0.218710046574314,0.0535413321398374,0.391655907359236))
body_9.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_9.SetMass(0.364051497440596)
body_9.SetInertiaXX(chrono.ChVector3d(0.00408204363389774,0.00104054206771479,0.00318444113837037))
body_9.SetInertiaXY(chrono.ChVector3d(-4.23413272321462e-11,-6.11651642359771e-10,-0.000719823333564868))
body_9.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-1.59228715578875e-08,0.0724885111288461,0.0511378350659033),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_9.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_4_2_shape = chrono.ChVisualShapeModelFile() 
body_4_2_shape.SetFilename(shapes_dir +'body_4_2.obj') 
body_9.AddVisualShape(body_4_2_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(-6.12303176911189E-17,-8.14015851325628E-17,1,1.65030317669818E-27)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_9.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_9.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999998,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_9.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999998,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_9.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999998,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_9.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999998,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_9.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_9.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_4_10_shape = chrono.ChVisualShapeModelFile() 
body_4_10_shape.SetFilename(shapes_dir +'body_4_10.obj') 
body_9.AddVisualShape(body_4_10_shape, chrono.ChFramed(chrono.ChVector3d(0,0.14679,0.12551), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_4_11_shape = chrono.ChVisualShapeModelFile() 
body_4_11_shape.SetFilename(shapes_dir +'body_4_11.obj') 
body_9.AddVisualShape(body_4_11_shape, chrono.ChFramed(chrono.ChVector3d(2.77555756156289E-17,-0.0558,0.12551), chrono.ChQuaterniond(0.878355111664487,0,0.478008679641768,0)))

# Visualization shape 
body_4_12_shape = chrono.ChVisualShapeModelFile() 
body_4_12_shape.SetFilename(shapes_dir +'body_4_12.obj') 
body_9.AddVisualShape(body_4_12_shape, chrono.ChFramed(chrono.ChVector3d(2.77555756156289E-17,-0.05261,0.12551), chrono.ChQuaterniond(0.707106781186548,0,0.707106781186547,0)))

exported_items.append(body_9)



# Rigid body part
body_10 = chrono.ChBodyAuxRef()
body_10.SetName('arm_assembly-4')
body_10.SetPos(chrono.ChVector3d(-0.219735252117716,0.0535413321398353,0.115855907357468))
body_10.SetRot(chrono.ChQuaterniond(4.92844550549504e-16,-2.77555756156281e-16,1,4.44029194545789e-15))
body_10.SetMass(0.364051497440596)
body_10.SetInertiaXX(chrono.ChVector3d(0.00408204363389774,0.00104054206771477,0.00318444113837038))
body_10.SetInertiaXY(chrono.ChVector3d(4.23413299020186e-11,-6.11651643752257e-10,0.000719823333564849))
body_10.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-1.59228715578904e-08,0.0724885111288461,0.0511378350659033),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_10.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-1.44170911167254E-17,1.40037966721206E-17,-0.707106781186547)))

# Visualization shape 
body_4_2_shape = chrono.ChVisualShapeModelFile() 
body_4_2_shape.SetFilename(shapes_dir +'body_4_2.obj') 
body_10.AddVisualShape(body_4_2_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(-4.92844550549504E-16,-2.77555756156281E-16,1,4.44029194545789E-15)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_10.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.92925761838102E-17,1.44170911143914E-17,0.707106781186547)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_10.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-1.44170911167254E-17,1.40037966721206E-17,-0.707106781186547)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_10.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999998,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.92925761838102E-17,1.44170911143914E-17,0.707106781186547)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_10.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999998,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.92925761838102E-17,1.44170911143914E-17,0.707106781186547)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_10.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-1.44170911167254E-17,1.40037966721206E-17,-0.707106781186547)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_10.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.92925761838102E-17,1.44170911143914E-17,0.707106781186547)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_10.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-1.44170911167254E-17,1.40037966721206E-17,-0.707106781186547)))

# Visualization shape 
body_4_10_shape = chrono.ChVisualShapeModelFile() 
body_4_10_shape.SetFilename(shapes_dir +'body_4_10.obj') 
body_10.AddVisualShape(body_4_10_shape, chrono.ChFramed(chrono.ChVector3d(-2.77555756156289E-17,0.14679,0.12551), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_4_11_shape = chrono.ChVisualShapeModelFile() 
body_4_11_shape.SetFilename(shapes_dir +'body_4_11.obj') 
body_10.AddVisualShape(body_4_11_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.0558,0.12551), chrono.ChQuaterniond(0.878355111664487,5.53303520153522E-17,0.478008679641767,4.48614121768739E-18)))

# Visualization shape 
body_4_12_shape = chrono.ChVisualShapeModelFile() 
body_4_12_shape.SetFilename(shapes_dir +'body_4_12.obj') 
body_10.AddVisualShape(body_4_12_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.05261,0.12551), chrono.ChQuaterniond(0.707106781186548,3.94589586905534E-17,0.707106781186547,-3.90456642436136E-17)))

exported_items.append(body_10)



# Rigid body part
body_11 = chrono.ChBodyAuxRef()
body_11.SetName('Assem6^cobra_assem_4_2-1')
body_11.SetPos(chrono.ChVector3d(-0.174970014956003,-0.262782497587976,0))
body_11.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_11.SetMass(6.97473074164516)
body_11.SetInertiaXX(chrono.ChVector3d(0.0957495205291372,0.114521734329455,0.157528973910192))
body_11.SetInertiaXY(chrono.ChVector3d(-0.000916434954738614,4.03319210062137e-06,1.60366675051668e-05))
body_11.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.144911276105567,0.445556856782739,0.253735221947171),chrono.ChQuaterniond(1,0,0,0)))
body_11.SetFixed(True)

# Visualization shape 
body_11_1_shape = chrono.ChVisualShapeModelFile() 
body_11_1_shape.SetFilename(shapes_dir +'body_11_1.obj') 
body_11.AddVisualShape(body_11_1_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834166,0.426513829733399,0.347405907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_2_shape = chrono.ChVisualShapeModelFile() 
body_11_2_shape.SetFilename(shapes_dir +'body_11_2.obj') 
body_11.AddVisualShape(body_11_2_shape, chrono.ChFramed(chrono.ChVector3d(0.202834762834166,0.629713829733399,0.122640907358352), chrono.ChQuaterniond(0,0,1,0)))

# Visualization shape 
body_11_2_shape = chrono.ChVisualShapeModelFile() 
body_11_2_shape.SetFilename(shapes_dir +'body_11_2.obj') 
body_11.AddVisualShape(body_11_2_shape, chrono.ChFramed(chrono.ChVector3d(0.101234762834166,0.629713829733399,0.384870907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_4_shape = chrono.ChVisualShapeModelFile() 
body_11_4_shape.SetFilename(shapes_dir +'body_11_4.obj') 
body_11.AddVisualShape(body_11_4_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762834166,0.634476329733399,0.253449907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_2_shape = chrono.ChVisualShapeModelFile() 
body_11_2_shape.SetFilename(shapes_dir +'body_11_2.obj') 
body_11.AddVisualShape(body_11_2_shape, chrono.ChFramed(chrono.ChVector3d(0.202834762834166,0.540813829733399,0.122640907358352), chrono.ChQuaterniond(0,0,1,0)))

# Visualization shape 
body_11_4_shape = chrono.ChVisualShapeModelFile() 
body_11_4_shape.SetFilename(shapes_dir +'body_11_4.obj') 
body_11.AddVisualShape(body_11_4_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762834166,0.545576329733399,0.253449907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_2_shape = chrono.ChVisualShapeModelFile() 
body_11_2_shape.SetFilename(shapes_dir +'body_11_2.obj') 
body_11.AddVisualShape(body_11_2_shape, chrono.ChFramed(chrono.ChVector3d(0.101234762834166,0.540813829733399,0.384870907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_2_shape = chrono.ChVisualShapeModelFile() 
body_11_2_shape.SetFilename(shapes_dir +'body_11_2.obj') 
body_11.AddVisualShape(body_11_2_shape, chrono.ChFramed(chrono.ChVector3d(0.202834762834166,0.451913829733399,0.122640907358352), chrono.ChQuaterniond(0,0,1,0)))

# Visualization shape 
body_11_4_shape = chrono.ChVisualShapeModelFile() 
body_11_4_shape.SetFilename(shapes_dir +'body_11_4.obj') 
body_11.AddVisualShape(body_11_4_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762834166,0.456676329733399,0.253449907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_1_shape = chrono.ChVisualShapeModelFile() 
body_11_1_shape.SetFilename(shapes_dir +'body_11_1.obj') 
body_11.AddVisualShape(body_11_1_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834166,0.426513829733399,0.153755907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_2_shape = chrono.ChVisualShapeModelFile() 
body_11_2_shape.SetFilename(shapes_dir +'body_11_2.obj') 
body_11.AddVisualShape(body_11_2_shape, chrono.ChFramed(chrono.ChVector3d(0.101234762834166,0.451913829733399,0.384870907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.043740031618308,0.324323829727832,0.385076107359235), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,-3.87555566842849E-15,-3.85864489921714E-15)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617132,0.39932382972781,0.123355907359389), chrono.ChQuaterniond(0.70710678118655,-0.707106781186545,2.59350884430325E-15,-3.28368045020259E-15)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837411,0.32432382972613,0.123355907345257), chrono.ChQuaterniond(-2.42051107587712E-15,3.16604287669643E-15,0.707106781186551,-0.707106781186544)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837402,0.324323829726011,0.384155907359311), chrono.ChQuaterniond(3.03943339214823E-15,2.84466058660162E-15,0.707106781186544,0.707106781186551)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837411,0.399323829726133,0.123355907344982), chrono.ChQuaterniond(0.707106781186551,-0.707106781186544,2.50389615269494E-15,-3.01391408471168E-15)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0437400316183114,0.399323829727813,0.385076107359236), chrono.ChQuaterniond(4.39389193448936E-16,5.79964487832136E-17,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837403,0.399323829727762,0.384155907361403), chrono.ChQuaterniond(3.08604551201541E-15,2.79804846673445E-15,0.707106781186544,0.707106781186551)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617139,0.324323829728003,0.123355907357452), chrono.ChQuaterniond(0.70710678118655,-0.707106781186545,2.56160942495213E-15,-3.25179140527763E-15)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834165,0.680113829730607,0.141055907357911), chrono.ChQuaterniond(-9.53150529647208E-16,0.707106781186548,5.71890317788325E-16,-0.707106781186547)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.126634762834165,0.677351329730607,0.141055907357911), chrono.ChQuaterniond(-9.53150529647208E-16,0.707106781186548,5.71890317788325E-16,-0.707106781186547)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.136572262834165,0.667413829730607,0.141055907357911), chrono.ChQuaterniond(0.500000000000001,-0.5,0.499999999999999,0.5)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617162,0.680113829730608,0.153755907360262), chrono.ChQuaterniond(5.39183362404072E-16,0,-8.08775043606108E-16,1)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617162,0.677351329730608,0.166455907360262), chrono.ChQuaterniond(5.39183362404072E-16,0,-8.08775043606108E-16,1)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617162,0.667413829730608,0.156518407360262), chrono.ChQuaterniond(3.81260211858883E-16,3.81260211858883E-16,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612741,0.680113829730608,0.141055907358866), chrono.ChQuaterniond(-1.90630105929442E-16,0.707106781186548,-1.33441074173247E-15,0.707106781186547)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612741,0.677351329730608,0.141055907358866), chrono.ChQuaterniond(-1.90630105929442E-16,0.707106781186548,-1.33441074173247E-15,0.707106781186547)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612741,0.667413829730608,0.141055907358866), chrono.ChQuaterniond(0.5,-0.5,-0.499999999999999,-0.500000000000001)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(-0.032065237161274,0.680113829730607,0.367553348962111), chrono.ChQuaterniond(0.499999999999999,0.500000000000001,0.5,-0.5)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.029302737161274,0.667413829730607,0.367553348962111), chrono.ChQuaterniond(0.499999999999999,0.500000000000001,0.5,-0.5)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612739,0.677351329730607,0.367553348962111), chrono.ChQuaterniond(-6.99327703394595E-16,0.707106781186548,4.44452932513277E-16,-0.707106781186547)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616918,0.680113829730608,0.353755907356447), chrono.ChQuaterniond(-8.08775043606108E-16,1,-1.07836672480814E-15,2.69591681202036E-16)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616918,0.677351329730608,0.341055907356447), chrono.ChQuaterniond(-8.08775043606108E-16,1,-1.07836672480814E-15,2.69591681202036E-16)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616918,0.667413829730608,0.350993407356447), chrono.ChQuaterniond(0.707106781186548,-0.707106781186547,5.71890317788325E-16,-9.53150529647208E-16)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.3298347628374,0.305113829730607,0.353755907356443), chrono.ChQuaterniond(8.47409175530384E-33,-1.80411241501588E-16,1,-3.41856075107737E-17)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.307876329730607,0.341055907356443), chrono.ChQuaterniond(8.47409175530384E-33,-1.80411241501588E-16,1,-3.41856075107737E-17)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.317813829730607,0.350993407356443), chrono.ChQuaterniond(1.3738309013483E-16,-1.17756934401283E-16,0.707106781186548,-0.707106781186547)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.164734762836957,0.305113829730607,0.366455907358794), chrono.ChQuaterniond(0.707106781186548,5.71890317788325E-16,0.707106781186547,1.90630105929442E-16)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.177434762836957,0.307876329730607,0.366455907358794), chrono.ChQuaterniond(0.707106781186548,5.71890317788325E-16,0.707106781186547,1.90630105929442E-16)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.167497262836957,0.317813829730607,0.366455907358794), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834165,0.305113829730607,0.366455907358794), chrono.ChQuaterniond(0.707106781186548,-3.81260211858883E-16,-0.707106781186547,0)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.126634762834165,0.307876329730607,0.366455907358794), chrono.ChQuaterniond(0.707106781186548,-3.81260211858883E-16,-0.707106781186547,0)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.136572262834165,0.317813829730607,0.366455907358794), chrono.ChQuaterniond(0.5,0.5,-0.5,0.5)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.305113829730607,0.36645590735784), chrono.ChQuaterniond(0.707106781186547,-3.81260211858883E-16,-0.707106781186548,-7.62520423717767E-16)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836957,0.307876329730607,0.36645590735784), chrono.ChQuaterniond(0.707106781186547,-3.81260211858883E-16,-0.707106781186548,-7.62520423717767E-16)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.317813829730607,0.36645590735784), chrono.ChQuaterniond(0.5,0.499999999999999,-0.500000000000001,0.5)))

# Visualization shape 
body_11_47_shape = chrono.ChVisualShapeModelFile() 
body_11_47_shape.SetFilename(shapes_dir +'body_11_47.obj') 
body_11.AddVisualShape(body_11_47_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371621582,0.692813829731486,0.141055907357469), chrono.ChQuaterniond(0.707106781186548,-3.8126021208526E-16,0.707106781186547,0)))

# Visualization shape 
body_11_48_shape = chrono.ChVisualShapeModelFile() 
body_11_48_shape.SetFilename(shapes_dir +'body_11_48.obj') 
body_11.AddVisualShape(body_11_48_shape, chrono.ChFramed(chrono.ChVector3d(-0.044765237161274,0.692813829731486,0.179155907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_48_shape = chrono.ChVisualShapeModelFile() 
body_11_48_shape.SetFilename(shapes_dir +'body_11_48.obj') 
body_11.AddVisualShape(body_11_48_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837842,0.692813829731485,0.179155907358353), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_47_shape = chrono.ChVisualShapeModelFile() 
body_11_47_shape.SetFilename(shapes_dir +'body_11_47.obj') 
body_11.AddVisualShape(body_11_47_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371621581,0.692813829731486,0.366455907358352), chrono.ChQuaterniond(0.707106781186548,3.81260211858883E-16,0.707106781186547,0)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.692813829732003,0.153755907358353), chrono.ChQuaterniond(0.5,0.5,-0.5,-0.5)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.692813829732003,0.156518407358353), chrono.ChQuaterniond(0.5,0.5,-0.5,-0.5)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.692813829732003,0.166455907358353), chrono.ChQuaterniond(6.31927204887826E-17,0.707106781186548,-0.707106781186547,-6.31927204887825E-17)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(-0.032065237161274,0.692813829732003,0.353755907358352), chrono.ChQuaterniond(0.5,-0.5,0.5,-0.5)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.019365237161274,0.692813829732003,0.350993407358352), chrono.ChQuaterniond(0.5,-0.5,0.5,-0.5)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.029302737161274,0.692813829732003,0.341055907358352), chrono.ChQuaterniond(0.707106781186547,-4.96290709266116E-17,1.36224676550161E-16,-0.707106781186548)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(-0.032065237161274,0.692813829732003,0.153755907358353), chrono.ChQuaterniond(0.707106781186547,2.97341532496038E-17,-2.97341532496038E-17,-0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.029302737161274,0.692813829732003,0.166455907358353), chrono.ChQuaterniond(0.707106781186547,2.97341532496038E-17,-2.97341532496038E-17,-0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.019365237161274,0.692813829732003,0.156518407358353), chrono.ChQuaterniond(-0.5,-0.5,0.5,0.5)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.692813829731978,0.353755907358375), chrono.ChQuaterniond(0.500000000000016,-0.499999999999983,-0.500000000000017,0.499999999999984)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.692813829731978,0.350993407358375), chrono.ChQuaterniond(0.500000000000016,-0.499999999999983,-0.500000000000017,0.499999999999984)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.692813829731979,0.341055907358375), chrono.ChQuaterniond(0.707106781186547,2.32369780257537E-14,-2.33633634667313E-14,0.707106781186548)))

# Visualization shape 
body_11_47_shape = chrono.ChVisualShapeModelFile() 
body_11_47_shape.SetFilename(shapes_dir +'body_11_47.obj') 
body_11.AddVisualShape(body_11_47_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371621584,0.292413829728693,0.141055907357469), chrono.ChQuaterniond(0.707106781186548,-3.8126021208526E-16,0.707106781186547,0)))

# Visualization shape 
body_11_48_shape = chrono.ChVisualShapeModelFile() 
body_11_48_shape.SetFilename(shapes_dir +'body_11_48.obj') 
body_11.AddVisualShape(body_11_48_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371612743,0.292413829728693,0.179155907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_48_shape = chrono.ChVisualShapeModelFile() 
body_11_48_shape.SetFilename(shapes_dir +'body_11_48.obj') 
body_11.AddVisualShape(body_11_48_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837842,0.292413829728693,0.179155907358353), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_47_shape = chrono.ChVisualShapeModelFile() 
body_11_47_shape.SetFilename(shapes_dir +'body_11_47.obj') 
body_11.AddVisualShape(body_11_47_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371621584,0.292413829728693,0.366455907358352), chrono.ChQuaterniond(0.707106781186548,3.81260211858883E-16,0.707106781186547,0)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.292413829729211,0.153755907358353), chrono.ChQuaterniond(0.5,0.5,-0.5,-0.5)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.292413829729211,0.156518407358353), chrono.ChQuaterniond(0.5,0.5,-0.5,-0.5)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.292413829729211,0.166455907358353), chrono.ChQuaterniond(6.31927204887826E-17,0.707106781186548,-0.707106781186547,-6.31927204887825E-17)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612742,0.292413829729211,0.353755907358352), chrono.ChQuaterniond(0.5,-0.5,0.5,-0.5)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612743,0.292413829729211,0.350993407358352), chrono.ChQuaterniond(0.5,-0.5,0.5,-0.5)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612742,0.292413829729211,0.341055907358352), chrono.ChQuaterniond(0.707106781186547,-4.96290709266116E-17,1.36224676550161E-16,-0.707106781186548)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612743,0.292413829729211,0.153755907358353), chrono.ChQuaterniond(0.707106781186547,2.97341532496038E-17,-2.97341532496038E-17,-0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612743,0.292413829729211,0.166455907358353), chrono.ChQuaterniond(0.707106781186547,2.97341532496038E-17,-2.97341532496038E-17,-0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612743,0.292413829729211,0.156518407358353), chrono.ChQuaterniond(-0.5,-0.5,0.5,0.5)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.292413829729186,0.353755907358375), chrono.ChQuaterniond(0.500000000000016,-0.499999999999983,-0.500000000000017,0.499999999999984)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.292413829729186,0.350993407358375), chrono.ChQuaterniond(0.500000000000016,-0.499999999999983,-0.500000000000017,0.499999999999984)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.292413829729186,0.341055907358375), chrono.ChQuaterniond(0.707106781186547,2.32369780257537E-14,-2.33633634667313E-14,0.707106781186548)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617163,0.305113829730607,0.153755907360262), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617163,0.307876329730607,0.166455907360262), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617163,0.317813829730607,0.156518407360262), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,1.74315279842105E-32,1.93528837224682E-48)))

# Visualization shape 
body_11_82_shape = chrono.ChVisualShapeModelFile() 
body_11_82_shape.SetFilename(shapes_dir +'body_11_82.obj') 
body_11.AddVisualShape(body_11_82_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762836079,0.654713829730607,0.141055907358352), chrono.ChQuaterniond(-0.5,-0.5,0.500000000000001,-0.5)))

# Visualization shape 
body_11_83_shape = chrono.ChVisualShapeModelFile() 
body_11_83_shape.SetFilename(shapes_dir +'body_11_83.obj') 
body_11.AddVisualShape(body_11_83_shape, chrono.ChFramed(chrono.ChVector3d(-0.0379652371644393,0.365438829731491,0.253755907358352), chrono.ChQuaterniond(-5.39183362404072E-16,1,7.75060634674567E-18,-6.52099496614874E-17)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.360263829731491,0.307095907358351), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_82_shape = chrono.ChVisualShapeModelFile() 
body_11_82_shape.SetFilename(shapes_dir +'body_11_82.obj') 
body_11.AddVisualShape(body_11_82_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762836078,0.654713829730607,0.366455907359236), chrono.ChQuaterniond(-0.5,-0.5,0.500000000000001,-0.5)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.330513829730607,0.353755907358351), chrono.ChQuaterniond(-5.81233805195342E-16,1,-2.69591681202036E-16,5.39183362564145E-16)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.327751329730607,0.341055907358351), chrono.ChQuaterniond(-5.81233805195342E-16,1,-2.69591681202036E-16,5.39183362564145E-16)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.317813829730607,0.350993407358351), chrono.ChQuaterniond(0.707106781186548,-0.707106781186547,-1.9063010604263E-16,-5.71890317901514E-16)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.355913829731492,0.153755907358351), chrono.ChQuaterniond(2.38487553120783E-14,-2.27580538441475E-14,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.368613829731492,0.156518407358351), chrono.ChQuaterniond(2.38487553120783E-14,-2.27580538441475E-14,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283556,0.358676329731492,0.166455907358351), chrono.ChQuaterniond(3.29143574404111E-14,7.71242404223993E-16,1,6.87057791361391E-16)))

# Visualization shape 
body_11_48_shape = chrono.ChVisualShapeModelFile() 
body_11_48_shape.SetFilename(shapes_dir +'body_11_48.obj') 
body_11.AddVisualShape(body_11_48_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762836079,0.343213829730607,0.328355907358351), chrono.ChQuaterniond(3.81260211858883E-16,-0.707106781186547,0.707106781186548,3.81260211858883E-16)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283556,0.355913829731492,0.353755907358351), chrono.ChQuaterniond(5.53061150371959E-16,1.30683382441082E-15,1,2.90599267418406E-16)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283556,0.358676329731492,0.341055907358352), chrono.ChQuaterniond(5.53061150371959E-16,1.30683382441082E-15,1,2.90599267418406E-16)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283556,0.368613829731492,0.350993407358352), chrono.ChQuaterniond(-5.23184691419221E-16,1.30533127109691E-15,0.707106781186548,-0.707106781186547)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835541,0.330513829730622,0.153755907358351), chrono.ChQuaterniond(0.707106781186547,0.707106781186548,-2.34475030493601E-14,-2.34475030493601E-14)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283554,0.317813829730622,0.156518407358351), chrono.ChQuaterniond(0.707106781186547,0.707106781186548,-2.34475030493601E-14,-2.34475030493601E-14)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835541,0.327751329730622,0.166455907358351), chrono.ChQuaterniond(-4.49815360045584E-16,1,-3.31597768161896E-14,-2.05642184200826E-29)))

# Visualization shape 
body_11_99_shape = chrono.ChVisualShapeModelFile() 
body_11_99_shape.SetFilename(shapes_dir +'body_11_99.obj') 
body_11.AddVisualShape(body_11_99_shape, chrono.ChFramed(chrono.ChVector3d(-0.0229652371644388,0.359088829731491,0.317255907358351), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_100_shape = chrono.ChVisualShapeModelFile() 
body_11_100_shape.SetFilename(shapes_dir +'body_11_100.obj') 
body_11.AddVisualShape(body_11_100_shape, chrono.ChFramed(chrono.ChVector3d(0.327034762835561,0.368613829731491,0.253755907358351), chrono.ChQuaterniond(-2.55140024536113E-16,1.2612018732277E-16,0.707106781186548,-0.707106781186547)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.360263829731491,0.200415907358351), chrono.ChQuaterniond(-6.12323399573674E-17,-9.3664216290059E-25,1,6.70601807553831E-16)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.164734762836957,0.305113829730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186548,3.81260211858883E-16,0.707106781186547,0)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.177434762836957,0.307876329730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186548,3.81260211858883E-16,0.707106781186547,0)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.167497262836957,0.317813829730607,0.141055907357911), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_11_82_shape = chrono.ChVisualShapeModelFile() 
body_11_82_shape.SetFilename(shapes_dir +'body_11_82.obj') 
body_11.AddVisualShape(body_11_82_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837842,0.654713829730607,0.366455907357322), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,-3.81260211858883E-16,0)))

# Visualization shape 
body_11_82_shape = chrono.ChVisualShapeModelFile() 
body_11_82_shape.SetFilename(shapes_dir +'body_11_82.obj') 
body_11.AddVisualShape(body_11_82_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371612741,0.654713829730607,0.366455907357323), chrono.ChQuaterniond(0.707106781186547,0.707106781186548,-3.81260211858883E-16,-3.4863055968421E-32)))

# Visualization shape 
body_11_82_shape = chrono.ChVisualShapeModelFile() 
body_11_82_shape.SetFilename(shapes_dir +'body_11_82.obj') 
body_11.AddVisualShape(body_11_82_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371612745,0.654713829730607,0.141055907358347), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,3.8126021208526E-16,-3.4863055968421E-32)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612743,0.305113829730607,0.141055907358865), chrono.ChQuaterniond(0.707106781186547,-3.8126021208526E-16,0.707106781186548,3.4863055968421E-32)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612743,0.307876329730607,0.141055907358865), chrono.ChQuaterniond(0.707106781186547,-3.8126021208526E-16,0.707106781186548,3.4863055968421E-32)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612743,0.317813829730607,0.141055907358865), chrono.ChQuaterniond(0.5,0.499999999999999,0.5,-0.5)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612742,0.305113829730607,0.367553348962111), chrono.ChQuaterniond(-0.5,0.5,0.5,0.5)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612742,0.317813829730607,0.367553348962111), chrono.ChQuaterniond(-0.5,0.5,0.5,0.5)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612742,0.307876329730607,0.367553348962111), chrono.ChQuaterniond(0.707106781186548,-2.53822826583835E-16,-0.707106781186547,-2.53822826252613E-16)))

# Visualization shape 
body_11_82_shape = chrono.ChVisualShapeModelFile() 
body_11_82_shape.SetFilename(shapes_dir +'body_11_82.obj') 
body_11.AddVisualShape(body_11_82_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837841,0.654713829730607,0.141055907358348), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,3.8126021208526E-16,0)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616935,0.305113829730607,0.353755907356446), chrono.ChQuaterniond(2.69591681202037E-16,-5.39183362404072E-16,1,0)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616935,0.307876329730607,0.341055907356446), chrono.ChQuaterniond(2.69591681202037E-16,-5.39183362404072E-16,1,0)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616935,0.317813829730607,0.350993407356446), chrono.ChQuaterniond(5.71890317788325E-16,-1.90630105929442E-16,0.707106781186548,-0.707106781186547)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834165,0.305113829730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186547,-3.81260211858884E-16,-0.707106781186548,-3.4863055968421E-32)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.126634762834165,0.307876329730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186547,-3.81260211858884E-16,-0.707106781186548,-3.4863055968421E-32)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.136572262834165,0.317813829730607,0.141055907357911), chrono.ChQuaterniond(0.5,0.499999999999999,-0.5,0.5)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.305113829730607,0.153755907360262), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.307876329730607,0.166455907360262), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.317813829730607,0.156518407360262), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,1.74315279842105E-32,1.93528837224682E-48)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836957,0.305113829730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186548,3.8126021208526E-16,-0.707106781186547,0)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836957,0.307876329730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186548,3.8126021208526E-16,-0.707106781186547,0)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836957,0.317813829730607,0.141055907357911), chrono.ChQuaterniond(0.5,0.500000000000001,-0.5,0.5)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.3298347628374,0.680113829730607,0.353755907356444), chrono.ChQuaterniond(-8.42960651116882E-16,1,-7.05716816097846E-16,-1.07481255273164E-31)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.3298347628374,0.677351329730607,0.341055907356444), chrono.ChQuaterniond(-8.42960651116882E-16,1,-7.05716816097846E-16,-1.07481255273164E-31)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.3298347628374,0.667413829730607,0.350993407356444), chrono.ChQuaterniond(0.707106781186548,-0.707106781186547,4.99017146260166E-16,-4.99017146260166E-16)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834165,0.680113829730607,0.366455907358794), chrono.ChQuaterniond(9.53150529647208E-16,-0.707106781186547,-5.71890317788325E-16,0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.126634762834165,0.677351329730607,0.366455907358794), chrono.ChQuaterniond(9.53150529647208E-16,-0.707106781186547,-5.71890317788325E-16,0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.136572262834165,0.667413829730607,0.366455907358794), chrono.ChQuaterniond(0.500000000000001,-0.499999999999999,0.5,0.500000000000001)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.164734762836958,0.680113829730608,0.141055907357911), chrono.ChQuaterniond(-1.90630105929442E-16,0.707106781186547,-5.71890317788325E-16,0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.177434762836958,0.677351329730607,0.141055907357911), chrono.ChQuaterniond(-1.90630105929442E-16,0.707106781186547,-5.71890317788325E-16,0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.167497262836958,0.667413829730607,0.141055907357911), chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.500000000000001)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.680113829730608,0.153755907360262), chrono.ChQuaterniond(5.39183362404072E-16,0,-8.08775043606108E-16,1)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.677351329730608,0.166455907360262), chrono.ChQuaterniond(5.39183362404072E-16,0,-8.08775043606108E-16,1)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.667413829730608,0.156518407360262), chrono.ChQuaterniond(3.81260211858883E-16,3.81260211858883E-16,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.680113829730607,0.36645590735784), chrono.ChQuaterniond(-1.90630105929441E-16,0.707106781186548,5.71890317788325E-16,-0.707106781186547)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.677351329730607,0.36645590735784), chrono.ChQuaterniond(-1.90630105929441E-16,0.707106781186548,5.71890317788325E-16,-0.707106781186547)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.667413829730607,0.36645590735784), chrono.ChQuaterniond(0.5,-0.5,0.499999999999999,0.5)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.164734762836957,0.680113829730607,0.366455907358794), chrono.ChQuaterniond(1.39452223873684E-31,0.707106781186547,-3.81260211858883E-16,0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.177434762836957,0.677351329730607,0.366455907358794), chrono.ChQuaterniond(1.39452223873684E-31,0.707106781186547,-3.81260211858883E-16,0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.167497262836957,0.667413829730607,0.366455907358794), chrono.ChQuaterniond(-0.5,0.5,0.5,0.5)))

# Visualization shape 
body_11_20_shape = chrono.ChVisualShapeModelFile() 
body_11_20_shape.SetFilename(shapes_dir +'body_11_20.obj') 
body_11.AddVisualShape(body_11_20_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836957,0.680113829730607,0.141055907357911), chrono.ChQuaterniond(9.53150529647208E-16,-0.707106781186547,1.90630106155817E-16,0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836957,0.677351329730607,0.141055907357911), chrono.ChQuaterniond(9.53150529647208E-16,-0.707106781186547,1.90630106155817E-16,0.707106781186548)))

# Visualization shape 
body_11_12_shape = chrono.ChVisualShapeModelFile() 
body_11_12_shape.SetFilename(shapes_dir +'body_11_12.obj') 
body_11.AddVisualShape(body_11_12_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836957,0.667413829730607,0.141055907357911), chrono.ChQuaterniond(0.5,-0.499999999999999,0.5,0.5)))

exported_items.append(body_11)



# Rigid body part
body_12 = chrono.ChBodyAuxRef()
body_12.SetName('hub_assem-4')
body_12.SetPos(chrono.ChVector3d(-0.127868786474809,0.0152569187836817,0.391656336190281))
body_12.SetRot(chrono.ChQuaterniond(0.994322390821008,-0.000139071129845742,-0.00129962045144819,-0.106401479115182))
body_12.SetMass(1.5598908069349)
body_12.SetInertiaXX(chrono.ChVector3d(0.00455731911417192,0.0021027534296609,0.00414576238789726))
body_12.SetInertiaXY(chrono.ChVector3d(0.000296279277479677,0.000301244020441806,0.000626930626183415))
body_12.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0870481233327876,0.072850189784672,0.0857992020333658),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_12.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.128151564600374,0.165433452720356,0.0755948276627572), chrono.ChQuaterniond(-0.00101730857317254,0.627854897824528,0.778329312645782,-0.000820632295209681)))

# Visualization shape 
body_1_2_shape = chrono.ChVisualShapeModelFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_12.AddVisualShape(body_1_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961949241651301,0.0165247077633611,0.125761461911144), chrono.ChQuaterniond(0.994322390821008,0.000139071129845742,0.00129962045144819,0.106401479115182)))

# Visualization shape 
body_1_3_shape = chrono.ChVisualShapeModelFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_12.AddVisualShape(body_1_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0713531392165592,0.0218992234984526,0.132196545530042), chrono.ChQuaterniond(0.666388969328945,-0.233706445072318,0.668133245007217,0.234318172586962)))

# Visualization shape 
body_1_3_shape = chrono.ChVisualShapeModelFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_12.AddVisualShape(body_1_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.10393587812052,-0.00766152532301644,0.132281719647764), chrono.ChQuaterniond(0.674333044626005,-0.209685254219402,0.676098113951778,0.210234106175032)))

# Visualization shape 
body_1_3_shape = chrono.ChVisualShapeModelFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_12.AddVisualShape(body_1_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.113244780633865,0.0353364251146472,0.132306053929816), chrono.ChQuaterniond(0.672485001165168,-0.215538590789487,0.674245233230107,0.216102763875997)))

# Visualization shape 
body_1_6_shape = chrono.ChVisualShapeModelFile() 
body_1_6_shape.SetFilename(shapes_dir +'body_1_6.obj') 
body_12.AddVisualShape(body_1_6_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961426426015955,0.0165247077633606,0.14576139357698), chrono.ChQuaterniond(0.999999145822587,4.70120440901168E-15,0.00130704020480687,1.46320688999867E-17)))

exported_items.append(body_12)



# Rigid body part
body_13 = chrono.ChBodyAuxRef()
body_13.SetName('hub_assem-3')
body_13.SetPos(chrono.ChVector3d(0.0640234877819044,0.0152569187820075,0.115855478526423))
body_13.SetRot(chrono.ChQuaterniond(0.00129962045144908,-0.106401479115183,0.994322390821007,0.000139071129855213))
body_13.SetMass(1.5598908069349)
body_13.SetInertiaXX(chrono.ChVector3d(0.00436080523071917,0.00230048447927597,0.00414454522173494))
body_13.SetInertiaXY(chrono.ChVector3d(0.000728725428031433,0.000534309901548284,-0.000448361570726465))
body_13.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0870481233327876,0.072850189784672,0.0857992020333658),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_13.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.128151564600374,0.165433452720356,0.0755948276627572), chrono.ChQuaterniond(-0.00101730857317258,0.627854897824528,0.778329312645782,-0.000820632295209721)))

# Visualization shape 
body_1_2_shape = chrono.ChVisualShapeModelFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_13.AddVisualShape(body_1_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961949241651301,0.0165247077633611,0.125761461911144), chrono.ChQuaterniond(0.994322390821007,0.000139071129845418,0.00129962045145291,0.106401479115182)))

# Visualization shape 
body_1_3_shape = chrono.ChVisualShapeModelFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_13.AddVisualShape(body_1_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0713531392165592,0.0218992234984526,0.132196545530042), chrono.ChQuaterniond(0.666388969328945,-0.233706445072318,0.668133245007216,0.234318172586962)))

# Visualization shape 
body_1_3_shape = chrono.ChVisualShapeModelFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_13.AddVisualShape(body_1_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.10393587812052,-0.00766152532301642,0.132281719647764), chrono.ChQuaterniond(0.674333044626005,-0.209685254219403,0.676098113951778,0.210234106175032)))

# Visualization shape 
body_1_3_shape = chrono.ChVisualShapeModelFile() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_13.AddVisualShape(body_1_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.113244780633865,0.0353364251146471,0.132306053929816), chrono.ChQuaterniond(0.672485001165168,-0.215538590789487,0.674245233230107,0.216102763875997)))

# Visualization shape 
body_1_6_shape = chrono.ChVisualShapeModelFile() 
body_1_6_shape.SetFilename(shapes_dir +'body_1_6.obj') 
body_13.AddVisualShape(body_1_6_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961426426015956,0.0165247077633606,0.14576139357698), chrono.ChQuaterniond(0.999999145822587,4.72100700412701E-15,0.00130704020480689,1.29104006833423E-17)))

exported_items.append(body_13)




# Auxiliary marker (coordinate system feature)
marker_0_1 = chrono.ChMarker()
marker_0_1.SetName('steer_arm_1')
body_0.AddMarker(marker_0_1)
marker_0_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.1548647478814,0.00483133213980971,0.517165907359235),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

# Motor from Solidworks marker
motor_0_1 = chrono.ChLinkMotorRotationTorque()
motor_0_1.SetName("steer_1")
motor_0_1.Initialize(body_5, body_8,chrono.ChFramed(marker_0_1.GetAbsFrame().GetPos(),marker_0_1.GetAbsFrame().GetRot()))
motor_0_1.SetSpindleConstraint(False, False, False, False, False)
exported_items.append(motor_0_1)

motfun_0_1 = chrono.ChFunctionSine()
motor_0_1.SetMotorFunction(motfun_0_1)

# Auxiliary marker (coordinate system feature)
marker_0_2 = chrono.ChMarker()
marker_0_2.SetName('steer_arm_2')
body_0.AddMarker(marker_0_2)
marker_0_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.218710046574314,0.00483133213983736,0.517165907359236),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_3 = chrono.ChMarker()
marker_0_3.SetName('steer_arm_3')
body_0.AddMarker(marker_0_3)
marker_0_3.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.154864747881409,0.00483133213818282,-0.00965409264253277),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_4 = chrono.ChMarker()
marker_0_4.SetName('steer_arm_4')
body_0.AddMarker(marker_0_4)
marker_0_4.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.219735252117715,0.00483133213983334,-0.00965409264253244),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_5 = chrono.ChMarker()
marker_0_5.SetName('steer_hub_1')
body_0.AddMarker(marker_0_5)
marker_0_5.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.154864747881374,-0.0026686678603153,0.51716590735919),chrono.ChQuaterniond(-0.445161660139419,0.445161660139409,0.549391569230832,0.549391569230841)))

# Auxiliary marker (coordinate system feature)
marker_0_6 = chrono.ChMarker()
marker_0_6.SetName('steer_hub_2')
body_0.AddMarker(marker_0_6)
marker_0_6.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.218710046574314,-0.00266866786016256,0.517165907359236),chrono.ChQuaterniond(-0.5,0.5,0.5,0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_7 = chrono.ChMarker()
marker_0_7.SetName('steer_hub_3')
body_0.AddMarker(marker_0_7)
marker_0_7.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.154864747881409,-0.00266866786181699,-0.00965409264253275),chrono.ChQuaterniond(0.500000000000007,-0.499999999999997,-0.499999999999993,-0.500000000000002)))

# Auxiliary marker (coordinate system feature)
marker_0_8 = chrono.ChMarker()
marker_0_8.SetName('steer_hub_4')
body_0.AddMarker(marker_0_8)
marker_0_8.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.219735252117715,-0.00266866786016669,-0.00965409264253272),chrono.ChQuaterniond(0.500000000000007,-0.499999999999998,-0.499999999999993,-0.500000000000002)))

# Auxiliary marker (coordinate system feature)
marker_0_9 = chrono.ChMarker()
marker_0_9.SetName('drive_hub_1')
body_0.AddMarker(marker_0_9)
marker_0_9.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.146312616984957,0.0518313321396832,0.557519637758381),chrono.ChQuaterniond(0.99455322937025,9.65503809338631E-15,-0.104229909091423,4.26459017704533E-16)))

# Auxiliary marker (coordinate system feature)
marker_0_10 = chrono.ChMarker()
marker_0_10.SetName('drive_hub_2')
body_0.AddMarker(marker_0_10)
marker_0_10.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.218710046574314,0.0518313321398367,0.558415907359236),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_11 = chrono.ChMarker()
marker_0_11.SetName('drive_hub_3')
body_0.AddMarker(marker_0_11)
marker_0_11.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.154864747881425,0.0518313321383082,-0.0509040926425787),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_12 = chrono.ChMarker()
marker_0_12.SetName('drive_hub_4')
body_0.AddMarker(marker_0_12)
marker_0_12.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.219735252117697,0.051831332139953,-0.0509040926425783),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_13 = chrono.ChMarker()
marker_0_13.SetName('drive_wheel_1')
body_0.AddMarker(marker_0_13)
marker_0_13.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.146312616984983,0.051831332139804,0.557519637758425),chrono.ChQuaterniond(0.991087846823857,-0.0086934126166222,-0.103866734454707,0.0829518289662404)))

# Auxiliary marker (coordinate system feature)
marker_0_14 = chrono.ChMarker()
marker_0_14.SetName('drive_wheel_2')
body_0.AddMarker(marker_0_14)
marker_0_14.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.218710046574314,0.0518313321398368,0.558415907359236),chrono.ChQuaterniond(0.999650404071471,4.83872123341665E-15,-3.02512959443703E-16,0.0264399251085184)))

# Auxiliary marker (coordinate system feature)
marker_0_15 = chrono.ChMarker()
marker_0_15.SetName('drive_wheel_3')
body_0.AddMarker(marker_0_15)
marker_0_15.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.154864747881722,0.051831332138781,-0.050904092642687),chrono.ChQuaterniond(0.999816178919164,4.65191995946034E-15,2.28667013718492E-17,0.0191731158521873)))

# Auxiliary marker (coordinate system feature)
marker_0_16 = chrono.ChMarker()
marker_0_16.SetName('drive_wheel_4')
body_0.AddMarker(marker_0_16)
marker_0_16.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.219735252117715,0.0518313321398334,-0.0509040926425317),chrono.ChQuaterniond(0.999472744354863,4.39354786867565E-15,-2.09998822109536E-16,0.0324689588955277)))

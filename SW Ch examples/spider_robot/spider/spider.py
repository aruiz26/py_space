# PyChrono model automatically generated using Chrono::SolidWorks add-in
# Assembly: C:\chrono_workspace\py_space\SW Ch examples\spider_robot\SPIDER_ROBOT.SLDASM


import pychrono as chrono 
import builtins 

# Some global settings 
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'spider_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0 = chrono.ChBodyAuxRef()
body_0.SetName('SLDW_GROUND')
body_0.SetFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('M-410iB-300 -1/M-410iB-300-12-1')
body_1.SetPos(chrono.ChVector3d(2.43833354378683,1.53452994138094,0.17486406101182))
body_1.SetRot(chrono.ChQuaterniond(0.999147807992026,-1.93556340972606e-05,0.0412727252884182,-0.000468569478897188))
body_1.SetMass(16.1636065115335)
body_1.SetInertiaXX(chrono.ChVector3d(0.270949711605444,0.400661918859637,0.427371867141467))
body_1.SetInertiaXY(chrono.ChVector3d(-0.0576658362005997,0.0375936407947645,0.0626245655339811))
body_1.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0294847451383035,0.131793864973377,-0.039955675141979),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Collision Model

body_1.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_1 = chrono.ChContactMaterialNSC()
p1 = chrono.ChVector3d(4.57739150408006E-17, 0, 0)
p2 = chrono.ChVector3d(4.57739150408006E-17, 0.147530764880198, 0)
body_1.GetCollisionModel().AddCylinder(mat_1, 0.0891514706007005, p1, p2)
body_1.EnableCollision(True)

exported_items.append(body_1)



# Rigid body part
body_2 = chrono.ChBodyAuxRef()
body_2.SetName('M-410iB-300 -1/M-410iB-300-02-1')
body_2.SetPos(chrono.ChVector3d(-0.140670357955037,2.15049691615662,0.37740311343739))
body_2.SetRot(chrono.ChQuaterniond(0.99914791786433,-2.80761023644036e-18,0.0412727298270155,-6.63209111352764e-17))
body_2.SetMass(286.960740367602)
body_2.SetInertiaXX(chrono.ChVector3d(20.3261470881377,23.3528740040787,23.2169905170889))
body_2.SetInertiaXY(chrono.ChVector3d(-5.60160689862223,-0.500091644770905,0.179388605538521))
body_2.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.175382085214385,0.199890816413736,-0.00351536323719578),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_2_1 = chrono.ChMarker()
marker_2_1.SetName('marker_M1_A')
body_2.AddMarker(marker_2_1)
marker_2_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.140670357955037,2.15049691615662,0.37740311343739),chrono.ChQuaterniond(0.520210323845673,-0.520210323845673,-0.478937594018657,-0.478937594018657)))

# Auxiliary marker (coordinate system feature)
marker_2_2 = chrono.ChMarker()
marker_2_2.SetName('marker_M2_B')
body_2.AddMarker(marker_2_2)
marker_2_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.237444144337344,2.51549691615662,0.21767389520805),chrono.ChQuaterniond(0.99914791786433,-2.80761023644036E-18,0.0412727298270155,-6.63209111352764E-17)))

exported_items.append(body_2)



# Rigid body part
body_3 = chrono.ChBodyAuxRef()
body_3.SetName('M-410iB-300 -1/M-410iB-300-03-1')
body_3.SetPos(chrono.ChVector3d(0.247467333170753,2.51550127212935,0.3388320021666))
body_3.SetRot(chrono.ChQuaterniond(0.773569283596727,-0.0261217409246431,0.0319545439404108,-0.632366290411082))
body_3.SetMass(72.2394925421727)
body_3.SetInertiaXX(chrono.ChVector3d(1.50592710700546,10.8484487852999,11.2634766916778))
body_3.SetInertiaXY(chrono.ChVector3d(2.12067361135961,-0.771273236415114,0.188132550160896))
body_3.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.0436192441530501,0.531901199956275,-0.00110013226020073),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_3_1 = chrono.ChMarker()
marker_3_1.SetName('marker_M2_A')
body_3.AddMarker(marker_3_1)
marker_3_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.234188396117152,2.51550127212935,0.178375167536711),chrono.ChQuaterniond(0.994146578292323,0.00412441456577471,0.0410661348542013,0.0998455940054075)))

# Auxiliary marker (coordinate system feature)
marker_3_2 = chrono.ChMarker()
marker_3_2.SetName('marker_M3_B')
body_3.AddMarker(marker_3_2)
marker_3_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(1.42574833632556,2.75811166841886,0.0797651614368332),chrono.ChQuaterniond(0.994146578292323,0.00412441456577471,0.0410661348542013,0.0998455940054075)))

exported_items.append(body_3)



# Rigid body part
body_4 = chrono.ChBodyAuxRef()
body_4.SetName('M-410iB-300 -1/M-410iB-300-06-1')
body_4.SetPos(chrono.ChVector3d(1.44321244386273,2.75811166841885,0.29079375534754))
body_4.SetRot(chrono.ChQuaterniond(0.886426582844683,-0.0190440063218605,0.0366164450839609,-0.461025460250217))
body_4.SetMass(57.487443257986)
body_4.SetInertiaXX(chrono.ChVector3d(7.9742261479953,5.28772781730799,12.6893237121296))
body_4.SetInertiaXY(chrono.ChVector3d(-5.71514273781038,-0.673403451868731,-0.929928236179133))
body_4.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.216990574023306,0.112589145111018,-0.097224117310279),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_4_1 = chrono.ChMarker()
marker_4_1.SetName('marker_M3_A')
body_4.AddMarker(marker_4_1)
marker_4_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(1.43001641665603,2.75811166324713,0.131338856251638),chrono.ChQuaterniond(0.959076201512031,0.0115713379289103,0.0396174502701619,0.280123903774525)))

exported_items.append(body_4)



# Rigid body part
body_5 = chrono.ChBodyAuxRef()
body_5.SetName('M-410iB-300 -1/ArmBase-1')
body_5.SetPos(chrono.ChVector3d(-0.140670357955037,1.75770592148926,0.37740311343739))
body_5.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_5.SetMass(29.4636133436255)
body_5.SetInertiaXX(chrono.ChVector3d(0.754351795243641,1.45825924231452,0.754351795243641))
body_5.SetInertiaXY(chrono.ChVector3d(-1.65340831304039e-18,-2.64545330086463e-17,8.26704156520197e-18))
body_5.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-9.77354995986777e-18,0.231605672678633,-6.24094154063845e-18),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChVisualShapeModelFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5.AddVisualShape(body_5_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_5_1 = chrono.ChMarker()
marker_5_1.SetName('marker_M1_B')
body_5.AddMarker(marker_5_1)
marker_5_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.140670357955037,1.75770592148926,0.37740311343739),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

exported_items.append(body_5)



# Rigid body part
body_6 = chrono.ChBodyAuxRef()
body_6.SetName('M-410iB-300 -1/M-410iB-300-04-1')
body_6.SetPos(chrono.ChVector3d(0.269877838330441,2.78048238827907,0.600190114160509))
body_6.SetRot(chrono.ChQuaterniond(-0.474433745777481,-0.483399481584651,-0.515318353824203,0.525056717206011))
body_6.SetMass(1.58709182620022)
body_6.SetInertiaXX(chrono.ChVector3d(0.112490505154964,0.112340274058519,0.00107509254003515))
body_6.SetInertiaXY(chrono.ChVector3d(7.64900044070149e-06,8.49929897824016e-05,-0.00311323795964494))
body_6.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.00250471893101799,0.259643195204338,6.66879538413109e-09),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChVisualShapeModelFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6.AddVisualShape(body_6_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_6)



# Rigid body part
body_7 = chrono.ChBodyAuxRef()
body_7.SetName('M-410iB-300 -1/M-410iB-300-07-1')
body_7.SetPos(chrono.ChVector3d(0.247503474379937,2.51550127212935,0.339268716641747))
body_7.SetRot(chrono.ChQuaterniond(0.888019269219919,-0.0189169716008925,0.0366822356573978,-0.457950149324953))
body_7.SetMass(6.52835711422343)
body_7.SetInertiaXX(chrono.ChVector3d(0.209548912501074,0.126804969236949,0.31378904147503))
body_7.SetInertiaXY(chrono.ChVector3d(-0.133468017634731,-0.014695334387768,-0.0204548735025853))
body_7.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.244379980001897,-0.0286291463382749,-0.0666992304590947),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChVisualShapeModelFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7.AddVisualShape(body_7_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_7)



# Rigid body part
body_8 = chrono.ChBodyAuxRef()
body_8.SetName('M-410iB-300 -1/M-410iB-300-11-1')
body_8.SetPos(chrono.ChVector3d(1.92042610465865,3.02764258400502,-0.00826812849480207))
body_8.SetRot(chrono.ChQuaterniond(0.886426585056933,-0.019044006146155,0.0366164451753445,-0.461025455996663))
body_8.SetMass(2.26635866531324)
body_8.SetInertiaXX(chrono.ChVector3d(0.342444567987369,0.170720483056036,0.50549125464023))
body_8.SetInertiaXY(chrono.ChVector3d(-0.237000685043158,-0.0239698113746433,-0.0341783798169186))
body_8.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.650000000546567,-0.000267013560427985,-4.19077490083405e-05),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChVisualShapeModelFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8.AddVisualShape(body_8_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_8)



# Rigid body part
body_9 = chrono.ChBodyAuxRef()
body_9.SetName('M-410iB-300 -1/M-410iB-300-05-1')
body_9.SetPos(chrono.ChVector3d(0.594774142300029,2.77437870841746,0.573302648884809))
body_9.SetRot(chrono.ChQuaterniond(0.699860409425343,-0.0294561142756602,0.0289097831045659,-0.713086228370467))
body_9.SetMass(44.264758578016)
body_9.SetInertiaXX(chrono.ChVector3d(0.419802161252818,2.77625004306057,2.76548569075428))
body_9.SetInertiaXY(chrono.ChVector3d(-0.0398199766034854,-0.0533803242613383,-5.78878132818095e-05))
body_9.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-5.19600690940307e-06,0.410805913274014,-0.00264008387504332),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_9_1_shape = chrono.ChVisualShapeModelFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_9.AddVisualShape(body_9_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_9)



# Rigid body part
body_10 = chrono.ChBodyAuxRef()
body_10.SetName('M-410iB-300 -1/M-410iB-300-08-1')
body_10.SetPos(chrono.ChVector3d(-0.0775367664376993,3.00995602354016,0.299148197809961))
body_10.SetRot(chrono.ChQuaterniond(0.77457390871473,-0.0260708930553939,0.0319960429220246,-0.631135343417726))
body_10.SetMass(7.16874140056196)
body_10.SetInertiaXX(chrono.ChVector3d(0.0767803688734156,1.02488822982072,1.09908804347466))
body_10.SetInertiaXY(chrono.ChVector3d(0.211091413570172,1.79884424153787e-05,-0.00250201297676742))
body_10.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0995028745288738,0.617303418169042,1.66091348067665e-08),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_10_1_shape = chrono.ChVisualShapeModelFile() 
body_10_1_shape.SetFilename(shapes_dir +'body_10_1.obj') 
body_10.AddVisualShape(body_10_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_10)



# Rigid body part
body_11 = chrono.ChBodyAuxRef()
body_11.SetName('M-410iB-300 -1/M-410iB-300-09-1')
body_11.SetPos(chrono.ChVector3d(1.41934259561721,2.75811166841883,0.00236100827493818))
body_11.SetRot(chrono.ChQuaterniond(0.999147807995971,-1.93552865822696e-05,0.0412727252885812,-0.000468561066093758))
body_11.SetMass(8.44776262879024)
body_11.SetInertiaXX(chrono.ChVector3d(0.11496494349016,0.723349083568589,0.823884312212851))
body_11.SetInertiaXY(chrono.ChVector3d(0.00405542478900029,-0.0591110909356657,0.00173001226666931))
body_11.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.00309747019490025,0.11726872541838,-0.0225919700688117),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_1_shape = chrono.ChVisualShapeModelFile() 
body_11_1_shape.SetFilename(shapes_dir +'body_11_1.obj') 
body_11.AddVisualShape(body_11_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_11)



# Rigid body part
body_12 = chrono.ChBodyAuxRef()
body_12.SetName('M-410iB-300 -1/M-410iB-300-10-1')
body_12.SetPos(chrono.ChVector3d(-0.277686877786646,2.78749692402101,0.0676160406005467))
body_12.SetRot(chrono.ChQuaterniond(0.773755292789647,-0.0261123387416691,0.0319622275946799,-0.632138678339361))
body_12.SetMass(2.24487855545089)
body_12.SetInertiaXX(chrono.ChVector3d(0.0179735699808056,0.41151320286575,0.428952544587403))
body_12.SetInertiaXY(chrono.ChVector3d(0.0835568879793482,-7.20152596639639e-06,-3.53811009408747e-05))
body_12.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-7.01323711472189e-15,0.610001635976697,-2.13860676946226e-05),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_12_1_shape = chrono.ChVisualShapeModelFile() 
body_12_1_shape.SetFilename(shapes_dir +'body_12_1.obj') 
body_12.AddVisualShape(body_12_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_12)



# Rigid body part
body_13 = chrono.ChBodyAuxRef()
body_13.SetName('M-410iB-300 -2/M-410iB-300-06-1')
body_13.SetPos(chrono.ChVector3d(1.44321244386273,2.75811166841885,-1.15920624465246))
body_13.SetRot(chrono.ChQuaterniond(0.886426582844683,-0.0190440063218605,0.0366164450839609,-0.461025460250217))
body_13.SetMass(57.487443257986)
body_13.SetInertiaXX(chrono.ChVector3d(7.9742261479953,5.28772781730799,12.6893237121296))
body_13.SetInertiaXY(chrono.ChVector3d(-5.71514273781038,-0.673403451868731,-0.929928236179133))
body_13.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.216990574023306,0.112589145111018,-0.097224117310279),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_13.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_13_1 = chrono.ChMarker()
marker_13_1.SetName('marker_M3_A')
body_13.AddMarker(marker_13_1)
marker_13_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(1.43001641665603,2.75811166324713,-1.31866114374836),chrono.ChQuaterniond(0.959076201512031,0.0115713379289103,0.0396174502701619,0.280123903774525)))

exported_items.append(body_13)



# Rigid body part
body_14 = chrono.ChBodyAuxRef()
body_14.SetName('M-410iB-300 -2/M-410iB-300-02-1')
body_14.SetPos(chrono.ChVector3d(-0.140670357955037,2.15049691615662,-1.07259688656261))
body_14.SetRot(chrono.ChQuaterniond(0.99914791786433,-2.80761023644036e-18,0.0412727298270155,-6.63209111352764e-17))
body_14.SetMass(286.960740367602)
body_14.SetInertiaXX(chrono.ChVector3d(20.3261470881377,23.3528740040787,23.2169905170889))
body_14.SetInertiaXY(chrono.ChVector3d(-5.60160689862223,-0.500091644770905,0.179388605538521))
body_14.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.175382085214385,0.199890816413736,-0.00351536323719578),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_14.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_14_1 = chrono.ChMarker()
marker_14_1.SetName('marker_M1_A')
body_14.AddMarker(marker_14_1)
marker_14_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.140670357955037,2.15049691615662,-1.07259688656261),chrono.ChQuaterniond(0.520210323845673,-0.520210323845673,-0.478937594018657,-0.478937594018657)))

# Auxiliary marker (coordinate system feature)
marker_14_2 = chrono.ChMarker()
marker_14_2.SetName('marker_M2_B')
body_14.AddMarker(marker_14_2)
marker_14_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.237444144337344,2.51549691615662,-1.23232610479195),chrono.ChQuaterniond(0.99914791786433,-2.80761023644036E-18,0.0412727298270155,-6.63209111352764E-17)))

exported_items.append(body_14)



# Rigid body part
body_15 = chrono.ChBodyAuxRef()
body_15.SetName('M-410iB-300 -2/M-410iB-300-03-1')
body_15.SetPos(chrono.ChVector3d(0.247467333170754,2.51550127212935,-1.1111679978334))
body_15.SetRot(chrono.ChQuaterniond(0.773569283596727,-0.0261217409246431,0.0319545439404108,-0.632366290411082))
body_15.SetMass(72.2394925421727)
body_15.SetInertiaXX(chrono.ChVector3d(1.50592710700546,10.8484487852999,11.2634766916778))
body_15.SetInertiaXY(chrono.ChVector3d(2.12067361135961,-0.771273236415114,0.188132550160896))
body_15.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.0436192441530501,0.531901199956275,-0.00110013226020073),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_15.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_15_1 = chrono.ChMarker()
marker_15_1.SetName('marker_M2_A')
body_15.AddMarker(marker_15_1)
marker_15_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.234188396117152,2.51550127212935,-1.27162483246329),chrono.ChQuaterniond(0.994146578292323,0.00412441456577471,0.0410661348542013,0.0998455940054075)))

# Auxiliary marker (coordinate system feature)
marker_15_2 = chrono.ChMarker()
marker_15_2.SetName('marker_M3_B')
body_15.AddMarker(marker_15_2)
marker_15_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(1.42574833632556,2.75811166841886,-1.37023483856317),chrono.ChQuaterniond(0.994146578292323,0.00412441456577471,0.0410661348542013,0.0998455940054075)))

exported_items.append(body_15)



# Rigid body part
body_16 = chrono.ChBodyAuxRef()
body_16.SetName('M-410iB-300 -2/M-410iB-300-12-1')
body_16.SetPos(chrono.ChVector3d(2.43833354378683,1.53452994138094,-1.27513593898818))
body_16.SetRot(chrono.ChQuaterniond(0.999147807992026,-1.93556340972606e-05,0.0412727252884182,-0.000468569478897188))
body_16.SetMass(16.1636065115335)
body_16.SetInertiaXX(chrono.ChVector3d(0.270949711605444,0.400661918859637,0.427371867141467))
body_16.SetInertiaXY(chrono.ChVector3d(-0.0576658362005997,0.0375936407947645,0.0626245655339811))
body_16.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0294847451383035,0.131793864973377,-0.039955675141979),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_16.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Collision Model

body_16.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_16 = chrono.ChContactMaterialNSC()
p1 = chrono.ChVector3d(4.57739150408006E-17, 0, 0)
p2 = chrono.ChVector3d(4.57739150408006E-17, 0.147530764880198, 0)
body_16.GetCollisionModel().AddCylinder(mat_16, 0.0891514706007005, p1, p2)
body_16.EnableCollision(True)

exported_items.append(body_16)



# Rigid body part
body_17 = chrono.ChBodyAuxRef()
body_17.SetName('M-410iB-300 -2/M-410iB-300-05-1')
body_17.SetPos(chrono.ChVector3d(0.594774142300029,2.77437870841746,-0.876697351115191))
body_17.SetRot(chrono.ChQuaterniond(0.699860409425343,-0.0294561142756602,0.0289097831045659,-0.713086228370467))
body_17.SetMass(44.264758578016)
body_17.SetInertiaXX(chrono.ChVector3d(0.419802161252818,2.77625004306057,2.76548569075428))
body_17.SetInertiaXY(chrono.ChVector3d(-0.0398199766034854,-0.0533803242613383,-5.78878132818095e-05))
body_17.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-5.19600690940307e-06,0.410805913274014,-0.00264008387504332),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_9_1_shape = chrono.ChVisualShapeModelFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_17.AddVisualShape(body_9_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_17)



# Rigid body part
body_18 = chrono.ChBodyAuxRef()
body_18.SetName('M-410iB-300 -2/ArmBase-1')
body_18.SetPos(chrono.ChVector3d(-0.140670357955037,1.75770592148926,-1.07259688656261))
body_18.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_18.SetMass(29.4636133436255)
body_18.SetInertiaXX(chrono.ChVector3d(0.754351795243641,1.45825924231452,0.754351795243641))
body_18.SetInertiaXY(chrono.ChVector3d(-1.65340831304039e-18,-2.64545330086463e-17,8.26704156520197e-18))
body_18.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-9.77354995986777e-18,0.231605672678633,-6.24094154063845e-18),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChVisualShapeModelFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_18.AddVisualShape(body_5_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_18_1 = chrono.ChMarker()
marker_18_1.SetName('marker_M1_B')
body_18.AddMarker(marker_18_1)
marker_18_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.140670357955037,1.75770592148926,-1.07259688656261),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

exported_items.append(body_18)



# Rigid body part
body_19 = chrono.ChBodyAuxRef()
body_19.SetName('M-410iB-300 -2/M-410iB-300-11-1')
body_19.SetPos(chrono.ChVector3d(1.92042610465865,3.02764258400502,-1.4582681284948))
body_19.SetRot(chrono.ChQuaterniond(0.886426585056933,-0.019044006146155,0.0366164451753445,-0.461025455996663))
body_19.SetMass(2.26635866531324)
body_19.SetInertiaXX(chrono.ChVector3d(0.342444567987369,0.170720483056036,0.50549125464023))
body_19.SetInertiaXY(chrono.ChVector3d(-0.237000685043158,-0.0239698113746433,-0.0341783798169186))
body_19.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.650000000546567,-0.000267013560427985,-4.19077490083405e-05),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChVisualShapeModelFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_19.AddVisualShape(body_8_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_19)



# Rigid body part
body_20 = chrono.ChBodyAuxRef()
body_20.SetName('M-410iB-300 -2/M-410iB-300-04-1')
body_20.SetPos(chrono.ChVector3d(0.269877838330441,2.78048238827907,-0.849809885839491))
body_20.SetRot(chrono.ChQuaterniond(-0.474433745777481,-0.483399481584651,-0.515318353824203,0.525056717206011))
body_20.SetMass(1.58709182620022)
body_20.SetInertiaXX(chrono.ChVector3d(0.112490505154964,0.112340274058519,0.00107509254003515))
body_20.SetInertiaXY(chrono.ChVector3d(7.64900044070149e-06,8.49929897824016e-05,-0.00311323795964494))
body_20.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.00250471893101799,0.259643195204338,6.66879538413109e-09),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChVisualShapeModelFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_20.AddVisualShape(body_6_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_20)



# Rigid body part
body_21 = chrono.ChBodyAuxRef()
body_21.SetName('M-410iB-300 -2/M-410iB-300-07-1')
body_21.SetPos(chrono.ChVector3d(0.247503474379937,2.51550127212935,-1.11073128335825))
body_21.SetRot(chrono.ChQuaterniond(0.888019269219919,-0.0189169716008925,0.0366822356573978,-0.457950149324953))
body_21.SetMass(6.52835711422343)
body_21.SetInertiaXX(chrono.ChVector3d(0.209548912501074,0.126804969236949,0.31378904147503))
body_21.SetInertiaXY(chrono.ChVector3d(-0.133468017634731,-0.014695334387768,-0.0204548735025853))
body_21.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.244379980001897,-0.0286291463382749,-0.0666992304590947),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChVisualShapeModelFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_21.AddVisualShape(body_7_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_21)



# Rigid body part
body_22 = chrono.ChBodyAuxRef()
body_22.SetName('M-410iB-300 -2/M-410iB-300-09-1')
body_22.SetPos(chrono.ChVector3d(1.41934259561721,2.75811166841883,-1.44763899172506))
body_22.SetRot(chrono.ChQuaterniond(0.999147807995971,-1.93552865822696e-05,0.0412727252885812,-0.000468561066093758))
body_22.SetMass(8.44776262879024)
body_22.SetInertiaXX(chrono.ChVector3d(0.11496494349016,0.723349083568589,0.823884312212851))
body_22.SetInertiaXY(chrono.ChVector3d(0.00405542478900029,-0.0591110909356657,0.00173001226666931))
body_22.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.00309747019490025,0.11726872541838,-0.0225919700688117),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_1_shape = chrono.ChVisualShapeModelFile() 
body_11_1_shape.SetFilename(shapes_dir +'body_11_1.obj') 
body_22.AddVisualShape(body_11_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_22)



# Rigid body part
body_23 = chrono.ChBodyAuxRef()
body_23.SetName('M-410iB-300 -2/M-410iB-300-08-1')
body_23.SetPos(chrono.ChVector3d(-0.077536766437699,3.00995602354016,-1.15085180219004))
body_23.SetRot(chrono.ChQuaterniond(0.77457390871473,-0.0260708930553939,0.0319960429220246,-0.631135343417726))
body_23.SetMass(7.16874140056196)
body_23.SetInertiaXX(chrono.ChVector3d(0.0767803688734156,1.02488822982072,1.09908804347466))
body_23.SetInertiaXY(chrono.ChVector3d(0.211091413570172,1.79884424153787e-05,-0.00250201297676742))
body_23.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0995028745288738,0.617303418169042,1.66091348067665e-08),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_10_1_shape = chrono.ChVisualShapeModelFile() 
body_10_1_shape.SetFilename(shapes_dir +'body_10_1.obj') 
body_23.AddVisualShape(body_10_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_23)



# Rigid body part
body_24 = chrono.ChBodyAuxRef()
body_24.SetName('M-410iB-300 -2/M-410iB-300-10-1')
body_24.SetPos(chrono.ChVector3d(-0.277686877786646,2.78749692402101,-1.38238395939945))
body_24.SetRot(chrono.ChQuaterniond(0.773755292789647,-0.0261123387416691,0.0319622275946799,-0.632138678339361))
body_24.SetMass(2.24487855545089)
body_24.SetInertiaXX(chrono.ChVector3d(0.0179735699808056,0.41151320286575,0.428952544587403))
body_24.SetInertiaXY(chrono.ChVector3d(0.0835568879793482,-7.20152596639639e-06,-3.53811009408747e-05))
body_24.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-7.01323711472189e-15,0.610001635976697,-2.13860676946226e-05),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_12_1_shape = chrono.ChVisualShapeModelFile() 
body_12_1_shape.SetFilename(shapes_dir +'body_12_1.obj') 
body_24.AddVisualShape(body_12_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_24)



# Rigid body part
body_25 = chrono.ChBodyAuxRef()
body_25.SetName('Part3^SPIDER_ROBOT-1')
body_25.SetPos(chrono.ChVector3d(-0.620670357955037,1.94456417249918,0.727403113437383))
body_25.SetRot(chrono.ChQuaterniond(1.74574066942157e-15,1,0,0))
body_25.SetMass(1472.20792264893)
body_25.SetInertiaXX(chrono.ChVector3d(1948.56933336626,2184.15530557198,283.239773065818))
body_25.SetInertiaXY(chrono.ChVector3d(-1.01016366481125e-05,0.000194532690193684,5.83016939382041))
body_25.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.200000019877454,0.0526986503540632,1.84480172081189),chrono.ChQuaterniond(1,0,0,0)))
body_25.SetFixed(True)

# Visualization shape 
body_25_1_shape = chrono.ChVisualShapeModelFile() 
body_25_1_shape.SetFilename(shapes_dir +'body_25_1.obj') 
body_25.AddVisualShape(body_25_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_25)



# Rigid body part
body_26 = chrono.ChBodyAuxRef()
body_26.SetName('M-410iB-300 -9/M-410iB-300-02-1')
body_26.SetPos(chrono.ChVector3d(-1.50067035795504,2.15049691615662,0.377403113437382))
body_26.SetRot(chrono.ChQuaterniond(-0.0412727298270154,-2.39528823459568e-17,0.99914791786433,-1.7763160888523e-15))
body_26.SetMass(286.960740367602)
body_26.SetInertiaXX(chrono.ChVector3d(20.3261470881377,23.3528740040787,23.2169905170889))
body_26.SetInertiaXY(chrono.ChVector3d(5.60160689862223,-0.500091644770925,-0.179388605538523))
body_26.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.175382085214385,0.199890816413736,-0.00351536323719578),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_26.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_26_1 = chrono.ChMarker()
marker_26_1.SetName('marker_M1_A')
body_26.AddMarker(marker_26_1)
marker_26_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-1.50067035795504,2.15049691615662,0.377403113437382),chrono.ChQuaterniond(0.478937594018657,-0.478937594018658,0.520210323845674,0.520210323845672)))

# Auxiliary marker (coordinate system feature)
marker_26_2 = chrono.ChMarker()
marker_26_2.SetName('marker_M2_B')
body_26.AddMarker(marker_26_2)
marker_26_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-1.87878486024742,2.51549691615663,0.537132331666721),chrono.ChQuaterniond(-0.0412727298270154,-2.39528823459568E-17,0.99914791786433,-1.7763160888523E-15)))

exported_items.append(body_26)



# Rigid body part
body_27 = chrono.ChBodyAuxRef()
body_27.SetName('M-410iB-300 -9/M-410iB-300-12-1')
body_27.SetPos(chrono.ChVector3d(-4.07967425969691,1.53452994138094,0.579942165862954))
body_27.SetRot(chrono.ChQuaterniond(-0.0412727252884181,-0.000468569478897146,0.999147807992026,1.93556340954814e-05))
body_27.SetMass(16.1636065115335)
body_27.SetInertiaXX(chrono.ChVector3d(0.270733820597613,0.400877809867468,0.427371867141468))
body_27.SetInertiaXY(chrono.ChVector3d(0.0574221068634286,0.0377110505251339,-0.0625539343672037))
body_27.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0294847451383035,0.131793864973377,-0.039955675141979),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_27.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Collision Model

body_27.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_27 = chrono.ChContactMaterialNSC()
p1 = chrono.ChVector3d(4.57739150408006E-17, 0, 0)
p2 = chrono.ChVector3d(4.57739150408006E-17, 0.147530764880198, 0)
body_27.GetCollisionModel().AddCylinder(mat_27, 0.0891514706007005, p1, p2)
body_27.EnableCollision(True)

exported_items.append(body_27)



# Rigid body part
body_28 = chrono.ChBodyAuxRef()
body_28.SetName('M-410iB-300 -9/ArmBase-1')
body_28.SetPos(chrono.ChVector3d(-1.50067035795504,1.75770592148926,0.377403113437384))
body_28.SetRot(chrono.ChQuaterniond(1.11022302462516e-16,-3.10973640124651e-17,1,-1.77935638377312e-15))
body_28.SetMass(29.4636133436255)
body_28.SetInertiaXX(chrono.ChVector3d(0.754351795243641,1.45825924231452,0.754351795243641))
body_28.SetInertiaXY(chrono.ChVector3d(-4.2125923912256e-17,-2.6454533008646e-17,-2.51327146062721e-15))
body_28.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-9.77354995986777e-18,0.231605672678633,-6.24094154063845e-18),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChVisualShapeModelFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_28.AddVisualShape(body_5_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_28_1 = chrono.ChMarker()
marker_28_1.SetName('marker_M1_B')
body_28.AddMarker(marker_28_1)
marker_28_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-1.50067035795504,1.75770592148926,0.377403113437384),chrono.ChQuaterniond(-0.499999999999999,0.500000000000001,-0.500000000000001,-0.499999999999999)))

exported_items.append(body_28)



# Rigid body part
body_29 = chrono.ChBodyAuxRef()
body_29.SetName('M-410iB-300 -9/M-410iB-300-03-1')
body_29.SetPos(chrono.ChVector3d(-1.88880804908083,2.51550127212935,0.415974224708171))
body_29.SetRot(chrono.ChQuaterniond(-0.0319545439404119,-0.632366290411082,0.773569283596727,0.0261217409246416))
body_29.SetMass(72.2394925421727)
body_29.SetInertiaXX(chrono.ChVector3d(1.40287854682595,10.9514973454794,11.2634766916778))
body_29.SetInertiaXY(chrono.ChVector3d(1.87720647579531,0.783602183259728,-0.127372995689095))
body_29.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.0436192441530501,0.531901199956275,-0.00110013226020073),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_29.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_29_1 = chrono.ChMarker()
marker_29_1.SetName('marker_M2_A')
body_29.AddMarker(marker_29_1)
marker_29_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-1.87552911202723,2.51550127212935,0.57643105933806),chrono.ChQuaterniond(-0.041066134854201,0.0998455940054075,0.994146578292323,-0.00412441456577647)))

# Auxiliary marker (coordinate system feature)
marker_29_2 = chrono.ChMarker()
marker_29_2.SetName('marker_M3_B')
body_29.AddMarker(marker_29_2)
marker_29_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-3.06708905223563,2.75811166841886,0.675041065437937),chrono.ChQuaterniond(-0.041066134854201,0.0998455940054075,0.994146578292323,-0.00412441456577647)))

exported_items.append(body_29)



# Rigid body part
body_30 = chrono.ChBodyAuxRef()
body_30.SetName('M-410iB-300 -9/M-410iB-300-07-1')
body_30.SetPos(chrono.ChVector3d(-1.88884419029001,2.51550127212935,0.415537510233024))
body_30.SetRot(chrono.ChQuaterniond(-0.0366822356573985,-0.457950149324953,0.888019269219919,0.0189169716008908))
body_30.SetMass(6.52835711422343)
body_30.SetInertiaXX(chrono.ChVector3d(0.218294896592719,0.118058985145305,0.31378904147503))
body_30.SetInertiaXY(chrono.ChVector3d(-0.130435970047168,-0.0145129242114027,-0.0205846965877362))
body_30.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.244379980001897,-0.0286291463382749,-0.0666992304590947),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChVisualShapeModelFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_30.AddVisualShape(body_7_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_30)



# Rigid body part
body_31 = chrono.ChBodyAuxRef()
body_31.SetName('M-410iB-300 -9/M-410iB-300-09-1')
body_31.SetPos(chrono.ChVector3d(-3.06068331152728,2.75811166841883,0.752445218599832))
body_31.SetRot(chrono.ChQuaterniond(-0.0412727252885811,-0.000468561066093716,0.999147807995971,1.93552865804904e-05))
body_31.SetMass(8.44776262879024)
body_31.SetInertiaXX(chrono.ChVector3d(0.114982298903477,0.723331728155272,0.823884312212851))
body_31.SetInertiaXY(chrono.ChVector3d(-0.00519662652260749,-0.0591077417070737,-0.00184089226659357))
body_31.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.00309747019490025,0.11726872541838,-0.0225919700688117),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_1_shape = chrono.ChVisualShapeModelFile() 
body_11_1_shape.SetFilename(shapes_dir +'body_11_1.obj') 
body_31.AddVisualShape(body_11_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_31)



# Rigid body part
body_32 = chrono.ChBodyAuxRef()
body_32.SetName('M-410iB-300 -9/M-410iB-300-08-1')
body_32.SetPos(chrono.ChVector3d(-1.56380394947238,3.00995602354016,0.455658029064808))
body_32.SetRot(chrono.ChQuaterniond(-0.0319960429220257,-0.631135343417726,0.77457390871473,0.0260708930553924))
body_32.SetMass(7.16874140056196)
body_32.SetInertiaXX(chrono.ChVector3d(0.0717801649549736,1.02988843373916,1.09908804347466))
body_32.SetInertiaXY(chrono.ChVector3d(0.199483959762215,-0.00100638858175141,-0.00229075850811439))
body_32.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0995028745288738,0.617303418169042,1.66091348067665e-08),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_10_1_shape = chrono.ChVisualShapeModelFile() 
body_10_1_shape.SetFilename(shapes_dir +'body_10_1.obj') 
body_32.AddVisualShape(body_10_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_32)



# Rigid body part
body_33 = chrono.ChBodyAuxRef()
body_33.SetName('M-410iB-300 -9/M-410iB-300-11-1')
body_33.SetPos(chrono.ChVector3d(-3.56176682056872,3.02764258400503,0.763074355369571))
body_33.SetRot(chrono.ChQuaterniond(-0.0366164451753452,-0.461025455996663,0.886426585056933,0.0190440061461534))
body_33.SetMass(2.26635866531324)
body_33.SetInertiaXX(chrono.ChVector3d(0.342444575932242,0.170720475111163,0.50549125464023))
body_33.SetInertiaXY(chrono.ChVector3d(-0.237000682164841,-0.0239698954072387,-0.0341783208834424))
body_33.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.650000000546567,-0.000267013560427985,-4.19077490083405e-05),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChVisualShapeModelFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_33.AddVisualShape(body_8_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_33)



# Rigid body part
body_34 = chrono.ChBodyAuxRef()
body_34.SetName('M-410iB-300 -9/M-410iB-300-06-1')
body_34.SetPos(chrono.ChVector3d(-3.0845531597728,2.75811166841886,0.46401247152723))
body_34.SetRot(chrono.ChQuaterniond(-0.0366164450839617,-0.461025460250217,0.886426582844683,0.0190440063218589))
body_34.SetMass(57.487443257986)
body_34.SetInertiaXX(chrono.ChVector3d(9.2600016804482,4.0019522848551,12.6893237121296))
body_34.SetInertiaXY(chrono.ChVector3d(-5.2493241443179,-0.644943244770499,-0.949887858884848))
body_34.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.216990574023306,0.112589145111018,-0.097224117310279),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_34.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_34_1 = chrono.ChMarker()
marker_34_1.SetName('marker_M3_A')
body_34.AddMarker(marker_34_1)
marker_34_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-3.0713571325661,2.75811166324714,0.623467370623132),chrono.ChQuaterniond(-0.0396174502701613,0.280123903774525,0.959076201512031,-0.011571337928912)))

exported_items.append(body_34)



# Rigid body part
body_35 = chrono.ChBodyAuxRef()
body_35.SetName('M-410iB-300 -9/M-410iB-300-04-1')
body_35.SetPos(chrono.ChVector3d(-1.91121855424052,2.78048238827907,0.154616112714261))
body_35.SetRot(chrono.ChQuaterniond(0.515318353824204,0.52505671720601,-0.47443374577748,0.483399481584652))
body_35.SetMass(1.58709182620022)
body_35.SetInertiaXX(chrono.ChVector3d(0.112490505154964,0.112417280652057,0.000998085946496919))
body_35.SetInertiaXY(chrono.ChVector3d(4.46219075106793e-06,-8.52197416889096e-05,-0.00105743461725763))
body_35.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.00250471893101799,0.259643195204338,6.66879538413109e-09),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChVisualShapeModelFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_35.AddVisualShape(body_6_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_35)



# Rigid body part
body_36 = chrono.ChBodyAuxRef()
body_36.SetName('M-410iB-300 -9/M-410iB-300-05-1')
body_36.SetPos(chrono.ChVector3d(-2.2361148582101,2.77437870841746,0.181503577989961))
body_36.SetRot(chrono.ChQuaterniond(0.0289097831045671,0.713086228370467,-0.699860409425343,-0.0294561142756589))
body_36.SetMass(44.264758578016)
body_36.SetInertiaXX(chrono.ChVector3d(0.420124912385258,2.77592729192813,2.76548569075428))
body_36.SetInertiaXY(chrono.ChVector3d(-0.0484362735024024,0.0533450810289393,0.00194028329366022))
body_36.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-5.19600690940307e-06,0.410805913274014,-0.00264008387504332),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_9_1_shape = chrono.ChVisualShapeModelFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_36.AddVisualShape(body_9_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_36)



# Rigid body part
body_37 = chrono.ChBodyAuxRef()
body_37.SetName('M-410iB-300 -9/M-410iB-300-10-1')
body_37.SetPos(chrono.ChVector3d(-1.36365383812343,2.78749692402102,0.687190186274224))
body_37.SetRot(chrono.ChQuaterniond(-0.0319622275946809,-0.632138678339361,0.773755292789647,0.0261123387416676))
body_37.SetMass(2.24487855545089)
body_37.SetInertiaXX(chrono.ChVector3d(0.0179735699467435,0.411513202899812,0.428952544587403))
body_37.SetInertiaXY(chrono.ChVector3d(0.0835568878991346,-7.20049407702643e-06,-3.53813109576148e-05))
body_37.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-7.01323711472189e-15,0.610001635976697,-2.13860676946226e-05),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_12_1_shape = chrono.ChVisualShapeModelFile() 
body_12_1_shape.SetFilename(shapes_dir +'body_12_1.obj') 
body_37.AddVisualShape(body_12_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_37)



# Rigid body part
body_38 = chrono.ChBodyAuxRef()
body_38.SetName('M-410iB-300 -3/M-410iB-300-04-1')
body_38.SetPos(chrono.ChVector3d(0.269877838330441,2.78048238827907,-2.29980988583949))
body_38.SetRot(chrono.ChQuaterniond(-0.474433745777481,-0.483399481584651,-0.515318353824203,0.525056717206011))
body_38.SetMass(1.58709182620022)
body_38.SetInertiaXX(chrono.ChVector3d(0.112490505154964,0.112340274058519,0.00107509254003515))
body_38.SetInertiaXY(chrono.ChVector3d(7.64900044070149e-06,8.49929897824016e-05,-0.00311323795964494))
body_38.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.00250471893101799,0.259643195204338,6.66879538413109e-09),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChVisualShapeModelFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_38.AddVisualShape(body_6_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_38)



# Rigid body part
body_39 = chrono.ChBodyAuxRef()
body_39.SetName('M-410iB-300 -3/M-410iB-300-03-1')
body_39.SetPos(chrono.ChVector3d(0.247467333170754,2.51550127212935,-2.5611679978334))
body_39.SetRot(chrono.ChQuaterniond(0.773569283596727,-0.0261217409246431,0.0319545439404108,-0.632366290411082))
body_39.SetMass(72.2394925421727)
body_39.SetInertiaXX(chrono.ChVector3d(1.50592710700546,10.8484487852999,11.2634766916778))
body_39.SetInertiaXY(chrono.ChVector3d(2.12067361135961,-0.771273236415114,0.188132550160896))
body_39.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.0436192441530501,0.531901199956275,-0.00110013226020073),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_39.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_39_1 = chrono.ChMarker()
marker_39_1.SetName('marker_M2_A')
body_39.AddMarker(marker_39_1)
marker_39_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.234188396117152,2.51550127212935,-2.72162483246329),chrono.ChQuaterniond(0.994146578292323,0.00412441456577471,0.0410661348542013,0.0998455940054075)))

# Auxiliary marker (coordinate system feature)
marker_39_2 = chrono.ChMarker()
marker_39_2.SetName('marker_M3_B')
body_39.AddMarker(marker_39_2)
marker_39_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(1.42574833632556,2.75811166841886,-2.82023483856317),chrono.ChQuaterniond(0.994146578292323,0.00412441456577471,0.0410661348542013,0.0998455940054075)))

exported_items.append(body_39)



# Rigid body part
body_40 = chrono.ChBodyAuxRef()
body_40.SetName('M-410iB-300 -3/M-410iB-300-02-1')
body_40.SetPos(chrono.ChVector3d(-0.140670357955037,2.15049691615662,-2.52259688656261))
body_40.SetRot(chrono.ChQuaterniond(0.99914791786433,-2.80761023644036e-18,0.0412727298270155,-6.63209111352764e-17))
body_40.SetMass(286.960740367602)
body_40.SetInertiaXX(chrono.ChVector3d(20.3261470881377,23.3528740040787,23.2169905170889))
body_40.SetInertiaXY(chrono.ChVector3d(-5.60160689862223,-0.500091644770905,0.179388605538521))
body_40.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.175382085214385,0.199890816413736,-0.00351536323719578),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_40.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_40_1 = chrono.ChMarker()
marker_40_1.SetName('marker_M1_A')
body_40.AddMarker(marker_40_1)
marker_40_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.140670357955037,2.15049691615662,-2.52259688656261),chrono.ChQuaterniond(0.520210323845673,-0.520210323845673,-0.478937594018657,-0.478937594018657)))

# Auxiliary marker (coordinate system feature)
marker_40_2 = chrono.ChMarker()
marker_40_2.SetName('marker_M2_B')
body_40.AddMarker(marker_40_2)
marker_40_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.237444144337345,2.51549691615662,-2.68232610479195),chrono.ChQuaterniond(0.99914791786433,-2.80761023644036E-18,0.0412727298270155,-6.63209111352764E-17)))

exported_items.append(body_40)



# Rigid body part
body_41 = chrono.ChBodyAuxRef()
body_41.SetName('M-410iB-300 -3/M-410iB-300-06-1')
body_41.SetPos(chrono.ChVector3d(1.44321244386273,2.75811166841885,-2.60920624465246))
body_41.SetRot(chrono.ChQuaterniond(0.886426582844683,-0.0190440063218605,0.0366164450839609,-0.461025460250217))
body_41.SetMass(57.487443257986)
body_41.SetInertiaXX(chrono.ChVector3d(7.9742261479953,5.28772781730799,12.6893237121296))
body_41.SetInertiaXY(chrono.ChVector3d(-5.71514273781038,-0.673403451868731,-0.929928236179133))
body_41.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.216990574023306,0.112589145111018,-0.097224117310279),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_41.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_41_1 = chrono.ChMarker()
marker_41_1.SetName('marker_M3_A')
body_41.AddMarker(marker_41_1)
marker_41_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(1.43001641665603,2.75811166324713,-2.76866114374836),chrono.ChQuaterniond(0.959076201512031,0.0115713379289103,0.0396174502701619,0.280123903774525)))

exported_items.append(body_41)



# Rigid body part
body_42 = chrono.ChBodyAuxRef()
body_42.SetName('M-410iB-300 -3/M-410iB-300-12-1')
body_42.SetPos(chrono.ChVector3d(2.43833354378683,1.53452994138094,-2.72513593898818))
body_42.SetRot(chrono.ChQuaterniond(0.999147807992026,-1.93556340972606e-05,0.0412727252884182,-0.000468569478897188))
body_42.SetMass(16.1636065115335)
body_42.SetInertiaXX(chrono.ChVector3d(0.270949711605444,0.400661918859637,0.427371867141467))
body_42.SetInertiaXY(chrono.ChVector3d(-0.0576658362005997,0.0375936407947645,0.0626245655339811))
body_42.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0294847451383035,0.131793864973377,-0.039955675141979),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_42.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Collision Model

body_42.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_42 = chrono.ChContactMaterialNSC()
p1 = chrono.ChVector3d(4.57739150408006E-17, 0, 0)
p2 = chrono.ChVector3d(4.57739150408006E-17, 0.147530764880198, 0)
body_42.GetCollisionModel().AddCylinder(mat_42, 0.0891514706007005, p1, p2)
body_42.EnableCollision(True)

exported_items.append(body_42)



# Rigid body part
body_43 = chrono.ChBodyAuxRef()
body_43.SetName('M-410iB-300 -3/ArmBase-1')
body_43.SetPos(chrono.ChVector3d(-0.140670357955037,1.75770592148926,-2.52259688656261))
body_43.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_43.SetMass(29.4636133436255)
body_43.SetInertiaXX(chrono.ChVector3d(0.754351795243641,1.45825924231452,0.754351795243641))
body_43.SetInertiaXY(chrono.ChVector3d(-1.65340831304039e-18,-2.64545330086463e-17,8.26704156520197e-18))
body_43.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-9.77354995986777e-18,0.231605672678633,-6.24094154063845e-18),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChVisualShapeModelFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_43.AddVisualShape(body_5_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_43_1 = chrono.ChMarker()
marker_43_1.SetName('marker_M1_B')
body_43.AddMarker(marker_43_1)
marker_43_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.140670357955037,1.75770592148926,-2.52259688656261),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

exported_items.append(body_43)



# Rigid body part
body_44 = chrono.ChBodyAuxRef()
body_44.SetName('M-410iB-300 -3/M-410iB-300-05-1')
body_44.SetPos(chrono.ChVector3d(0.59477414230003,2.77437870841746,-2.32669735111519))
body_44.SetRot(chrono.ChQuaterniond(0.699860409425343,-0.0294561142756602,0.0289097831045659,-0.713086228370467))
body_44.SetMass(44.264758578016)
body_44.SetInertiaXX(chrono.ChVector3d(0.419802161252818,2.77625004306057,2.76548569075428))
body_44.SetInertiaXY(chrono.ChVector3d(-0.0398199766034854,-0.0533803242613383,-5.78878132818095e-05))
body_44.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-5.19600690940307e-06,0.410805913274014,-0.00264008387504332),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_9_1_shape = chrono.ChVisualShapeModelFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_44.AddVisualShape(body_9_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_44)



# Rigid body part
body_45 = chrono.ChBodyAuxRef()
body_45.SetName('M-410iB-300 -3/M-410iB-300-08-1')
body_45.SetPos(chrono.ChVector3d(-0.0775367664376988,3.00995602354016,-2.60085180219004))
body_45.SetRot(chrono.ChQuaterniond(0.77457390871473,-0.0260708930553939,0.0319960429220246,-0.631135343417726))
body_45.SetMass(7.16874140056196)
body_45.SetInertiaXX(chrono.ChVector3d(0.0767803688734156,1.02488822982072,1.09908804347466))
body_45.SetInertiaXY(chrono.ChVector3d(0.211091413570172,1.79884424153787e-05,-0.00250201297676742))
body_45.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0995028745288738,0.617303418169042,1.66091348067665e-08),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_10_1_shape = chrono.ChVisualShapeModelFile() 
body_10_1_shape.SetFilename(shapes_dir +'body_10_1.obj') 
body_45.AddVisualShape(body_10_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_45)



# Rigid body part
body_46 = chrono.ChBodyAuxRef()
body_46.SetName('M-410iB-300 -3/M-410iB-300-09-1')
body_46.SetPos(chrono.ChVector3d(1.41934259561721,2.75811166841883,-2.89763899172506))
body_46.SetRot(chrono.ChQuaterniond(0.999147807995971,-1.93552865822696e-05,0.0412727252885812,-0.000468561066093758))
body_46.SetMass(8.44776262879024)
body_46.SetInertiaXX(chrono.ChVector3d(0.11496494349016,0.723349083568589,0.823884312212851))
body_46.SetInertiaXY(chrono.ChVector3d(0.00405542478900029,-0.0591110909356657,0.00173001226666931))
body_46.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.00309747019490025,0.11726872541838,-0.0225919700688117),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_1_shape = chrono.ChVisualShapeModelFile() 
body_11_1_shape.SetFilename(shapes_dir +'body_11_1.obj') 
body_46.AddVisualShape(body_11_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_46)



# Rigid body part
body_47 = chrono.ChBodyAuxRef()
body_47.SetName('M-410iB-300 -3/M-410iB-300-07-1')
body_47.SetPos(chrono.ChVector3d(0.247503474379937,2.51550127212935,-2.56073128335825))
body_47.SetRot(chrono.ChQuaterniond(0.888019269219919,-0.0189169716008925,0.0366822356573978,-0.457950149324953))
body_47.SetMass(6.52835711422343)
body_47.SetInertiaXX(chrono.ChVector3d(0.209548912501074,0.126804969236949,0.31378904147503))
body_47.SetInertiaXY(chrono.ChVector3d(-0.133468017634731,-0.014695334387768,-0.0204548735025853))
body_47.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.244379980001897,-0.0286291463382749,-0.0666992304590947),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChVisualShapeModelFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_47.AddVisualShape(body_7_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_47)



# Rigid body part
body_48 = chrono.ChBodyAuxRef()
body_48.SetName('M-410iB-300 -3/M-410iB-300-10-1')
body_48.SetPos(chrono.ChVector3d(-0.277686877786645,2.78749692402101,-2.83238395939945))
body_48.SetRot(chrono.ChQuaterniond(0.773755292789647,-0.0261123387416691,0.0319622275946799,-0.632138678339361))
body_48.SetMass(2.24487855545089)
body_48.SetInertiaXX(chrono.ChVector3d(0.0179735699808056,0.41151320286575,0.428952544587403))
body_48.SetInertiaXY(chrono.ChVector3d(0.0835568879793482,-7.20152596639639e-06,-3.53811009408747e-05))
body_48.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-7.01323711472189e-15,0.610001635976697,-2.13860676946226e-05),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_12_1_shape = chrono.ChVisualShapeModelFile() 
body_12_1_shape.SetFilename(shapes_dir +'body_12_1.obj') 
body_48.AddVisualShape(body_12_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_48)



# Rigid body part
body_49 = chrono.ChBodyAuxRef()
body_49.SetName('M-410iB-300 -3/M-410iB-300-11-1')
body_49.SetPos(chrono.ChVector3d(1.92042610465865,3.02764258400502,-2.9082681284948))
body_49.SetRot(chrono.ChQuaterniond(0.886426585056933,-0.019044006146155,0.0366164451753445,-0.461025455996663))
body_49.SetMass(2.26635866531324)
body_49.SetInertiaXX(chrono.ChVector3d(0.342444567987369,0.170720483056036,0.50549125464023))
body_49.SetInertiaXY(chrono.ChVector3d(-0.237000685043158,-0.0239698113746433,-0.0341783798169186))
body_49.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.650000000546567,-0.000267013560427985,-4.19077490083405e-05),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChVisualShapeModelFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_49.AddVisualShape(body_8_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_49)



# Rigid body part
body_50 = chrono.ChBodyAuxRef()
body_50.SetName('M-410iB-300 -8/M-410iB-300-06-1')
body_50.SetPos(chrono.ChVector3d(-3.0845531597728,2.75811166841885,-0.985987528472769))
body_50.SetRot(chrono.ChQuaterniond(-0.0366164450839617,-0.461025460250217,0.886426582844683,0.0190440063218589))
body_50.SetMass(57.487443257986)
body_50.SetInertiaXX(chrono.ChVector3d(9.2600016804482,4.0019522848551,12.6893237121296))
body_50.SetInertiaXY(chrono.ChVector3d(-5.2493241443179,-0.6449432447705,-0.949887858884849))
body_50.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.216990574023306,0.112589145111018,-0.097224117310279),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_50.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_50_1 = chrono.ChMarker()
marker_50_1.SetName('marker_M3_A')
body_50.AddMarker(marker_50_1)
marker_50_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-3.0713571325661,2.75811166324713,-0.826532629376868),chrono.ChQuaterniond(-0.0396174502701614,0.280123903774525,0.959076201512031,-0.011571337928912)))

exported_items.append(body_50)



# Rigid body part
body_51 = chrono.ChBodyAuxRef()
body_51.SetName('M-410iB-300 -8/M-410iB-300-07-1')
body_51.SetPos(chrono.ChVector3d(-1.88884419029001,2.51550127212935,-1.03446248976697))
body_51.SetRot(chrono.ChQuaterniond(-0.0366822356573985,-0.457950149324953,0.888019269219919,0.0189169716008908))
body_51.SetMass(6.52835711422343)
body_51.SetInertiaXX(chrono.ChVector3d(0.218294896592719,0.118058985145305,0.31378904147503))
body_51.SetInertiaXY(chrono.ChVector3d(-0.130435970047168,-0.0145129242114027,-0.0205846965877363))
body_51.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.244379980001897,-0.0286291463382749,-0.0666992304590947),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChVisualShapeModelFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_51.AddVisualShape(body_7_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_51)



# Rigid body part
body_52 = chrono.ChBodyAuxRef()
body_52.SetName('M-410iB-300 -8/M-410iB-300-12-1')
body_52.SetPos(chrono.ChVector3d(-4.0796742596969,1.53452994138093,-0.870057834137045))
body_52.SetRot(chrono.ChQuaterniond(-0.0412727252884182,-0.00046856947889709,0.999147807992026,1.9355634095504e-05))
body_52.SetMass(16.1636065115335)
body_52.SetInertiaXX(chrono.ChVector3d(0.270733820597612,0.400877809867468,0.427371867141468))
body_52.SetInertiaXY(chrono.ChVector3d(0.0574221068634286,0.0377110505251339,-0.0625539343672037))
body_52.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0294847451383035,0.131793864973377,-0.039955675141979),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_52.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Collision Model

body_52.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_52 = chrono.ChContactMaterialNSC()
p1 = chrono.ChVector3d(4.57739150408006E-17, 0, 0)
p2 = chrono.ChVector3d(4.57739150408006E-17, 0.147530764880198, 0)
body_52.GetCollisionModel().AddCylinder(mat_52, 0.0891514706007005, p1, p2)
body_52.EnableCollision(True)

exported_items.append(body_52)



# Rigid body part
body_53 = chrono.ChBodyAuxRef()
body_53.SetName('M-410iB-300 -8/M-410iB-300-04-1')
body_53.SetPos(chrono.ChVector3d(-1.91121855424051,2.78048238827907,-1.29538388728574))
body_53.SetRot(chrono.ChQuaterniond(0.515318353824204,0.52505671720601,-0.47443374577748,0.483399481584652))
body_53.SetMass(1.58709182620022)
body_53.SetInertiaXX(chrono.ChVector3d(0.112490505154964,0.112417280652057,0.000998085946496918))
body_53.SetInertiaXY(chrono.ChVector3d(4.46219075106533e-06,-8.5219741688894e-05,-0.00105743461725761))
body_53.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.00250471893101799,0.259643195204338,6.66879538413109e-09),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChVisualShapeModelFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_53.AddVisualShape(body_6_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_53)



# Rigid body part
body_54 = chrono.ChBodyAuxRef()
body_54.SetName('M-410iB-300 -8/M-410iB-300-02-1')
body_54.SetPos(chrono.ChVector3d(-1.50067035795504,2.15049691615662,-1.07259688656262))
body_54.SetRot(chrono.ChQuaterniond(-0.0412727298270154,3.25742812180376e-17,0.99914791786433,-1.80125733083983e-15))
body_54.SetMass(286.960740367602)
body_54.SetInertiaXX(chrono.ChVector3d(20.3261470881377,23.3528740040787,23.2169905170889))
body_54.SetInertiaXY(chrono.ChVector3d(5.60160689862223,-0.50009164477093,-0.179388605538528))
body_54.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.175382085214385,0.199890816413736,-0.00351536323719578),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_54.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_54_1 = chrono.ChMarker()
marker_54_1.SetName('marker_M1_A')
body_54.AddMarker(marker_54_1)
marker_54_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-1.50067035795504,2.15049691615662,-1.07259688656262),chrono.ChQuaterniond(0.478937594018657,-0.478937594018658,0.520210323845674,0.520210323845672)))

# Auxiliary marker (coordinate system feature)
marker_54_2 = chrono.ChMarker()
marker_54_2.SetName('marker_M2_B')
body_54.AddMarker(marker_54_2)
marker_54_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-1.87878486024742,2.51549691615662,-0.912867668333278),chrono.ChQuaterniond(-0.0412727298270154,3.25742812180376E-17,0.99914791786433,-1.80125733083983E-15)))

exported_items.append(body_54)



# Rigid body part
body_55 = chrono.ChBodyAuxRef()
body_55.SetName('M-410iB-300 -8/M-410iB-300-03-1')
body_55.SetPos(chrono.ChVector3d(-1.88880804908083,2.51550127212935,-1.03402577529183))
body_55.SetRot(chrono.ChQuaterniond(-0.0319545439404119,-0.632366290411082,0.773569283596727,0.0261217409246417))
body_55.SetMass(72.2394925421727)
body_55.SetInertiaXX(chrono.ChVector3d(1.40287854682595,10.9514973454794,11.2634766916778))
body_55.SetInertiaXY(chrono.ChVector3d(1.87720647579531,0.783602183259728,-0.127372995689095))
body_55.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.0436192441530501,0.531901199956275,-0.00110013226020073),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_55.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_55_1 = chrono.ChMarker()
marker_55_1.SetName('marker_M2_A')
body_55.AddMarker(marker_55_1)
marker_55_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-1.87552911202723,2.51550127212935,-0.873568940661939),chrono.ChQuaterniond(-0.041066134854201,0.0998455940054076,0.994146578292323,-0.00412441456577645)))

# Auxiliary marker (coordinate system feature)
marker_55_2 = chrono.ChMarker()
marker_55_2.SetName('marker_M3_B')
body_55.AddMarker(marker_55_2)
marker_55_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-3.06708905223563,2.75811166841886,-0.774958934562062),chrono.ChQuaterniond(-0.041066134854201,0.0998455940054076,0.994146578292323,-0.00412441456577645)))

exported_items.append(body_55)



# Rigid body part
body_56 = chrono.ChBodyAuxRef()
body_56.SetName('M-410iB-300 -8/ArmBase-1')
body_56.SetPos(chrono.ChVector3d(-1.50067035795504,1.75770592148925,-1.07259688656262))
body_56.SetRot(chrono.ChQuaterniond(1.00613961606655e-16,2.24047304958526e-17,1,-1.80641517110252e-15))
body_56.SetMass(29.4636133436255)
body_56.SetInertiaXX(chrono.ChVector3d(0.754351795243641,1.45825924231452,0.754351795243641))
body_56.SetInertiaXY(chrono.ChVector3d(1.23873904251348e-17,-1.41610608623833e-16,-2.75999744864809e-15))
body_56.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-9.77354995986777e-18,0.231605672678633,-6.24094154063845e-18),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChVisualShapeModelFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_56.AddVisualShape(body_5_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_56_1 = chrono.ChMarker()
marker_56_1.SetName('marker_M1_B')
body_56.AddMarker(marker_56_1)
marker_56_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-1.50067035795504,1.75770592148925,-1.07259688656262),chrono.ChQuaterniond(-0.499999999999999,0.500000000000001,-0.500000000000001,-0.499999999999999)))

exported_items.append(body_56)



# Rigid body part
body_57 = chrono.ChBodyAuxRef()
body_57.SetName('M-410iB-300 -8/M-410iB-300-05-1')
body_57.SetPos(chrono.ChVector3d(-2.2361148582101,2.77437870841746,-1.26849642201004))
body_57.SetRot(chrono.ChQuaterniond(0.0289097831045672,0.713086228370467,-0.699860409425343,-0.0294561142756589))
body_57.SetMass(44.264758578016)
body_57.SetInertiaXX(chrono.ChVector3d(0.420124912385258,2.77592729192813,2.76548569075428))
body_57.SetInertiaXY(chrono.ChVector3d(-0.0484362735024021,0.0533450810289395,0.00194028329365972))
body_57.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-5.19600690940307e-06,0.410805913274014,-0.00264008387504332),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_9_1_shape = chrono.ChVisualShapeModelFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_57.AddVisualShape(body_9_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_57)



# Rigid body part
body_58 = chrono.ChBodyAuxRef()
body_58.SetName('M-410iB-300 -8/M-410iB-300-08-1')
body_58.SetPos(chrono.ChVector3d(-1.56380394947237,3.00995602354016,-0.994341970935191))
body_58.SetRot(chrono.ChQuaterniond(-0.0319960429220257,-0.631135343417726,0.77457390871473,0.0260708930553925))
body_58.SetMass(7.16874140056196)
body_58.SetInertiaXX(chrono.ChVector3d(0.0717801649549737,1.02988843373916,1.09908804347466))
body_58.SetInertiaXY(chrono.ChVector3d(0.199483959762215,-0.00100638858175135,-0.00229075850811437))
body_58.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0995028745288738,0.617303418169042,1.66091348067665e-08),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_10_1_shape = chrono.ChVisualShapeModelFile() 
body_10_1_shape.SetFilename(shapes_dir +'body_10_1.obj') 
body_58.AddVisualShape(body_10_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_58)



# Rigid body part
body_59 = chrono.ChBodyAuxRef()
body_59.SetName('M-410iB-300 -8/M-410iB-300-09-1')
body_59.SetPos(chrono.ChVector3d(-3.06068331152728,2.75811166841883,-0.697554781400167))
body_59.SetRot(chrono.ChQuaterniond(-0.0412727252885811,-0.000468561066093659,0.999147807995971,1.93552865804655e-05))
body_59.SetMass(8.44776262879024)
body_59.SetInertiaXX(chrono.ChVector3d(0.114982298903477,0.723331728155272,0.823884312212851))
body_59.SetInertiaXY(chrono.ChVector3d(-0.00519662652260743,-0.0591077417070738,-0.0018408922665937))
body_59.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.00309747019490025,0.11726872541838,-0.0225919700688117),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_1_shape = chrono.ChVisualShapeModelFile() 
body_11_1_shape.SetFilename(shapes_dir +'body_11_1.obj') 
body_59.AddVisualShape(body_11_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_59)



# Rigid body part
body_60 = chrono.ChBodyAuxRef()
body_60.SetName('M-410iB-300 -8/M-410iB-300-11-1')
body_60.SetPos(chrono.ChVector3d(-3.56176682056872,3.02764258400502,-0.686925644630428))
body_60.SetRot(chrono.ChQuaterniond(-0.0366164451753452,-0.461025455996663,0.886426585056933,0.0190440061461534))
body_60.SetMass(2.26635866531324)
body_60.SetInertiaXX(chrono.ChVector3d(0.342444575932242,0.170720475111163,0.50549125464023))
body_60.SetInertiaXY(chrono.ChVector3d(-0.237000682164841,-0.0239698954072387,-0.0341783208834423))
body_60.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.650000000546567,-0.000267013560427985,-4.19077490083405e-05),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChVisualShapeModelFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_60.AddVisualShape(body_8_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_60)



# Rigid body part
body_61 = chrono.ChBodyAuxRef()
body_61.SetName('M-410iB-300 -8/M-410iB-300-10-1')
body_61.SetPos(chrono.ChVector3d(-1.36365383812343,2.78749692402101,-0.762809813725776))
body_61.SetRot(chrono.ChQuaterniond(-0.031962227594681,-0.632138678339361,0.773755292789647,0.0261123387416677))
body_61.SetMass(2.24487855545089)
body_61.SetInertiaXX(chrono.ChVector3d(0.0179735699467435,0.411513202899812,0.428952544587403))
body_61.SetInertiaXY(chrono.ChVector3d(0.0835568878991346,-7.20049407700778e-06,-3.53813109576287e-05))
body_61.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-7.01323711472189e-15,0.610001635976697,-2.13860676946226e-05),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_12_1_shape = chrono.ChVisualShapeModelFile() 
body_12_1_shape.SetFilename(shapes_dir +'body_12_1.obj') 
body_61.AddVisualShape(body_12_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_61)



# Rigid body part
body_62 = chrono.ChBodyAuxRef()
body_62.SetName('M-410iB-300 -7/M-410iB-300-03-1')
body_62.SetPos(chrono.ChVector3d(-1.88880804908083,2.51550127212934,-2.48402577529183))
body_62.SetRot(chrono.ChQuaterniond(-0.0319545439404118,-0.632366290411082,0.773569283596727,0.0261217409246417))
body_62.SetMass(72.2394925421727)
body_62.SetInertiaXX(chrono.ChVector3d(1.40287854682595,10.9514973454794,11.2634766916778))
body_62.SetInertiaXY(chrono.ChVector3d(1.87720647579531,0.783602183259729,-0.127372995689095))
body_62.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.0436192441530501,0.531901199956275,-0.00110013226020073),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_62.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_62_1 = chrono.ChMarker()
marker_62_1.SetName('marker_M2_A')
body_62.AddMarker(marker_62_1)
marker_62_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-1.87552911202723,2.51550127212934,-2.32356894066194),chrono.ChQuaterniond(-0.041066134854201,0.0998455940054075,0.994146578292323,-0.00412441456577641)))

# Auxiliary marker (coordinate system feature)
marker_62_2 = chrono.ChMarker()
marker_62_2.SetName('marker_M3_B')
body_62.AddMarker(marker_62_2)
marker_62_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-3.06708905223563,2.75811166841885,-2.22495893456206),chrono.ChQuaterniond(-0.041066134854201,0.0998455940054075,0.994146578292323,-0.00412441456577641)))

exported_items.append(body_62)



# Rigid body part
body_63 = chrono.ChBodyAuxRef()
body_63.SetName('M-410iB-300 -7/M-410iB-300-09-1')
body_63.SetPos(chrono.ChVector3d(-3.06068331152728,2.75811166841883,-2.14755478140017))
body_63.SetRot(chrono.ChQuaterniond(-0.0412727252885811,-0.000468561066093719,0.999147807995971,1.93552865805488e-05))
body_63.SetMass(8.44776262879024)
body_63.SetInertiaXX(chrono.ChVector3d(0.114982298903477,0.723331728155272,0.823884312212851))
body_63.SetInertiaXY(chrono.ChVector3d(-0.00519662652260749,-0.0591077417070738,-0.00184089226659358))
body_63.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.00309747019490025,0.11726872541838,-0.0225919700688117),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_11_1_shape = chrono.ChVisualShapeModelFile() 
body_11_1_shape.SetFilename(shapes_dir +'body_11_1.obj') 
body_63.AddVisualShape(body_11_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_63)



# Rigid body part
body_64 = chrono.ChBodyAuxRef()
body_64.SetName('M-410iB-300 -7/ArmBase-1')
body_64.SetPos(chrono.ChVector3d(-1.50067035795504,1.75770592148925,-2.52259688656262))
body_64.SetRot(chrono.ChQuaterniond(1.08554747315437e-16,-3.21041963728343e-17,1,-1.72084568816899e-15))
body_64.SetMass(29.4636133436255)
body_64.SetInertiaXX(chrono.ChVector3d(0.754351795243641,1.45825924231452,0.754351795243641))
body_64.SetInertiaXY(chrono.ChVector3d(-4.35433575050877e-17,-2.64545330086461e-17,-2.43089923188912e-15))
body_64.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-9.77354995986777e-18,0.231605672678633,-6.24094154063845e-18),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChVisualShapeModelFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_64.AddVisualShape(body_5_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_64_1 = chrono.ChMarker()
marker_64_1.SetName('marker_M1_B')
body_64.AddMarker(marker_64_1)
marker_64_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-1.50067035795504,1.75770592148925,-2.52259688656262),chrono.ChQuaterniond(-0.499999999999999,0.500000000000001,-0.500000000000001,-0.499999999999999)))

exported_items.append(body_64)



# Rigid body part
body_65 = chrono.ChBodyAuxRef()
body_65.SetName('M-410iB-300 -7/M-410iB-300-06-1')
body_65.SetPos(chrono.ChVector3d(-3.0845531597728,2.75811166841885,-2.43598752847277))
body_65.SetRot(chrono.ChQuaterniond(-0.0366164450839616,-0.461025460250217,0.886426582844683,0.019044006321859))
body_65.SetMass(57.487443257986)
body_65.SetInertiaXX(chrono.ChVector3d(9.2600016804482,4.0019522848551,12.6893237121296))
body_65.SetInertiaXY(chrono.ChVector3d(-5.2493241443179,-0.644943244770499,-0.949887858884848))
body_65.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.216990574023306,0.112589145111018,-0.097224117310279),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_65.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_65_1 = chrono.ChMarker()
marker_65_1.SetName('marker_M3_A')
body_65.AddMarker(marker_65_1)
marker_65_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-3.0713571325661,2.75811166324713,-2.27653262937687),chrono.ChQuaterniond(-0.0396174502701613,0.280123903774525,0.959076201512031,-0.0115713379289119)))

exported_items.append(body_65)



# Rigid body part
body_66 = chrono.ChBodyAuxRef()
body_66.SetName('M-410iB-300 -7/M-410iB-300-05-1')
body_66.SetPos(chrono.ChVector3d(-2.2361148582101,2.77437870841745,-2.71849642201004))
body_66.SetRot(chrono.ChQuaterniond(0.0289097831045671,0.713086228370467,-0.699860409425343,-0.029456114275659))
body_66.SetMass(44.264758578016)
body_66.SetInertiaXX(chrono.ChVector3d(0.420124912385258,2.77592729192813,2.76548569075428))
body_66.SetInertiaXY(chrono.ChVector3d(-0.0484362735024024,0.0533450810289396,0.00194028329366022))
body_66.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-5.19600690940307e-06,0.410805913274014,-0.00264008387504332),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_9_1_shape = chrono.ChVisualShapeModelFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_66.AddVisualShape(body_9_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_66)



# Rigid body part
body_67 = chrono.ChBodyAuxRef()
body_67.SetName('M-410iB-300 -7/M-410iB-300-02-1')
body_67.SetPos(chrono.ChVector3d(-1.50067035795504,2.15049691615661,-2.52259688656262))
body_67.SetRot(chrono.ChQuaterniond(-0.0412727298270154,-2.7373752934118e-17,0.99914791786433,-1.71789680388663e-15))
body_67.SetMass(286.960740367602)
body_67.SetInertiaXX(chrono.ChVector3d(20.3261470881377,23.3528740040787,23.2169905170889))
body_67.SetInertiaXY(chrono.ChVector3d(5.60160689862223,-0.500091644770924,-0.179388605538523))
body_67.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.175382085214385,0.199890816413736,-0.00351536323719578),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_67.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_67_1 = chrono.ChMarker()
marker_67_1.SetName('marker_M1_A')
body_67.AddMarker(marker_67_1)
marker_67_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-1.50067035795504,2.15049691615661,-2.52259688656262),chrono.ChQuaterniond(0.478937594018657,-0.478937594018658,0.520210323845674,0.520210323845672)))

# Auxiliary marker (coordinate system feature)
marker_67_2 = chrono.ChMarker()
marker_67_2.SetName('marker_M2_B')
body_67.AddMarker(marker_67_2)
marker_67_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-1.87878486024742,2.51549691615662,-2.36286766833328),chrono.ChQuaterniond(-0.0412727298270154,-2.7373752934118E-17,0.99914791786433,-1.71789680388663E-15)))

exported_items.append(body_67)



# Rigid body part
body_68 = chrono.ChBodyAuxRef()
body_68.SetName('M-410iB-300 -7/M-410iB-300-07-1')
body_68.SetPos(chrono.ChVector3d(-1.88884419029001,2.51550127212935,-2.48446248976697))
body_68.SetRot(chrono.ChQuaterniond(-0.0366822356573985,-0.457950149324953,0.888019269219919,0.0189169716008909))
body_68.SetMass(6.52835711422343)
body_68.SetInertiaXX(chrono.ChVector3d(0.218294896592719,0.118058985145305,0.31378904147503))
body_68.SetInertiaXY(chrono.ChVector3d(-0.130435970047168,-0.0145129242114027,-0.0205846965877362))
body_68.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.244379980001897,-0.0286291463382749,-0.0666992304590947),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChVisualShapeModelFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_68.AddVisualShape(body_7_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_68)



# Rigid body part
body_69 = chrono.ChBodyAuxRef()
body_69.SetName('M-410iB-300 -7/M-410iB-300-08-1')
body_69.SetPos(chrono.ChVector3d(-1.56380394947237,3.00995602354015,-2.44434197093519))
body_69.SetRot(chrono.ChQuaterniond(-0.0319960429220256,-0.631135343417726,0.77457390871473,0.0260708930553925))
body_69.SetMass(7.16874140056196)
body_69.SetInertiaXX(chrono.ChVector3d(0.0717801649549736,1.02988843373916,1.09908804347466))
body_69.SetInertiaXY(chrono.ChVector3d(0.199483959762215,-0.00100638858175128,-0.00229075850811442))
body_69.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0995028745288738,0.617303418169042,1.66091348067665e-08),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_10_1_shape = chrono.ChVisualShapeModelFile() 
body_10_1_shape.SetFilename(shapes_dir +'body_10_1.obj') 
body_69.AddVisualShape(body_10_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_69)



# Rigid body part
body_70 = chrono.ChBodyAuxRef()
body_70.SetName('M-410iB-300 -7/M-410iB-300-12-1')
body_70.SetPos(chrono.ChVector3d(-4.0796742596969,1.53452994138093,-2.32005783413704))
body_70.SetRot(chrono.ChQuaterniond(-0.0412727252884181,-0.000468569478897149,0.999147807992026,1.93556340955399e-05))
body_70.SetMass(16.1636065115335)
body_70.SetInertiaXX(chrono.ChVector3d(0.270733820597613,0.400877809867468,0.427371867141468))
body_70.SetInertiaXY(chrono.ChVector3d(0.0574221068634286,0.0377110505251339,-0.0625539343672037))
body_70.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0294847451383035,0.131793864973377,-0.039955675141979),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_70.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Collision Model

body_70.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_70 = chrono.ChContactMaterialNSC()
p1 = chrono.ChVector3d(4.57739150408006E-17, 0, 0)
p2 = chrono.ChVector3d(4.57739150408006E-17, 0.147530764880198, 0)
body_70.GetCollisionModel().AddCylinder(mat_70, 0.0891514706007005, p1, p2)
body_70.EnableCollision(True)

exported_items.append(body_70)



# Rigid body part
body_71 = chrono.ChBodyAuxRef()
body_71.SetName('M-410iB-300 -7/M-410iB-300-04-1')
body_71.SetPos(chrono.ChVector3d(-1.91121855424051,2.78048238827906,-2.74538388728574))
body_71.SetRot(chrono.ChQuaterniond(0.515318353824204,0.52505671720601,-0.47443374577748,0.483399481584652))
body_71.SetMass(1.58709182620022)
body_71.SetInertiaXX(chrono.ChVector3d(0.112490505154964,0.112417280652057,0.000998085946496919))
body_71.SetInertiaXY(chrono.ChVector3d(4.46219075106793e-06,-8.52197416889226e-05,-0.00105743461725763))
body_71.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.00250471893101799,0.259643195204338,6.66879538413109e-09),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChVisualShapeModelFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_71.AddVisualShape(body_6_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_71)



# Rigid body part
body_72 = chrono.ChBodyAuxRef()
body_72.SetName('M-410iB-300 -7/M-410iB-300-10-1')
body_72.SetPos(chrono.ChVector3d(-1.36365383812343,2.78749692402101,-2.21280981372578))
body_72.SetRot(chrono.ChQuaterniond(-0.0319622275946809,-0.632138678339361,0.773755292789647,0.0261123387416677))
body_72.SetMass(2.24487855545089)
body_72.SetInertiaXX(chrono.ChVector3d(0.0179735699467434,0.411513202899812,0.428952544587403))
body_72.SetInertiaXY(chrono.ChVector3d(0.0835568878991346,-7.20049407697872e-06,-3.53813109576287e-05))
body_72.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-7.01323711472189e-15,0.610001635976697,-2.13860676946226e-05),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_12_1_shape = chrono.ChVisualShapeModelFile() 
body_12_1_shape.SetFilename(shapes_dir +'body_12_1.obj') 
body_72.AddVisualShape(body_12_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_72)



# Rigid body part
body_73 = chrono.ChBodyAuxRef()
body_73.SetName('M-410iB-300 -7/M-410iB-300-11-1')
body_73.SetPos(chrono.ChVector3d(-3.56176682056872,3.02764258400502,-2.13692564463043))
body_73.SetRot(chrono.ChQuaterniond(-0.0366164451753452,-0.461025455996663,0.886426585056933,0.0190440061461534))
body_73.SetMass(2.26635866531324)
body_73.SetInertiaXX(chrono.ChVector3d(0.342444575932242,0.170720475111163,0.50549125464023))
body_73.SetInertiaXY(chrono.ChVector3d(-0.237000682164841,-0.0239698954072387,-0.0341783208834424))
body_73.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.650000000546567,-0.000267013560427985,-4.19077490083405e-05),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChVisualShapeModelFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_73.AddVisualShape(body_8_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_73)




# Mate constraint: Coincident1 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: M-410iB-300 -1/ArmBase-1 ,  SW ref.type:2 (2)
link_1 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.620670357955037,1.94456417249918,0.727403113437383)
cB = chrono.ChVector3d(-0.140670357955037,1.94456417249918,0.37740311343739)
dA = chrono.ChVector3d(0,1,-3.49148133884313e-15)
dB = chrono.ChVector3d(0,-1,0)
link_1.Initialize(body_25,body_5,False,cA,cB,dB)
link_1.SetDistance(0)
link_1.SetName("Coincident1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.620670357955037,1.94456417249918,0.727403113437383)
dA = chrono.ChVector3d(0,1,-3.49148133884313e-15)
cB = chrono.ChVector3d(-0.140670357955037,1.94456417249918,0.37740311343739)
dB = chrono.ChVector3d(0,-1,0)
link_2.SetFlipped(True)
link_2.Initialize(body_25,body_5,False,cA,cB,dA,dB)
link_2.SetName("Coincident1")
exported_items.append(link_2)


# Mate constraint: Distance1 [MateDistanceDim] type:5 align:0 flip:False
#   Entity 0: C::E name: body_5 , SW name: M-410iB-300 -1/ArmBase-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
link_3 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.460670357955037,1.94456417249918,0.69740311343739)
cB = chrono.ChVector3d(-0.620670357955037,1.69456417249918,0.727403113437384)
dA = chrono.ChVector3d(0,0,1)
dB = chrono.ChVector3d(0,3.49148133884313e-15,1)
link_3.Initialize(body_5,body_25,False,cA,cB,dB)
link_3.SetDistance(-0.03)
link_3.SetName("Distance1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.460670357955037,1.94456417249918,0.69740311343739)
dA = chrono.ChVector3d(0,0,1)
cB = chrono.ChVector3d(-0.620670357955037,1.69456417249918,0.727403113437384)
dB = chrono.ChVector3d(0,3.49148133884313e-15,1)
link_4.Initialize(body_5,body_25,False,cA,cB,dA,dB)
link_4.SetName("Distance1")
exported_items.append(link_4)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:2 flip:False
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: M-410iB-300 -1/ArmBase-1 ,  SW ref.type:1 (1)
link_5 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.179329642044963,1.69456417249918,0.727403113437384)
cB = chrono.ChVector3d(0.179329642044963,1.94456417249918,0.37740311343739)
dA = chrono.ChVector3d(1,5.53760424633245e-31,1.58603289232165e-16)
dB = chrono.ChVector3d(1,0,0)
link_5.Initialize(body_5,body_25,False,cB,cA,dA)
link_5.SetDistance(0)
link_5.SetName("Coincident3")
exported_items.append(link_5)


# ChLinkMateOrthogonal skipped because directions not orthogonal! 

# Mate constraint: Coincident4_issue [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_18 , SW name: M-410iB-300 -2/ArmBase-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
link_6 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.179329642044963,1.94456417249918,-1.07259688656261)
cB = chrono.ChVector3d(0.179329642044963,1.69456417249918,-0.722596886562616)
dA = chrono.ChVector3d(1,0,0)
dB = chrono.ChVector3d(1,5.53760424633245e-31,1.58603289232165e-16)
link_6.Initialize(body_18,body_25,False,cA,cB,dB)
link_6.SetDistance(0)
link_6.SetName("Coincident4_issue")
exported_items.append(link_6)


# ChLinkMateOrthogonal skipped because directions not orthogonal! 

# Mate constraint: Coincident5 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_18 , SW name: M-410iB-300 -2/ArmBase-1 ,  SW ref.type:2 (2)
link_7 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.620670357955037,1.94456417249918,-0.722596886562617)
cB = chrono.ChVector3d(-0.140670357955037,1.94456417249918,-1.07259688656261)
dA = chrono.ChVector3d(0,1,-3.49148133884313e-15)
dB = chrono.ChVector3d(0,-1,0)
link_7.Initialize(body_25,body_18,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident5")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.620670357955037,1.94456417249918,-0.722596886562617)
dA = chrono.ChVector3d(0,1,-3.49148133884313e-15)
cB = chrono.ChVector3d(-0.140670357955037,1.94456417249918,-1.07259688656261)
dB = chrono.ChVector3d(0,-1,0)
link_8.SetFlipped(True)
link_8.Initialize(body_25,body_18,False,cA,cB,dA,dB)
link_8.SetName("Coincident5")
exported_items.append(link_8)


# Mate constraint: Distance2 [MateDistanceDim] type:5 align:0 flip:False
#   Entity 0: C::E name: body_18 , SW name: M-410iB-300 -2/ArmBase-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
link_9 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.460670357955037,1.94456417249918,-1.39259688656261)
cB = chrono.ChVector3d(-0.620670357955037,1.69456417249917,-1.42259688656262)
dA = chrono.ChVector3d(0,0,-1)
dB = chrono.ChVector3d(0,-3.49148133884313e-15,-1)
link_9.Initialize(body_18,body_25,False,cA,cB,dB)
link_9.SetDistance(-0.03)
link_9.SetName("Distance2")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.460670357955037,1.94456417249918,-1.39259688656261)
dA = chrono.ChVector3d(0,0,-1)
cB = chrono.ChVector3d(-0.620670357955037,1.69456417249917,-1.42259688656262)
dB = chrono.ChVector3d(0,-3.49148133884313e-15,-1)
link_10.Initialize(body_18,body_25,False,cA,cB,dA,dB)
link_10.SetName("Distance2")
exported_items.append(link_10)


# Mate constraint: Coincident7 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_43 , SW name: M-410iB-300 -3/ArmBase-1 ,  SW ref.type:2 (2)
link_11 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.620670357955037,1.94456417249917,-2.17259688656262)
cB = chrono.ChVector3d(-0.140670357955037,1.94456417249918,-2.52259688656261)
dA = chrono.ChVector3d(0,1,-3.49148133884313e-15)
dB = chrono.ChVector3d(0,-1,0)
link_11.Initialize(body_25,body_43,False,cA,cB,dB)
link_11.SetDistance(0)
link_11.SetName("Coincident7")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.620670357955037,1.94456417249917,-2.17259688656262)
dA = chrono.ChVector3d(0,1,-3.49148133884313e-15)
cB = chrono.ChVector3d(-0.140670357955037,1.94456417249918,-2.52259688656261)
dB = chrono.ChVector3d(0,-1,0)
link_12.SetFlipped(True)
link_12.Initialize(body_25,body_43,False,cA,cB,dA,dB)
link_12.SetName("Coincident7")
exported_items.append(link_12)


# Mate constraint: Distance3 [MateDistanceDim] type:5 align:0 flip:False
#   Entity 0: C::E name: body_43 , SW name: M-410iB-300 -3/ArmBase-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
link_13 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.460670357955037,1.94456417249918,-2.84259688656261)
cB = chrono.ChVector3d(-0.620670357955037,1.69456417249917,-2.87259688656262)
dA = chrono.ChVector3d(0,0,-1)
dB = chrono.ChVector3d(0,-3.49148133884313e-15,-1)
link_13.Initialize(body_43,body_25,False,cA,cB,dB)
link_13.SetDistance(-0.03)
link_13.SetName("Distance3")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.460670357955037,1.94456417249918,-2.84259688656261)
dA = chrono.ChVector3d(0,0,-1)
cB = chrono.ChVector3d(-0.620670357955037,1.69456417249917,-2.87259688656262)
dB = chrono.ChVector3d(0,-3.49148133884313e-15,-1)
link_14.Initialize(body_43,body_25,False,cA,cB,dA,dB)
link_14.SetName("Distance3")
exported_items.append(link_14)


# Mate constraint: Coincident9 [MateCoincident] type:0 align:2 flip:False
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_43 , SW name: M-410iB-300 -3/ArmBase-1 ,  SW ref.type:1 (1)
link_15 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.179329642044963,1.69456417249917,-2.17259688656262)
cB = chrono.ChVector3d(0.179329642044963,1.94456417249918,-2.52259688656261)
dA = chrono.ChVector3d(1,5.53760424633245e-31,1.58603289232165e-16)
dB = chrono.ChVector3d(1,0,0)
link_15.Initialize(body_43,body_25,False,cB,cA,dA)
link_15.SetDistance(0)
link_15.SetName("Coincident9")
exported_items.append(link_15)


# ChLinkMateOrthogonal skipped because directions not orthogonal! 

# Mate constraint: Coincident11 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_64 , SW name: M-410iB-300 -7/ArmBase-1 ,  SW ref.type:2 (2)
link_16 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.82067035795504,1.69456417249917,-2.17259688656262)
cB = chrono.ChVector3d(-1.82067035795504,1.94456417249917,-2.20259688656262)
dA = chrono.ChVector3d(-1,-3.01405864546147e-31,-8.63260705973055e-17)
dB = chrono.ChVector3d(-1,-6.4208392745669e-17,-2.17109494630873e-16)
link_16.Initialize(body_25,body_64,False,cA,cB,dB)
link_16.SetDistance(0)
link_16.SetName("Coincident11")
exported_items.append(link_16)

link_17 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.82067035795504,1.69456417249917,-2.17259688656262)
dA = chrono.ChVector3d(-1,-3.01405864546147e-31,-8.63260705973055e-17)
cB = chrono.ChVector3d(-1.82067035795504,1.94456417249917,-2.20259688656262)
dB = chrono.ChVector3d(-1,-6.4208392745669e-17,-2.17109494630873e-16)
link_17.Initialize(body_25,body_64,False,cA,cB,dA,dB)
link_17.SetName("Coincident11")
exported_items.append(link_17)


# Mate constraint: Coincident12 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_56 , SW name: M-410iB-300 -8/ArmBase-1 ,  SW ref.type:2 (2)
link_18 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.02067035795504,1.94456417249918,-0.722596886562617)
cB = chrono.ChVector3d(-1.50067035795504,1.94456417249918,-1.07259688656262)
dA = chrono.ChVector3d(0,1,-3.49148133884313e-15)
dB = chrono.ChVector3d(-5.42136132923115e-17,-1,3.51853802391695e-15)
link_18.Initialize(body_25,body_56,False,cA,cB,dB)
link_18.SetDistance(0)
link_18.SetName("Coincident12")
exported_items.append(link_18)

link_19 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.02067035795504,1.94456417249918,-0.722596886562617)
dA = chrono.ChVector3d(0,1,-3.49148133884313e-15)
cB = chrono.ChVector3d(-1.50067035795504,1.94456417249918,-1.07259688656262)
dB = chrono.ChVector3d(-5.42136132923115e-17,-1,3.51853802391695e-15)
link_19.SetFlipped(True)
link_19.Initialize(body_25,body_56,False,cA,cB,dA,dB)
link_19.SetName("Coincident12")
exported_items.append(link_19)


# Mate constraint: Coincident14 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_28 , SW name: M-410iB-300 -9/ArmBase-1 ,  SW ref.type:2 (2)
link_20 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.02067035795504,1.94456417249918,0.727403113437383)
cB = chrono.ChVector3d(-1.50067035795504,1.94456417249918,0.377403113437383)
dA = chrono.ChVector3d(0,1,-3.49148133884313e-15)
dB = chrono.ChVector3d(6.21947280249299e-17,-1,3.55871276754624e-15)
link_20.Initialize(body_25,body_28,False,cA,cB,dB)
link_20.SetDistance(0)
link_20.SetName("Coincident14")
exported_items.append(link_20)

link_21 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.02067035795504,1.94456417249918,0.727403113437383)
dA = chrono.ChVector3d(0,1,-3.49148133884313e-15)
cB = chrono.ChVector3d(-1.50067035795504,1.94456417249918,0.377403113437383)
dB = chrono.ChVector3d(6.21947280249299e-17,-1,3.55871276754624e-15)
link_21.SetFlipped(True)
link_21.Initialize(body_25,body_28,False,cA,cB,dA,dB)
link_21.SetName("Coincident14")
exported_items.append(link_21)


# Mate constraint: Coincident16 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_28 , SW name: M-410iB-300 -9/ArmBase-1 ,  SW ref.type:2 (2)
link_22 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.82067035795504,1.69456417249918,0.727403113437384)
cB = chrono.ChVector3d(-1.82067035795504,1.94456417249918,0.697403113437383)
dA = chrono.ChVector3d(-1,-3.01405864546147e-31,-8.63260705973055e-17)
dB = chrono.ChVector3d(-1,-6.21947280249306e-17,-2.22044604925031e-16)
link_22.Initialize(body_25,body_28,False,cA,cB,dB)
link_22.SetDistance(0)
link_22.SetName("Coincident16")
exported_items.append(link_22)

link_23 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.82067035795504,1.69456417249918,0.727403113437384)
dA = chrono.ChVector3d(-1,-3.01405864546147e-31,-8.63260705973055e-17)
cB = chrono.ChVector3d(-1.82067035795504,1.94456417249918,0.697403113437383)
dB = chrono.ChVector3d(-1,-6.21947280249306e-17,-2.22044604925031e-16)
link_23.Initialize(body_25,body_28,False,cA,cB,dA,dB)
link_23.SetName("Coincident16")
exported_items.append(link_23)


# Mate constraint: Coincident17 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_64 , SW name: M-410iB-300 -7/ArmBase-1 ,  SW ref.type:2 (2)
link_24 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.02067035795504,1.94456417249917,-2.17259688656262)
cB = chrono.ChVector3d(-1.50067035795504,1.94456417249917,-2.52259688656262)
dA = chrono.ChVector3d(0,1,-3.49148133884313e-15)
dB = chrono.ChVector3d(6.42083927456682e-17,-1,3.44169137633798e-15)
link_24.Initialize(body_25,body_64,False,cA,cB,dB)
link_24.SetDistance(0)
link_24.SetName("Coincident17")
exported_items.append(link_24)

link_25 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.02067035795504,1.94456417249917,-2.17259688656262)
dA = chrono.ChVector3d(0,1,-3.49148133884313e-15)
cB = chrono.ChVector3d(-1.50067035795504,1.94456417249917,-2.52259688656262)
dB = chrono.ChVector3d(6.42083927456682e-17,-1,3.44169137633798e-15)
link_25.SetFlipped(True)
link_25.Initialize(body_25,body_64,False,cA,cB,dA,dB)
link_25.SetName("Coincident17")
exported_items.append(link_25)


# Mate constraint: Coincident18 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_56 , SW name: M-410iB-300 -8/ArmBase-1 ,  SW ref.type:2 (2)
link_26 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.82067035795504,1.69456417249918,-0.722596886562616)
cB = chrono.ChVector3d(-1.82067035795504,1.94456417249918,-0.752596886562616)
dA = chrono.ChVector3d(-1,-3.01405864546147e-31,-8.63260705973055e-17)
dB = chrono.ChVector3d(-1,3.54053086910991e-17,-1.2490009027033e-16)
link_26.Initialize(body_25,body_56,False,cA,cB,dB)
link_26.SetDistance(0)
link_26.SetName("Coincident18")
exported_items.append(link_26)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.82067035795504,1.69456417249918,-0.722596886562616)
dA = chrono.ChVector3d(-1,-3.01405864546147e-31,-8.63260705973055e-17)
cB = chrono.ChVector3d(-1.82067035795504,1.94456417249918,-0.752596886562616)
dB = chrono.ChVector3d(-1,3.54053086910991e-17,-1.2490009027033e-16)
link_27.Initialize(body_25,body_56,False,cA,cB,dA,dB)
link_27.SetName("Coincident18")
exported_items.append(link_27)


# Mate constraint: Distance4 [MateDistanceDim] type:5 align:0 flip:True
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_64 , SW name: M-410iB-300 -7/ArmBase-1 ,  SW ref.type:2 (2)
link_28 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.02067035795504,1.69456417249917,-2.87259688656262)
cB = chrono.ChVector3d(-1.18067035795504,1.94456417249917,-2.84259688656262)
dA = chrono.ChVector3d(2.44929359829471e-16,-3.49148133884313e-15,-1)
dB = chrono.ChVector3d(2.17109494630873e-16,-3.44169137633798e-15,-1)
link_28.Initialize(body_25,body_64,False,cA,cB,dB)
link_28.SetDistance(0.0300000000000003)
link_28.SetName("Distance4")
exported_items.append(link_28)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.02067035795504,1.69456417249917,-2.87259688656262)
dA = chrono.ChVector3d(2.44929359829471e-16,-3.49148133884313e-15,-1)
cB = chrono.ChVector3d(-1.18067035795504,1.94456417249917,-2.84259688656262)
dB = chrono.ChVector3d(2.17109494630873e-16,-3.44169137633798e-15,-1)
link_29.Initialize(body_25,body_64,False,cA,cB,dA,dB)
link_29.SetName("Distance4")
exported_items.append(link_29)


# Mate constraint: Distance5 [MateDistanceDim] type:5 align:0 flip:True
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_56 , SW name: M-410iB-300 -8/ArmBase-1 ,  SW ref.type:2 (2)
link_30 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.02067035795504,1.69456417249917,-1.42259688656262)
cB = chrono.ChVector3d(-1.18067035795504,1.94456417249917,-1.39259688656262)
dA = chrono.ChVector3d(2.44929359829471e-16,-3.49148133884313e-15,-1)
dB = chrono.ChVector3d(2.77555756156289e-16,-3.70712266049311e-15,-1)
link_30.Initialize(body_25,body_56,False,cA,cB,dB)
link_30.SetDistance(0.03)
link_30.SetName("Distance5")
exported_items.append(link_30)

link_31 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.02067035795504,1.69456417249917,-1.42259688656262)
dA = chrono.ChVector3d(2.44929359829471e-16,-3.49148133884313e-15,-1)
cB = chrono.ChVector3d(-1.18067035795504,1.94456417249917,-1.39259688656262)
dB = chrono.ChVector3d(2.77555756156289e-16,-3.70712266049311e-15,-1)
link_31.Initialize(body_25,body_56,False,cA,cB,dA,dB)
link_31.SetName("Distance5")
exported_items.append(link_31)


# Mate constraint: Distance6 [MateDistanceDim] type:5 align:0 flip:True
#   Entity 0: C::E name: body_25 , SW name: Part3^SPIDER_ROBOT-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_28 , SW name: M-410iB-300 -9/ArmBase-1 ,  SW ref.type:2 (2)
link_32 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.02067035795504,1.69456417249918,0.0274031134373841)
cB = chrono.ChVector3d(-1.18067035795504,1.94456417249918,0.0574031134373831)
dA = chrono.ChVector3d(2.44929359829471e-16,-3.49148133884313e-15,-1)
dB = chrono.ChVector3d(2.22044604925031e-16,-3.55871276754624e-15,-1)
link_32.Initialize(body_25,body_28,False,cA,cB,dB)
link_32.SetDistance(0.03)
link_32.SetName("Distance6")
exported_items.append(link_32)

link_33 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.02067035795504,1.69456417249918,0.0274031134373841)
dA = chrono.ChVector3d(2.44929359829471e-16,-3.49148133884313e-15,-1)
cB = chrono.ChVector3d(-1.18067035795504,1.94456417249918,0.0574031134373831)
dB = chrono.ChVector3d(2.22044604925031e-16,-3.55871276754624e-15,-1)
link_33.Initialize(body_25,body_28,False,cA,cB,dA,dB)
link_33.SetName("Distance6")
exported_items.append(link_33)


# Mate constraint: Coincident2_hinge [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: M-410iB-300 -1/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_3 , SW name: M-410iB-300 -1/M-410iB-300-03-1 ,  SW ref.type:5 (5)
link_34 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.237440667378504,2.51550127212935,0.217674182950967)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
cB = chrono.ChVector3d(0.256663804363385,2.51550127212935,0.449958115000637)
dB = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
link_34.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_34.SetName("Coincident2_hinge")
exported_items.append(link_34)

link_35 = chrono.ChLinkMateGeneric()
link_35.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.237440667378504,2.51550127212935,0.217674182950967)
cB = chrono.ChVector3d(0.256663804363385,2.51550127212935,0.449958115000637)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
link_35.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_35.SetName("Coincident2_hinge")
exported_items.append(link_35)


# Mate constraint: Distance2 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: M-410iB-300 -1/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: M-410iB-300 -1/M-410iB-300-03-1 ,  SW ref.type:2 (2)
link_36 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.468847901417992,2.84164228947283,0.443357718519636)
cB = chrono.ChVector3d(1.09486376832202,2.54318522667954,0.388492061667059)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424792,-9.11814027060309e-17,0.996593123545252)
link_36.Initialize(body_2,body_3,False,cA,cB,dB)
link_36.SetDistance(0)
link_36.SetName("Distance2")
exported_items.append(link_36)

link_37 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.468847901417992,2.84164228947283,0.443357718519636)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
cB = chrono.ChVector3d(1.09486376832202,2.54318522667954,0.388492061667059)
dB = chrono.ChVector3d(0.0824751241424792,-9.11814027060309e-17,0.996593123545252)
link_37.SetFlipped(True)
link_37.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_37.SetName("Distance2")
exported_items.append(link_37)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: M-410iB-300 -1/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_6 , SW name: M-410iB-300 -1/M-410iB-300-04-1 ,  SW ref.type:5 (5)
link_38 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.260985806741079,2.78049690546384,0.502140937748153)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
cB = chrono.ChVector3d(0.266759107195713,2.78049690546384,0.57190296106215)
dB = chrono.ChVector3d(0.0824751241424787,-6.19079440489223e-17,0.996593123545253)
link_38.Initialize(body_2,body_6,False,cA,cB,dA,dB)
link_38.SetName("Coincident3")
exported_items.append(link_38)

link_39 = chrono.ChLinkMateGeneric()
link_39.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.260985806741079,2.78049690546384,0.502140937748153)
cB = chrono.ChVector3d(0.266759107195713,2.78049690546384,0.57190296106215)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424787,-6.19079440489223e-17,0.996593123545253)
link_39.Initialize(body_2,body_6,False,cA,cB,dA,dB)
link_39.SetName("Coincident3")
exported_items.append(link_39)


# Mate constraint: Distance3 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: M-410iB-300 -1/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: M-410iB-300 -1/M-410iB-300-04-1 ,  SW ref.type:2 (2)
link_40 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.264664235980002,2.78049691677857,0.546589495977547)
cB = chrono.ChVector3d(0.336053492470978,2.80967719196082,0.566168360960131)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424787,6.19079440489223e-17,-0.996593123545253)
link_40.Initialize(body_2,body_6,False,cA,cB,dB)
link_40.SetDistance(0)
link_40.SetName("Distance3")
exported_items.append(link_40)

link_41 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.264664235980002,2.78049691677857,0.546589495977547)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
cB = chrono.ChVector3d(0.336053492470978,2.80967719196082,0.566168360960131)
dB = chrono.ChVector3d(-0.0824751241424787,6.19079440489223e-17,-0.996593123545253)
link_41.SetFlipped(True)
link_41.Initialize(body_2,body_6,False,cA,cB,dA,dB)
link_41.SetName("Distance3")
exported_items.append(link_41)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_6 , SW name: M-410iB-300 -1/M-410iB-300-04-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_9 , SW name: M-410iB-300 -1/M-410iB-300-05-1 ,  SW ref.type:5 (5)
link_42 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.07009216653166,2.7654491237564,0.533966723190072)
dA = chrono.ChVector3d(-0.996418499736232,0.0187192635196773,0.0824606727881728)
cB = chrono.ChVector3d(1.35881310090398,2.76002505419567,0.510073025408795)
dB = chrono.ChVector3d(-0.996418499736232,0.0187192635196774,0.0824606727881729)
link_42.Initialize(body_6,body_9,False,cA,cB,dA,dB)
link_42.SetName("Coincident4")
exported_items.append(link_42)

link_43 = chrono.ChLinkMateGeneric()
link_43.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.07009216653166,2.7654491237564,0.533966723190072)
cB = chrono.ChVector3d(1.35881310090398,2.76002505419567,0.510073025408795)
dA = chrono.ChVector3d(-0.996418499736232,0.0187192635196773,0.0824606727881728)
dB = chrono.ChVector3d(-0.996418499736232,0.0187192635196774,0.0824606727881729)
link_43.Initialize(body_6,body_9,False,cA,cB,dA,dB)
link_43.SetName("Coincident4")
exported_items.append(link_43)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: M-410iB-300 -1/M-410iB-300-03-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_9 , SW name: M-410iB-300 -1/M-410iB-300-05-1 ,  SW ref.type:5 (5)
link_44 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.44822374457179,2.75811166841886,0.35134810890076)
dA = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
cB = chrono.ChVector3d(1.45777518922982,2.75811166841886,0.466763564956043)
dB = chrono.ChVector3d(-0.0824751241424788,-1.81929124543068e-16,-0.996593123545253)
link_44.Initialize(body_3,body_9,False,cA,cB,dA,dB)
link_44.SetName("Coincident5")
exported_items.append(link_44)

link_45 = chrono.ChLinkMateGeneric()
link_45.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.44822374457179,2.75811166841886,0.35134810890076)
cB = chrono.ChVector3d(1.45777518922982,2.75811166841886,0.466763564956043)
dA = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424788,-1.81929124543068e-16,-0.996593123545253)
link_45.Initialize(body_3,body_9,False,cA,cB,dA,dB)
link_45.SetName("Coincident5")
exported_items.append(link_45)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: M-410iB-300 -1/M-410iB-300-03-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_4 , SW name: M-410iB-300 -1/M-410iB-300-06-1 ,  SW ref.type:5 (5)
link_46 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.42574833632556,2.75811166841886,0.0797651614368332)
dA = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
cB = chrono.ChVector3d(1.42836692151708,2.75811166841885,0.111406993109395)
dB = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
link_46.SetFlipped(True)
link_46.Initialize(body_3,body_4,False,cA,cB,dA,dB)
link_46.SetName("Coincident6")
exported_items.append(link_46)

link_47 = chrono.ChLinkMateGeneric()
link_47.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.42574833632556,2.75811166841886,0.0797651614368332)
cB = chrono.ChVector3d(1.42836692151708,2.75811166841885,0.111406993109395)
dA = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
link_47.Initialize(body_3,body_4,False,cA,cB,dA,dB)
link_47.SetName("Coincident6")
exported_items.append(link_47)


# Mate constraint: Distance4 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: M-410iB-300 -1/M-410iB-300-03-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: M-410iB-300 -1/M-410iB-300-06-1 ,  SW ref.type:2 (2)
link_48 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(1.24088928761079,2.91434507456169,0.0950635541624164)
cB = chrono.ChVector3d(1.32186931481946,2.58269164685799,0.120220422708444)
dA = chrono.ChVector3d(0.0824751241424792,-9.11814027060309e-17,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
link_48.Initialize(body_3,body_4,False,cA,cB,dB)
link_48.SetDistance(0)
link_48.SetName("Distance4")
exported_items.append(link_48)

link_49 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.24088928761079,2.91434507456169,0.0950635541624164)
dA = chrono.ChVector3d(0.0824751241424792,-9.11814027060309e-17,0.996593123545252)
cB = chrono.ChVector3d(1.32186931481946,2.58269164685799,0.120220422708444)
dB = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
link_49.SetFlipped(True)
link_49.Initialize(body_3,body_4,False,cA,cB,dA,dB)
link_49.SetName("Distance4")
exported_items.append(link_49)


# Mate constraint: Coincident7 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: M-410iB-300 -1/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_7 , SW name: M-410iB-300 -1/M-410iB-300-07-1 ,  SW ref.type:5 (5)
link_50 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.264245082724809,2.51550127212935,0.541566948103163)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
cB = chrono.ChVector3d(0.239613811261857,2.51550127212935,0.243933497782502)
dB = chrono.ChVector3d(0.0824751241424797,1.09694154801221e-16,0.996593123545252)
link_50.SetFlipped(True)
link_50.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_50.SetName("Coincident7")
exported_items.append(link_50)

link_51 = chrono.ChLinkMateGeneric()
link_51.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.264245082724809,2.51550127212935,0.541566948103163)
cB = chrono.ChVector3d(0.239613811261857,2.51550127212935,0.243933497782502)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424797,1.09694154801221e-16,0.996593123545252)
link_51.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_51.SetName("Coincident7")
exported_items.append(link_51)


# Mate constraint: Coincident8 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_4 , SW name: M-410iB-300 -1/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: M-410iB-300 -1/M-410iB-300-07-1 ,  SW ref.type:2 (2)
link_52 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.965778716625616,3.10515332885273,0.260065473812372)
cB = chrono.ChVector3d(-0.0736523530408301,3.00995602354016,0.346085740742695)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424797,-1.09694154801221e-16,-0.996593123545252)
link_52.Initialize(body_4,body_7,False,cA,cB,dB)
link_52.SetDistance(0)
link_52.SetName("Coincident8")
exported_items.append(link_52)

link_53 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.965778716625616,3.10515332885273,0.260065473812372)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
cB = chrono.ChVector3d(-0.0736523530408301,3.00995602354016,0.346085740742695)
dB = chrono.ChVector3d(-0.0824751241424797,-1.09694154801221e-16,-0.996593123545252)
link_53.Initialize(body_4,body_7,False,cA,cB,dA,dB)
link_53.SetName("Coincident8")
exported_items.append(link_53)


# Mate constraint: Distance5 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: M-410iB-300 -1/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: M-410iB-300 -1/M-410iB-300-08-1 ,  SW ref.type:2 (2)
link_54 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.965778716625616,3.10515332885273,0.260065473812372)
cB = chrono.ChVector3d(-0.068656085438093,3.01604196029193,0.323498721768785)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424794,-3.71122403641788e-16,0.996593123545252)
link_54.Initialize(body_4,body_10,False,cA,cB,dB)
link_54.SetDistance(0)
link_54.SetName("Distance5")
exported_items.append(link_54)

link_55 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.965778716625616,3.10515332885273,0.260065473812372)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
cB = chrono.ChVector3d(-0.068656085438093,3.01604196029193,0.323498721768785)
dB = chrono.ChVector3d(0.0824751241424794,-3.71122403641788e-16,0.996593123545252)
link_55.SetFlipped(True)
link_55.Initialize(body_4,body_10,False,cA,cB,dA,dB)
link_55.SetName("Distance5")
exported_items.append(link_55)


# Mate constraint: Coincident9 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_4 , SW name: M-410iB-300 -1/M-410iB-300-06-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_10 , SW name: M-410iB-300 -1/M-410iB-300-08-1 ,  SW ref.type:5 (5)
link_56 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.12117568604869,3.25502265002171,0.247205276363948)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
cB = chrono.ChVector3d(1.11895512580627,3.25502265002172,0.220373003105613)
dB = chrono.ChVector3d(-0.0824751241424794,3.71122403641788e-16,-0.996593123545252)
link_56.Initialize(body_4,body_10,False,cA,cB,dA,dB)
link_56.SetName("Coincident9")
exported_items.append(link_56)

link_57 = chrono.ChLinkMateGeneric()
link_57.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.12117568604869,3.25502265002171,0.247205276363948)
cB = chrono.ChVector3d(1.11895512580627,3.25502265002172,0.220373003105613)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424794,3.71122403641788e-16,-0.996593123545252)
link_57.Initialize(body_4,body_10,False,cA,cB,dA,dB)
link_57.SetName("Coincident9")
exported_items.append(link_57)


# Mate constraint: Coincident10 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_11 , SW name: M-410iB-300 -1/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_4 , SW name: M-410iB-300 -1/M-410iB-300-06-1 ,  SW ref.type:5 (5)
link_58 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.41485957776932,2.75811166841883,-0.0518098075484875)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
cB = chrono.ChVector3d(1.4207379725339,2.75811166841885,0.0192221291814594)
dB = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
link_58.Initialize(body_11,body_4,False,cA,cB,dA,dB)
link_58.SetName("Coincident10")
exported_items.append(link_58)

link_59 = chrono.ChLinkMateGeneric()
link_59.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.41485957776932,2.75811166841883,-0.0518098075484875)
cB = chrono.ChVector3d(1.4207379725339,2.75811166841885,0.0192221291814594)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
link_59.Initialize(body_11,body_4,False,cA,cB,dA,dB)
link_59.SetName("Coincident10")
exported_items.append(link_59)


# Mate constraint: Coincident11 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: M-410iB-300 -1/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_11 , SW name: M-410iB-300 -1/M-410iB-300-09-1 ,  SW ref.type:2 (2)
link_60 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.128154728112769,2.72491052060182,0.0822572387461377)
cB = chrono.ChVector3d(1.41507253573634,3.21365467148159,-0.0454557237046155)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424791,7.87401827767598e-18,-0.996593123545253)
link_60.Initialize(body_2,body_11,False,cA,cB,dB)
link_60.SetDistance(0)
link_60.SetName("Coincident11")
exported_items.append(link_60)

link_61 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.128154728112769,2.72491052060182,0.0822572387461377)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
cB = chrono.ChVector3d(1.41507253573634,3.21365467148159,-0.0454557237046155)
dB = chrono.ChVector3d(-0.0824751241424791,7.87401827767598e-18,-0.996593123545253)
link_61.Initialize(body_2,body_11,False,cA,cB,dA,dB)
link_61.SetName("Coincident11")
exported_items.append(link_61)


# Mate constraint: Coincident12 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_11 , SW name: M-410iB-300 -1/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_12 , SW name: M-410iB-300 -1/M-410iB-300-10-1 ,  SW ref.type:5 (5)
link_62 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.916474724406216,3.03081076163703,0.00217847651718128)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
cB = chrono.ChVector3d(0.911740322379911,3.03081076163706,-0.0550299551468113)
dB = chrono.ChVector3d(0.0824751241424785,-3.85108611666851e-16,0.996593123545252)
link_62.Initialize(body_11,body_12,False,cA,cB,dA,dB)
link_62.SetName("Coincident12")
exported_items.append(link_62)

link_63 = chrono.ChLinkMateGeneric()
link_63.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.916474724406216,3.03081076163703,0.00217847651718128)
cB = chrono.ChVector3d(0.911740322379911,3.03081076163706,-0.0550299551468113)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424785,-3.85108611666851e-16,0.996593123545252)
link_63.Initialize(body_11,body_12,False,cA,cB,dA,dB)
link_63.SetName("Coincident12")
exported_items.append(link_63)


# Mate constraint: Distance7 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_11 , SW name: M-410iB-300 -1/M-410iB-300-09-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: M-410iB-300 -1/M-410iB-300-10-1 ,  SW ref.type:2 (2)
link_64 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(1.41507253573634,3.21365467148159,-0.0454557237046155)
cB = chrono.ChVector3d(0.915699623189495,3.03081076163706,-0.00718750565789794)
dA = chrono.ChVector3d(-0.0824751241424791,7.87401827767598e-18,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424785,-3.85108611666851e-16,0.996593123545252)
link_64.Initialize(body_11,body_12,False,cA,cB,dB)
link_64.SetDistance(0)
link_64.SetName("Distance7")
exported_items.append(link_64)

link_65 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.41507253573634,3.21365467148159,-0.0454557237046155)
dA = chrono.ChVector3d(-0.0824751241424791,7.87401827767598e-18,-0.996593123545253)
cB = chrono.ChVector3d(0.915699623189495,3.03081076163706,-0.00718750565789794)
dB = chrono.ChVector3d(0.0824751241424785,-3.85108611666851e-16,0.996593123545252)
link_65.SetFlipped(True)
link_65.Initialize(body_11,body_12,False,cA,cB,dA,dB)
link_65.SetName("Distance7")
exported_items.append(link_65)


# Mate constraint: Coincident13 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: M-410iB-300 -1/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_12 , SW name: M-410iB-300 -1/M-410iB-300-10-1 ,  SW ref.type:5 (5)
link_66 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.275466317544227,2.78749692402101,0.0944483138588827)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
cB = chrono.ChVector3d(-0.27571770172262,2.78749692402101,0.0914106980183131)
dB = chrono.ChVector3d(-0.0824751241424785,3.85108611666851e-16,-0.996593123545252)
link_66.SetFlipped(True)
link_66.Initialize(body_2,body_12,False,cA,cB,dA,dB)
link_66.SetName("Coincident13")
exported_items.append(link_66)

link_67 = chrono.ChLinkMateGeneric()
link_67.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-0.275466317544227,2.78749692402101,0.0944483138588827)
cB = chrono.ChVector3d(-0.27571770172262,2.78749692402101,0.0914106980183131)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424785,3.85108611666851e-16,-0.996593123545252)
link_67.Initialize(body_2,body_12,False,cA,cB,dA,dB)
link_67.SetName("Coincident13")
exported_items.append(link_67)


# Mate constraint: Coincident14 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_11 , SW name: M-410iB-300 -1/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_8 , SW name: M-410iB-300 -1/M-410iB-300-11-1 ,  SW ref.type:5 (5)
link_68 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.914455730422,3.02764258400498,-0.0804115047082415)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
cB = chrono.ChVector3d(1.92293994644251,3.02764258400502,0.0221080299108572)
dB = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545252)
link_68.SetFlipped(True)
link_68.Initialize(body_11,body_8,False,cA,cB,dA,dB)
link_68.SetName("Coincident14")
exported_items.append(link_68)

link_69 = chrono.ChLinkMateGeneric()
link_69.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.914455730422,3.02764258400498,-0.0804115047082415)
cB = chrono.ChVector3d(1.92293994644251,3.02764258400502,0.0221080299108572)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545252)
link_69.Initialize(body_11,body_8,False,cA,cB,dA,dB)
link_69.SetName("Coincident14")
exported_items.append(link_69)


# Mate constraint: Distance8 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_11 , SW name: M-410iB-300 -1/M-410iB-300-09-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: M-410iB-300 -1/M-410iB-300-11-1 ,  SW ref.type:2 (2)
link_70 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(1.41903183654593,3.21365467148159,0.00238672578429783)
cB = chrono.ChVector3d(1.91776562210406,3.02764258400502,-0.0404162294741248)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545253)
link_70.Initialize(body_11,body_8,False,cA,cB,dB)
link_70.SetDistance(0)
link_70.SetName("Distance8")
exported_items.append(link_70)

link_71 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.41903183654593,3.21365467148159,0.00238672578429783)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
cB = chrono.ChVector3d(1.91776562210406,3.02764258400502,-0.0404162294741248)
dB = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545253)
link_71.SetFlipped(True)
link_71.Initialize(body_11,body_8,False,cA,cB,dA,dB)
link_71.SetName("Distance8")
exported_items.append(link_71)


# Mate constraint: Coincident15 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: M-410iB-300 -1/M-410iB-300-06-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_1 , SW name: M-410iB-300 -1/M-410iB-300-12-1 ,  SW ref.type:5 (5)
link_72 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(2.17391479491138,1.6937690405165,0.0697760081379131)
dA = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
cB = chrono.ChVector3d(2.17288698991431,1.69376904051649,0.057356464632291)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_72.SetFlipped(True)
link_72.Initialize(body_4,body_1,False,cA,cB,dA,dB)
link_72.SetName("Coincident15")
exported_items.append(link_72)

link_73 = chrono.ChLinkMateGeneric()
link_73.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(2.17391479491138,1.6937690405165,0.0697760081379131)
cB = chrono.ChVector3d(2.17288698991431,1.69376904051649,0.057356464632291)
dA = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_73.Initialize(body_4,body_1,False,cA,cB,dA,dB)
link_73.SetName("Coincident15")
exported_items.append(link_73)


# Mate constraint: Distance9 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: M-410iB-300 -1/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: M-410iB-300 -1/M-410iB-300-12-1 ,  SW ref.type:2 (2)
link_74 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(1.54693693736679,2.27955349819168,0.262141450068309)
cB = chrono.ChVector3d(2.18650874636793,1.69376904051649,0.22195577810327)
dA = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_74.Initialize(body_4,body_1,False,cA,cB,dB)
link_74.SetDistance(0)
link_74.SetName("Distance9")
exported_items.append(link_74)

link_75 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.54693693736679,2.27955349819168,0.262141450068309)
dA = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
cB = chrono.ChVector3d(2.18650874636793,1.69376904051649,0.22195577810327)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_75.SetFlipped(True)
link_75.Initialize(body_4,body_1,False,cA,cB,dA,dB)
link_75.SetName("Distance9")
exported_items.append(link_75)


# Mate constraint: Coincident16 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_8 , SW name: M-410iB-300 -1/M-410iB-300-11-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_1 , SW name: M-410iB-300 -1/M-410iB-300-12-1 ,  SW ref.type:5 (5)
link_76 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(2.66683833509357,1.96329996858996,-0.0394548190631867)
dA = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545252)
cB = chrono.ChVector3d(2.67143572623521,1.96329996858993,0.0160980333350027)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_76.Initialize(body_8,body_1,False,cA,cB,dA,dB)
link_76.SetName("Coincident16")
exported_items.append(link_76)

link_77 = chrono.ChLinkMateGeneric()
link_77.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(2.66683833509357,1.96329996858996,-0.0394548190631867)
cB = chrono.ChVector3d(2.67143572623521,1.96329996858993,0.0160980333350027)
dA = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545252)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_77.Initialize(body_8,body_1,False,cA,cB,dA,dB)
link_77.SetName("Coincident16")
exported_items.append(link_77)


# Mate constraint: Coincident17 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: M-410iB-300 -1/M-410iB-300-07-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_10 , SW name: M-410iB-300 -1/M-410iB-300-08-1 ,  SW ref.type:5 (5)
link_78 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.0809607212164676,3.00995602354016,0.257774634285979)
dA = chrono.ChVector3d(0.0824751241424797,1.09694154801221e-16,0.996593123545252)
cB = chrono.ChVector3d(-0.0758729132832489,3.00995602354016,0.319253467484363)
dB = chrono.ChVector3d(-0.0824751241424794,3.71122403641788e-16,-0.996593123545252)
link_78.SetFlipped(True)
link_78.Initialize(body_7,body_10,False,cA,cB,dA,dB)
link_78.SetName("Coincident17")
exported_items.append(link_78)

link_79 = chrono.ChLinkMateGeneric()
link_79.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-0.0809607212164676,3.00995602354016,0.257774634285979)
cB = chrono.ChVector3d(-0.0758729132832489,3.00995602354016,0.319253467484363)
dA = chrono.ChVector3d(0.0824751241424797,1.09694154801221e-16,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424794,3.71122403641788e-16,-0.996593123545252)
link_79.Initialize(body_7,body_10,False,cA,cB,dA,dB)
link_79.SetName("Coincident17")
exported_items.append(link_79)


# Mate constraint: Coincident18 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: M-410iB-300 -1/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: M-410iB-300 -1/ArmBase-1 ,  SW ref.type:2 (2)
link_80 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.140670357955037,2.04602671615662,0.37740311343739)
cB = chrono.ChVector3d(-0.382669423498732,2.04602671615662,0.37740311343739)
dA = chrono.ChVector3d(-1.32297045065857e-16,-1,1.10849259381635e-17)
dB = chrono.ChVector3d(0,1,0)
link_80.Initialize(body_2,body_5,False,cA,cB,dB)
link_80.SetDistance(0)
link_80.SetName("Coincident18")
exported_items.append(link_80)

link_81 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.140670357955037,2.04602671615662,0.37740311343739)
dA = chrono.ChVector3d(-1.32297045065857e-16,-1,1.10849259381635e-17)
cB = chrono.ChVector3d(-0.382669423498732,2.04602671615662,0.37740311343739)
dB = chrono.ChVector3d(0,1,0)
link_81.SetFlipped(True)
link_81.Initialize(body_2,body_5,False,cA,cB,dA,dB)
link_81.SetName("Coincident18")
exported_items.append(link_81)


# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: M-410iB-300 -1/M-410iB-300-02-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_5 , SW name: M-410iB-300 -1/ArmBase-1 ,  SW ref.type:1 (1)
link_82 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.140670357955037,2.04755071615662,0.37740311343739)
dA = chrono.ChVector3d(1.32297045065857e-16,1,-1.10849259381635e-17)
cB = chrono.ChVector3d(-0.140670357955037,2.04602671615662,0.37740311343739)
dB = chrono.ChVector3d(0,1,0)
link_82.Initialize(body_2,body_5,False,cA,cB,dA,dB)
link_82.SetName("Concentric1")
exported_items.append(link_82)

link_83 = chrono.ChLinkMateGeneric()
link_83.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-0.140670357955037,2.04755071615662,0.37740311343739)
cB = chrono.ChVector3d(-0.140670357955037,2.04602671615662,0.37740311343739)
dA = chrono.ChVector3d(1.32297045065857e-16,1,-1.10849259381635e-17)
dB = chrono.ChVector3d(0,1,0)
link_83.Initialize(body_2,body_5,False,cA,cB,dA,dB)
link_83.SetName("Concentric1")
exported_items.append(link_83)


# Mate constraint: Coincident2_hinge [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_14 , SW name: M-410iB-300 -2/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_15 , SW name: M-410iB-300 -2/M-410iB-300-03-1 ,  SW ref.type:5 (5)
link_84 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.237440667378504,2.51550127212935,-1.23232581704903)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
cB = chrono.ChVector3d(0.256663804363385,2.51550127212935,-1.00004188499936)
dB = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
link_84.Initialize(body_14,body_15,False,cA,cB,dA,dB)
link_84.SetName("Coincident2_hinge")
exported_items.append(link_84)

link_85 = chrono.ChLinkMateGeneric()
link_85.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.237440667378504,2.51550127212935,-1.23232581704903)
cB = chrono.ChVector3d(0.256663804363385,2.51550127212935,-1.00004188499936)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
link_85.Initialize(body_14,body_15,False,cA,cB,dA,dB)
link_85.SetName("Coincident2_hinge")
exported_items.append(link_85)


# Mate constraint: Distance2 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_14 , SW name: M-410iB-300 -2/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_15 , SW name: M-410iB-300 -2/M-410iB-300-03-1 ,  SW ref.type:2 (2)
link_86 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.468847901417992,2.84164228947283,-1.00664228148036)
cB = chrono.ChVector3d(1.09486376832202,2.54318522667954,-1.06150793833294)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424792,-9.11814027060309e-17,0.996593123545252)
link_86.Initialize(body_14,body_15,False,cA,cB,dB)
link_86.SetDistance(0)
link_86.SetName("Distance2")
exported_items.append(link_86)

link_87 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.468847901417992,2.84164228947283,-1.00664228148036)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
cB = chrono.ChVector3d(1.09486376832202,2.54318522667954,-1.06150793833294)
dB = chrono.ChVector3d(0.0824751241424792,-9.11814027060309e-17,0.996593123545252)
link_87.SetFlipped(True)
link_87.Initialize(body_14,body_15,False,cA,cB,dA,dB)
link_87.SetName("Distance2")
exported_items.append(link_87)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_14 , SW name: M-410iB-300 -2/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_20 , SW name: M-410iB-300 -2/M-410iB-300-04-1 ,  SW ref.type:5 (5)
link_88 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.260985806741079,2.78049690546384,-0.947859062251847)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
cB = chrono.ChVector3d(0.266759107195713,2.78049690546384,-0.87809703893785)
dB = chrono.ChVector3d(0.0824751241424787,-6.19079440489223e-17,0.996593123545253)
link_88.Initialize(body_14,body_20,False,cA,cB,dA,dB)
link_88.SetName("Coincident3")
exported_items.append(link_88)

link_89 = chrono.ChLinkMateGeneric()
link_89.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.260985806741079,2.78049690546384,-0.947859062251847)
cB = chrono.ChVector3d(0.266759107195713,2.78049690546384,-0.87809703893785)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424787,-6.19079440489223e-17,0.996593123545253)
link_89.Initialize(body_14,body_20,False,cA,cB,dA,dB)
link_89.SetName("Coincident3")
exported_items.append(link_89)


# Mate constraint: Distance3 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_14 , SW name: M-410iB-300 -2/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_20 , SW name: M-410iB-300 -2/M-410iB-300-04-1 ,  SW ref.type:2 (2)
link_90 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.264664235980002,2.78049691677857,-0.903410504022453)
cB = chrono.ChVector3d(0.336053492470978,2.80967719196082,-0.883831639039869)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424787,6.19079440489223e-17,-0.996593123545253)
link_90.Initialize(body_14,body_20,False,cA,cB,dB)
link_90.SetDistance(0)
link_90.SetName("Distance3")
exported_items.append(link_90)

link_91 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.264664235980002,2.78049691677857,-0.903410504022453)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
cB = chrono.ChVector3d(0.336053492470978,2.80967719196082,-0.883831639039869)
dB = chrono.ChVector3d(-0.0824751241424787,6.19079440489223e-17,-0.996593123545253)
link_91.SetFlipped(True)
link_91.Initialize(body_14,body_20,False,cA,cB,dA,dB)
link_91.SetName("Distance3")
exported_items.append(link_91)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_20 , SW name: M-410iB-300 -2/M-410iB-300-04-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_17 , SW name: M-410iB-300 -2/M-410iB-300-05-1 ,  SW ref.type:5 (5)
link_92 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.07009216653166,2.7654491237564,-0.916033276809928)
dA = chrono.ChVector3d(-0.996418499736232,0.0187192635196773,0.0824606727881728)
cB = chrono.ChVector3d(1.35881310090398,2.76002505419567,-0.939926974591205)
dB = chrono.ChVector3d(-0.996418499736232,0.0187192635196774,0.0824606727881729)
link_92.Initialize(body_20,body_17,False,cA,cB,dA,dB)
link_92.SetName("Coincident4")
exported_items.append(link_92)

link_93 = chrono.ChLinkMateGeneric()
link_93.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.07009216653166,2.7654491237564,-0.916033276809928)
cB = chrono.ChVector3d(1.35881310090398,2.76002505419567,-0.939926974591205)
dA = chrono.ChVector3d(-0.996418499736232,0.0187192635196773,0.0824606727881728)
dB = chrono.ChVector3d(-0.996418499736232,0.0187192635196774,0.0824606727881729)
link_93.Initialize(body_20,body_17,False,cA,cB,dA,dB)
link_93.SetName("Coincident4")
exported_items.append(link_93)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_15 , SW name: M-410iB-300 -2/M-410iB-300-03-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_17 , SW name: M-410iB-300 -2/M-410iB-300-05-1 ,  SW ref.type:5 (5)
link_94 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.44822374457179,2.75811166841886,-1.09865189109924)
dA = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
cB = chrono.ChVector3d(1.45777518922982,2.75811166841886,-0.983236435043957)
dB = chrono.ChVector3d(-0.0824751241424788,-1.81929124543068e-16,-0.996593123545253)
link_94.Initialize(body_15,body_17,False,cA,cB,dA,dB)
link_94.SetName("Coincident5")
exported_items.append(link_94)

link_95 = chrono.ChLinkMateGeneric()
link_95.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.44822374457179,2.75811166841886,-1.09865189109924)
cB = chrono.ChVector3d(1.45777518922982,2.75811166841886,-0.983236435043957)
dA = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424788,-1.81929124543068e-16,-0.996593123545253)
link_95.Initialize(body_15,body_17,False,cA,cB,dA,dB)
link_95.SetName("Coincident5")
exported_items.append(link_95)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_15 , SW name: M-410iB-300 -2/M-410iB-300-03-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_13 , SW name: M-410iB-300 -2/M-410iB-300-06-1 ,  SW ref.type:5 (5)
link_96 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.42574833632556,2.75811166841886,-1.37023483856317)
dA = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
cB = chrono.ChVector3d(1.42836692151708,2.75811166841885,-1.33859300689061)
dB = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
link_96.SetFlipped(True)
link_96.Initialize(body_15,body_13,False,cA,cB,dA,dB)
link_96.SetName("Coincident6")
exported_items.append(link_96)

link_97 = chrono.ChLinkMateGeneric()
link_97.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.42574833632556,2.75811166841886,-1.37023483856317)
cB = chrono.ChVector3d(1.42836692151708,2.75811166841885,-1.33859300689061)
dA = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
link_97.Initialize(body_15,body_13,False,cA,cB,dA,dB)
link_97.SetName("Coincident6")
exported_items.append(link_97)


# Mate constraint: Distance4 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_15 , SW name: M-410iB-300 -2/M-410iB-300-03-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_13 , SW name: M-410iB-300 -2/M-410iB-300-06-1 ,  SW ref.type:2 (2)
link_98 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(1.24088928761079,2.91434507456169,-1.35493644583758)
cB = chrono.ChVector3d(1.32186931481946,2.58269164685799,-1.32977957729156)
dA = chrono.ChVector3d(0.0824751241424792,-9.11814027060309e-17,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
link_98.Initialize(body_15,body_13,False,cA,cB,dB)
link_98.SetDistance(0)
link_98.SetName("Distance4")
exported_items.append(link_98)

link_99 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.24088928761079,2.91434507456169,-1.35493644583758)
dA = chrono.ChVector3d(0.0824751241424792,-9.11814027060309e-17,0.996593123545252)
cB = chrono.ChVector3d(1.32186931481946,2.58269164685799,-1.32977957729156)
dB = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
link_99.SetFlipped(True)
link_99.Initialize(body_15,body_13,False,cA,cB,dA,dB)
link_99.SetName("Distance4")
exported_items.append(link_99)


# Mate constraint: Coincident7 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_14 , SW name: M-410iB-300 -2/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_21 , SW name: M-410iB-300 -2/M-410iB-300-07-1 ,  SW ref.type:5 (5)
link_100 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.264245082724809,2.51550127212935,-0.908433051896837)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
cB = chrono.ChVector3d(0.239613811261857,2.51550127212935,-1.2060665022175)
dB = chrono.ChVector3d(0.0824751241424797,1.09694154801221e-16,0.996593123545252)
link_100.SetFlipped(True)
link_100.Initialize(body_14,body_21,False,cA,cB,dA,dB)
link_100.SetName("Coincident7")
exported_items.append(link_100)

link_101 = chrono.ChLinkMateGeneric()
link_101.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.264245082724809,2.51550127212935,-0.908433051896837)
cB = chrono.ChVector3d(0.239613811261857,2.51550127212935,-1.2060665022175)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424797,1.09694154801221e-16,0.996593123545252)
link_101.Initialize(body_14,body_21,False,cA,cB,dA,dB)
link_101.SetName("Coincident7")
exported_items.append(link_101)


# Mate constraint: Coincident8 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_13 , SW name: M-410iB-300 -2/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_21 , SW name: M-410iB-300 -2/M-410iB-300-07-1 ,  SW ref.type:2 (2)
link_102 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.965778716625616,3.10515332885273,-1.18993452618763)
cB = chrono.ChVector3d(-0.0736523530408298,3.00995602354016,-1.10391425925731)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424797,-1.09694154801221e-16,-0.996593123545252)
link_102.Initialize(body_13,body_21,False,cA,cB,dB)
link_102.SetDistance(0)
link_102.SetName("Coincident8")
exported_items.append(link_102)

link_103 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.965778716625616,3.10515332885273,-1.18993452618763)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
cB = chrono.ChVector3d(-0.0736523530408298,3.00995602354016,-1.10391425925731)
dB = chrono.ChVector3d(-0.0824751241424797,-1.09694154801221e-16,-0.996593123545252)
link_103.Initialize(body_13,body_21,False,cA,cB,dA,dB)
link_103.SetName("Coincident8")
exported_items.append(link_103)


# Mate constraint: Distance5 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_13 , SW name: M-410iB-300 -2/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_23 , SW name: M-410iB-300 -2/M-410iB-300-08-1 ,  SW ref.type:2 (2)
link_104 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.965778716625616,3.10515332885273,-1.18993452618763)
cB = chrono.ChVector3d(-0.0686560854380927,3.01604196029193,-1.12650127823122)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424794,-3.71122403641788e-16,0.996593123545252)
link_104.Initialize(body_13,body_23,False,cA,cB,dB)
link_104.SetDistance(0)
link_104.SetName("Distance5")
exported_items.append(link_104)

link_105 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.965778716625616,3.10515332885273,-1.18993452618763)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
cB = chrono.ChVector3d(-0.0686560854380927,3.01604196029193,-1.12650127823122)
dB = chrono.ChVector3d(0.0824751241424794,-3.71122403641788e-16,0.996593123545252)
link_105.SetFlipped(True)
link_105.Initialize(body_13,body_23,False,cA,cB,dA,dB)
link_105.SetName("Distance5")
exported_items.append(link_105)


# Mate constraint: Coincident9 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_13 , SW name: M-410iB-300 -2/M-410iB-300-06-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_23 , SW name: M-410iB-300 -2/M-410iB-300-08-1 ,  SW ref.type:5 (5)
link_106 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.12117568604869,3.25502265002171,-1.20279472363605)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
cB = chrono.ChVector3d(1.11895512580627,3.25502265002172,-1.22962699689439)
dB = chrono.ChVector3d(-0.0824751241424794,3.71122403641788e-16,-0.996593123545252)
link_106.Initialize(body_13,body_23,False,cA,cB,dA,dB)
link_106.SetName("Coincident9")
exported_items.append(link_106)

link_107 = chrono.ChLinkMateGeneric()
link_107.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.12117568604869,3.25502265002171,-1.20279472363605)
cB = chrono.ChVector3d(1.11895512580627,3.25502265002172,-1.22962699689439)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424794,3.71122403641788e-16,-0.996593123545252)
link_107.Initialize(body_13,body_23,False,cA,cB,dA,dB)
link_107.SetName("Coincident9")
exported_items.append(link_107)


# Mate constraint: Coincident10 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_22 , SW name: M-410iB-300 -2/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_13 , SW name: M-410iB-300 -2/M-410iB-300-06-1 ,  SW ref.type:5 (5)
link_108 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.41485957776932,2.75811166841883,-1.50180980754849)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
cB = chrono.ChVector3d(1.4207379725339,2.75811166841885,-1.43077787081854)
dB = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
link_108.Initialize(body_22,body_13,False,cA,cB,dA,dB)
link_108.SetName("Coincident10")
exported_items.append(link_108)

link_109 = chrono.ChLinkMateGeneric()
link_109.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.41485957776932,2.75811166841883,-1.50180980754849)
cB = chrono.ChVector3d(1.4207379725339,2.75811166841885,-1.43077787081854)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
link_109.Initialize(body_22,body_13,False,cA,cB,dA,dB)
link_109.SetName("Coincident10")
exported_items.append(link_109)


# Mate constraint: Coincident11 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_14 , SW name: M-410iB-300 -2/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_22 , SW name: M-410iB-300 -2/M-410iB-300-09-1 ,  SW ref.type:2 (2)
link_110 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.128154728112769,2.72491052060182,-1.36774276125386)
cB = chrono.ChVector3d(1.41507253573634,3.21365467148159,-1.49545572370462)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424791,7.87401827767598e-18,-0.996593123545253)
link_110.Initialize(body_14,body_22,False,cA,cB,dB)
link_110.SetDistance(0)
link_110.SetName("Coincident11")
exported_items.append(link_110)

link_111 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.128154728112769,2.72491052060182,-1.36774276125386)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
cB = chrono.ChVector3d(1.41507253573634,3.21365467148159,-1.49545572370462)
dB = chrono.ChVector3d(-0.0824751241424791,7.87401827767598e-18,-0.996593123545253)
link_111.Initialize(body_14,body_22,False,cA,cB,dA,dB)
link_111.SetName("Coincident11")
exported_items.append(link_111)


# Mate constraint: Coincident12 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_22 , SW name: M-410iB-300 -2/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_24 , SW name: M-410iB-300 -2/M-410iB-300-10-1 ,  SW ref.type:5 (5)
link_112 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.916474724406216,3.03081076163703,-1.44782152348282)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
cB = chrono.ChVector3d(0.911740322379911,3.03081076163706,-1.50502995514681)
dB = chrono.ChVector3d(0.0824751241424785,-3.85108611666851e-16,0.996593123545252)
link_112.Initialize(body_22,body_24,False,cA,cB,dA,dB)
link_112.SetName("Coincident12")
exported_items.append(link_112)

link_113 = chrono.ChLinkMateGeneric()
link_113.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.916474724406216,3.03081076163703,-1.44782152348282)
cB = chrono.ChVector3d(0.911740322379911,3.03081076163706,-1.50502995514681)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424785,-3.85108611666851e-16,0.996593123545252)
link_113.Initialize(body_22,body_24,False,cA,cB,dA,dB)
link_113.SetName("Coincident12")
exported_items.append(link_113)


# Mate constraint: Distance7 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_22 , SW name: M-410iB-300 -2/M-410iB-300-09-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_24 , SW name: M-410iB-300 -2/M-410iB-300-10-1 ,  SW ref.type:2 (2)
link_114 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(1.41507253573634,3.21365467148159,-1.49545572370462)
cB = chrono.ChVector3d(0.915699623189495,3.03081076163706,-1.4571875056579)
dA = chrono.ChVector3d(-0.0824751241424791,7.87401827767598e-18,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424785,-3.85108611666851e-16,0.996593123545252)
link_114.Initialize(body_22,body_24,False,cA,cB,dB)
link_114.SetDistance(0)
link_114.SetName("Distance7")
exported_items.append(link_114)

link_115 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.41507253573634,3.21365467148159,-1.49545572370462)
dA = chrono.ChVector3d(-0.0824751241424791,7.87401827767598e-18,-0.996593123545253)
cB = chrono.ChVector3d(0.915699623189495,3.03081076163706,-1.4571875056579)
dB = chrono.ChVector3d(0.0824751241424785,-3.85108611666851e-16,0.996593123545252)
link_115.SetFlipped(True)
link_115.Initialize(body_22,body_24,False,cA,cB,dA,dB)
link_115.SetName("Distance7")
exported_items.append(link_115)


# Mate constraint: Coincident13 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_14 , SW name: M-410iB-300 -2/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_24 , SW name: M-410iB-300 -2/M-410iB-300-10-1 ,  SW ref.type:5 (5)
link_116 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.275466317544226,2.78749692402101,-1.35555168614112)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
cB = chrono.ChVector3d(-0.27571770172262,2.78749692402101,-1.35858930198169)
dB = chrono.ChVector3d(-0.0824751241424785,3.85108611666851e-16,-0.996593123545252)
link_116.SetFlipped(True)
link_116.Initialize(body_14,body_24,False,cA,cB,dA,dB)
link_116.SetName("Coincident13")
exported_items.append(link_116)

link_117 = chrono.ChLinkMateGeneric()
link_117.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-0.275466317544226,2.78749692402101,-1.35555168614112)
cB = chrono.ChVector3d(-0.27571770172262,2.78749692402101,-1.35858930198169)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424785,3.85108611666851e-16,-0.996593123545252)
link_117.Initialize(body_14,body_24,False,cA,cB,dA,dB)
link_117.SetName("Coincident13")
exported_items.append(link_117)


# Mate constraint: Coincident14 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_22 , SW name: M-410iB-300 -2/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_19 , SW name: M-410iB-300 -2/M-410iB-300-11-1 ,  SW ref.type:5 (5)
link_118 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.914455730422,3.02764258400498,-1.53041150470824)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
cB = chrono.ChVector3d(1.92293994644251,3.02764258400502,-1.42789197008914)
dB = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545252)
link_118.SetFlipped(True)
link_118.Initialize(body_22,body_19,False,cA,cB,dA,dB)
link_118.SetName("Coincident14")
exported_items.append(link_118)

link_119 = chrono.ChLinkMateGeneric()
link_119.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.914455730422,3.02764258400498,-1.53041150470824)
cB = chrono.ChVector3d(1.92293994644251,3.02764258400502,-1.42789197008914)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545252)
link_119.Initialize(body_22,body_19,False,cA,cB,dA,dB)
link_119.SetName("Coincident14")
exported_items.append(link_119)


# Mate constraint: Distance8 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_22 , SW name: M-410iB-300 -2/M-410iB-300-09-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_19 , SW name: M-410iB-300 -2/M-410iB-300-11-1 ,  SW ref.type:2 (2)
link_120 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(1.41903183654593,3.21365467148159,-1.4476132742157)
cB = chrono.ChVector3d(1.91776562210406,3.02764258400502,-1.49041622947412)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545253)
link_120.Initialize(body_22,body_19,False,cA,cB,dB)
link_120.SetDistance(0)
link_120.SetName("Distance8")
exported_items.append(link_120)

link_121 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.41903183654593,3.21365467148159,-1.4476132742157)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
cB = chrono.ChVector3d(1.91776562210406,3.02764258400502,-1.49041622947412)
dB = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545253)
link_121.SetFlipped(True)
link_121.Initialize(body_22,body_19,False,cA,cB,dA,dB)
link_121.SetName("Distance8")
exported_items.append(link_121)


# Mate constraint: Coincident15 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_13 , SW name: M-410iB-300 -2/M-410iB-300-06-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_16 , SW name: M-410iB-300 -2/M-410iB-300-12-1 ,  SW ref.type:5 (5)
link_122 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(2.17391479491138,1.6937690405165,-1.38022399186209)
dA = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
cB = chrono.ChVector3d(2.17288698991431,1.69376904051649,-1.39264353536771)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_122.SetFlipped(True)
link_122.Initialize(body_13,body_16,False,cA,cB,dA,dB)
link_122.SetName("Coincident15")
exported_items.append(link_122)

link_123 = chrono.ChLinkMateGeneric()
link_123.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(2.17391479491138,1.6937690405165,-1.38022399186209)
cB = chrono.ChVector3d(2.17288698991431,1.69376904051649,-1.39264353536771)
dA = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_123.Initialize(body_13,body_16,False,cA,cB,dA,dB)
link_123.SetName("Coincident15")
exported_items.append(link_123)


# Mate constraint: Distance9 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_13 , SW name: M-410iB-300 -2/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_16 , SW name: M-410iB-300 -2/M-410iB-300-12-1 ,  SW ref.type:2 (2)
link_124 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(1.54693693736679,2.27955349819168,-1.18785854993169)
cB = chrono.ChVector3d(2.18650874636793,1.69376904051649,-1.22804422189673)
dA = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_124.Initialize(body_13,body_16,False,cA,cB,dB)
link_124.SetDistance(0)
link_124.SetName("Distance9")
exported_items.append(link_124)

link_125 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.54693693736679,2.27955349819168,-1.18785854993169)
dA = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
cB = chrono.ChVector3d(2.18650874636793,1.69376904051649,-1.22804422189673)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_125.SetFlipped(True)
link_125.Initialize(body_13,body_16,False,cA,cB,dA,dB)
link_125.SetName("Distance9")
exported_items.append(link_125)


# Mate constraint: Coincident16 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_19 , SW name: M-410iB-300 -2/M-410iB-300-11-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_16 , SW name: M-410iB-300 -2/M-410iB-300-12-1 ,  SW ref.type:5 (5)
link_126 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(2.66683833509357,1.96329996858996,-1.48945481906319)
dA = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545252)
cB = chrono.ChVector3d(2.67143572623521,1.96329996858993,-1.433901966665)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_126.Initialize(body_19,body_16,False,cA,cB,dA,dB)
link_126.SetName("Coincident16")
exported_items.append(link_126)

link_127 = chrono.ChLinkMateGeneric()
link_127.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(2.66683833509357,1.96329996858996,-1.48945481906319)
cB = chrono.ChVector3d(2.67143572623521,1.96329996858993,-1.433901966665)
dA = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545252)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_127.Initialize(body_19,body_16,False,cA,cB,dA,dB)
link_127.SetName("Coincident16")
exported_items.append(link_127)


# Mate constraint: Coincident17 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_21 , SW name: M-410iB-300 -2/M-410iB-300-07-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_23 , SW name: M-410iB-300 -2/M-410iB-300-08-1 ,  SW ref.type:5 (5)
link_128 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.0809607212164674,3.00995602354016,-1.19222536571402)
dA = chrono.ChVector3d(0.0824751241424797,1.09694154801221e-16,0.996593123545252)
cB = chrono.ChVector3d(-0.0758729132832486,3.00995602354016,-1.13074653251564)
dB = chrono.ChVector3d(-0.0824751241424794,3.71122403641788e-16,-0.996593123545252)
link_128.SetFlipped(True)
link_128.Initialize(body_21,body_23,False,cA,cB,dA,dB)
link_128.SetName("Coincident17")
exported_items.append(link_128)

link_129 = chrono.ChLinkMateGeneric()
link_129.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-0.0809607212164674,3.00995602354016,-1.19222536571402)
cB = chrono.ChVector3d(-0.0758729132832486,3.00995602354016,-1.13074653251564)
dA = chrono.ChVector3d(0.0824751241424797,1.09694154801221e-16,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424794,3.71122403641788e-16,-0.996593123545252)
link_129.Initialize(body_21,body_23,False,cA,cB,dA,dB)
link_129.SetName("Coincident17")
exported_items.append(link_129)


# Mate constraint: Coincident18 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_14 , SW name: M-410iB-300 -2/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_18 , SW name: M-410iB-300 -2/ArmBase-1 ,  SW ref.type:2 (2)
link_130 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.140670357955037,2.04602671615662,-1.07259688656261)
cB = chrono.ChVector3d(-0.382669423498732,2.04602671615662,-1.07259688656261)
dA = chrono.ChVector3d(-1.32297045065857e-16,-1,1.10849259381635e-17)
dB = chrono.ChVector3d(0,1,0)
link_130.Initialize(body_14,body_18,False,cA,cB,dB)
link_130.SetDistance(0)
link_130.SetName("Coincident18")
exported_items.append(link_130)

link_131 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.140670357955037,2.04602671615662,-1.07259688656261)
dA = chrono.ChVector3d(-1.32297045065857e-16,-1,1.10849259381635e-17)
cB = chrono.ChVector3d(-0.382669423498732,2.04602671615662,-1.07259688656261)
dB = chrono.ChVector3d(0,1,0)
link_131.SetFlipped(True)
link_131.Initialize(body_14,body_18,False,cA,cB,dA,dB)
link_131.SetName("Coincident18")
exported_items.append(link_131)


# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_14 , SW name: M-410iB-300 -2/M-410iB-300-02-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_18 , SW name: M-410iB-300 -2/ArmBase-1 ,  SW ref.type:1 (1)
link_132 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.140670357955037,2.04755071615662,-1.07259688656261)
dA = chrono.ChVector3d(1.32297045065857e-16,1,-1.10849259381635e-17)
cB = chrono.ChVector3d(-0.140670357955037,2.04602671615662,-1.07259688656261)
dB = chrono.ChVector3d(0,1,0)
link_132.Initialize(body_14,body_18,False,cA,cB,dA,dB)
link_132.SetName("Concentric1")
exported_items.append(link_132)

link_133 = chrono.ChLinkMateGeneric()
link_133.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-0.140670357955037,2.04755071615662,-1.07259688656261)
cB = chrono.ChVector3d(-0.140670357955037,2.04602671615662,-1.07259688656261)
dA = chrono.ChVector3d(1.32297045065857e-16,1,-1.10849259381635e-17)
dB = chrono.ChVector3d(0,1,0)
link_133.Initialize(body_14,body_18,False,cA,cB,dA,dB)
link_133.SetName("Concentric1")
exported_items.append(link_133)


# Mate constraint: Coincident2_hinge [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_26 , SW name: M-410iB-300 -9/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_29 , SW name: M-410iB-300 -9/M-410iB-300-03-1 ,  SW ref.type:5 (5)
link_134 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.87878138328858,2.51550127212935,0.537132043923804)
dA = chrono.ChVector3d(0.0824751241424789,3.55158224497465e-15,0.996593123545252)
cB = chrono.ChVector3d(-1.89800452027346,2.51550127212935,0.304848111874134)
dB = chrono.ChVector3d(0.082475124142479,3.64289959343017e-15,0.996593123545252)
link_134.Initialize(body_26,body_29,False,cA,cB,dA,dB)
link_134.SetName("Coincident2_hinge")
exported_items.append(link_134)

link_135 = chrono.ChLinkMateGeneric()
link_135.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.87878138328858,2.51550127212935,0.537132043923804)
cB = chrono.ChVector3d(-1.89800452027346,2.51550127212935,0.304848111874134)
dA = chrono.ChVector3d(0.0824751241424789,3.55158224497465e-15,0.996593123545252)
dB = chrono.ChVector3d(0.082475124142479,3.64289959343017e-15,0.996593123545252)
link_135.Initialize(body_26,body_29,False,cA,cB,dA,dB)
link_135.SetName("Coincident2_hinge")
exported_items.append(link_135)


# Mate constraint: Distance2 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_26 , SW name: M-410iB-300 -9/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_29 , SW name: M-410iB-300 -9/M-410iB-300-03-1 ,  SW ref.type:2 (2)
link_136 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-2.11018861732807,2.84164228947283,0.311448508355134)
cB = chrono.ChVector3d(-2.73620448423209,2.54318522667954,0.366314165207712)
dA = chrono.ChVector3d(0.0824751241424789,3.55158224497465e-15,0.996593123545252)
dB = chrono.ChVector3d(-0.082475124142479,-3.64289959343017e-15,-0.996593123545252)
link_136.Initialize(body_26,body_29,False,cA,cB,dB)
link_136.SetDistance(0)
link_136.SetName("Distance2")
exported_items.append(link_136)

link_137 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.11018861732807,2.84164228947283,0.311448508355134)
dA = chrono.ChVector3d(0.0824751241424789,3.55158224497465e-15,0.996593123545252)
cB = chrono.ChVector3d(-2.73620448423209,2.54318522667954,0.366314165207712)
dB = chrono.ChVector3d(-0.082475124142479,-3.64289959343017e-15,-0.996593123545252)
link_137.SetFlipped(True)
link_137.Initialize(body_26,body_29,False,cA,cB,dA,dB)
link_137.SetName("Distance2")
exported_items.append(link_137)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_26 , SW name: M-410iB-300 -9/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_35 , SW name: M-410iB-300 -9/M-410iB-300-04-1 ,  SW ref.type:5 (5)
link_138 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.90232652265115,2.78049690546384,0.252665289126617)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55158224497465e-15,-0.996593123545252)
cB = chrono.ChVector3d(-1.90809982310579,2.78049690546384,0.18290326581262)
dB = chrono.ChVector3d(-0.0824751241424785,-3.61362613477307e-15,-0.996593123545253)
link_138.Initialize(body_26,body_35,False,cA,cB,dA,dB)
link_138.SetName("Coincident3")
exported_items.append(link_138)

link_139 = chrono.ChLinkMateGeneric()
link_139.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.90232652265115,2.78049690546384,0.252665289126617)
cB = chrono.ChVector3d(-1.90809982310579,2.78049690546384,0.18290326581262)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55158224497465e-15,-0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424785,-3.61362613477307e-15,-0.996593123545253)
link_139.Initialize(body_26,body_35,False,cA,cB,dA,dB)
link_139.SetName("Coincident3")
exported_items.append(link_139)


# Mate constraint: Distance3 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_26 , SW name: M-410iB-300 -9/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_35 , SW name: M-410iB-300 -9/M-410iB-300-04-1 ,  SW ref.type:2 (2)
link_140 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.90600495189008,2.78049691677857,0.208216730897223)
cB = chrono.ChVector3d(-1.97739420838105,2.80967719196082,0.188637865914639)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55158224497465e-15,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424785,3.61362613477307e-15,0.996593123545253)
link_140.Initialize(body_26,body_35,False,cA,cB,dB)
link_140.SetDistance(0)
link_140.SetName("Distance3")
exported_items.append(link_140)

link_141 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.90600495189008,2.78049691677857,0.208216730897223)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55158224497465e-15,-0.996593123545252)
cB = chrono.ChVector3d(-1.97739420838105,2.80967719196082,0.188637865914639)
dB = chrono.ChVector3d(0.0824751241424785,3.61362613477307e-15,0.996593123545253)
link_141.SetFlipped(True)
link_141.Initialize(body_26,body_35,False,cA,cB,dA,dB)
link_141.SetName("Distance3")
exported_items.append(link_141)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_35 , SW name: M-410iB-300 -9/M-410iB-300-04-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_36 , SW name: M-410iB-300 -9/M-410iB-300-05-1 ,  SW ref.type:5 (5)
link_142 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.71143288244173,2.7654491237564,0.220839503684697)
dA = chrono.ChVector3d(0.996418499736232,0.0187192635196771,-0.0824606727881726)
cB = chrono.ChVector3d(-3.00015381681405,2.76002505419568,0.244733201465975)
dB = chrono.ChVector3d(0.996418499736232,0.0187192635196772,-0.0824606727881727)
link_142.Initialize(body_35,body_36,False,cA,cB,dA,dB)
link_142.SetName("Coincident4")
exported_items.append(link_142)

link_143 = chrono.ChLinkMateGeneric()
link_143.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-2.71143288244173,2.7654491237564,0.220839503684697)
cB = chrono.ChVector3d(-3.00015381681405,2.76002505419568,0.244733201465975)
dA = chrono.ChVector3d(0.996418499736232,0.0187192635196771,-0.0824606727881726)
dB = chrono.ChVector3d(0.996418499736232,0.0187192635196772,-0.0824606727881727)
link_143.Initialize(body_35,body_36,False,cA,cB,dA,dB)
link_143.SetName("Coincident4")
exported_items.append(link_143)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_29 , SW name: M-410iB-300 -9/M-410iB-300-03-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_36 , SW name: M-410iB-300 -9/M-410iB-300-05-1 ,  SW ref.type:5 (5)
link_144 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.08956446048187,2.75811166841886,0.40345811797401)
dA = chrono.ChVector3d(0.082475124142479,3.64289959343017e-15,0.996593123545252)
cB = chrono.ChVector3d(-3.0991159051399,2.75811166841886,0.288042661918727)
dB = chrono.ChVector3d(0.0824751241424786,3.36978906618108e-15,0.996593123545253)
link_144.Initialize(body_29,body_36,False,cA,cB,dA,dB)
link_144.SetName("Coincident5")
exported_items.append(link_144)

link_145 = chrono.ChLinkMateGeneric()
link_145.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.08956446048187,2.75811166841886,0.40345811797401)
cB = chrono.ChVector3d(-3.0991159051399,2.75811166841886,0.288042661918727)
dA = chrono.ChVector3d(0.082475124142479,3.64289959343017e-15,0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424786,3.36978906618108e-15,0.996593123545253)
link_145.Initialize(body_29,body_36,False,cA,cB,dA,dB)
link_145.SetName("Coincident5")
exported_items.append(link_145)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_29 , SW name: M-410iB-300 -9/M-410iB-300-03-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_34 , SW name: M-410iB-300 -9/M-410iB-300-06-1 ,  SW ref.type:5 (5)
link_146 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.06708905223563,2.75811166841886,0.675041065437937)
dA = chrono.ChVector3d(0.082475124142479,3.64289959343017e-15,0.996593123545252)
cB = chrono.ChVector3d(-3.06970763742716,2.75811166841886,0.643399233765375)
dB = chrono.ChVector3d(-0.0824751241424783,-4.53761033121952e-15,-0.996593123545253)
link_146.SetFlipped(True)
link_146.Initialize(body_29,body_34,False,cA,cB,dA,dB)
link_146.SetName("Coincident6")
exported_items.append(link_146)

link_147 = chrono.ChLinkMateGeneric()
link_147.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.06708905223563,2.75811166841886,0.675041065437937)
cB = chrono.ChVector3d(-3.06970763742716,2.75811166841886,0.643399233765375)
dA = chrono.ChVector3d(0.082475124142479,3.64289959343017e-15,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424783,-4.53761033121952e-15,-0.996593123545253)
link_147.Initialize(body_29,body_34,False,cA,cB,dA,dB)
link_147.SetName("Coincident6")
exported_items.append(link_147)


# Mate constraint: Distance4 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_29 , SW name: M-410iB-300 -9/M-410iB-300-03-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_34 , SW name: M-410iB-300 -9/M-410iB-300-06-1 ,  SW ref.type:2 (2)
link_148 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-2.88223000352087,2.91434507456169,0.659742672712353)
cB = chrono.ChVector3d(-2.96321003072954,2.58269164685799,0.634585804166326)
dA = chrono.ChVector3d(-0.082475124142479,-3.64289959343017e-15,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424783,4.53761033121952e-15,0.996593123545253)
link_148.Initialize(body_29,body_34,False,cA,cB,dB)
link_148.SetDistance(0)
link_148.SetName("Distance4")
exported_items.append(link_148)

link_149 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.88223000352087,2.91434507456169,0.659742672712353)
dA = chrono.ChVector3d(-0.082475124142479,-3.64289959343017e-15,-0.996593123545252)
cB = chrono.ChVector3d(-2.96321003072954,2.58269164685799,0.634585804166326)
dB = chrono.ChVector3d(0.0824751241424783,4.53761033121952e-15,0.996593123545253)
link_149.SetFlipped(True)
link_149.Initialize(body_29,body_34,False,cA,cB,dA,dB)
link_149.SetName("Distance4")
exported_items.append(link_149)


# Mate constraint: Coincident7 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_26 , SW name: M-410iB-300 -9/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_30 , SW name: M-410iB-300 -9/M-410iB-300-07-1 ,  SW ref.type:5 (5)
link_150 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.90558579863488,2.51550127212935,0.213239278771608)
dA = chrono.ChVector3d(0.0824751241424789,3.55158224497465e-15,0.996593123545252)
cB = chrono.ChVector3d(-1.88095452717193,2.51550127212936,0.510872729092269)
dB = chrono.ChVector3d(-0.0824751241424795,-3.44202403592292e-15,-0.996593123545252)
link_150.SetFlipped(True)
link_150.Initialize(body_26,body_30,False,cA,cB,dA,dB)
link_150.SetName("Coincident7")
exported_items.append(link_150)

link_151 = chrono.ChLinkMateGeneric()
link_151.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.90558579863488,2.51550127212935,0.213239278771608)
cB = chrono.ChVector3d(-1.88095452717193,2.51550127212936,0.510872729092269)
dA = chrono.ChVector3d(0.0824751241424789,3.55158224497465e-15,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424795,-3.44202403592292e-15,-0.996593123545252)
link_151.Initialize(body_26,body_30,False,cA,cB,dA,dB)
link_151.SetName("Coincident7")
exported_items.append(link_151)


# Mate constraint: Coincident8 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_34 , SW name: M-410iB-300 -9/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_30 , SW name: M-410iB-300 -9/M-410iB-300-07-1 ,  SW ref.type:2 (2)
link_152 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-2.60711943253569,3.10515332885273,0.494740753062397)
cB = chrono.ChVector3d(-1.56768836286924,3.00995602354016,0.408720486132075)
dA = chrono.ChVector3d(0.0824751241424783,4.53761033121952e-15,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424795,3.44202403592292e-15,0.996593123545252)
link_152.Initialize(body_34,body_30,False,cA,cB,dB)
link_152.SetDistance(0)
link_152.SetName("Coincident8")
exported_items.append(link_152)

link_153 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.60711943253569,3.10515332885273,0.494740753062397)
dA = chrono.ChVector3d(0.0824751241424783,4.53761033121952e-15,0.996593123545253)
cB = chrono.ChVector3d(-1.56768836286924,3.00995602354016,0.408720486132075)
dB = chrono.ChVector3d(0.0824751241424795,3.44202403592292e-15,0.996593123545252)
link_153.Initialize(body_34,body_30,False,cA,cB,dA,dB)
link_153.SetName("Coincident8")
exported_items.append(link_153)


# Mate constraint: Distance5 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_34 , SW name: M-410iB-300 -9/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_32 , SW name: M-410iB-300 -9/M-410iB-300-08-1 ,  SW ref.type:2 (2)
link_154 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-2.60711943253569,3.10515332885273,0.494740753062397)
cB = chrono.ChVector3d(-1.57268463047198,3.01604196029193,0.431307505105985)
dA = chrono.ChVector3d(0.0824751241424783,4.53761033121952e-15,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424792,-3.92284059436593e-15,-0.996593123545252)
link_154.Initialize(body_34,body_32,False,cA,cB,dB)
link_154.SetDistance(0)
link_154.SetName("Distance5")
exported_items.append(link_154)

link_155 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.60711943253569,3.10515332885273,0.494740753062397)
dA = chrono.ChVector3d(0.0824751241424783,4.53761033121952e-15,0.996593123545253)
cB = chrono.ChVector3d(-1.57268463047198,3.01604196029193,0.431307505105985)
dB = chrono.ChVector3d(-0.0824751241424792,-3.92284059436593e-15,-0.996593123545252)
link_155.SetFlipped(True)
link_155.Initialize(body_34,body_32,False,cA,cB,dA,dB)
link_155.SetName("Distance5")
exported_items.append(link_155)


# Mate constraint: Coincident9 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_34 , SW name: M-410iB-300 -9/M-410iB-300-06-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_32 , SW name: M-410iB-300 -9/M-410iB-300-08-1 ,  SW ref.type:5 (5)
link_156 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.76251640195877,3.25502265002171,0.50760095051082)
dA = chrono.ChVector3d(0.0824751241424783,4.53761033121952e-15,0.996593123545253)
cB = chrono.ChVector3d(-2.76029584171634,3.25502265002172,0.534433223769155)
dB = chrono.ChVector3d(0.0824751241424792,3.92284059436593e-15,0.996593123545252)
link_156.Initialize(body_34,body_32,False,cA,cB,dA,dB)
link_156.SetName("Coincident9")
exported_items.append(link_156)

link_157 = chrono.ChLinkMateGeneric()
link_157.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-2.76251640195877,3.25502265002171,0.50760095051082)
cB = chrono.ChVector3d(-2.76029584171634,3.25502265002172,0.534433223769155)
dA = chrono.ChVector3d(0.0824751241424783,4.53761033121952e-15,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424792,3.92284059436593e-15,0.996593123545252)
link_157.Initialize(body_34,body_32,False,cA,cB,dA,dB)
link_157.SetName("Coincident9")
exported_items.append(link_157)


# Mate constraint: Coincident10 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_31 , SW name: M-410iB-300 -9/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_34 , SW name: M-410iB-300 -9/M-410iB-300-06-1 ,  SW ref.type:5 (5)
link_158 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.0562002936794,2.75811166841883,0.806616034423257)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55959220900182e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.06207868844398,2.75811166841886,0.735584097693311)
dB = chrono.ChVector3d(-0.0824751241424783,-4.53761033121952e-15,-0.996593123545253)
link_158.Initialize(body_31,body_34,False,cA,cB,dA,dB)
link_158.SetName("Coincident10")
exported_items.append(link_158)

link_159 = chrono.ChLinkMateGeneric()
link_159.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.0562002936794,2.75811166841883,0.806616034423257)
cB = chrono.ChVector3d(-3.06207868844398,2.75811166841886,0.735584097693311)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55959220900182e-15,-0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424783,-4.53761033121952e-15,-0.996593123545253)
link_159.Initialize(body_31,body_34,False,cA,cB,dA,dB)
link_159.SetName("Coincident10")
exported_items.append(link_159)


# Mate constraint: Coincident11 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_26 , SW name: M-410iB-300 -9/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_31 , SW name: M-410iB-300 -9/M-410iB-300-09-1 ,  SW ref.type:2 (2)
link_160 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.51318598779731,2.72491052060182,0.672548988128633)
cB = chrono.ChVector3d(-3.05641325164642,3.21365467148159,0.800261950579384)
dA = chrono.ChVector3d(0.0824751241424789,3.55158224497465e-15,0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424789,3.55959220900182e-15,0.996593123545253)
link_160.Initialize(body_26,body_31,False,cA,cB,dB)
link_160.SetDistance(0)
link_160.SetName("Coincident11")
exported_items.append(link_160)

link_161 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.51318598779731,2.72491052060182,0.672548988128633)
dA = chrono.ChVector3d(0.0824751241424789,3.55158224497465e-15,0.996593123545252)
cB = chrono.ChVector3d(-3.05641325164642,3.21365467148159,0.800261950579384)
dB = chrono.ChVector3d(0.0824751241424789,3.55959220900182e-15,0.996593123545253)
link_161.Initialize(body_26,body_31,False,cA,cB,dA,dB)
link_161.SetName("Coincident11")
exported_items.append(link_161)


# Mate constraint: Coincident12 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_31 , SW name: M-410iB-300 -9/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_37 , SW name: M-410iB-300 -9/M-410iB-300-10-1 ,  SW ref.type:5 (5)
link_162 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.55781544031629,3.03081076163703,0.752627750357588)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55959220900182e-15,-0.996593123545253)
cB = chrono.ChVector3d(-2.55308103828999,3.03081076163706,0.80983618202158)
dB = chrono.ChVector3d(-0.0824751241424783,-3.93682680239099e-15,-0.996593123545252)
link_162.Initialize(body_31,body_37,False,cA,cB,dA,dB)
link_162.SetName("Coincident12")
exported_items.append(link_162)

link_163 = chrono.ChLinkMateGeneric()
link_163.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-2.55781544031629,3.03081076163703,0.752627750357588)
cB = chrono.ChVector3d(-2.55308103828999,3.03081076163706,0.80983618202158)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55959220900182e-15,-0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424783,-3.93682680239099e-15,-0.996593123545252)
link_163.Initialize(body_31,body_37,False,cA,cB,dA,dB)
link_163.SetName("Coincident12")
exported_items.append(link_163)


# Mate constraint: Distance7 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_31 , SW name: M-410iB-300 -9/M-410iB-300-09-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_37 , SW name: M-410iB-300 -9/M-410iB-300-10-1 ,  SW ref.type:2 (2)
link_164 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-3.05641325164642,3.21365467148159,0.800261950579384)
cB = chrono.ChVector3d(-2.55704033909957,3.03081076163706,0.761993732532667)
dA = chrono.ChVector3d(0.0824751241424789,3.55959220900182e-15,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424783,-3.93682680239099e-15,-0.996593123545252)
link_164.Initialize(body_31,body_37,False,cA,cB,dB)
link_164.SetDistance(0)
link_164.SetName("Distance7")
exported_items.append(link_164)

link_165 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.05641325164642,3.21365467148159,0.800261950579384)
dA = chrono.ChVector3d(0.0824751241424789,3.55959220900182e-15,0.996593123545253)
cB = chrono.ChVector3d(-2.55704033909957,3.03081076163706,0.761993732532667)
dB = chrono.ChVector3d(-0.0824751241424783,-3.93682680239099e-15,-0.996593123545252)
link_165.SetFlipped(True)
link_165.Initialize(body_31,body_37,False,cA,cB,dA,dB)
link_165.SetName("Distance7")
exported_items.append(link_165)


# Mate constraint: Coincident13 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_26 , SW name: M-410iB-300 -9/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_37 , SW name: M-410iB-300 -9/M-410iB-300-10-1 ,  SW ref.type:5 (5)
link_166 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.36587439836585,2.78749692402102,0.660357913015888)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55158224497465e-15,-0.996593123545252)
cB = chrono.ChVector3d(-1.36562301418745,2.78749692402102,0.663395528856457)
dB = chrono.ChVector3d(0.0824751241424783,3.93682680239099e-15,0.996593123545252)
link_166.SetFlipped(True)
link_166.Initialize(body_26,body_37,False,cA,cB,dA,dB)
link_166.SetName("Coincident13")
exported_items.append(link_166)

link_167 = chrono.ChLinkMateGeneric()
link_167.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.36587439836585,2.78749692402102,0.660357913015888)
cB = chrono.ChVector3d(-1.36562301418745,2.78749692402102,0.663395528856457)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55158224497465e-15,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424783,3.93682680239099e-15,0.996593123545252)
link_167.Initialize(body_26,body_37,False,cA,cB,dA,dB)
link_167.SetName("Coincident13")
exported_items.append(link_167)


# Mate constraint: Coincident14 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_31 , SW name: M-410iB-300 -9/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_33 , SW name: M-410iB-300 -9/M-410iB-300-11-1 ,  SW ref.type:5 (5)
link_168 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.55579644633207,3.02764258400498,0.83521773158301)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55959220900182e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.56428066235258,3.02764258400503,0.732698196963912)
dB = chrono.ChVector3d(0.0824751241424785,4.759085730004e-15,0.996593123545252)
link_168.SetFlipped(True)
link_168.Initialize(body_31,body_33,False,cA,cB,dA,dB)
link_168.SetName("Coincident14")
exported_items.append(link_168)

link_169 = chrono.ChLinkMateGeneric()
link_169.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.55579644633207,3.02764258400498,0.83521773158301)
cB = chrono.ChVector3d(-3.56428066235258,3.02764258400503,0.732698196963912)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55959220900182e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424785,4.759085730004e-15,0.996593123545252)
link_169.Initialize(body_31,body_33,False,cA,cB,dA,dB)
link_169.SetName("Coincident14")
exported_items.append(link_169)


# Mate constraint: Distance8 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_31 , SW name: M-410iB-300 -9/M-410iB-300-09-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_33 , SW name: M-410iB-300 -9/M-410iB-300-11-1 ,  SW ref.type:2 (2)
link_170 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-3.060372552456,3.21365467148159,0.75241950109047)
cB = chrono.ChVector3d(-3.55910633801413,3.02764258400503,0.795222456348894)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55959220900182e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424785,4.759085730004e-15,0.996593123545253)
link_170.Initialize(body_31,body_33,False,cA,cB,dB)
link_170.SetDistance(0)
link_170.SetName("Distance8")
exported_items.append(link_170)

link_171 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.060372552456,3.21365467148159,0.75241950109047)
dA = chrono.ChVector3d(-0.0824751241424789,-3.55959220900182e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.55910633801413,3.02764258400503,0.795222456348894)
dB = chrono.ChVector3d(0.0824751241424785,4.759085730004e-15,0.996593123545253)
link_171.SetFlipped(True)
link_171.Initialize(body_31,body_33,False,cA,cB,dA,dB)
link_171.SetName("Distance8")
exported_items.append(link_171)


# Mate constraint: Coincident15 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_34 , SW name: M-410iB-300 -9/M-410iB-300-06-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_27 , SW name: M-410iB-300 -9/M-410iB-300-12-1 ,  SW ref.type:5 (5)
link_172 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.81525551082145,1.6937690405165,0.68503021873686)
dA = chrono.ChVector3d(-0.0824751241424783,-4.53761033121952e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.81422770582439,1.69376904051649,0.697449762242482)
dB = chrono.ChVector3d(0.0824751241424788,4.52631154697786e-15,0.996593123545253)
link_172.SetFlipped(True)
link_172.Initialize(body_34,body_27,False,cA,cB,dA,dB)
link_172.SetName("Coincident15")
exported_items.append(link_172)

link_173 = chrono.ChLinkMateGeneric()
link_173.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.81525551082145,1.6937690405165,0.68503021873686)
cB = chrono.ChVector3d(-3.81422770582439,1.69376904051649,0.697449762242482)
dA = chrono.ChVector3d(-0.0824751241424783,-4.53761033121952e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424788,4.52631154697786e-15,0.996593123545253)
link_173.Initialize(body_34,body_27,False,cA,cB,dA,dB)
link_173.SetName("Coincident15")
exported_items.append(link_173)


# Mate constraint: Distance9 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_34 , SW name: M-410iB-300 -9/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_27 , SW name: M-410iB-300 -9/M-410iB-300-12-1 ,  SW ref.type:2 (2)
link_174 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-3.18827765327686,2.27955349819168,0.492664776806463)
cB = chrono.ChVector3d(-3.82784946227801,1.69376904051649,0.532850448771503)
dA = chrono.ChVector3d(-0.0824751241424783,-4.53761033121952e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424788,4.52631154697786e-15,0.996593123545253)
link_174.Initialize(body_34,body_27,False,cA,cB,dB)
link_174.SetDistance(0)
link_174.SetName("Distance9")
exported_items.append(link_174)

link_175 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.18827765327686,2.27955349819168,0.492664776806463)
dA = chrono.ChVector3d(-0.0824751241424783,-4.53761033121952e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.82784946227801,1.69376904051649,0.532850448771503)
dB = chrono.ChVector3d(0.0824751241424788,4.52631154697786e-15,0.996593123545253)
link_175.SetFlipped(True)
link_175.Initialize(body_34,body_27,False,cA,cB,dA,dB)
link_175.SetName("Distance9")
exported_items.append(link_175)


# Mate constraint: Coincident16 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_33 , SW name: M-410iB-300 -9/M-410iB-300-11-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_27 , SW name: M-410iB-300 -9/M-410iB-300-12-1 ,  SW ref.type:5 (5)
link_176 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-4.30817905100364,1.96329996858997,0.794261045937959)
dA = chrono.ChVector3d(0.0824751241424785,4.759085730004e-15,0.996593123545252)
cB = chrono.ChVector3d(-4.31277644214529,1.96329996858994,0.73870819353977)
dB = chrono.ChVector3d(0.0824751241424788,4.52631154697786e-15,0.996593123545253)
link_176.Initialize(body_33,body_27,False,cA,cB,dA,dB)
link_176.SetName("Coincident16")
exported_items.append(link_176)

link_177 = chrono.ChLinkMateGeneric()
link_177.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-4.30817905100364,1.96329996858997,0.794261045937959)
cB = chrono.ChVector3d(-4.31277644214529,1.96329996858994,0.73870819353977)
dA = chrono.ChVector3d(0.0824751241424785,4.759085730004e-15,0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424788,4.52631154697786e-15,0.996593123545253)
link_177.Initialize(body_33,body_27,False,cA,cB,dA,dB)
link_177.SetName("Coincident16")
exported_items.append(link_177)


# Mate constraint: Coincident17 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_30 , SW name: M-410iB-300 -9/M-410iB-300-07-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_32 , SW name: M-410iB-300 -9/M-410iB-300-08-1 ,  SW ref.type:5 (5)
link_178 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.56037999469361,3.00995602354016,0.49703159258879)
dA = chrono.ChVector3d(-0.0824751241424795,-3.44202403592292e-15,-0.996593123545252)
cB = chrono.ChVector3d(-1.56546780262683,3.00995602354016,0.435552759390407)
dB = chrono.ChVector3d(0.0824751241424792,3.92284059436593e-15,0.996593123545252)
link_178.SetFlipped(True)
link_178.Initialize(body_30,body_32,False,cA,cB,dA,dB)
link_178.SetName("Coincident17")
exported_items.append(link_178)

link_179 = chrono.ChLinkMateGeneric()
link_179.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.56037999469361,3.00995602354016,0.49703159258879)
cB = chrono.ChVector3d(-1.56546780262683,3.00995602354016,0.435552759390407)
dA = chrono.ChVector3d(-0.0824751241424795,-3.44202403592292e-15,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424792,3.92284059436593e-15,0.996593123545252)
link_179.Initialize(body_30,body_32,False,cA,cB,dA,dB)
link_179.SetName("Coincident17")
exported_items.append(link_179)


# Mate constraint: Coincident18 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_26 , SW name: M-410iB-300 -9/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_28 , SW name: M-410iB-300 -9/ArmBase-1 ,  SW ref.type:2 (2)
link_180 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.50067035795504,2.04602671615662,0.377403113437383)
cB = chrono.ChVector3d(-1.25867129241134,2.04602671615662,0.377403113437383)
dA = chrono.ChVector3d(1.94491773090787e-16,-1,3.54762784160808e-15)
dB = chrono.ChVector3d(-6.21947280249299e-17,1,-3.55871276754624e-15)
link_180.Initialize(body_26,body_28,False,cA,cB,dB)
link_180.SetDistance(0)
link_180.SetName("Coincident18")
exported_items.append(link_180)

link_181 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.50067035795504,2.04602671615662,0.377403113437383)
dA = chrono.ChVector3d(1.94491773090787e-16,-1,3.54762784160808e-15)
cB = chrono.ChVector3d(-1.25867129241134,2.04602671615662,0.377403113437383)
dB = chrono.ChVector3d(-6.21947280249299e-17,1,-3.55871276754624e-15)
link_181.SetFlipped(True)
link_181.Initialize(body_26,body_28,False,cA,cB,dA,dB)
link_181.SetName("Coincident18")
exported_items.append(link_181)


# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_26 , SW name: M-410iB-300 -9/M-410iB-300-02-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_28 , SW name: M-410iB-300 -9/ArmBase-1 ,  SW ref.type:1 (1)
link_182 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.50067035795504,2.04755071615662,0.377403113437383)
dA = chrono.ChVector3d(-1.94491773090787e-16,1,-3.54762784160808e-15)
cB = chrono.ChVector3d(-1.50067035795504,2.04602671615662,0.377403113437383)
dB = chrono.ChVector3d(-6.21947280249299e-17,1,-3.55871276754624e-15)
link_182.Initialize(body_26,body_28,False,cA,cB,dA,dB)
link_182.SetName("Concentric1")
exported_items.append(link_182)

link_183 = chrono.ChLinkMateGeneric()
link_183.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.50067035795504,2.04755071615662,0.377403113437383)
cB = chrono.ChVector3d(-1.50067035795504,2.04602671615662,0.377403113437383)
dA = chrono.ChVector3d(-1.94491773090787e-16,1,-3.54762784160808e-15)
dB = chrono.ChVector3d(-6.21947280249299e-17,1,-3.55871276754624e-15)
link_183.Initialize(body_26,body_28,False,cA,cB,dA,dB)
link_183.SetName("Concentric1")
exported_items.append(link_183)


# Mate constraint: Coincident2_hinge [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_40 , SW name: M-410iB-300 -3/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_39 , SW name: M-410iB-300 -3/M-410iB-300-03-1 ,  SW ref.type:5 (5)
link_184 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.237440667378504,2.51550127212935,-2.68232581704903)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
cB = chrono.ChVector3d(0.256663804363385,2.51550127212935,-2.45004188499936)
dB = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
link_184.Initialize(body_40,body_39,False,cA,cB,dA,dB)
link_184.SetName("Coincident2_hinge")
exported_items.append(link_184)

link_185 = chrono.ChLinkMateGeneric()
link_185.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.237440667378504,2.51550127212935,-2.68232581704903)
cB = chrono.ChVector3d(0.256663804363385,2.51550127212935,-2.45004188499936)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
link_185.Initialize(body_40,body_39,False,cA,cB,dA,dB)
link_185.SetName("Coincident2_hinge")
exported_items.append(link_185)


# Mate constraint: Distance2 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_40 , SW name: M-410iB-300 -3/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_39 , SW name: M-410iB-300 -3/M-410iB-300-03-1 ,  SW ref.type:2 (2)
link_186 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.468847901417993,2.84164228947283,-2.45664228148036)
cB = chrono.ChVector3d(1.09486376832202,2.54318522667954,-2.51150793833294)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424792,-9.11814027060309e-17,0.996593123545252)
link_186.Initialize(body_40,body_39,False,cA,cB,dB)
link_186.SetDistance(0)
link_186.SetName("Distance2")
exported_items.append(link_186)

link_187 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.468847901417993,2.84164228947283,-2.45664228148036)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
cB = chrono.ChVector3d(1.09486376832202,2.54318522667954,-2.51150793833294)
dB = chrono.ChVector3d(0.0824751241424792,-9.11814027060309e-17,0.996593123545252)
link_187.SetFlipped(True)
link_187.Initialize(body_40,body_39,False,cA,cB,dA,dB)
link_187.SetName("Distance2")
exported_items.append(link_187)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_40 , SW name: M-410iB-300 -3/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_38 , SW name: M-410iB-300 -3/M-410iB-300-04-1 ,  SW ref.type:5 (5)
link_188 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.260985806741079,2.78049690546384,-2.39785906225185)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
cB = chrono.ChVector3d(0.266759107195714,2.78049690546384,-2.32809703893785)
dB = chrono.ChVector3d(0.0824751241424787,-6.19079440489223e-17,0.996593123545253)
link_188.Initialize(body_40,body_38,False,cA,cB,dA,dB)
link_188.SetName("Coincident3")
exported_items.append(link_188)

link_189 = chrono.ChLinkMateGeneric()
link_189.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.260985806741079,2.78049690546384,-2.39785906225185)
cB = chrono.ChVector3d(0.266759107195714,2.78049690546384,-2.32809703893785)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424787,-6.19079440489223e-17,0.996593123545253)
link_189.Initialize(body_40,body_38,False,cA,cB,dA,dB)
link_189.SetName("Coincident3")
exported_items.append(link_189)


# Mate constraint: Distance3 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_40 , SW name: M-410iB-300 -3/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_38 , SW name: M-410iB-300 -3/M-410iB-300-04-1 ,  SW ref.type:2 (2)
link_190 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.264664235980002,2.78049691677857,-2.35341050402245)
cB = chrono.ChVector3d(0.336053492470978,2.80967719196082,-2.33383163903987)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424787,6.19079440489223e-17,-0.996593123545253)
link_190.Initialize(body_40,body_38,False,cA,cB,dB)
link_190.SetDistance(0)
link_190.SetName("Distance3")
exported_items.append(link_190)

link_191 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.264664235980002,2.78049691677857,-2.35341050402245)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
cB = chrono.ChVector3d(0.336053492470978,2.80967719196082,-2.33383163903987)
dB = chrono.ChVector3d(-0.0824751241424787,6.19079440489223e-17,-0.996593123545253)
link_191.SetFlipped(True)
link_191.Initialize(body_40,body_38,False,cA,cB,dA,dB)
link_191.SetName("Distance3")
exported_items.append(link_191)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_38 , SW name: M-410iB-300 -3/M-410iB-300-04-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_44 , SW name: M-410iB-300 -3/M-410iB-300-05-1 ,  SW ref.type:5 (5)
link_192 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.07009216653166,2.7654491237564,-2.36603327680993)
dA = chrono.ChVector3d(-0.996418499736232,0.0187192635196773,0.0824606727881728)
cB = chrono.ChVector3d(1.35881310090398,2.76002505419567,-2.3899269745912)
dB = chrono.ChVector3d(-0.996418499736232,0.0187192635196774,0.0824606727881729)
link_192.Initialize(body_38,body_44,False,cA,cB,dA,dB)
link_192.SetName("Coincident4")
exported_items.append(link_192)

link_193 = chrono.ChLinkMateGeneric()
link_193.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.07009216653166,2.7654491237564,-2.36603327680993)
cB = chrono.ChVector3d(1.35881310090398,2.76002505419567,-2.3899269745912)
dA = chrono.ChVector3d(-0.996418499736232,0.0187192635196773,0.0824606727881728)
dB = chrono.ChVector3d(-0.996418499736232,0.0187192635196774,0.0824606727881729)
link_193.Initialize(body_38,body_44,False,cA,cB,dA,dB)
link_193.SetName("Coincident4")
exported_items.append(link_193)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_39 , SW name: M-410iB-300 -3/M-410iB-300-03-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_44 , SW name: M-410iB-300 -3/M-410iB-300-05-1 ,  SW ref.type:5 (5)
link_194 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.44822374457179,2.75811166841886,-2.54865189109924)
dA = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
cB = chrono.ChVector3d(1.45777518922982,2.75811166841886,-2.43323643504396)
dB = chrono.ChVector3d(-0.0824751241424788,-1.81929124543068e-16,-0.996593123545253)
link_194.Initialize(body_39,body_44,False,cA,cB,dA,dB)
link_194.SetName("Coincident5")
exported_items.append(link_194)

link_195 = chrono.ChLinkMateGeneric()
link_195.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.44822374457179,2.75811166841886,-2.54865189109924)
cB = chrono.ChVector3d(1.45777518922982,2.75811166841886,-2.43323643504396)
dA = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424788,-1.81929124543068e-16,-0.996593123545253)
link_195.Initialize(body_39,body_44,False,cA,cB,dA,dB)
link_195.SetName("Coincident5")
exported_items.append(link_195)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_39 , SW name: M-410iB-300 -3/M-410iB-300-03-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_41 , SW name: M-410iB-300 -3/M-410iB-300-06-1 ,  SW ref.type:5 (5)
link_196 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.42574833632556,2.75811166841886,-2.82023483856317)
dA = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
cB = chrono.ChVector3d(1.42836692151708,2.75811166841885,-2.78859300689061)
dB = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
link_196.SetFlipped(True)
link_196.Initialize(body_39,body_41,False,cA,cB,dA,dB)
link_196.SetName("Coincident6")
exported_items.append(link_196)

link_197 = chrono.ChLinkMateGeneric()
link_197.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.42574833632556,2.75811166841886,-2.82023483856317)
cB = chrono.ChVector3d(1.42836692151708,2.75811166841885,-2.78859300689061)
dA = chrono.ChVector3d(-0.0824751241424792,9.11814027060309e-17,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
link_197.Initialize(body_39,body_41,False,cA,cB,dA,dB)
link_197.SetName("Coincident6")
exported_items.append(link_197)


# Mate constraint: Distance4 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_39 , SW name: M-410iB-300 -3/M-410iB-300-03-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: M-410iB-300 -3/M-410iB-300-06-1 ,  SW ref.type:2 (2)
link_198 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(1.24088928761079,2.91434507456168,-2.80493644583758)
cB = chrono.ChVector3d(1.32186931481946,2.58269164685799,-2.77977957729156)
dA = chrono.ChVector3d(0.0824751241424792,-9.11814027060309e-17,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
link_198.Initialize(body_39,body_41,False,cA,cB,dB)
link_198.SetDistance(0)
link_198.SetName("Distance4")
exported_items.append(link_198)

link_199 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.24088928761079,2.91434507456168,-2.80493644583758)
dA = chrono.ChVector3d(0.0824751241424792,-9.11814027060309e-17,0.996593123545252)
cB = chrono.ChVector3d(1.32186931481946,2.58269164685799,-2.77977957729156)
dB = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
link_199.SetFlipped(True)
link_199.Initialize(body_39,body_41,False,cA,cB,dA,dB)
link_199.SetName("Distance4")
exported_items.append(link_199)


# Mate constraint: Coincident7 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_40 , SW name: M-410iB-300 -3/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_47 , SW name: M-410iB-300 -3/M-410iB-300-07-1 ,  SW ref.type:5 (5)
link_200 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.264245082724809,2.51550127212935,-2.35843305189684)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
cB = chrono.ChVector3d(0.239613811261857,2.51550127212935,-2.6560665022175)
dB = chrono.ChVector3d(0.0824751241424797,1.09694154801221e-16,0.996593123545252)
link_200.SetFlipped(True)
link_200.Initialize(body_40,body_47,False,cA,cB,dA,dB)
link_200.SetName("Coincident7")
exported_items.append(link_200)

link_201 = chrono.ChLinkMateGeneric()
link_201.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.264245082724809,2.51550127212935,-2.35843305189684)
cB = chrono.ChVector3d(0.239613811261857,2.51550127212935,-2.6560665022175)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424797,1.09694154801221e-16,0.996593123545252)
link_201.Initialize(body_40,body_47,False,cA,cB,dA,dB)
link_201.SetName("Coincident7")
exported_items.append(link_201)


# Mate constraint: Coincident8 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_41 , SW name: M-410iB-300 -3/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_47 , SW name: M-410iB-300 -3/M-410iB-300-07-1 ,  SW ref.type:2 (2)
link_202 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.965778716625616,3.10515332885273,-2.63993452618763)
cB = chrono.ChVector3d(-0.0736523530408296,3.00995602354016,-2.55391425925731)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424797,-1.09694154801221e-16,-0.996593123545252)
link_202.Initialize(body_41,body_47,False,cA,cB,dB)
link_202.SetDistance(0)
link_202.SetName("Coincident8")
exported_items.append(link_202)

link_203 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.965778716625616,3.10515332885273,-2.63993452618763)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
cB = chrono.ChVector3d(-0.0736523530408296,3.00995602354016,-2.55391425925731)
dB = chrono.ChVector3d(-0.0824751241424797,-1.09694154801221e-16,-0.996593123545252)
link_203.Initialize(body_41,body_47,False,cA,cB,dA,dB)
link_203.SetName("Coincident8")
exported_items.append(link_203)


# Mate constraint: Distance5 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_41 , SW name: M-410iB-300 -3/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_45 , SW name: M-410iB-300 -3/M-410iB-300-08-1 ,  SW ref.type:2 (2)
link_204 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.965778716625616,3.10515332885273,-2.63993452618763)
cB = chrono.ChVector3d(-0.0686560854380925,3.01604196029193,-2.57650127823121)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424794,-3.71122403641788e-16,0.996593123545252)
link_204.Initialize(body_41,body_45,False,cA,cB,dB)
link_204.SetDistance(0)
link_204.SetName("Distance5")
exported_items.append(link_204)

link_205 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.965778716625616,3.10515332885273,-2.63993452618763)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
cB = chrono.ChVector3d(-0.0686560854380925,3.01604196029193,-2.57650127823121)
dB = chrono.ChVector3d(0.0824751241424794,-3.71122403641788e-16,0.996593123545252)
link_205.SetFlipped(True)
link_205.Initialize(body_41,body_45,False,cA,cB,dA,dB)
link_205.SetName("Distance5")
exported_items.append(link_205)


# Mate constraint: Coincident9 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_41 , SW name: M-410iB-300 -3/M-410iB-300-06-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_45 , SW name: M-410iB-300 -3/M-410iB-300-08-1 ,  SW ref.type:5 (5)
link_206 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.12117568604869,3.25502265002171,-2.65279472363605)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
cB = chrono.ChVector3d(1.11895512580627,3.25502265002172,-2.67962699689439)
dB = chrono.ChVector3d(-0.0824751241424794,3.71122403641788e-16,-0.996593123545252)
link_206.Initialize(body_41,body_45,False,cA,cB,dA,dB)
link_206.SetName("Coincident9")
exported_items.append(link_206)

link_207 = chrono.ChLinkMateGeneric()
link_207.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.12117568604869,3.25502265002171,-2.65279472363605)
cB = chrono.ChVector3d(1.11895512580627,3.25502265002172,-2.67962699689439)
dA = chrono.ChVector3d(-0.0824751241424786,9.85892140495381e-16,-0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424794,3.71122403641788e-16,-0.996593123545252)
link_207.Initialize(body_41,body_45,False,cA,cB,dA,dB)
link_207.SetName("Coincident9")
exported_items.append(link_207)


# Mate constraint: Coincident10 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_46 , SW name: M-410iB-300 -3/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_41 , SW name: M-410iB-300 -3/M-410iB-300-06-1 ,  SW ref.type:5 (5)
link_208 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.41485957776932,2.75811166841883,-2.95180980754849)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
cB = chrono.ChVector3d(1.42073797253391,2.75811166841885,-2.88077787081854)
dB = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
link_208.Initialize(body_46,body_41,False,cA,cB,dA,dB)
link_208.SetName("Coincident10")
exported_items.append(link_208)

link_209 = chrono.ChLinkMateGeneric()
link_209.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.41485957776932,2.75811166841883,-2.95180980754849)
cB = chrono.ChVector3d(1.42073797253391,2.75811166841885,-2.88077787081854)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
link_209.Initialize(body_46,body_41,False,cA,cB,dA,dB)
link_209.SetName("Coincident10")
exported_items.append(link_209)


# Mate constraint: Coincident11 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_40 , SW name: M-410iB-300 -3/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_46 , SW name: M-410iB-300 -3/M-410iB-300-09-1 ,  SW ref.type:2 (2)
link_210 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.128154728112769,2.72491052060182,-2.81774276125386)
cB = chrono.ChVector3d(1.41507253573634,3.21365467148159,-2.94545572370462)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424791,7.87401827767598e-18,-0.996593123545253)
link_210.Initialize(body_40,body_46,False,cA,cB,dB)
link_210.SetDistance(0)
link_210.SetName("Coincident11")
exported_items.append(link_210)

link_211 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.128154728112769,2.72491052060182,-2.81774276125386)
dA = chrono.ChVector3d(-0.0824751241424792,-1.35945749492389e-19,-0.996593123545252)
cB = chrono.ChVector3d(1.41507253573634,3.21365467148159,-2.94545572370462)
dB = chrono.ChVector3d(-0.0824751241424791,7.87401827767598e-18,-0.996593123545253)
link_211.Initialize(body_40,body_46,False,cA,cB,dA,dB)
link_211.SetName("Coincident11")
exported_items.append(link_211)


# Mate constraint: Coincident12 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_46 , SW name: M-410iB-300 -3/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_48 , SW name: M-410iB-300 -3/M-410iB-300-10-1 ,  SW ref.type:5 (5)
link_212 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.916474724406216,3.03081076163703,-2.89782152348282)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
cB = chrono.ChVector3d(0.911740322379911,3.03081076163706,-2.95502995514681)
dB = chrono.ChVector3d(0.0824751241424785,-3.85108611666851e-16,0.996593123545252)
link_212.Initialize(body_46,body_48,False,cA,cB,dA,dB)
link_212.SetName("Coincident12")
exported_items.append(link_212)

link_213 = chrono.ChLinkMateGeneric()
link_213.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.916474724406216,3.03081076163703,-2.89782152348282)
cB = chrono.ChVector3d(0.911740322379911,3.03081076163706,-2.95502995514681)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424785,-3.85108611666851e-16,0.996593123545252)
link_213.Initialize(body_46,body_48,False,cA,cB,dA,dB)
link_213.SetName("Coincident12")
exported_items.append(link_213)


# Mate constraint: Distance7 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_46 , SW name: M-410iB-300 -3/M-410iB-300-09-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_48 , SW name: M-410iB-300 -3/M-410iB-300-10-1 ,  SW ref.type:2 (2)
link_214 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(1.41507253573634,3.21365467148159,-2.94545572370462)
cB = chrono.ChVector3d(0.915699623189495,3.03081076163706,-2.9071875056579)
dA = chrono.ChVector3d(-0.0824751241424791,7.87401827767598e-18,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424785,-3.85108611666851e-16,0.996593123545252)
link_214.Initialize(body_46,body_48,False,cA,cB,dB)
link_214.SetDistance(0)
link_214.SetName("Distance7")
exported_items.append(link_214)

link_215 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.41507253573634,3.21365467148159,-2.94545572370462)
dA = chrono.ChVector3d(-0.0824751241424791,7.87401827767598e-18,-0.996593123545253)
cB = chrono.ChVector3d(0.915699623189495,3.03081076163706,-2.9071875056579)
dB = chrono.ChVector3d(0.0824751241424785,-3.85108611666851e-16,0.996593123545252)
link_215.SetFlipped(True)
link_215.Initialize(body_46,body_48,False,cA,cB,dA,dB)
link_215.SetName("Distance7")
exported_items.append(link_215)


# Mate constraint: Coincident13 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_40 , SW name: M-410iB-300 -3/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_48 , SW name: M-410iB-300 -3/M-410iB-300-10-1 ,  SW ref.type:5 (5)
link_216 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.275466317544226,2.78749692402101,-2.80555168614112)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
cB = chrono.ChVector3d(-0.27571770172262,2.78749692402101,-2.80858930198169)
dB = chrono.ChVector3d(-0.0824751241424785,3.85108611666851e-16,-0.996593123545252)
link_216.SetFlipped(True)
link_216.Initialize(body_40,body_48,False,cA,cB,dA,dB)
link_216.SetName("Coincident13")
exported_items.append(link_216)

link_217 = chrono.ChLinkMateGeneric()
link_217.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-0.275466317544226,2.78749692402101,-2.80555168614112)
cB = chrono.ChVector3d(-0.27571770172262,2.78749692402101,-2.80858930198169)
dA = chrono.ChVector3d(0.0824751241424792,1.35945749492389e-19,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424785,3.85108611666851e-16,-0.996593123545252)
link_217.Initialize(body_40,body_48,False,cA,cB,dA,dB)
link_217.SetName("Coincident13")
exported_items.append(link_217)


# Mate constraint: Coincident14 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_46 , SW name: M-410iB-300 -3/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_49 , SW name: M-410iB-300 -3/M-410iB-300-11-1 ,  SW ref.type:5 (5)
link_218 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.914455730422,3.02764258400498,-2.98041150470824)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
cB = chrono.ChVector3d(1.92293994644251,3.02764258400502,-2.87789197008914)
dB = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545252)
link_218.SetFlipped(True)
link_218.Initialize(body_46,body_49,False,cA,cB,dA,dB)
link_218.SetName("Coincident14")
exported_items.append(link_218)

link_219 = chrono.ChLinkMateGeneric()
link_219.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(1.914455730422,3.02764258400498,-2.98041150470824)
cB = chrono.ChVector3d(1.92293994644251,3.02764258400502,-2.87789197008914)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545252)
link_219.Initialize(body_46,body_49,False,cA,cB,dA,dB)
link_219.SetName("Coincident14")
exported_items.append(link_219)


# Mate constraint: Distance8 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_46 , SW name: M-410iB-300 -3/M-410iB-300-09-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_49 , SW name: M-410iB-300 -3/M-410iB-300-11-1 ,  SW ref.type:2 (2)
link_220 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(1.41903183654593,3.21365467148159,-2.8976132742157)
cB = chrono.ChVector3d(1.91776562210406,3.02764258400502,-2.94041622947412)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545253)
link_220.Initialize(body_46,body_49,False,cA,cB,dB)
link_220.SetDistance(0)
link_220.SetName("Distance8")
exported_items.append(link_220)

link_221 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.41903183654593,3.21365467148159,-2.8976132742157)
dA = chrono.ChVector3d(0.0824751241424791,-7.87401827767598e-18,0.996593123545253)
cB = chrono.ChVector3d(1.91776562210406,3.02764258400502,-2.94041622947412)
dB = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545253)
link_221.SetFlipped(True)
link_221.Initialize(body_46,body_49,False,cA,cB,dA,dB)
link_221.SetName("Distance8")
exported_items.append(link_221)


# Mate constraint: Coincident15 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_41 , SW name: M-410iB-300 -3/M-410iB-300-06-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_42 , SW name: M-410iB-300 -3/M-410iB-300-12-1 ,  SW ref.type:5 (5)
link_222 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(2.17391479491138,1.6937690405165,-2.83022399186209)
dA = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
cB = chrono.ChVector3d(2.17288698991431,1.69376904051649,-2.84264353536771)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_222.SetFlipped(True)
link_222.Initialize(body_41,body_42,False,cA,cB,dA,dB)
link_222.SetName("Coincident15")
exported_items.append(link_222)

link_223 = chrono.ChLinkMateGeneric()
link_223.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(2.17391479491138,1.6937690405165,-2.83022399186209)
cB = chrono.ChVector3d(2.17288698991431,1.69376904051649,-2.84264353536771)
dA = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_223.Initialize(body_41,body_42,False,cA,cB,dA,dB)
link_223.SetName("Coincident15")
exported_items.append(link_223)


# Mate constraint: Distance9 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_41 , SW name: M-410iB-300 -3/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_42 , SW name: M-410iB-300 -3/M-410iB-300-12-1 ,  SW ref.type:2 (2)
link_224 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(1.54693693736679,2.27955349819168,-2.63785854993169)
cB = chrono.ChVector3d(2.18650874636793,1.69376904051649,-2.67804422189673)
dA = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_224.Initialize(body_41,body_42,False,cA,cB,dB)
link_224.SetDistance(0)
link_224.SetName("Distance9")
exported_items.append(link_224)

link_225 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(1.54693693736679,2.27955349819168,-2.63785854993169)
dA = chrono.ChVector3d(0.0824751241424786,-9.85892140495381e-16,0.996593123545253)
cB = chrono.ChVector3d(2.18650874636793,1.69376904051649,-2.67804422189673)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_225.SetFlipped(True)
link_225.Initialize(body_41,body_42,False,cA,cB,dA,dB)
link_225.SetName("Distance9")
exported_items.append(link_225)


# Mate constraint: Coincident16 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_49 , SW name: M-410iB-300 -3/M-410iB-300-11-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_42 , SW name: M-410iB-300 -3/M-410iB-300-12-1 ,  SW ref.type:5 (5)
link_226 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(2.66683833509357,1.96329996858996,-2.93945481906319)
dA = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545252)
cB = chrono.ChVector3d(2.67143572623521,1.96329996858993,-2.883901966665)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_226.Initialize(body_49,body_42,False,cA,cB,dA,dB)
link_226.SetName("Coincident16")
exported_items.append(link_226)

link_227 = chrono.ChLinkMateGeneric()
link_227.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(2.66683833509357,1.96329996858996,-2.93945481906319)
cB = chrono.ChVector3d(2.67143572623521,1.96329996858993,-2.883901966665)
dA = chrono.ChVector3d(-0.0824751241424787,1.20736753927986e-15,-0.996593123545252)
dB = chrono.ChVector3d(-0.082475124142479,9.74593356253719e-16,-0.996593123545253)
link_227.Initialize(body_49,body_42,False,cA,cB,dA,dB)
link_227.SetName("Coincident16")
exported_items.append(link_227)


# Mate constraint: Coincident17 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_47 , SW name: M-410iB-300 -3/M-410iB-300-07-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_45 , SW name: M-410iB-300 -3/M-410iB-300-08-1 ,  SW ref.type:5 (5)
link_228 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.0809607212164672,3.00995602354016,-2.64222536571402)
dA = chrono.ChVector3d(0.0824751241424797,1.09694154801221e-16,0.996593123545252)
cB = chrono.ChVector3d(-0.0758729132832484,3.00995602354016,-2.58074653251564)
dB = chrono.ChVector3d(-0.0824751241424794,3.71122403641788e-16,-0.996593123545252)
link_228.SetFlipped(True)
link_228.Initialize(body_47,body_45,False,cA,cB,dA,dB)
link_228.SetName("Coincident17")
exported_items.append(link_228)

link_229 = chrono.ChLinkMateGeneric()
link_229.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-0.0809607212164672,3.00995602354016,-2.64222536571402)
cB = chrono.ChVector3d(-0.0758729132832484,3.00995602354016,-2.58074653251564)
dA = chrono.ChVector3d(0.0824751241424797,1.09694154801221e-16,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424794,3.71122403641788e-16,-0.996593123545252)
link_229.Initialize(body_47,body_45,False,cA,cB,dA,dB)
link_229.SetName("Coincident17")
exported_items.append(link_229)


# Mate constraint: Coincident18 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_40 , SW name: M-410iB-300 -3/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_43 , SW name: M-410iB-300 -3/ArmBase-1 ,  SW ref.type:2 (2)
link_230 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.140670357955037,2.04602671615662,-2.52259688656261)
cB = chrono.ChVector3d(-0.382669423498731,2.04602671615662,-2.52259688656261)
dA = chrono.ChVector3d(-1.32297045065857e-16,-1,1.10849259381635e-17)
dB = chrono.ChVector3d(0,1,0)
link_230.Initialize(body_40,body_43,False,cA,cB,dB)
link_230.SetDistance(0)
link_230.SetName("Coincident18")
exported_items.append(link_230)

link_231 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.140670357955037,2.04602671615662,-2.52259688656261)
dA = chrono.ChVector3d(-1.32297045065857e-16,-1,1.10849259381635e-17)
cB = chrono.ChVector3d(-0.382669423498731,2.04602671615662,-2.52259688656261)
dB = chrono.ChVector3d(0,1,0)
link_231.SetFlipped(True)
link_231.Initialize(body_40,body_43,False,cA,cB,dA,dB)
link_231.SetName("Coincident18")
exported_items.append(link_231)


# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_40 , SW name: M-410iB-300 -3/M-410iB-300-02-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_43 , SW name: M-410iB-300 -3/ArmBase-1 ,  SW ref.type:1 (1)
link_232 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.140670357955037,2.04755071615662,-2.52259688656261)
dA = chrono.ChVector3d(1.32297045065857e-16,1,-1.10849259381635e-17)
cB = chrono.ChVector3d(-0.140670357955037,2.04602671615662,-2.52259688656261)
dB = chrono.ChVector3d(0,1,0)
link_232.Initialize(body_40,body_43,False,cA,cB,dA,dB)
link_232.SetName("Concentric1")
exported_items.append(link_232)

link_233 = chrono.ChLinkMateGeneric()
link_233.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-0.140670357955037,2.04755071615662,-2.52259688656261)
cB = chrono.ChVector3d(-0.140670357955037,2.04602671615662,-2.52259688656261)
dA = chrono.ChVector3d(1.32297045065857e-16,1,-1.10849259381635e-17)
dB = chrono.ChVector3d(0,1,0)
link_233.Initialize(body_40,body_43,False,cA,cB,dA,dB)
link_233.SetName("Concentric1")
exported_items.append(link_233)


# Mate constraint: Coincident2_hinge [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_54 , SW name: M-410iB-300 -8/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_55 , SW name: M-410iB-300 -8/M-410iB-300-03-1 ,  SW ref.type:5 (5)
link_234 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.87878138328858,2.51550127212935,-0.912867956076195)
dA = chrono.ChVector3d(0.0824751241424789,3.69143694860712e-15,0.996593123545253)
cB = chrono.ChVector3d(-1.89800452027346,2.51550127212935,-1.14515188812587)
dB = chrono.ChVector3d(0.082475124142479,3.78275429706264e-15,0.996593123545253)
link_234.Initialize(body_54,body_55,False,cA,cB,dA,dB)
link_234.SetName("Coincident2_hinge")
exported_items.append(link_234)

link_235 = chrono.ChLinkMateGeneric()
link_235.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.87878138328858,2.51550127212935,-0.912867956076195)
cB = chrono.ChVector3d(-1.89800452027346,2.51550127212935,-1.14515188812587)
dA = chrono.ChVector3d(0.0824751241424789,3.69143694860712e-15,0.996593123545253)
dB = chrono.ChVector3d(0.082475124142479,3.78275429706264e-15,0.996593123545253)
link_235.Initialize(body_54,body_55,False,cA,cB,dA,dB)
link_235.SetName("Coincident2_hinge")
exported_items.append(link_235)


# Mate constraint: Distance2 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_54 , SW name: M-410iB-300 -8/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_55 , SW name: M-410iB-300 -8/M-410iB-300-03-1 ,  SW ref.type:2 (2)
link_236 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-2.11018861732807,2.84164228947283,-1.13855149164487)
cB = chrono.ChVector3d(-2.73620448423209,2.54318522667954,-1.08368583479229)
dA = chrono.ChVector3d(0.0824751241424789,3.69143694860712e-15,0.996593123545253)
dB = chrono.ChVector3d(-0.082475124142479,-3.78275429706264e-15,-0.996593123545253)
link_236.Initialize(body_54,body_55,False,cA,cB,dB)
link_236.SetDistance(0)
link_236.SetName("Distance2")
exported_items.append(link_236)

link_237 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.11018861732807,2.84164228947283,-1.13855149164487)
dA = chrono.ChVector3d(0.0824751241424789,3.69143694860712e-15,0.996593123545253)
cB = chrono.ChVector3d(-2.73620448423209,2.54318522667954,-1.08368583479229)
dB = chrono.ChVector3d(-0.082475124142479,-3.78275429706264e-15,-0.996593123545253)
link_237.SetFlipped(True)
link_237.Initialize(body_54,body_55,False,cA,cB,dA,dB)
link_237.SetName("Distance2")
exported_items.append(link_237)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_54 , SW name: M-410iB-300 -8/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_53 , SW name: M-410iB-300 -8/M-410iB-300-04-1 ,  SW ref.type:5 (5)
link_238 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.90232652265115,2.78049690546384,-1.19733471087338)
dA = chrono.ChVector3d(-0.0824751241424789,-3.69143694860712e-15,-0.996593123545253)
cB = chrono.ChVector3d(-1.90809982310579,2.78049690546384,-1.26709673418738)
dB = chrono.ChVector3d(-0.0824751241424784,-3.75348083840554e-15,-0.996593123545253)
link_238.Initialize(body_54,body_53,False,cA,cB,dA,dB)
link_238.SetName("Coincident3")
exported_items.append(link_238)

link_239 = chrono.ChLinkMateGeneric()
link_239.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.90232652265115,2.78049690546384,-1.19733471087338)
cB = chrono.ChVector3d(-1.90809982310579,2.78049690546384,-1.26709673418738)
dA = chrono.ChVector3d(-0.0824751241424789,-3.69143694860712e-15,-0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424784,-3.75348083840554e-15,-0.996593123545253)
link_239.Initialize(body_54,body_53,False,cA,cB,dA,dB)
link_239.SetName("Coincident3")
exported_items.append(link_239)


# Mate constraint: Distance3 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_54 , SW name: M-410iB-300 -8/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_53 , SW name: M-410iB-300 -8/M-410iB-300-04-1 ,  SW ref.type:2 (2)
link_240 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.90600495189008,2.78049691677857,-1.24178326910278)
cB = chrono.ChVector3d(-1.97739420838105,2.80967719196081,-1.26136213408536)
dA = chrono.ChVector3d(-0.0824751241424789,-3.69143694860712e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424784,3.75348083840554e-15,0.996593123545253)
link_240.Initialize(body_54,body_53,False,cA,cB,dB)
link_240.SetDistance(0)
link_240.SetName("Distance3")
exported_items.append(link_240)

link_241 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.90600495189008,2.78049691677857,-1.24178326910278)
dA = chrono.ChVector3d(-0.0824751241424789,-3.69143694860712e-15,-0.996593123545253)
cB = chrono.ChVector3d(-1.97739420838105,2.80967719196081,-1.26136213408536)
dB = chrono.ChVector3d(0.0824751241424784,3.75348083840554e-15,0.996593123545253)
link_241.SetFlipped(True)
link_241.Initialize(body_54,body_53,False,cA,cB,dA,dB)
link_241.SetName("Distance3")
exported_items.append(link_241)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_53 , SW name: M-410iB-300 -8/M-410iB-300-04-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_57 , SW name: M-410iB-300 -8/M-410iB-300-05-1 ,  SW ref.type:5 (5)
link_242 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.71143288244173,2.7654491237564,-1.2291604963153)
dA = chrono.ChVector3d(0.996418499736232,0.018719263519677,-0.0824606727881727)
cB = chrono.ChVector3d(-3.00015381681405,2.76002505419567,-1.20526679853402)
dB = chrono.ChVector3d(0.996418499736232,0.0187192635196771,-0.0824606727881728)
link_242.Initialize(body_53,body_57,False,cA,cB,dA,dB)
link_242.SetName("Coincident4")
exported_items.append(link_242)

link_243 = chrono.ChLinkMateGeneric()
link_243.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-2.71143288244173,2.7654491237564,-1.2291604963153)
cB = chrono.ChVector3d(-3.00015381681405,2.76002505419567,-1.20526679853402)
dA = chrono.ChVector3d(0.996418499736232,0.018719263519677,-0.0824606727881727)
dB = chrono.ChVector3d(0.996418499736232,0.0187192635196771,-0.0824606727881728)
link_243.Initialize(body_53,body_57,False,cA,cB,dA,dB)
link_243.SetName("Coincident4")
exported_items.append(link_243)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_55 , SW name: M-410iB-300 -8/M-410iB-300-03-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_57 , SW name: M-410iB-300 -8/M-410iB-300-05-1 ,  SW ref.type:5 (5)
link_244 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.08956446048186,2.75811166841885,-1.04654188202599)
dA = chrono.ChVector3d(0.082475124142479,3.78275429706264e-15,0.996593123545253)
cB = chrono.ChVector3d(-3.0991159051399,2.75811166841886,-1.16195733808127)
dB = chrono.ChVector3d(0.0824751241424785,3.50964376981355e-15,0.996593123545253)
link_244.Initialize(body_55,body_57,False,cA,cB,dA,dB)
link_244.SetName("Coincident5")
exported_items.append(link_244)

link_245 = chrono.ChLinkMateGeneric()
link_245.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.08956446048186,2.75811166841885,-1.04654188202599)
cB = chrono.ChVector3d(-3.0991159051399,2.75811166841886,-1.16195733808127)
dA = chrono.ChVector3d(0.082475124142479,3.78275429706264e-15,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424785,3.50964376981355e-15,0.996593123545253)
link_245.Initialize(body_55,body_57,False,cA,cB,dA,dB)
link_245.SetName("Coincident5")
exported_items.append(link_245)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_55 , SW name: M-410iB-300 -8/M-410iB-300-03-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_50 , SW name: M-410iB-300 -8/M-410iB-300-06-1 ,  SW ref.type:5 (5)
link_246 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.06708905223563,2.75811166841886,-0.774958934562062)
dA = chrono.ChVector3d(0.082475124142479,3.78275429706264e-15,0.996593123545253)
cB = chrono.ChVector3d(-3.06970763742716,2.75811166841885,-0.806600766234624)
dB = chrono.ChVector3d(-0.0824751241424783,-4.67746503485199e-15,-0.996593123545253)
link_246.SetFlipped(True)
link_246.Initialize(body_55,body_50,False,cA,cB,dA,dB)
link_246.SetName("Coincident6")
exported_items.append(link_246)

link_247 = chrono.ChLinkMateGeneric()
link_247.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.06708905223563,2.75811166841886,-0.774958934562062)
cB = chrono.ChVector3d(-3.06970763742716,2.75811166841885,-0.806600766234624)
dA = chrono.ChVector3d(0.082475124142479,3.78275429706264e-15,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424783,-4.67746503485199e-15,-0.996593123545253)
link_247.Initialize(body_55,body_50,False,cA,cB,dA,dB)
link_247.SetName("Coincident6")
exported_items.append(link_247)


# Mate constraint: Distance4 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_55 , SW name: M-410iB-300 -8/M-410iB-300-03-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_50 , SW name: M-410iB-300 -8/M-410iB-300-06-1 ,  SW ref.type:2 (2)
link_248 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-2.88223000352087,2.91434507456168,-0.790257327287646)
cB = chrono.ChVector3d(-2.96321003072953,2.58269164685798,-0.815414195833673)
dA = chrono.ChVector3d(-0.082475124142479,-3.78275429706264e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424783,4.67746503485199e-15,0.996593123545253)
link_248.Initialize(body_55,body_50,False,cA,cB,dB)
link_248.SetDistance(0)
link_248.SetName("Distance4")
exported_items.append(link_248)

link_249 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.88223000352087,2.91434507456168,-0.790257327287646)
dA = chrono.ChVector3d(-0.082475124142479,-3.78275429706264e-15,-0.996593123545253)
cB = chrono.ChVector3d(-2.96321003072953,2.58269164685798,-0.815414195833673)
dB = chrono.ChVector3d(0.0824751241424783,4.67746503485199e-15,0.996593123545253)
link_249.SetFlipped(True)
link_249.Initialize(body_55,body_50,False,cA,cB,dA,dB)
link_249.SetName("Distance4")
exported_items.append(link_249)


# Mate constraint: Coincident7 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_54 , SW name: M-410iB-300 -8/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_51 , SW name: M-410iB-300 -8/M-410iB-300-07-1 ,  SW ref.type:5 (5)
link_250 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.90558579863488,2.51550127212935,-1.23676072122839)
dA = chrono.ChVector3d(0.0824751241424789,3.69143694860712e-15,0.996593123545253)
cB = chrono.ChVector3d(-1.88095452717193,2.51550127212935,-0.93912727090773)
dB = chrono.ChVector3d(-0.0824751241424795,-3.58187873955539e-15,-0.996593123545253)
link_250.SetFlipped(True)
link_250.Initialize(body_54,body_51,False,cA,cB,dA,dB)
link_250.SetName("Coincident7")
exported_items.append(link_250)

link_251 = chrono.ChLinkMateGeneric()
link_251.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.90558579863488,2.51550127212935,-1.23676072122839)
cB = chrono.ChVector3d(-1.88095452717193,2.51550127212935,-0.93912727090773)
dA = chrono.ChVector3d(0.0824751241424789,3.69143694860712e-15,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424795,-3.58187873955539e-15,-0.996593123545253)
link_251.Initialize(body_54,body_51,False,cA,cB,dA,dB)
link_251.SetName("Coincident7")
exported_items.append(link_251)


# Mate constraint: Coincident8 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_50 , SW name: M-410iB-300 -8/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_51 , SW name: M-410iB-300 -8/M-410iB-300-07-1 ,  SW ref.type:2 (2)
link_252 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-2.60711943253569,3.10515332885273,-0.955259246937602)
cB = chrono.ChVector3d(-1.56768836286924,3.00995602354016,-1.04127951386792)
dA = chrono.ChVector3d(0.0824751241424783,4.67746503485199e-15,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424795,3.58187873955539e-15,0.996593123545253)
link_252.Initialize(body_50,body_51,False,cA,cB,dB)
link_252.SetDistance(0)
link_252.SetName("Coincident8")
exported_items.append(link_252)

link_253 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.60711943253569,3.10515332885273,-0.955259246937602)
dA = chrono.ChVector3d(0.0824751241424783,4.67746503485199e-15,0.996593123545253)
cB = chrono.ChVector3d(-1.56768836286924,3.00995602354016,-1.04127951386792)
dB = chrono.ChVector3d(0.0824751241424795,3.58187873955539e-15,0.996593123545253)
link_253.Initialize(body_50,body_51,False,cA,cB,dA,dB)
link_253.SetName("Coincident8")
exported_items.append(link_253)


# Mate constraint: Distance5 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_50 , SW name: M-410iB-300 -8/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_58 , SW name: M-410iB-300 -8/M-410iB-300-08-1 ,  SW ref.type:2 (2)
link_254 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-2.60711943253569,3.10515332885273,-0.955259246937602)
cB = chrono.ChVector3d(-1.57268463047198,3.01604196029193,-1.01869249489401)
dA = chrono.ChVector3d(0.0824751241424783,4.67746503485199e-15,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424791,-4.0626952979984e-15,-0.996593123545253)
link_254.Initialize(body_50,body_58,False,cA,cB,dB)
link_254.SetDistance(0)
link_254.SetName("Distance5")
exported_items.append(link_254)

link_255 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.60711943253569,3.10515332885273,-0.955259246937602)
dA = chrono.ChVector3d(0.0824751241424783,4.67746503485199e-15,0.996593123545253)
cB = chrono.ChVector3d(-1.57268463047198,3.01604196029193,-1.01869249489401)
dB = chrono.ChVector3d(-0.0824751241424791,-4.0626952979984e-15,-0.996593123545253)
link_255.SetFlipped(True)
link_255.Initialize(body_50,body_58,False,cA,cB,dA,dB)
link_255.SetName("Distance5")
exported_items.append(link_255)


# Mate constraint: Coincident9 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_50 , SW name: M-410iB-300 -8/M-410iB-300-06-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_58 , SW name: M-410iB-300 -8/M-410iB-300-08-1 ,  SW ref.type:5 (5)
link_256 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.76251640195877,3.2550226500217,-0.942399049489179)
dA = chrono.ChVector3d(0.0824751241424783,4.67746503485199e-15,0.996593123545253)
cB = chrono.ChVector3d(-2.76029584171634,3.25502265002172,-0.915566776230844)
dB = chrono.ChVector3d(0.0824751241424791,4.0626952979984e-15,0.996593123545253)
link_256.Initialize(body_50,body_58,False,cA,cB,dA,dB)
link_256.SetName("Coincident9")
exported_items.append(link_256)

link_257 = chrono.ChLinkMateGeneric()
link_257.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-2.76251640195877,3.2550226500217,-0.942399049489179)
cB = chrono.ChVector3d(-2.76029584171634,3.25502265002172,-0.915566776230844)
dA = chrono.ChVector3d(0.0824751241424783,4.67746503485199e-15,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424791,4.0626952979984e-15,0.996593123545253)
link_257.Initialize(body_50,body_58,False,cA,cB,dA,dB)
link_257.SetName("Coincident9")
exported_items.append(link_257)


# Mate constraint: Coincident10 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_59 , SW name: M-410iB-300 -8/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_50 , SW name: M-410iB-300 -8/M-410iB-300-06-1 ,  SW ref.type:5 (5)
link_258 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.0562002936794,2.75811166841883,-0.643383965576742)
dA = chrono.ChVector3d(-0.0824751241424788,-3.69944691263429e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.06207868844398,2.75811166841885,-0.714415902306689)
dB = chrono.ChVector3d(-0.0824751241424783,-4.67746503485199e-15,-0.996593123545253)
link_258.Initialize(body_59,body_50,False,cA,cB,dA,dB)
link_258.SetName("Coincident10")
exported_items.append(link_258)

link_259 = chrono.ChLinkMateGeneric()
link_259.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.0562002936794,2.75811166841883,-0.643383965576742)
cB = chrono.ChVector3d(-3.06207868844398,2.75811166841885,-0.714415902306689)
dA = chrono.ChVector3d(-0.0824751241424788,-3.69944691263429e-15,-0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424783,-4.67746503485199e-15,-0.996593123545253)
link_259.Initialize(body_59,body_50,False,cA,cB,dA,dB)
link_259.SetName("Coincident10")
exported_items.append(link_259)


# Mate constraint: Coincident11 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_54 , SW name: M-410iB-300 -8/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_59 , SW name: M-410iB-300 -8/M-410iB-300-09-1 ,  SW ref.type:2 (2)
link_260 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.5131859877973,2.72491052060182,-0.777451011871367)
cB = chrono.ChVector3d(-3.05641325164642,3.21365467148159,-0.649738049420615)
dA = chrono.ChVector3d(0.0824751241424789,3.69143694860712e-15,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424788,3.69944691263429e-15,0.996593123545253)
link_260.Initialize(body_54,body_59,False,cA,cB,dB)
link_260.SetDistance(0)
link_260.SetName("Coincident11")
exported_items.append(link_260)

link_261 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.5131859877973,2.72491052060182,-0.777451011871367)
dA = chrono.ChVector3d(0.0824751241424789,3.69143694860712e-15,0.996593123545253)
cB = chrono.ChVector3d(-3.05641325164642,3.21365467148159,-0.649738049420615)
dB = chrono.ChVector3d(0.0824751241424788,3.69944691263429e-15,0.996593123545253)
link_261.Initialize(body_54,body_59,False,cA,cB,dA,dB)
link_261.SetName("Coincident11")
exported_items.append(link_261)


# Mate constraint: Coincident12 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_59 , SW name: M-410iB-300 -8/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_61 , SW name: M-410iB-300 -8/M-410iB-300-10-1 ,  SW ref.type:5 (5)
link_262 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.55781544031629,3.03081076163703,-0.697372249642411)
dA = chrono.ChVector3d(-0.0824751241424788,-3.69944691263429e-15,-0.996593123545253)
cB = chrono.ChVector3d(-2.55308103828999,3.03081076163705,-0.640163817978419)
dB = chrono.ChVector3d(-0.0824751241424782,-4.07668150602346e-15,-0.996593123545253)
link_262.Initialize(body_59,body_61,False,cA,cB,dA,dB)
link_262.SetName("Coincident12")
exported_items.append(link_262)

link_263 = chrono.ChLinkMateGeneric()
link_263.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-2.55781544031629,3.03081076163703,-0.697372249642411)
cB = chrono.ChVector3d(-2.55308103828999,3.03081076163705,-0.640163817978419)
dA = chrono.ChVector3d(-0.0824751241424788,-3.69944691263429e-15,-0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424782,-4.07668150602346e-15,-0.996593123545253)
link_263.Initialize(body_59,body_61,False,cA,cB,dA,dB)
link_263.SetName("Coincident12")
exported_items.append(link_263)


# Mate constraint: Distance7 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_59 , SW name: M-410iB-300 -8/M-410iB-300-09-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_61 , SW name: M-410iB-300 -8/M-410iB-300-10-1 ,  SW ref.type:2 (2)
link_264 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-3.05641325164642,3.21365467148159,-0.649738049420615)
cB = chrono.ChVector3d(-2.55704033909957,3.03081076163705,-0.688006267467332)
dA = chrono.ChVector3d(0.0824751241424788,3.69944691263429e-15,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424782,-4.07668150602346e-15,-0.996593123545253)
link_264.Initialize(body_59,body_61,False,cA,cB,dB)
link_264.SetDistance(0)
link_264.SetName("Distance7")
exported_items.append(link_264)

link_265 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.05641325164642,3.21365467148159,-0.649738049420615)
dA = chrono.ChVector3d(0.0824751241424788,3.69944691263429e-15,0.996593123545253)
cB = chrono.ChVector3d(-2.55704033909957,3.03081076163705,-0.688006267467332)
dB = chrono.ChVector3d(-0.0824751241424782,-4.07668150602346e-15,-0.996593123545253)
link_265.SetFlipped(True)
link_265.Initialize(body_59,body_61,False,cA,cB,dA,dB)
link_265.SetName("Distance7")
exported_items.append(link_265)


# Mate constraint: Coincident13 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_54 , SW name: M-410iB-300 -8/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_61 , SW name: M-410iB-300 -8/M-410iB-300-10-1 ,  SW ref.type:5 (5)
link_266 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.36587439836585,2.78749692402101,-0.789642086984112)
dA = chrono.ChVector3d(-0.0824751241424789,-3.69143694860712e-15,-0.996593123545253)
cB = chrono.ChVector3d(-1.36562301418745,2.78749692402101,-0.786604471143542)
dB = chrono.ChVector3d(0.0824751241424782,4.07668150602346e-15,0.996593123545253)
link_266.SetFlipped(True)
link_266.Initialize(body_54,body_61,False,cA,cB,dA,dB)
link_266.SetName("Coincident13")
exported_items.append(link_266)

link_267 = chrono.ChLinkMateGeneric()
link_267.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.36587439836585,2.78749692402101,-0.789642086984112)
cB = chrono.ChVector3d(-1.36562301418745,2.78749692402101,-0.786604471143542)
dA = chrono.ChVector3d(-0.0824751241424789,-3.69143694860712e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424782,4.07668150602346e-15,0.996593123545253)
link_267.Initialize(body_54,body_61,False,cA,cB,dA,dB)
link_267.SetName("Coincident13")
exported_items.append(link_267)


# Mate constraint: Coincident14 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_59 , SW name: M-410iB-300 -8/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_60 , SW name: M-410iB-300 -8/M-410iB-300-11-1 ,  SW ref.type:5 (5)
link_268 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.55579644633207,3.02764258400498,-0.614782268416989)
dA = chrono.ChVector3d(-0.0824751241424788,-3.69944691263429e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.56428066235258,3.02764258400502,-0.717301803036087)
dB = chrono.ChVector3d(0.0824751241424784,4.89894043363647e-15,0.996593123545253)
link_268.SetFlipped(True)
link_268.Initialize(body_59,body_60,False,cA,cB,dA,dB)
link_268.SetName("Coincident14")
exported_items.append(link_268)

link_269 = chrono.ChLinkMateGeneric()
link_269.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.55579644633207,3.02764258400498,-0.614782268416989)
cB = chrono.ChVector3d(-3.56428066235258,3.02764258400502,-0.717301803036087)
dA = chrono.ChVector3d(-0.0824751241424788,-3.69944691263429e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424784,4.89894043363647e-15,0.996593123545253)
link_269.Initialize(body_59,body_60,False,cA,cB,dA,dB)
link_269.SetName("Coincident14")
exported_items.append(link_269)


# Mate constraint: Distance8 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_59 , SW name: M-410iB-300 -8/M-410iB-300-09-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_60 , SW name: M-410iB-300 -8/M-410iB-300-11-1 ,  SW ref.type:2 (2)
link_270 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-3.060372552456,3.21365467148159,-0.697580498909529)
cB = chrono.ChVector3d(-3.55910633801413,3.02764258400502,-0.654777543651105)
dA = chrono.ChVector3d(-0.0824751241424788,-3.69944691263429e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424785,4.89894043363647e-15,0.996593123545253)
link_270.Initialize(body_59,body_60,False,cA,cB,dB)
link_270.SetDistance(0)
link_270.SetName("Distance8")
exported_items.append(link_270)

link_271 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.060372552456,3.21365467148159,-0.697580498909529)
dA = chrono.ChVector3d(-0.0824751241424788,-3.69944691263429e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.55910633801413,3.02764258400502,-0.654777543651105)
dB = chrono.ChVector3d(0.0824751241424785,4.89894043363647e-15,0.996593123545253)
link_271.SetFlipped(True)
link_271.Initialize(body_59,body_60,False,cA,cB,dA,dB)
link_271.SetName("Distance8")
exported_items.append(link_271)


# Mate constraint: Coincident15 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_50 , SW name: M-410iB-300 -8/M-410iB-300-06-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_52 , SW name: M-410iB-300 -8/M-410iB-300-12-1 ,  SW ref.type:5 (5)
link_272 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.81525551082145,1.6937690405165,-0.764969781263139)
dA = chrono.ChVector3d(-0.0824751241424783,-4.67746503485199e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.81422770582439,1.69376904051648,-0.752550237757517)
dB = chrono.ChVector3d(0.0824751241424788,4.66616625061033e-15,0.996593123545253)
link_272.SetFlipped(True)
link_272.Initialize(body_50,body_52,False,cA,cB,dA,dB)
link_272.SetName("Coincident15")
exported_items.append(link_272)

link_273 = chrono.ChLinkMateGeneric()
link_273.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.81525551082145,1.6937690405165,-0.764969781263139)
cB = chrono.ChVector3d(-3.81422770582439,1.69376904051648,-0.752550237757517)
dA = chrono.ChVector3d(-0.0824751241424783,-4.67746503485199e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424788,4.66616625061033e-15,0.996593123545253)
link_273.Initialize(body_50,body_52,False,cA,cB,dA,dB)
link_273.SetName("Coincident15")
exported_items.append(link_273)


# Mate constraint: Distance9 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_50 , SW name: M-410iB-300 -8/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_52 , SW name: M-410iB-300 -8/M-410iB-300-12-1 ,  SW ref.type:2 (2)
link_274 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-3.18827765327686,2.27955349819168,-0.957335223193536)
cB = chrono.ChVector3d(-3.82784946227801,1.69376904051648,-0.917149551228496)
dA = chrono.ChVector3d(-0.0824751241424783,-4.67746503485199e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424788,4.66616625061033e-15,0.996593123545253)
link_274.Initialize(body_50,body_52,False,cA,cB,dB)
link_274.SetDistance(0)
link_274.SetName("Distance9")
exported_items.append(link_274)

link_275 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.18827765327686,2.27955349819168,-0.957335223193536)
dA = chrono.ChVector3d(-0.0824751241424783,-4.67746503485199e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.82784946227801,1.69376904051648,-0.917149551228496)
dB = chrono.ChVector3d(0.0824751241424788,4.66616625061033e-15,0.996593123545253)
link_275.SetFlipped(True)
link_275.Initialize(body_50,body_52,False,cA,cB,dA,dB)
link_275.SetName("Distance9")
exported_items.append(link_275)


# Mate constraint: Coincident16 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_60 , SW name: M-410iB-300 -8/M-410iB-300-11-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_52 , SW name: M-410iB-300 -8/M-410iB-300-12-1 ,  SW ref.type:5 (5)
link_276 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-4.30817905100364,1.96329996858996,-0.65573895406204)
dA = chrono.ChVector3d(0.0824751241424784,4.89894043363647e-15,0.996593123545253)
cB = chrono.ChVector3d(-4.31277644214529,1.96329996858993,-0.711291806460229)
dB = chrono.ChVector3d(0.0824751241424788,4.66616625061033e-15,0.996593123545253)
link_276.Initialize(body_60,body_52,False,cA,cB,dA,dB)
link_276.SetName("Coincident16")
exported_items.append(link_276)

link_277 = chrono.ChLinkMateGeneric()
link_277.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-4.30817905100364,1.96329996858996,-0.65573895406204)
cB = chrono.ChVector3d(-4.31277644214529,1.96329996858993,-0.711291806460229)
dA = chrono.ChVector3d(0.0824751241424784,4.89894043363647e-15,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424788,4.66616625061033e-15,0.996593123545253)
link_277.Initialize(body_60,body_52,False,cA,cB,dA,dB)
link_277.SetName("Coincident16")
exported_items.append(link_277)


# Mate constraint: Coincident17 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_51 , SW name: M-410iB-300 -8/M-410iB-300-07-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_58 , SW name: M-410iB-300 -8/M-410iB-300-08-1 ,  SW ref.type:5 (5)
link_278 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.56037999469361,3.00995602354016,-0.952968407411209)
dA = chrono.ChVector3d(-0.0824751241424795,-3.58187873955539e-15,-0.996593123545253)
cB = chrono.ChVector3d(-1.56546780262682,3.00995602354016,-1.01444724060959)
dB = chrono.ChVector3d(0.0824751241424791,4.0626952979984e-15,0.996593123545253)
link_278.SetFlipped(True)
link_278.Initialize(body_51,body_58,False,cA,cB,dA,dB)
link_278.SetName("Coincident17")
exported_items.append(link_278)

link_279 = chrono.ChLinkMateGeneric()
link_279.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.56037999469361,3.00995602354016,-0.952968407411209)
cB = chrono.ChVector3d(-1.56546780262682,3.00995602354016,-1.01444724060959)
dA = chrono.ChVector3d(-0.0824751241424795,-3.58187873955539e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424791,4.0626952979984e-15,0.996593123545253)
link_279.Initialize(body_51,body_58,False,cA,cB,dA,dB)
link_279.SetName("Coincident17")
exported_items.append(link_279)


# Mate constraint: Coincident18 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_54 , SW name: M-410iB-300 -8/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_56 , SW name: M-410iB-300 -8/ArmBase-1 ,  SW ref.type:2 (2)
link_280 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.50067035795504,2.04602671615662,-1.07259688656262)
cB = chrono.ChVector3d(-1.25867129241134,2.04602671615662,-1.07259688656262)
dA = chrono.ChVector3d(7.80834317735457e-17,-1,3.50745309797879e-15)
dB = chrono.ChVector3d(5.42136132923115e-17,1,-3.51853802391695e-15)
link_280.Initialize(body_54,body_56,False,cA,cB,dB)
link_280.SetDistance(0)
link_280.SetName("Coincident18")
exported_items.append(link_280)

link_281 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.50067035795504,2.04602671615662,-1.07259688656262)
dA = chrono.ChVector3d(7.80834317735457e-17,-1,3.50745309797879e-15)
cB = chrono.ChVector3d(-1.25867129241134,2.04602671615662,-1.07259688656262)
dB = chrono.ChVector3d(5.42136132923115e-17,1,-3.51853802391695e-15)
link_281.SetFlipped(True)
link_281.Initialize(body_54,body_56,False,cA,cB,dA,dB)
link_281.SetName("Coincident18")
exported_items.append(link_281)


# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_54 , SW name: M-410iB-300 -8/M-410iB-300-02-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_56 , SW name: M-410iB-300 -8/ArmBase-1 ,  SW ref.type:1 (1)
link_282 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.50067035795504,2.04755071615662,-1.07259688656262)
dA = chrono.ChVector3d(-7.80834317735457e-17,1,-3.50745309797879e-15)
cB = chrono.ChVector3d(-1.50067035795504,2.04602671615662,-1.07259688656262)
dB = chrono.ChVector3d(5.42136132923115e-17,1,-3.51853802391695e-15)
link_282.Initialize(body_54,body_56,False,cA,cB,dA,dB)
link_282.SetName("Concentric1")
exported_items.append(link_282)

link_283 = chrono.ChLinkMateGeneric()
link_283.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.50067035795504,2.04755071615662,-1.07259688656262)
cB = chrono.ChVector3d(-1.50067035795504,2.04602671615662,-1.07259688656262)
dA = chrono.ChVector3d(-7.80834317735457e-17,1,-3.50745309797879e-15)
dB = chrono.ChVector3d(5.42136132923115e-17,1,-3.51853802391695e-15)
link_283.Initialize(body_54,body_56,False,cA,cB,dA,dB)
link_283.SetName("Concentric1")
exported_items.append(link_283)


# Mate constraint: Coincident2_hinge [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_67 , SW name: M-410iB-300 -7/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_62 , SW name: M-410iB-300 -7/M-410iB-300-03-1 ,  SW ref.type:5 (5)
link_284 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.87878138328858,2.51550127212934,-2.36286795607619)
dA = chrono.ChVector3d(0.0824751241424789,3.43512560843663e-15,0.996593123545252)
cB = chrono.ChVector3d(-1.89800452027346,2.51550127212934,-2.59515188812587)
dB = chrono.ChVector3d(0.082475124142479,3.52644295689215e-15,0.996593123545252)
link_284.Initialize(body_67,body_62,False,cA,cB,dA,dB)
link_284.SetName("Coincident2_hinge")
exported_items.append(link_284)

link_285 = chrono.ChLinkMateGeneric()
link_285.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.87878138328858,2.51550127212934,-2.36286795607619)
cB = chrono.ChVector3d(-1.89800452027346,2.51550127212934,-2.59515188812587)
dA = chrono.ChVector3d(0.0824751241424789,3.43512560843663e-15,0.996593123545252)
dB = chrono.ChVector3d(0.082475124142479,3.52644295689215e-15,0.996593123545252)
link_285.Initialize(body_67,body_62,False,cA,cB,dA,dB)
link_285.SetName("Coincident2_hinge")
exported_items.append(link_285)


# Mate constraint: Distance2 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_67 , SW name: M-410iB-300 -7/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_62 , SW name: M-410iB-300 -7/M-410iB-300-03-1 ,  SW ref.type:2 (2)
link_286 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-2.11018861732807,2.84164228947283,-2.58855149164487)
cB = chrono.ChVector3d(-2.73620448423209,2.54318522667953,-2.53368583479229)
dA = chrono.ChVector3d(0.0824751241424789,3.43512560843663e-15,0.996593123545252)
dB = chrono.ChVector3d(-0.082475124142479,-3.52644295689215e-15,-0.996593123545252)
link_286.Initialize(body_67,body_62,False,cA,cB,dB)
link_286.SetDistance(0)
link_286.SetName("Distance2")
exported_items.append(link_286)

link_287 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.11018861732807,2.84164228947283,-2.58855149164487)
dA = chrono.ChVector3d(0.0824751241424789,3.43512560843663e-15,0.996593123545252)
cB = chrono.ChVector3d(-2.73620448423209,2.54318522667953,-2.53368583479229)
dB = chrono.ChVector3d(-0.082475124142479,-3.52644295689215e-15,-0.996593123545252)
link_287.SetFlipped(True)
link_287.Initialize(body_67,body_62,False,cA,cB,dA,dB)
link_287.SetName("Distance2")
exported_items.append(link_287)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_67 , SW name: M-410iB-300 -7/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_71 , SW name: M-410iB-300 -7/M-410iB-300-04-1 ,  SW ref.type:5 (5)
link_288 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.90232652265115,2.78049690546383,-2.64733471087338)
dA = chrono.ChVector3d(-0.0824751241424789,-3.43512560843663e-15,-0.996593123545252)
cB = chrono.ChVector3d(-1.90809982310579,2.78049690546383,-2.71709673418738)
dB = chrono.ChVector3d(-0.0824751241424785,-3.49716949823504e-15,-0.996593123545253)
link_288.Initialize(body_67,body_71,False,cA,cB,dA,dB)
link_288.SetName("Coincident3")
exported_items.append(link_288)

link_289 = chrono.ChLinkMateGeneric()
link_289.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.90232652265115,2.78049690546383,-2.64733471087338)
cB = chrono.ChVector3d(-1.90809982310579,2.78049690546383,-2.71709673418738)
dA = chrono.ChVector3d(-0.0824751241424789,-3.43512560843663e-15,-0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424785,-3.49716949823504e-15,-0.996593123545253)
link_289.Initialize(body_67,body_71,False,cA,cB,dA,dB)
link_289.SetName("Coincident3")
exported_items.append(link_289)


# Mate constraint: Distance3 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_67 , SW name: M-410iB-300 -7/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_71 , SW name: M-410iB-300 -7/M-410iB-300-04-1 ,  SW ref.type:2 (2)
link_290 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.90600495189008,2.78049691677856,-2.69178326910278)
cB = chrono.ChVector3d(-1.97739420838105,2.80967719196081,-2.71136213408536)
dA = chrono.ChVector3d(-0.0824751241424789,-3.43512560843663e-15,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424785,3.49716949823504e-15,0.996593123545253)
link_290.Initialize(body_67,body_71,False,cA,cB,dB)
link_290.SetDistance(0)
link_290.SetName("Distance3")
exported_items.append(link_290)

link_291 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.90600495189008,2.78049691677856,-2.69178326910278)
dA = chrono.ChVector3d(-0.0824751241424789,-3.43512560843663e-15,-0.996593123545252)
cB = chrono.ChVector3d(-1.97739420838105,2.80967719196081,-2.71136213408536)
dB = chrono.ChVector3d(0.0824751241424785,3.49716949823504e-15,0.996593123545253)
link_291.SetFlipped(True)
link_291.Initialize(body_67,body_71,False,cA,cB,dA,dB)
link_291.SetName("Distance3")
exported_items.append(link_291)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_71 , SW name: M-410iB-300 -7/M-410iB-300-04-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_66 , SW name: M-410iB-300 -7/M-410iB-300-05-1 ,  SW ref.type:5 (5)
link_292 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.71143288244173,2.76544912375639,-2.6791604963153)
dA = chrono.ChVector3d(0.996418499736232,0.0187192635196771,-0.0824606727881726)
cB = chrono.ChVector3d(-3.00015381681405,2.76002505419567,-2.65526679853402)
dB = chrono.ChVector3d(0.996418499736232,0.0187192635196772,-0.0824606727881727)
link_292.Initialize(body_71,body_66,False,cA,cB,dA,dB)
link_292.SetName("Coincident4")
exported_items.append(link_292)

link_293 = chrono.ChLinkMateGeneric()
link_293.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-2.71143288244173,2.76544912375639,-2.6791604963153)
cB = chrono.ChVector3d(-3.00015381681405,2.76002505419567,-2.65526679853402)
dA = chrono.ChVector3d(0.996418499736232,0.0187192635196771,-0.0824606727881726)
dB = chrono.ChVector3d(0.996418499736232,0.0187192635196772,-0.0824606727881727)
link_293.Initialize(body_71,body_66,False,cA,cB,dA,dB)
link_293.SetName("Coincident4")
exported_items.append(link_293)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_62 , SW name: M-410iB-300 -7/M-410iB-300-03-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_66 , SW name: M-410iB-300 -7/M-410iB-300-05-1 ,  SW ref.type:5 (5)
link_294 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.08956446048186,2.75811166841885,-2.49654188202599)
dA = chrono.ChVector3d(0.082475124142479,3.52644295689215e-15,0.996593123545252)
cB = chrono.ChVector3d(-3.0991159051399,2.75811166841885,-2.61195733808127)
dB = chrono.ChVector3d(0.0824751241424786,3.25333242964305e-15,0.996593123545253)
link_294.Initialize(body_62,body_66,False,cA,cB,dA,dB)
link_294.SetName("Coincident5")
exported_items.append(link_294)

link_295 = chrono.ChLinkMateGeneric()
link_295.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.08956446048186,2.75811166841885,-2.49654188202599)
cB = chrono.ChVector3d(-3.0991159051399,2.75811166841885,-2.61195733808127)
dA = chrono.ChVector3d(0.082475124142479,3.52644295689215e-15,0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424786,3.25333242964305e-15,0.996593123545253)
link_295.Initialize(body_62,body_66,False,cA,cB,dA,dB)
link_295.SetName("Coincident5")
exported_items.append(link_295)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_62 , SW name: M-410iB-300 -7/M-410iB-300-03-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_65 , SW name: M-410iB-300 -7/M-410iB-300-06-1 ,  SW ref.type:5 (5)
link_296 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.06708905223563,2.75811166841885,-2.22495893456206)
dA = chrono.ChVector3d(0.082475124142479,3.52644295689215e-15,0.996593123545252)
cB = chrono.ChVector3d(-3.06970763742716,2.75811166841885,-2.25660076623462)
dB = chrono.ChVector3d(-0.0824751241424783,-4.4211536946815e-15,-0.996593123545253)
link_296.SetFlipped(True)
link_296.Initialize(body_62,body_65,False,cA,cB,dA,dB)
link_296.SetName("Coincident6")
exported_items.append(link_296)

link_297 = chrono.ChLinkMateGeneric()
link_297.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.06708905223563,2.75811166841885,-2.22495893456206)
cB = chrono.ChVector3d(-3.06970763742716,2.75811166841885,-2.25660076623462)
dA = chrono.ChVector3d(0.082475124142479,3.52644295689215e-15,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424783,-4.4211536946815e-15,-0.996593123545253)
link_297.Initialize(body_62,body_65,False,cA,cB,dA,dB)
link_297.SetName("Coincident6")
exported_items.append(link_297)


# Mate constraint: Distance4 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_62 , SW name: M-410iB-300 -7/M-410iB-300-03-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_65 , SW name: M-410iB-300 -7/M-410iB-300-06-1 ,  SW ref.type:2 (2)
link_298 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-2.88223000352087,2.91434507456168,-2.24025732728765)
cB = chrono.ChVector3d(-2.96321003072953,2.58269164685798,-2.26541419583367)
dA = chrono.ChVector3d(-0.082475124142479,-3.52644295689215e-15,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424783,4.4211536946815e-15,0.996593123545253)
link_298.Initialize(body_62,body_65,False,cA,cB,dB)
link_298.SetDistance(0)
link_298.SetName("Distance4")
exported_items.append(link_298)

link_299 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.88223000352087,2.91434507456168,-2.24025732728765)
dA = chrono.ChVector3d(-0.082475124142479,-3.52644295689215e-15,-0.996593123545252)
cB = chrono.ChVector3d(-2.96321003072953,2.58269164685798,-2.26541419583367)
dB = chrono.ChVector3d(0.0824751241424783,4.4211536946815e-15,0.996593123545253)
link_299.SetFlipped(True)
link_299.Initialize(body_62,body_65,False,cA,cB,dA,dB)
link_299.SetName("Distance4")
exported_items.append(link_299)


# Mate constraint: Coincident7 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_67 , SW name: M-410iB-300 -7/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_68 , SW name: M-410iB-300 -7/M-410iB-300-07-1 ,  SW ref.type:5 (5)
link_300 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.90558579863488,2.51550127212934,-2.68676072122839)
dA = chrono.ChVector3d(0.0824751241424789,3.43512560843663e-15,0.996593123545252)
cB = chrono.ChVector3d(-1.88095452717193,2.51550127212935,-2.38912727090773)
dB = chrono.ChVector3d(-0.0824751241424795,-3.3255673993849e-15,-0.996593123545252)
link_300.SetFlipped(True)
link_300.Initialize(body_67,body_68,False,cA,cB,dA,dB)
link_300.SetName("Coincident7")
exported_items.append(link_300)

link_301 = chrono.ChLinkMateGeneric()
link_301.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.90558579863488,2.51550127212934,-2.68676072122839)
cB = chrono.ChVector3d(-1.88095452717193,2.51550127212935,-2.38912727090773)
dA = chrono.ChVector3d(0.0824751241424789,3.43512560843663e-15,0.996593123545252)
dB = chrono.ChVector3d(-0.0824751241424795,-3.3255673993849e-15,-0.996593123545252)
link_301.Initialize(body_67,body_68,False,cA,cB,dA,dB)
link_301.SetName("Coincident7")
exported_items.append(link_301)


# Mate constraint: Coincident8 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_65 , SW name: M-410iB-300 -7/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_68 , SW name: M-410iB-300 -7/M-410iB-300-07-1 ,  SW ref.type:2 (2)
link_302 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-2.60711943253569,3.10515332885272,-2.4052592469376)
cB = chrono.ChVector3d(-1.56768836286924,3.00995602354015,-2.49127951386792)
dA = chrono.ChVector3d(0.0824751241424783,4.4211536946815e-15,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424795,3.3255673993849e-15,0.996593123545252)
link_302.Initialize(body_65,body_68,False,cA,cB,dB)
link_302.SetDistance(0)
link_302.SetName("Coincident8")
exported_items.append(link_302)

link_303 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.60711943253569,3.10515332885272,-2.4052592469376)
dA = chrono.ChVector3d(0.0824751241424783,4.4211536946815e-15,0.996593123545253)
cB = chrono.ChVector3d(-1.56768836286924,3.00995602354015,-2.49127951386792)
dB = chrono.ChVector3d(0.0824751241424795,3.3255673993849e-15,0.996593123545252)
link_303.Initialize(body_65,body_68,False,cA,cB,dA,dB)
link_303.SetName("Coincident8")
exported_items.append(link_303)


# Mate constraint: Distance5 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_65 , SW name: M-410iB-300 -7/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_69 , SW name: M-410iB-300 -7/M-410iB-300-08-1 ,  SW ref.type:2 (2)
link_304 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-2.60711943253569,3.10515332885272,-2.4052592469376)
cB = chrono.ChVector3d(-1.57268463047198,3.01604196029192,-2.46869249489401)
dA = chrono.ChVector3d(0.0824751241424783,4.4211536946815e-15,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424792,-3.80638395782791e-15,-0.996593123545252)
link_304.Initialize(body_65,body_69,False,cA,cB,dB)
link_304.SetDistance(0)
link_304.SetName("Distance5")
exported_items.append(link_304)

link_305 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.60711943253569,3.10515332885272,-2.4052592469376)
dA = chrono.ChVector3d(0.0824751241424783,4.4211536946815e-15,0.996593123545253)
cB = chrono.ChVector3d(-1.57268463047198,3.01604196029192,-2.46869249489401)
dB = chrono.ChVector3d(-0.0824751241424792,-3.80638395782791e-15,-0.996593123545252)
link_305.SetFlipped(True)
link_305.Initialize(body_65,body_69,False,cA,cB,dA,dB)
link_305.SetName("Distance5")
exported_items.append(link_305)


# Mate constraint: Coincident9 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_65 , SW name: M-410iB-300 -7/M-410iB-300-06-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_69 , SW name: M-410iB-300 -7/M-410iB-300-08-1 ,  SW ref.type:5 (5)
link_306 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.76251640195877,3.2550226500217,-2.39239904948918)
dA = chrono.ChVector3d(0.0824751241424783,4.4211536946815e-15,0.996593123545253)
cB = chrono.ChVector3d(-2.76029584171634,3.25502265002171,-2.36556677623084)
dB = chrono.ChVector3d(0.0824751241424792,3.80638395782791e-15,0.996593123545252)
link_306.Initialize(body_65,body_69,False,cA,cB,dA,dB)
link_306.SetName("Coincident9")
exported_items.append(link_306)

link_307 = chrono.ChLinkMateGeneric()
link_307.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-2.76251640195877,3.2550226500217,-2.39239904948918)
cB = chrono.ChVector3d(-2.76029584171634,3.25502265002171,-2.36556677623084)
dA = chrono.ChVector3d(0.0824751241424783,4.4211536946815e-15,0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424792,3.80638395782791e-15,0.996593123545252)
link_307.Initialize(body_65,body_69,False,cA,cB,dA,dB)
link_307.SetName("Coincident9")
exported_items.append(link_307)


# Mate constraint: Coincident10 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_63 , SW name: M-410iB-300 -7/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_65 , SW name: M-410iB-300 -7/M-410iB-300-06-1 ,  SW ref.type:5 (5)
link_308 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.05620029367939,2.75811166841883,-2.09338396557674)
dA = chrono.ChVector3d(-0.0824751241424789,-3.4431355724638e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.06207868844398,2.75811166841885,-2.16441590230669)
dB = chrono.ChVector3d(-0.0824751241424783,-4.4211536946815e-15,-0.996593123545253)
link_308.Initialize(body_63,body_65,False,cA,cB,dA,dB)
link_308.SetName("Coincident10")
exported_items.append(link_308)

link_309 = chrono.ChLinkMateGeneric()
link_309.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.05620029367939,2.75811166841883,-2.09338396557674)
cB = chrono.ChVector3d(-3.06207868844398,2.75811166841885,-2.16441590230669)
dA = chrono.ChVector3d(-0.0824751241424789,-3.4431355724638e-15,-0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424783,-4.4211536946815e-15,-0.996593123545253)
link_309.Initialize(body_63,body_65,False,cA,cB,dA,dB)
link_309.SetName("Coincident10")
exported_items.append(link_309)


# Mate constraint: Coincident11 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_67 , SW name: M-410iB-300 -7/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_63 , SW name: M-410iB-300 -7/M-410iB-300-09-1 ,  SW ref.type:2 (2)
link_310 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.5131859877973,2.72491052060181,-2.22745101187137)
cB = chrono.ChVector3d(-3.05641325164641,3.21365467148158,-2.09973804942062)
dA = chrono.ChVector3d(0.0824751241424789,3.43512560843663e-15,0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424789,3.4431355724638e-15,0.996593123545253)
link_310.Initialize(body_67,body_63,False,cA,cB,dB)
link_310.SetDistance(0)
link_310.SetName("Coincident11")
exported_items.append(link_310)

link_311 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.5131859877973,2.72491052060181,-2.22745101187137)
dA = chrono.ChVector3d(0.0824751241424789,3.43512560843663e-15,0.996593123545252)
cB = chrono.ChVector3d(-3.05641325164641,3.21365467148158,-2.09973804942062)
dB = chrono.ChVector3d(0.0824751241424789,3.4431355724638e-15,0.996593123545253)
link_311.Initialize(body_67,body_63,False,cA,cB,dA,dB)
link_311.SetName("Coincident11")
exported_items.append(link_311)


# Mate constraint: Coincident12 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_63 , SW name: M-410iB-300 -7/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_72 , SW name: M-410iB-300 -7/M-410iB-300-10-1 ,  SW ref.type:5 (5)
link_312 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-2.55781544031629,3.03081076163702,-2.14737224964241)
dA = chrono.ChVector3d(-0.0824751241424789,-3.4431355724638e-15,-0.996593123545253)
cB = chrono.ChVector3d(-2.55308103828998,3.03081076163705,-2.09016381797842)
dB = chrono.ChVector3d(-0.0824751241424783,-3.82037016585297e-15,-0.996593123545252)
link_312.Initialize(body_63,body_72,False,cA,cB,dA,dB)
link_312.SetName("Coincident12")
exported_items.append(link_312)

link_313 = chrono.ChLinkMateGeneric()
link_313.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-2.55781544031629,3.03081076163702,-2.14737224964241)
cB = chrono.ChVector3d(-2.55308103828998,3.03081076163705,-2.09016381797842)
dA = chrono.ChVector3d(-0.0824751241424789,-3.4431355724638e-15,-0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424783,-3.82037016585297e-15,-0.996593123545252)
link_313.Initialize(body_63,body_72,False,cA,cB,dA,dB)
link_313.SetName("Coincident12")
exported_items.append(link_313)


# Mate constraint: Distance7 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_63 , SW name: M-410iB-300 -7/M-410iB-300-09-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_72 , SW name: M-410iB-300 -7/M-410iB-300-10-1 ,  SW ref.type:2 (2)
link_314 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-3.05641325164641,3.21365467148158,-2.09973804942062)
cB = chrono.ChVector3d(-2.55704033909957,3.03081076163705,-2.13800626746733)
dA = chrono.ChVector3d(0.0824751241424789,3.4431355724638e-15,0.996593123545253)
dB = chrono.ChVector3d(-0.0824751241424783,-3.82037016585297e-15,-0.996593123545252)
link_314.Initialize(body_63,body_72,False,cA,cB,dB)
link_314.SetDistance(0)
link_314.SetName("Distance7")
exported_items.append(link_314)

link_315 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.05641325164641,3.21365467148158,-2.09973804942062)
dA = chrono.ChVector3d(0.0824751241424789,3.4431355724638e-15,0.996593123545253)
cB = chrono.ChVector3d(-2.55704033909957,3.03081076163705,-2.13800626746733)
dB = chrono.ChVector3d(-0.0824751241424783,-3.82037016585297e-15,-0.996593123545252)
link_315.SetFlipped(True)
link_315.Initialize(body_63,body_72,False,cA,cB,dA,dB)
link_315.SetName("Distance7")
exported_items.append(link_315)


# Mate constraint: Coincident13 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_67 , SW name: M-410iB-300 -7/M-410iB-300-02-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_72 , SW name: M-410iB-300 -7/M-410iB-300-10-1 ,  SW ref.type:5 (5)
link_316 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.36587439836585,2.78749692402101,-2.23964208698411)
dA = chrono.ChVector3d(-0.0824751241424789,-3.43512560843663e-15,-0.996593123545252)
cB = chrono.ChVector3d(-1.36562301418745,2.78749692402101,-2.23660447114354)
dB = chrono.ChVector3d(0.0824751241424783,3.82037016585297e-15,0.996593123545252)
link_316.SetFlipped(True)
link_316.Initialize(body_67,body_72,False,cA,cB,dA,dB)
link_316.SetName("Coincident13")
exported_items.append(link_316)

link_317 = chrono.ChLinkMateGeneric()
link_317.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.36587439836585,2.78749692402101,-2.23964208698411)
cB = chrono.ChVector3d(-1.36562301418745,2.78749692402101,-2.23660447114354)
dA = chrono.ChVector3d(-0.0824751241424789,-3.43512560843663e-15,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424783,3.82037016585297e-15,0.996593123545252)
link_317.Initialize(body_67,body_72,False,cA,cB,dA,dB)
link_317.SetName("Coincident13")
exported_items.append(link_317)


# Mate constraint: Coincident14 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_63 , SW name: M-410iB-300 -7/M-410iB-300-09-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_73 , SW name: M-410iB-300 -7/M-410iB-300-11-1 ,  SW ref.type:5 (5)
link_318 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.55579644633207,3.02764258400497,-2.06478226841699)
dA = chrono.ChVector3d(-0.0824751241424789,-3.4431355724638e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.56428066235258,3.02764258400502,-2.16730180303609)
dB = chrono.ChVector3d(0.0824751241424785,4.64262909346598e-15,0.996593123545252)
link_318.SetFlipped(True)
link_318.Initialize(body_63,body_73,False,cA,cB,dA,dB)
link_318.SetName("Coincident14")
exported_items.append(link_318)

link_319 = chrono.ChLinkMateGeneric()
link_319.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.55579644633207,3.02764258400497,-2.06478226841699)
cB = chrono.ChVector3d(-3.56428066235258,3.02764258400502,-2.16730180303609)
dA = chrono.ChVector3d(-0.0824751241424789,-3.4431355724638e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424785,4.64262909346598e-15,0.996593123545252)
link_319.Initialize(body_63,body_73,False,cA,cB,dA,dB)
link_319.SetName("Coincident14")
exported_items.append(link_319)


# Mate constraint: Distance8 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_63 , SW name: M-410iB-300 -7/M-410iB-300-09-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_73 , SW name: M-410iB-300 -7/M-410iB-300-11-1 ,  SW ref.type:2 (2)
link_320 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-3.060372552456,3.21365467148158,-2.14758049890953)
cB = chrono.ChVector3d(-3.55910633801413,3.02764258400502,-2.10477754365111)
dA = chrono.ChVector3d(-0.0824751241424789,-3.4431355724638e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424785,4.64262909346598e-15,0.996593123545253)
link_320.Initialize(body_63,body_73,False,cA,cB,dB)
link_320.SetDistance(0)
link_320.SetName("Distance8")
exported_items.append(link_320)

link_321 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.060372552456,3.21365467148158,-2.14758049890953)
dA = chrono.ChVector3d(-0.0824751241424789,-3.4431355724638e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.55910633801413,3.02764258400502,-2.10477754365111)
dB = chrono.ChVector3d(0.0824751241424785,4.64262909346598e-15,0.996593123545253)
link_321.SetFlipped(True)
link_321.Initialize(body_63,body_73,False,cA,cB,dA,dB)
link_321.SetName("Distance8")
exported_items.append(link_321)


# Mate constraint: Coincident15 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_65 , SW name: M-410iB-300 -7/M-410iB-300-06-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_70 , SW name: M-410iB-300 -7/M-410iB-300-12-1 ,  SW ref.type:5 (5)
link_322 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.81525551082145,1.69376904051649,-2.21496978126314)
dA = chrono.ChVector3d(-0.0824751241424783,-4.4211536946815e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.81422770582439,1.69376904051648,-2.20255023775752)
dB = chrono.ChVector3d(0.0824751241424788,4.40985491043984e-15,0.996593123545253)
link_322.SetFlipped(True)
link_322.Initialize(body_65,body_70,False,cA,cB,dA,dB)
link_322.SetName("Coincident15")
exported_items.append(link_322)

link_323 = chrono.ChLinkMateGeneric()
link_323.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-3.81525551082145,1.69376904051649,-2.21496978126314)
cB = chrono.ChVector3d(-3.81422770582439,1.69376904051648,-2.20255023775752)
dA = chrono.ChVector3d(-0.0824751241424783,-4.4211536946815e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424788,4.40985491043984e-15,0.996593123545253)
link_323.Initialize(body_65,body_70,False,cA,cB,dA,dB)
link_323.SetName("Coincident15")
exported_items.append(link_323)


# Mate constraint: Distance9 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_65 , SW name: M-410iB-300 -7/M-410iB-300-06-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_70 , SW name: M-410iB-300 -7/M-410iB-300-12-1 ,  SW ref.type:2 (2)
link_324 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-3.18827765327686,2.27955349819167,-2.40733522319354)
cB = chrono.ChVector3d(-3.82784946227801,1.69376904051648,-2.3671495512285)
dA = chrono.ChVector3d(-0.0824751241424783,-4.4211536946815e-15,-0.996593123545253)
dB = chrono.ChVector3d(0.0824751241424788,4.40985491043984e-15,0.996593123545253)
link_324.Initialize(body_65,body_70,False,cA,cB,dB)
link_324.SetDistance(0)
link_324.SetName("Distance9")
exported_items.append(link_324)

link_325 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-3.18827765327686,2.27955349819167,-2.40733522319354)
dA = chrono.ChVector3d(-0.0824751241424783,-4.4211536946815e-15,-0.996593123545253)
cB = chrono.ChVector3d(-3.82784946227801,1.69376904051648,-2.3671495512285)
dB = chrono.ChVector3d(0.0824751241424788,4.40985491043984e-15,0.996593123545253)
link_325.SetFlipped(True)
link_325.Initialize(body_65,body_70,False,cA,cB,dA,dB)
link_325.SetName("Distance9")
exported_items.append(link_325)


# Mate constraint: Coincident16 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_73 , SW name: M-410iB-300 -7/M-410iB-300-11-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_70 , SW name: M-410iB-300 -7/M-410iB-300-12-1 ,  SW ref.type:5 (5)
link_326 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-4.30817905100364,1.96329996858996,-2.10573895406204)
dA = chrono.ChVector3d(0.0824751241424785,4.64262909346598e-15,0.996593123545252)
cB = chrono.ChVector3d(-4.31277644214529,1.96329996858993,-2.16129180646023)
dB = chrono.ChVector3d(0.0824751241424788,4.40985491043984e-15,0.996593123545253)
link_326.Initialize(body_73,body_70,False,cA,cB,dA,dB)
link_326.SetName("Coincident16")
exported_items.append(link_326)

link_327 = chrono.ChLinkMateGeneric()
link_327.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-4.30817905100364,1.96329996858996,-2.10573895406204)
cB = chrono.ChVector3d(-4.31277644214529,1.96329996858993,-2.16129180646023)
dA = chrono.ChVector3d(0.0824751241424785,4.64262909346598e-15,0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424788,4.40985491043984e-15,0.996593123545253)
link_327.Initialize(body_73,body_70,False,cA,cB,dA,dB)
link_327.SetName("Coincident16")
exported_items.append(link_327)


# Mate constraint: Coincident17 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_68 , SW name: M-410iB-300 -7/M-410iB-300-07-1 ,  SW ref.type:5 (5)
#   Entity 1: C::E name: body_69 , SW name: M-410iB-300 -7/M-410iB-300-08-1 ,  SW ref.type:5 (5)
link_328 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.56037999469361,3.00995602354015,-2.40296840741121)
dA = chrono.ChVector3d(-0.0824751241424795,-3.3255673993849e-15,-0.996593123545252)
cB = chrono.ChVector3d(-1.56546780262682,3.00995602354015,-2.46444724060959)
dB = chrono.ChVector3d(0.0824751241424792,3.80638395782791e-15,0.996593123545252)
link_328.SetFlipped(True)
link_328.Initialize(body_68,body_69,False,cA,cB,dA,dB)
link_328.SetName("Coincident17")
exported_items.append(link_328)

link_329 = chrono.ChLinkMateGeneric()
link_329.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.56037999469361,3.00995602354015,-2.40296840741121)
cB = chrono.ChVector3d(-1.56546780262682,3.00995602354015,-2.46444724060959)
dA = chrono.ChVector3d(-0.0824751241424795,-3.3255673993849e-15,-0.996593123545252)
dB = chrono.ChVector3d(0.0824751241424792,3.80638395782791e-15,0.996593123545252)
link_329.Initialize(body_68,body_69,False,cA,cB,dA,dB)
link_329.SetName("Coincident17")
exported_items.append(link_329)


# Mate constraint: Coincident18 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_67 , SW name: M-410iB-300 -7/M-410iB-300-02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_64 , SW name: M-410iB-300 -7/ArmBase-1 ,  SW ref.type:2 (2)
link_330 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-1.50067035795504,2.04602671615661,-2.52259688656262)
cB = chrono.ChVector3d(-1.25867129241134,2.04602671615662,-2.52259688656262)
dA = chrono.ChVector3d(1.96505437811525e-16,-1,3.43060645039982e-15)
dB = chrono.ChVector3d(-6.42083927456682e-17,1,-3.44169137633798e-15)
link_330.Initialize(body_67,body_64,False,cA,cB,dB)
link_330.SetDistance(0)
link_330.SetName("Coincident18")
exported_items.append(link_330)

link_331 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.50067035795504,2.04602671615661,-2.52259688656262)
dA = chrono.ChVector3d(1.96505437811525e-16,-1,3.43060645039982e-15)
cB = chrono.ChVector3d(-1.25867129241134,2.04602671615662,-2.52259688656262)
dB = chrono.ChVector3d(-6.42083927456682e-17,1,-3.44169137633798e-15)
link_331.SetFlipped(True)
link_331.Initialize(body_67,body_64,False,cA,cB,dA,dB)
link_331.SetName("Coincident18")
exported_items.append(link_331)


# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_67 , SW name: M-410iB-300 -7/M-410iB-300-02-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_64 , SW name: M-410iB-300 -7/ArmBase-1 ,  SW ref.type:1 (1)
link_332 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-1.50067035795504,2.04755071615662,-2.52259688656262)
dA = chrono.ChVector3d(-1.96505437811525e-16,1,-3.43060645039982e-15)
cB = chrono.ChVector3d(-1.50067035795504,2.04602671615662,-2.52259688656262)
dB = chrono.ChVector3d(-6.42083927456682e-17,1,-3.44169137633798e-15)
link_332.Initialize(body_67,body_64,False,cA,cB,dA,dB)
link_332.SetName("Concentric1")
exported_items.append(link_332)

link_333 = chrono.ChLinkMateGeneric()
link_333.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-1.50067035795504,2.04755071615662,-2.52259688656262)
cB = chrono.ChVector3d(-1.50067035795504,2.04602671615662,-2.52259688656262)
dA = chrono.ChVector3d(-1.96505437811525e-16,1,-3.43060645039982e-15)
dB = chrono.ChVector3d(-6.42083927456682e-17,1,-3.44169137633798e-15)
link_333.Initialize(body_67,body_64,False,cA,cB,dA,dB)
link_333.SetName("Concentric1")
exported_items.append(link_333)


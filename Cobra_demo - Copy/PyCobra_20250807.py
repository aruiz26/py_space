# PyChrono model automatically generated using Chrono::SolidWorks add-in
# Assembly: M:\ruiza\Downloads\Cobra_CAD-SW2025\cobra_4_1_pyMarkers - Copy.SLDASM


import pychrono as chrono 
import builtins 

# Some global settings 
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'PyCobra_20250807_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0 = chrono.ChBodyAuxRef()
body_0.SetName('SLDW_GROUND')
body_0.SetFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('Assem6^cobra_4_1_pyMarkers - Copy-1')
body_1.SetPos(chrono.ChVector3d(0.0447652371612743,-0.281923629727815,-0.253755907358352))
body_1.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_1.SetMass(10.7141671389581)
body_1.SetInertiaXX(chrono.ChVector3d(0.387475760255156,0.213853598249627,0.489332419164563))
body_1.SetInertiaXY(chrono.ChVector3d(-0.0386301203014744,2.86803409342521e-06,9.91372976974357e-06))
body_1.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.154114809263048,0.508724676714838,0.253741403915262),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837402,0.324323829726013,0.384155907359311), chrono.ChQuaterniond(3.03943339214823E-15,2.84466058660162E-15,0.707106781186544,0.707106781186551)))

# Visualization shape 
body_1_2_shape = chrono.ChVisualShapeModelFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_1.AddVisualShape(body_1_2_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.757456829733399,0.141157299661483), chrono.ChQuaterniond(-0.0731636374323121,0.0731636374323132,0.703311511463926,0.703311511463927)))

# Visualization shape 
body_1_2_shape = chrono.ChVisualShapeModelFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_1.AddVisualShape(body_1_2_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.757456829733399,0.366157299661484), chrono.ChQuaterniond(-0.0731636374323121,0.0731636374323132,0.703311511463926,0.703311511463927)))

# Visualization shape 
body_1_4_shape = chrono.ChVisualShapeModelFile() 
body_1_4_shape.SetFilename(shapes_dir +'body_1_4.obj') 
body_1.AddVisualShape(body_1_4_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.710606529733399,0.141157299661483), chrono.ChQuaterniond(-0.277117631253953,-0.277117631253952,0.650542710702533,-0.650542710702532)))

# Visualization shape 
body_1_2_shape = chrono.ChVisualShapeModelFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_1.AddVisualShape(body_1_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.0271174606580949,0.7574568297334,0.366157299661484), chrono.ChQuaterniond(-0.0731636374323121,0.0731636374323132,0.703311511463926,0.703311511463927)))

# Visualization shape 
body_1_4_shape = chrono.ChVisualShapeModelFile() 
body_1_4_shape.SetFilename(shapes_dir +'body_1_4.obj') 
body_1.AddVisualShape(body_1_4_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.710606529733399,0.366157299661483), chrono.ChQuaterniond(-0.277117631253953,-0.277117631253952,0.650542710702533,-0.650542710702532)))

# Visualization shape 
body_1_7_shape = chrono.ChVisualShapeModelFile() 
body_1_7_shape.SetFilename(shapes_dir +'body_1_7.obj') 
body_1.AddVisualShape(body_1_7_shape, chrono.ChFramed(chrono.ChVector3d(-0.0271174606580949,0.7060853297334,0.366157299661483), chrono.ChQuaterniond(0.500020607772399,-0.499979391378206,-0.499979391378206,0.500020607772398)))

# Visualization shape 
body_1_7_shape = chrono.ChVisualShapeModelFile() 
body_1_7_shape.SetFilename(shapes_dir +'body_1_7.obj') 
body_1.AddVisualShape(body_1_7_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.706085329733399,0.366157299661483), chrono.ChQuaterniond(0.500020607772399,-0.499979391378206,-0.499979391378206,0.500020607772398)))

# Visualization shape 
body_1_4_shape = chrono.ChVisualShapeModelFile() 
body_1_4_shape.SetFilename(shapes_dir +'body_1_4.obj') 
body_1.AddVisualShape(body_1_4_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.807304329733399,0.141157299661483), chrono.ChQuaterniond(-0.0435546902795118,0.0435546902795129,0.705764117077835,0.705764117077835)))

# Visualization shape 
body_1_4_shape = chrono.ChVisualShapeModelFile() 
body_1_4_shape.SetFilename(shapes_dir +'body_1_4.obj') 
body_1.AddVisualShape(body_1_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0271174606580948,0.8073043297334,0.366157299661484), chrono.ChQuaterniond(-0.0435546902795118,0.0435546902795129,0.705764117077835,0.705764117077835)))

# Visualization shape 
body_1_4_shape = chrono.ChVisualShapeModelFile() 
body_1_4_shape.SetFilename(shapes_dir +'body_1_4.obj') 
body_1.AddVisualShape(body_1_4_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.807304329733399,0.366157299661484), chrono.ChQuaterniond(-0.0435546902795118,0.0435546902795129,0.705764117077835,0.705764117077835)))

# Visualization shape 
body_1_4_shape = chrono.ChVisualShapeModelFile() 
body_1_4_shape.SetFilename(shapes_dir +'body_1_4.obj') 
body_1.AddVisualShape(body_1_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0271174606580949,0.7106065297334,0.366157299661483), chrono.ChQuaterniond(-0.277117631253953,-0.277117631253952,0.650542710702533,-0.650542710702532)))

# Visualization shape 
body_1_7_shape = chrono.ChVisualShapeModelFile() 
body_1_7_shape.SetFilename(shapes_dir +'body_1_7.obj') 
body_1.AddVisualShape(body_1_7_shape, chrono.ChFramed(chrono.ChVector3d(0.322382539341905,0.706085329733399,0.141157299661483), chrono.ChQuaterniond(0.500020607772399,-0.499979391378206,-0.499979391378206,0.500020607772398)))

# Visualization shape 
body_1_14_shape = chrono.ChVisualShapeModelFile() 
body_1_14_shape.SetFilename(shapes_dir +'body_1_14.obj') 
body_1.AddVisualShape(body_1_14_shape, chrono.ChFramed(chrono.ChVector3d(0.265188762837843,0.869606829733399,0.253755907359236), chrono.ChQuaterniond(1.11022302462516E-16,8.08775043606109E-16,1,2.69591681202036E-16)))

# Visualization shape 
body_1_2_shape = chrono.ChVisualShapeModelFile() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_1.AddVisualShape(body_1_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.0271174606580949,0.7574568297334,0.141157299661483), chrono.ChQuaterniond(-0.0731636374323121,0.0731636374323132,0.703311511463926,0.703311511463927)))

# Visualization shape 
body_1_16_shape = chrono.ChVisualShapeModelFile() 
body_1_16_shape.SetFilename(shapes_dir +'body_1_16.obj') 
body_1.AddVisualShape(body_1_16_shape, chrono.ChFramed(chrono.ChVector3d(0.147534762837843,0.808256829733399,0.253755907359236), chrono.ChQuaterniond(0.707106781186548,-3.81260211858883E-16,-0.707106781186547,-7.62520423717767E-16)))

# Visualization shape 
body_1_4_shape = chrono.ChVisualShapeModelFile() 
body_1_4_shape.SetFilename(shapes_dir +'body_1_4.obj') 
body_1.AddVisualShape(body_1_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0271174606580948,0.8073043297334,0.141157299661483), chrono.ChQuaterniond(-0.0435546902795118,0.0435546902795129,0.705764117077835,0.705764117077835)))

# Visualization shape 
body_1_18_shape = chrono.ChVisualShapeModelFile() 
body_1_18_shape.SetFilename(shapes_dir +'body_1_18.obj') 
body_1.AddVisualShape(body_1_18_shape, chrono.ChFramed(chrono.ChVector3d(0.265634762837843,0.864606829733399,0.253755907359236), chrono.ChQuaterniond(-1.16879339985135E-31,8.08775043606108E-16,1,2.69591681202036E-16)))

# Visualization shape 
body_1_7_shape = chrono.ChVisualShapeModelFile() 
body_1_7_shape.SetFilename(shapes_dir +'body_1_7.obj') 
body_1.AddVisualShape(body_1_7_shape, chrono.ChFramed(chrono.ChVector3d(-0.0271174606580949,0.7060853297334,0.141157299661483), chrono.ChQuaterniond(0.500020607772399,-0.499979391378206,-0.499979391378206,0.500020607772398)))

# Visualization shape 
body_1_4_shape = chrono.ChVisualShapeModelFile() 
body_1_4_shape.SetFilename(shapes_dir +'body_1_4.obj') 
body_1.AddVisualShape(body_1_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.0271174606580949,0.7106065297334,0.141157299661483), chrono.ChQuaterniond(-0.277117631253953,-0.277117631253952,0.650542710702533,-0.650542710702532)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0437400316183114,0.399323829727813,0.385076107359236), chrono.ChQuaterniond(4.39389193448936E-16,5.79964487832136E-17,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617132,0.39932382972781,0.123355907359389), chrono.ChQuaterniond(0.70710678118655,-0.707106781186545,2.59350884430325E-15,-3.28368045020259E-15)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837403,0.399323829727764,0.384155907361403), chrono.ChQuaterniond(3.08604551201541E-15,2.79804846673445E-15,0.707106781186544,0.707106781186551)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617139,0.324323829728003,0.123355907357452), chrono.ChQuaterniond(0.70710678118655,-0.707106781186545,2.56160942495213E-15,-3.25179140527763E-15)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.043740031618308,0.324323829727831,0.385076107359235), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,-3.87555566842849E-15,-3.85864489921714E-15)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837411,0.324323829726133,0.123355907345278), chrono.ChQuaterniond(-2.42051107587712E-15,3.16604287669643E-15,0.707106781186551,-0.707106781186544)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837411,0.399323829726136,0.123355907345004), chrono.ChQuaterniond(0.707106781186551,-0.707106781186544,2.50389615269494E-15,-3.01391408471168E-15)))

# Visualization shape 
body_1_28_shape = chrono.ChVisualShapeModelFile() 
body_1_28_shape.SetFilename(shapes_dir +'body_1_28.obj') 
body_1.AddVisualShape(body_1_28_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371621584,0.292413829728693,0.141055907357469), chrono.ChQuaterniond(0.707106781186548,-3.8126021208526E-16,0.707106781186547,0)))

# Visualization shape 
body_1_29_shape = chrono.ChVisualShapeModelFile() 
body_1_29_shape.SetFilename(shapes_dir +'body_1_29.obj') 
body_1.AddVisualShape(body_1_29_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837842,0.292413829728693,0.179155907358353), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_29_shape = chrono.ChVisualShapeModelFile() 
body_1_29_shape.SetFilename(shapes_dir +'body_1_29.obj') 
body_1.AddVisualShape(body_1_29_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371612742,0.292413829728693,0.179155907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_28_shape = chrono.ChVisualShapeModelFile() 
body_1_28_shape.SetFilename(shapes_dir +'body_1_28.obj') 
body_1.AddVisualShape(body_1_28_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371621584,0.292413829728693,0.366455907358352), chrono.ChQuaterniond(0.707106781186548,3.81260211858883E-16,0.707106781186547,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.292413829729211,0.166455907358353), chrono.ChQuaterniond(6.31927204887826E-17,0.707106781186548,-0.707106781186547,-6.31927204887825E-17)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.292413829729211,0.156518407358353), chrono.ChQuaterniond(0.5,0.5,-0.5,-0.5)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.292413829729211,0.153755907358353), chrono.ChQuaterniond(0.5,0.5,-0.5,-0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.292413829729186,0.341055907358375), chrono.ChQuaterniond(0.707106781186547,2.32369780257537E-14,-2.33633634667313E-14,0.707106781186548)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.292413829729186,0.350993407358375), chrono.ChQuaterniond(0.500000000000016,-0.499999999999983,-0.500000000000017,0.499999999999984)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.292413829729186,0.353755907358375), chrono.ChQuaterniond(0.500000000000016,-0.499999999999983,-0.500000000000017,0.499999999999984)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612742,0.292413829729211,0.341055907358352), chrono.ChQuaterniond(0.707106781186547,-4.96290709266116E-17,1.36224676550161E-16,-0.707106781186548)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612742,0.292413829729211,0.350993407358352), chrono.ChQuaterniond(0.5,-0.5,0.5,-0.5)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612742,0.292413829729211,0.353755907358352), chrono.ChQuaterniond(0.5,-0.5,0.5,-0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612742,0.292413829729211,0.156518407358353), chrono.ChQuaterniond(-0.5,-0.5,0.5,0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612742,0.292413829729211,0.166455907358353), chrono.ChQuaterniond(0.707106781186547,2.97341532496038E-17,-2.97341532496038E-17,-0.707106781186548)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612742,0.292413829729211,0.153755907358353), chrono.ChQuaterniond(0.707106781186547,2.97341532496038E-17,-2.97341532496038E-17,-0.707106781186548)))

# Visualization shape 
body_1_44_shape = chrono.ChVisualShapeModelFile() 
body_1_44_shape.SetFilename(shapes_dir +'body_1_44.obj') 
body_1.AddVisualShape(body_1_44_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371612745,0.654713829730607,0.141055907358347), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,3.8126021208526E-16,-3.4863055968421E-32)))

# Visualization shape 
body_1_44_shape = chrono.ChVisualShapeModelFile() 
body_1_44_shape.SetFilename(shapes_dir +'body_1_44.obj') 
body_1.AddVisualShape(body_1_44_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837842,0.654713829730607,0.366455907357322), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,-3.81260211858883E-16,0)))

# Visualization shape 
body_1_44_shape = chrono.ChVisualShapeModelFile() 
body_1_44_shape.SetFilename(shapes_dir +'body_1_44.obj') 
body_1.AddVisualShape(body_1_44_shape, chrono.ChFramed(chrono.ChVector3d(-0.044765237161274,0.654713829730607,0.366455907357323), chrono.ChQuaterniond(0.707106781186547,0.707106781186548,-3.81260211858883E-16,-3.4863055968421E-32)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616935,0.317813829730607,0.350993407356446), chrono.ChQuaterniond(5.71890317788325E-16,-1.90630105929442E-16,0.707106781186548,-0.707106781186547)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616935,0.307876329730607,0.341055907356446), chrono.ChQuaterniond(2.69591681202037E-16,-5.39183362404072E-16,1,0)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616935,0.305113829730607,0.353755907356446), chrono.ChQuaterniond(2.69591681202037E-16,-5.39183362404072E-16,1,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612743,0.317813829730607,0.141055907358865), chrono.ChQuaterniond(0.5,0.499999999999999,0.5,-0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612743,0.307876329730607,0.141055907358865), chrono.ChQuaterniond(0.707106781186547,-3.8126021208526E-16,0.707106781186548,3.4863055968421E-32)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612743,0.305113829730607,0.141055907358865), chrono.ChQuaterniond(0.707106781186547,-3.8126021208526E-16,0.707106781186548,3.4863055968421E-32)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612742,0.307876329730607,0.367553348962111), chrono.ChQuaterniond(0.707106781186548,-2.53822826583835E-16,-0.707106781186547,-2.53822826252613E-16)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612742,0.317813829730607,0.367553348962111), chrono.ChQuaterniond(-0.5,0.5,0.5,0.5)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612742,0.305113829730607,0.367553348962111), chrono.ChQuaterniond(-0.5,0.5,0.5,0.5)))

# Visualization shape 
body_1_28_shape = chrono.ChVisualShapeModelFile() 
body_1_28_shape.SetFilename(shapes_dir +'body_1_28.obj') 
body_1.AddVisualShape(body_1_28_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371621582,0.692813829731486,0.141055907357469), chrono.ChQuaterniond(0.707106781186548,-3.8126021208526E-16,0.707106781186547,0)))

# Visualization shape 
body_1_29_shape = chrono.ChVisualShapeModelFile() 
body_1_29_shape.SetFilename(shapes_dir +'body_1_29.obj') 
body_1.AddVisualShape(body_1_29_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837842,0.692813829731485,0.179155907358353), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_29_shape = chrono.ChVisualShapeModelFile() 
body_1_29_shape.SetFilename(shapes_dir +'body_1_29.obj') 
body_1.AddVisualShape(body_1_29_shape, chrono.ChFramed(chrono.ChVector3d(-0.044765237161274,0.692813829731486,0.179155907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_28_shape = chrono.ChVisualShapeModelFile() 
body_1_28_shape.SetFilename(shapes_dir +'body_1_28.obj') 
body_1.AddVisualShape(body_1_28_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371621581,0.692813829731486,0.366455907358352), chrono.ChQuaterniond(0.707106781186548,3.81260211858883E-16,0.707106781186547,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.692813829732003,0.166455907358353), chrono.ChQuaterniond(6.31927204887826E-17,0.707106781186548,-0.707106781186547,-6.31927204887825E-17)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.692813829732003,0.156518407358353), chrono.ChQuaterniond(0.5,0.5,-0.5,-0.5)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.692813829732003,0.153755907358353), chrono.ChQuaterniond(0.5,0.5,-0.5,-0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.692813829731979,0.341055907358375), chrono.ChQuaterniond(0.707106781186547,2.32369780257537E-14,-2.33633634667313E-14,0.707106781186548)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.692813829731978,0.350993407358375), chrono.ChQuaterniond(0.500000000000016,-0.499999999999983,-0.500000000000017,0.499999999999984)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.692813829731978,0.353755907358375), chrono.ChQuaterniond(0.500000000000016,-0.499999999999983,-0.500000000000017,0.499999999999984)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.029302737161274,0.692813829732003,0.341055907358352), chrono.ChQuaterniond(0.707106781186547,-4.96290709266116E-17,1.36224676550161E-16,-0.707106781186548)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.019365237161274,0.692813829732003,0.350993407358352), chrono.ChQuaterniond(0.5,-0.5,0.5,-0.5)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(-0.032065237161274,0.692813829732003,0.353755907358352), chrono.ChQuaterniond(0.5,-0.5,0.5,-0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.019365237161274,0.692813829732003,0.156518407358353), chrono.ChQuaterniond(-0.5,-0.5,0.5,0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.029302737161274,0.692813829732003,0.166455907358353), chrono.ChQuaterniond(0.707106781186547,2.97341532496038E-17,-2.97341532496038E-17,-0.707106781186548)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(-0.032065237161274,0.692813829732003,0.153755907358353), chrono.ChQuaterniond(0.707106781186547,2.97341532496038E-17,-2.97341532496038E-17,-0.707106781186548)))

# Visualization shape 
body_1_44_shape = chrono.ChVisualShapeModelFile() 
body_1_44_shape.SetFilename(shapes_dir +'body_1_44.obj') 
body_1.AddVisualShape(body_1_44_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837841,0.654713829730607,0.141055907358348), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,3.8126021208526E-16,0)))

# Visualization shape 
body_1_73_shape = chrono.ChVisualShapeModelFile() 
body_1_73_shape.SetFilename(shapes_dir +'body_1_73.obj') 
body_1.AddVisualShape(body_1_73_shape, chrono.ChFramed(chrono.ChVector3d(0.327034762835561,0.368613829731491,0.253755907358351), chrono.ChQuaterniond(-2.55140024536113E-16,1.2612018732277E-16,0.707106781186548,-0.707106781186547)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283556,0.368613829731492,0.350993407358351), chrono.ChQuaterniond(-5.23184691419221E-16,1.30533127109691E-15,0.707106781186548,-0.707106781186547)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283556,0.358676329731492,0.341055907358352), chrono.ChQuaterniond(5.53061150371959E-16,1.30683382441082E-15,1,2.90599267418406E-16)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283556,0.355913829731492,0.353755907358351), chrono.ChQuaterniond(5.53061150371959E-16,1.30683382441082E-15,1,2.90599267418406E-16)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.360263829731491,0.307095907358351), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_29_shape = chrono.ChVisualShapeModelFile() 
body_1_29_shape.SetFilename(shapes_dir +'body_1_29.obj') 
body_1.AddVisualShape(body_1_29_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762836079,0.343213829730607,0.328355907358351), chrono.ChQuaterniond(3.81260211858883E-16,-0.707106781186547,0.707106781186548,3.81260211858883E-16)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835541,0.327751329730622,0.166455907358351), chrono.ChQuaterniond(-4.49815360045584E-16,1,-3.31597768161896E-14,-2.05642184200826E-29)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283554,0.317813829730622,0.156518407358351), chrono.ChQuaterniond(0.707106781186547,0.707106781186548,-2.34475030493601E-14,-2.34475030493601E-14)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835541,0.330513829730622,0.153755907358351), chrono.ChQuaterniond(0.707106781186547,0.707106781186548,-2.34475030493601E-14,-2.34475030493601E-14)))

# Visualization shape 
body_1_44_shape = chrono.ChVisualShapeModelFile() 
body_1_44_shape.SetFilename(shapes_dir +'body_1_44.obj') 
body_1.AddVisualShape(body_1_44_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762836078,0.654713829730607,0.366455907359236), chrono.ChQuaterniond(-0.5,-0.5,0.500000000000001,-0.5)))

# Visualization shape 
body_1_83_shape = chrono.ChVisualShapeModelFile() 
body_1_83_shape.SetFilename(shapes_dir +'body_1_83.obj') 
body_1.AddVisualShape(body_1_83_shape, chrono.ChFramed(chrono.ChVector3d(-0.0229652371644388,0.359088829731491,0.317255907358351), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_84_shape = chrono.ChVisualShapeModelFile() 
body_1_84_shape.SetFilename(shapes_dir +'body_1_84.obj') 
body_1.AddVisualShape(body_1_84_shape, chrono.ChFramed(chrono.ChVector3d(-0.0379652371644393,0.365438829731491,0.253755907358352), chrono.ChQuaterniond(-5.39183362404072E-16,1,7.75060634674567E-18,-6.52099496614874E-17)))

# Visualization shape 
body_1_44_shape = chrono.ChVisualShapeModelFile() 
body_1_44_shape.SetFilename(shapes_dir +'body_1_44.obj') 
body_1.AddVisualShape(body_1_44_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762836079,0.654713829730607,0.141055907358352), chrono.ChQuaterniond(-0.5,-0.5,0.500000000000001,-0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.317813829730607,0.350993407358351), chrono.ChQuaterniond(0.707106781186548,-0.707106781186547,-1.9063010604263E-16,-5.71890317901514E-16)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.327751329730607,0.341055907358351), chrono.ChQuaterniond(-5.81233805195342E-16,1,-2.69591681202036E-16,5.39183362564145E-16)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.330513829730607,0.353755907358351), chrono.ChQuaterniond(-5.81233805195342E-16,1,-2.69591681202036E-16,5.39183362564145E-16)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.15203476283556,0.358676329731492,0.166455907358351), chrono.ChQuaterniond(3.29143574404111E-14,7.71242404223993E-16,1,6.87057791361391E-16)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.368613829731492,0.156518407358351), chrono.ChQuaterniond(2.38487553120783E-14,-2.27580538441475E-14,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.355913829731492,0.153755907358351), chrono.ChQuaterniond(2.38487553120783E-14,-2.27580538441475E-14,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762835561,0.360263829731491,0.200415907358351), chrono.ChQuaterniond(-6.12323399573674E-17,-9.3664216290059E-25,1,6.70601807553831E-16)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617163,0.317813829730607,0.156518407360262), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,1.74315279842105E-32,1.93528837224682E-48)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617163,0.307876329730607,0.166455907360262), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617163,0.305113829730607,0.153755907360262), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.317813829730607,0.350993407356443), chrono.ChQuaterniond(1.3738309013483E-16,-1.17756934401283E-16,0.707106781186548,-0.707106781186547)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.307876329730607,0.341055907356443), chrono.ChQuaterniond(8.47409175530384E-33,-1.80411241501588E-16,1,-3.41856075107737E-17)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.305113829730607,0.353755907356443), chrono.ChQuaterniond(8.47409175530384E-33,-1.80411241501588E-16,1,-3.41856075107737E-17)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.136572262834165,0.317813829730607,0.366455907358794), chrono.ChQuaterniond(0.5,0.5,-0.5,0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.126634762834165,0.307876329730607,0.366455907358794), chrono.ChQuaterniond(0.707106781186548,-3.81260211858883E-16,-0.707106781186547,0)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834165,0.305113829730607,0.366455907358794), chrono.ChQuaterniond(0.707106781186548,-3.81260211858883E-16,-0.707106781186547,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.167497262836957,0.317813829730607,0.141055907357911), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.177434762836957,0.307876329730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186548,3.81260211858883E-16,0.707106781186547,0)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.164734762836957,0.305113829730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186548,3.81260211858883E-16,0.707106781186547,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.167497262836957,0.317813829730607,0.366455907358794), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.177434762836957,0.307876329730607,0.366455907358794), chrono.ChQuaterniond(0.707106781186548,5.71890317788325E-16,0.707106781186547,1.90630105929442E-16)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.164734762836957,0.305113829730607,0.366455907358794), chrono.ChQuaterniond(0.707106781186548,5.71890317788325E-16,0.707106781186547,1.90630105929442E-16)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.136572262834165,0.317813829730607,0.141055907357911), chrono.ChQuaterniond(0.5,0.499999999999999,-0.5,0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.126634762834165,0.307876329730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186547,-3.81260211858884E-16,-0.707106781186548,-3.4863055968421E-32)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834165,0.305113829730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186547,-3.81260211858884E-16,-0.707106781186548,-3.4863055968421E-32)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.317813829730607,0.156518407360262), chrono.ChQuaterniond(0.707106781186548,0.707106781186547,1.74315279842105E-32,1.93528837224682E-48)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.307876329730607,0.166455907360262), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.305113829730607,0.153755907360262), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836957,0.317813829730607,0.141055907357911), chrono.ChQuaterniond(0.5,0.500000000000001,-0.5,0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836957,0.307876329730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186548,3.8126021208526E-16,-0.707106781186547,0)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836957,0.305113829730607,0.141055907357911), chrono.ChQuaterniond(0.707106781186548,3.8126021208526E-16,-0.707106781186547,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.317813829730607,0.36645590735784), chrono.ChQuaterniond(0.5,0.499999999999999,-0.500000000000001,0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836957,0.307876329730607,0.36645590735784), chrono.ChQuaterniond(0.707106781186547,-3.81260211858883E-16,-0.707106781186548,-7.62520423717767E-16)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.305113829730607,0.36645590735784), chrono.ChQuaterniond(0.707106781186547,-3.81260211858883E-16,-0.707106781186548,-7.62520423717767E-16)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.136572262834165,0.667413829730607,0.366455907358794), chrono.ChQuaterniond(0.500000000000001,-0.499999999999999,0.5,0.500000000000001)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.126634762834165,0.677351329730607,0.366455907358794), chrono.ChQuaterniond(9.53150529647208E-16,-0.707106781186547,-5.71890317788325E-16,0.707106781186548)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834165,0.680113829730607,0.366455907358794), chrono.ChQuaterniond(9.53150529647208E-16,-0.707106781186547,-5.71890317788325E-16,0.707106781186548)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.667413829730608,0.156518407360262), chrono.ChQuaterniond(3.81260211858883E-16,3.81260211858883E-16,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.677351329730608,0.166455907360262), chrono.ChQuaterniond(5.39183362404072E-16,0,-8.08775043606108E-16,1)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.329834762837399,0.680113829730608,0.153755907360262), chrono.ChQuaterniond(5.39183362404072E-16,0,-8.08775043606108E-16,1)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836957,0.667413829730607,0.141055907357911), chrono.ChQuaterniond(0.5,-0.499999999999999,0.5,0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836957,0.677351329730607,0.141055907357911), chrono.ChQuaterniond(9.53150529647208E-16,-0.707106781186547,1.90630106155817E-16,0.707106781186548)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836957,0.680113829730607,0.141055907357911), chrono.ChQuaterniond(9.53150529647208E-16,-0.707106781186547,1.90630106155817E-16,0.707106781186548)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.167497262836958,0.667413829730607,0.141055907357911), chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.500000000000001)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.177434762836958,0.677351329730607,0.141055907357911), chrono.ChQuaterniond(-1.90630105929442E-16,0.707106781186547,-5.71890317788325E-16,0.707106781186548)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.164734762836958,0.680113829730608,0.141055907357911), chrono.ChQuaterniond(-1.90630105929442E-16,0.707106781186547,-5.71890317788325E-16,0.707106781186548)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.3298347628374,0.667413829730607,0.350993407356444), chrono.ChQuaterniond(0.707106781186548,-0.707106781186547,4.99017146260166E-16,-4.99017146260166E-16)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.3298347628374,0.677351329730607,0.341055907356444), chrono.ChQuaterniond(-8.42960651116882E-16,1,-7.05716816097846E-16,-1.07481255273164E-31)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.3298347628374,0.680113829730607,0.353755907356444), chrono.ChQuaterniond(-8.42960651116882E-16,1,-7.05716816097846E-16,-1.07481255273164E-31)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.136572262834165,0.667413829730607,0.141055907357911), chrono.ChQuaterniond(0.500000000000001,-0.5,0.499999999999999,0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.126634762834165,0.677351329730607,0.141055907357911), chrono.ChQuaterniond(-9.53150529647208E-16,0.707106781186548,5.71890317788325E-16,-0.707106781186547)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834165,0.680113829730607,0.141055907357911), chrono.ChQuaterniond(-9.53150529647208E-16,0.707106781186548,5.71890317788325E-16,-0.707106781186547)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.314372262836958,0.667413829730607,0.36645590735784), chrono.ChQuaterniond(0.5,-0.5,0.499999999999999,0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.304434762836958,0.677351329730607,0.36645590735784), chrono.ChQuaterniond(-1.90630105929441E-16,0.707106781186548,5.71890317788325E-16,-0.707106781186547)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.317134762836958,0.680113829730607,0.36645590735784), chrono.ChQuaterniond(-1.90630105929441E-16,0.707106781186548,5.71890317788325E-16,-0.707106781186547)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616918,0.667413829730608,0.350993407356447), chrono.ChQuaterniond(0.707106781186548,-0.707106781186547,5.71890317788325E-16,-9.53150529647208E-16)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616918,0.677351329730608,0.341055907356447), chrono.ChQuaterniond(-8.08775043606108E-16,1,-1.07836672480814E-15,2.69591681202036E-16)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371616918,0.680113829730608,0.353755907356447), chrono.ChQuaterniond(-8.08775043606108E-16,1,-1.07836672480814E-15,2.69591681202036E-16)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.167497262836957,0.667413829730607,0.366455907358794), chrono.ChQuaterniond(-0.5,0.5,0.5,0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0.177434762836957,0.677351329730607,0.366455907358794), chrono.ChQuaterniond(1.39452223873684E-31,0.707106781186547,-3.81260211858883E-16,0.707106781186548)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(0.164734762836957,0.680113829730607,0.366455907358794), chrono.ChQuaterniond(1.39452223873684E-31,0.707106781186547,-3.81260211858883E-16,0.707106781186548)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.019365237161274,0.677351329730607,0.367553348962111), chrono.ChQuaterniond(-6.99327703394595E-16,0.707106781186548,4.44452932513277E-16,-0.707106781186547)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.029302737161274,0.667413829730607,0.367553348962111), chrono.ChQuaterniond(0.499999999999999,0.500000000000001,0.5,-0.5)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(-0.032065237161274,0.680113829730607,0.367553348962111), chrono.ChQuaterniond(0.499999999999999,0.500000000000001,0.5,-0.5)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0293027371612741,0.667413829730608,0.141055907358866), chrono.ChQuaterniond(0.5,-0.5,-0.499999999999999,-0.500000000000001)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0193652371612741,0.677351329730608,0.141055907358866), chrono.ChQuaterniond(-1.90630105929442E-16,0.707106781186548,-1.33441074173247E-15,0.707106781186547)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(-0.0320652371612741,0.680113829730608,0.141055907358866), chrono.ChQuaterniond(-1.90630105929442E-16,0.707106781186548,-1.33441074173247E-15,0.707106781186547)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617161,0.667413829730608,0.156518407360262), chrono.ChQuaterniond(3.81260211858883E-16,3.81260211858883E-16,0.707106781186547,0.707106781186548)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617161,0.677351329730608,0.166455907360262), chrono.ChQuaterniond(5.39183362404072E-16,0,-8.08775043606108E-16,1)))

# Visualization shape 
body_1_34_shape = chrono.ChVisualShapeModelFile() 
body_1_34_shape.SetFilename(shapes_dir +'body_1_34.obj') 
body_1.AddVisualShape(body_1_34_shape, chrono.ChFramed(chrono.ChVector3d(-0.0447652371617161,0.680113829730608,0.153755907360262), chrono.ChQuaterniond(5.39183362404072E-16,0,-8.08775043606108E-16,1)))

# Visualization shape 
body_1_156_shape = chrono.ChVisualShapeModelFile() 
body_1_156_shape.SetFilename(shapes_dir +'body_1_156.obj') 
body_1.AddVisualShape(body_1_156_shape, chrono.ChFramed(chrono.ChVector3d(0.101234762834166,0.540813829733399,0.384870907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_156_shape = chrono.ChVisualShapeModelFile() 
body_1_156_shape.SetFilename(shapes_dir +'body_1_156.obj') 
body_1.AddVisualShape(body_1_156_shape, chrono.ChFramed(chrono.ChVector3d(0.202834762834166,0.629713829733399,0.122640907358352), chrono.ChQuaterniond(0,0,1,0)))

# Visualization shape 
body_1_156_shape = chrono.ChVisualShapeModelFile() 
body_1_156_shape.SetFilename(shapes_dir +'body_1_156.obj') 
body_1.AddVisualShape(body_1_156_shape, chrono.ChFramed(chrono.ChVector3d(0.101234762834166,0.629713829733399,0.384870907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_159_shape = chrono.ChVisualShapeModelFile() 
body_1_159_shape.SetFilename(shapes_dir +'body_1_159.obj') 
body_1.AddVisualShape(body_1_159_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762834166,0.545576329733399,0.253449907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_156_shape = chrono.ChVisualShapeModelFile() 
body_1_156_shape.SetFilename(shapes_dir +'body_1_156.obj') 
body_1.AddVisualShape(body_1_156_shape, chrono.ChFramed(chrono.ChVector3d(0.202834762834166,0.540813829733399,0.122640907358352), chrono.ChQuaterniond(0,0,1,0)))

# Visualization shape 
body_1_159_shape = chrono.ChVisualShapeModelFile() 
body_1_159_shape.SetFilename(shapes_dir +'body_1_159.obj') 
body_1.AddVisualShape(body_1_159_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762834166,0.634476329733399,0.253449907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_159_shape = chrono.ChVisualShapeModelFile() 
body_1_159_shape.SetFilename(shapes_dir +'body_1_159.obj') 
body_1.AddVisualShape(body_1_159_shape, chrono.ChFramed(chrono.ChVector3d(0.152034762834166,0.456676329733399,0.253449907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_156_shape = chrono.ChVisualShapeModelFile() 
body_1_156_shape.SetFilename(shapes_dir +'body_1_156.obj') 
body_1.AddVisualShape(body_1_156_shape, chrono.ChFramed(chrono.ChVector3d(0.202834762834166,0.451913829733399,0.122640907358352), chrono.ChQuaterniond(0,0,1,0)))

# Visualization shape 
body_1_164_shape = chrono.ChVisualShapeModelFile() 
body_1_164_shape.SetFilename(shapes_dir +'body_1_164.obj') 
body_1.AddVisualShape(body_1_164_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834166,0.426513829733399,0.153755907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_156_shape = chrono.ChVisualShapeModelFile() 
body_1_156_shape.SetFilename(shapes_dir +'body_1_156.obj') 
body_1.AddVisualShape(body_1_156_shape, chrono.ChFramed(chrono.ChVector3d(0.101234762834166,0.451913829733399,0.384870907358352), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_164_shape = chrono.ChVisualShapeModelFile() 
body_1_164_shape.SetFilename(shapes_dir +'body_1_164.obj') 
body_1.AddVisualShape(body_1_164_shape, chrono.ChFramed(chrono.ChVector3d(0.139334762834166,0.426513829733399,0.347405907358352), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_1_1 = chrono.ChMarker()
marker_1_1.SetName('Coordinate System1')
body_1.AddMarker(marker_1_1)
marker_1_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999999116,0.0104902000008786,1.55431223447522E-15),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_1_1 = chrono.ChMarker()
marker_1_1.SetName('Coordinate System1')
body_1.AddMarker(marker_1_1)
marker_1_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(5.54096623275982E-17,0.0104902000008788,0),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_1_1 = chrono.ChMarker()
marker_1_1.SetName('Coordinate System1')
body_1.AddMarker(marker_1_1)
marker_1_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999999116,0.410890200003671,1.49880108324396E-15),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_1_1 = chrono.ChMarker()
marker_1_1.SetName('Coordinate System1')
body_1.AddMarker(marker_1_1)
marker_1_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(2.7745426725263E-16,0.410890200003671,-5.55111512312578E-17),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_1_1 = chrono.ChMarker()
marker_1_1.SetName('Coordinate System1')
body_1.AddMarker(marker_1_1)
marker_1_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.196799999997353,0.0612902000027925,-2.4980018054066E-16),chrono.ChQuaterniond(3.81260211858883E-16,-0.707106781186547,0.707106781186548,3.81260211858883E-16)))

exported_items.append(body_1)



# Rigid body part
body_2 = chrono.ChBodyAuxRef()
body_2.SetName('wheel_grouser-2')
body_2.SetPos(chrono.ChVector3d(0.359154889115197,0.0323643039009282,-0.311124889049841))
body_2.SetRot(chrono.ChQuaterniond(-0.00321429673581218,0.707099475531197,0.0032142967358056,0.707099475531197))
body_2.SetMass(3.37288824913969)
body_2.SetInertiaXX(chrono.ChVector3d(0.0254841571859158,0.0254929298825732,0.0451706451005354))
body_2.SetInertiaXY(chrono.ChVector3d(-3.6191474792222e-06,-2.56574208358306e-09,0.000178907680465351))
body_2.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0277857956919186,-0.000196880891992981,0.0154844680014934),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0290351109510424,-0.000185466335892667,0.0154474354087597), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_2_shape = chrono.ChVisualShapeModelFile() 
body_2_2_shape.SetFilename(shapes_dir +'body_2_2.obj') 
body_2.AddVisualShape(body_2_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.00253511095104247,-0.000185466335892663,0.0154474354087597), chrono.ChQuaterniond(0.669230211120907,0.228321975558784,-0.669230211120907,-0.228321975558784)))

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
body_2_1_collision_mesh.Transform(chrono.ChVector3d(-0.0290351109510424, -0.000185466335892667, 0.0154474354087597), mr) 
collshape = chrono.ChCollisionShapeTriangleMesh(mat_2,body_2_1_collision_mesh,False,False,sphereswept_r)
body_2.GetCollisionModel().AddShape(collshape)
body_2.EnableCollision(True)

exported_items.append(body_2)



# Rigid body part
body_3 = chrono.ChBodyAuxRef()
body_3.SetName('arm_assembly-3')
body_3.SetPos(chrono.ChVector3d(0.00102520554296287,0.0344001999999988,0.137900000000884))
body_3.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_3.SetMass(0.364051497440596)
body_3.SetInertiaXX(chrono.ChVector3d(0.00408204363389774,0.00104054206771479,0.00318444113837037))
body_3.SetInertiaXY(chrono.ChVector3d(-4.23413272321306e-11,-6.11651642363858e-10,-0.000719823333564868))
body_3.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-1.5922871557872e-08,0.0724885111288461,0.0511378350659033),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999999,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_2_shape = chrono.ChVisualShapeModelFile() 
body_3_2_shape.SetFilename(shapes_dir +'body_3_2.obj') 
body_3.AddVisualShape(body_3_2_shape, chrono.ChFramed(chrono.ChVector3d(-8.67361737988404E-18,0.14679,0.12551), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_3_3_shape = chrono.ChVisualShapeModelFile() 
body_3_3_shape.SetFilename(shapes_dir +'body_3_3.obj') 
body_3.AddVisualShape(body_3_3_shape, chrono.ChFramed(chrono.ChVector3d(2.38524477946811E-17,-0.05261,0.12551), chrono.ChQuaterniond(0.707106781186548,0,0.707106781186547,0)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_3.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999999,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_3.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.00500000000000001,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_3.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999999,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_7_shape = chrono.ChVisualShapeModelFile() 
body_3_7_shape.SetFilename(shapes_dir +'body_3_7.obj') 
body_3.AddVisualShape(body_3_7_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(-6.12303176911189E-17,-8.14015851325628E-17,1,1.65030317669818E-27)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_3.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.00500000000000001,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.00500000000000001,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999998,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.00500000000000001,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_12_shape = chrono.ChVisualShapeModelFile() 
body_3_12_shape.SetFilename(shapes_dir +'body_3_12.obj') 
body_3.AddVisualShape(body_3_12_shape, chrono.ChFramed(chrono.ChVector3d(1.88651178012478E-17,-0.0558,0.12551), chrono.ChQuaterniond(0.838331738920779,0,0.545160430990789,0)))

# Auxiliary marker (coordinate system feature)
marker_3_1 = chrono.ChMarker()
marker_3_1.SetName('arm_steer_marker')
body_3.AddMarker(marker_3_1)
marker_3_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.00102520554296289,-0.0143098000000013,0.263410000000884),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

exported_items.append(body_3)



# Rigid body part
body_4 = chrono.ChBodyAuxRef()
body_4.SetName('hub_assem-2')
body_4.SetPos(chrono.ChVector3d(-0.0908412600999432,-0.00388421335616071,-0.137900428831929))
body_4.SetRot(chrono.ChQuaterniond(0.00129962045144924,-0.106401479115182,0.994322390821007,0.00013907112985486))
body_4.SetMass(1.5598908069349)
body_4.SetInertiaXX(chrono.ChVector3d(0.00436080523071917,0.00230048447927596,0.00414454522173494))
body_4.SetInertiaXY(chrono.ChVector3d(0.000728725428031431,0.000534309901548283,-0.000448361570726464))
body_4.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0870481233327876,0.072850189784672,0.0857992020333658),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0713531392165592,0.0218992234984526,0.132196545530042), chrono.ChQuaterniond(0.666388969328945,-0.233706445072318,0.668133245007216,0.234318172586962)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.10393587812052,-0.00766152532301642,0.132281719647764), chrono.ChQuaterniond(0.674333044626005,-0.209685254219403,0.676098113951778,0.210234106175032)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_4.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961949241651301,0.0165247077633611,0.125761461911144), chrono.ChQuaterniond(0.994322390821007,0.000139071129845377,0.00129962045145291,0.106401479115182)))

# Visualization shape 
body_4_4_shape = chrono.ChVisualShapeModelFile() 
body_4_4_shape.SetFilename(shapes_dir +'body_4_4.obj') 
body_4.AddVisualShape(body_4_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.128151564600374,0.165433452720356,0.0755948276627572), chrono.ChQuaterniond(-0.00101730857317256,0.627854897824528,0.778329312645782,-0.000820632295209695)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.113244780633865,0.0353364251146471,0.132306053929816), chrono.ChQuaterniond(0.672485001165168,-0.215538590789487,0.674245233230107,0.216102763875997)))

# Visualization shape 
body_4_6_shape = chrono.ChVisualShapeModelFile() 
body_4_6_shape.SetFilename(shapes_dir +'body_4_6.obj') 
body_4.AddVisualShape(body_4_6_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961426426015955,0.0165247077633606,0.14576139357698), chrono.ChQuaterniond(0.999999145822587,4.70059926117162E-15,0.00130704020480688,1.24585519117578E-17)))

# Auxiliary marker (coordinate system feature)
marker_4_1 = chrono.ChMarker()
marker_4_1.SetName('hub_steer_marker')
body_4.AddMarker(marker_4_1)
marker_4_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-4.38649117029399E-13,-0.0218098000000027,-0.263410000000884),chrono.ChQuaterniond(0.500000000000002,-0.499999999999993,0.499999999999998,0.500000000000007)))

# Auxiliary marker (coordinate system feature)
marker_4_2 = chrono.ChMarker()
marker_4_2.SetName('hub_drive_marker')
body_4.AddMarker(marker_4_2)
marker_4_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-4.38676872605015E-13,0.0326901999999974,-0.304660000000883),chrono.ChQuaterniond(-4.66196092147042E-15,-9.61029288273744E-17,1,9.03880377663147E-15)))

exported_items.append(body_4)



# Rigid body part
body_5 = chrono.ChBodyAuxRef()
body_5.SetName('wheel_grouser-1')
body_5.SetPos(chrono.ChVector3d(0.376601151557989,0.0480085893051669,0.311124889049841))
body_5.SetRot(chrono.ChQuaterniond(0.469674639080807,0.528588434800004,0.469674639080808,-0.528588434799995))
body_5.SetMass(3.37288824913969)
body_5.SetInertiaXX(chrono.ChVector3d(0.0254841571859158,0.0448999798374464,0.0257635951456622))
body_5.SetInertiaXY(chrono.ChVector3d(4.60896625711343e-07,3.58968095515666e-06,-0.00229887412442416))
body_5.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0277857956919186,-0.000196880891992981,0.0154844680014934),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_5.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0290351109510424,-0.000185466335892615,0.0154474354087597), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_2_shape = chrono.ChVisualShapeModelFile() 
body_2_2_shape.SetFilename(shapes_dir +'body_2_2.obj') 
body_5.AddVisualShape(body_2_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.00253511095104247,-0.00018546633589267,0.0154474354087597), chrono.ChQuaterniond(0.669230211120907,0.228321975558784,-0.669230211120907,-0.228321975558784)))

# Collision Model

body_5.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_5 = chrono.ChContactMaterialNSC()

# Triangle mesh collision shape 
body_2_1_collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_2_1_collision.obj', False, True) 
mr = chrono.ChMatrix33d()
mr[0,0]=1; mr[1,0]=0; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
mr[0,2]=0; mr[1,2]=0; mr[2,2]=1 
body_2_1_collision_mesh.Transform(chrono.ChVector3d(-0.0290351109510424, -0.000185466335892615, 0.0154474354087597), mr) 
collshape = chrono.ChCollisionShapeTriangleMesh(mat_5,body_2_1_collision_mesh,False,False,sphereswept_r)
body_5.GetCollisionModel().AddShape(collshape)
body_5.EnableCollision(True)

exported_items.append(body_5)



# Rigid body part
body_6 = chrono.ChBodyAuxRef()
body_6.SetName('wheel_grouser-3')
body_6.SetPos(chrono.ChVector3d(0.00475768670292342,0.0476810719846456,0.311124889049842))
body_6.SetRot(chrono.ChQuaterniond(0.438765292178574,0.554513316683604,0.438765292178579,-0.554513316683599))
body_6.SetMass(3.37288824913969)
body_6.SetInertiaXX(chrono.ChVector3d(0.0254841571859158,0.0441316860235234,0.0265318889595851))
body_6.SetInertiaXY(chrono.ChVector3d(8.66665326483787e-07,3.51384778715071e-06,-0.00440419264281003))
body_6.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0277857956919186,-0.000196880891992981,0.0154844680014934),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_6.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0290351109510424,-0.000185466335892668,0.0154474354087597), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_2_shape = chrono.ChVisualShapeModelFile() 
body_2_2_shape.SetFilename(shapes_dir +'body_2_2.obj') 
body_6.AddVisualShape(body_2_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.00253511095104247,-0.000185466335892671,0.0154474354087597), chrono.ChQuaterniond(0.669230211120907,0.228321975558784,-0.669230211120907,-0.228321975558784)))

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
body_2_1_collision_mesh.Transform(chrono.ChVector3d(-0.0290351109510424, -0.000185466335892668, 0.0154474354087597), mr) 
collshape = chrono.ChCollisionShapeTriangleMesh(mat_6,body_2_1_collision_mesh,False,False,sphereswept_r)
body_6.GetCollisionModel().AddShape(collshape)
body_6.EnableCollision(True)

exported_items.append(body_6)



# Rigid body part
body_7 = chrono.ChBodyAuxRef()
body_7.SetName('wheel_grouser-4')
body_7.SetPos(chrono.ChVector3d(-0.0154309786671752,0.0319536160901309,-0.311124889049841))
body_7.SetRot(chrono.ChQuaterniond(-0.0126184239327423,0.70699418341133,0.0126184239327361,0.70699418341133))
body_7.SetMass(3.37288824913969)
body_7.SetInertiaXX(chrono.ChVector3d(0.0254841571859158,0.0255163642179265,0.0451472107651821))
body_7.SetInertiaXY(chrono.ChVector3d(-3.61793534298532e-06,9.36958556769571e-08,0.000701849675828553))
body_7.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0277857956919186,-0.000196880891992981,0.0154844680014934),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_7.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0290351109510424,-0.00018546633589267,0.0154474354087597), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_2_shape = chrono.ChVisualShapeModelFile() 
body_2_2_shape.SetFilename(shapes_dir +'body_2_2.obj') 
body_7.AddVisualShape(body_2_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.00253511095104247,-0.00018546633589267,0.0154474354087597), chrono.ChQuaterniond(0.669230211120907,0.228321975558784,-0.669230211120907,-0.228321975558784)))

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
body_2_1_collision_mesh.Transform(chrono.ChVector3d(-0.0290351109510424, -0.00018546633589267, 0.0154474354087597), mr) 
collshape = chrono.ChCollisionShapeTriangleMesh(mat_7,body_2_1_collision_mesh,False,False,sphereswept_r)
body_7.GetCollisionModel().AddShape(collshape)
body_7.EnableCollision(True)

exported_items.append(body_7)



# Rigid body part
body_8 = chrono.ChBodyAuxRef()
body_8.SetName('arm_assembly-1')
body_8.SetPos(chrono.ChVector3d(0.374599999998685,0.0344001999983202,-0.137900000000884))
body_8.SetRot(chrono.ChQuaterniond(4.16660120460961e-16,-2.63677968348465e-16,1,4.76768293758141e-15))
body_8.SetMass(0.364051497440596)
body_8.SetInertiaXX(chrono.ChVector3d(0.00408204363389774,0.00104054206771477,0.00318444113837038))
body_8.SetInertiaXY(chrono.ChVector3d(4.23413295709166e-11,-6.11651643544129e-10,0.000719823333564847))
body_8.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-1.5922871557872e-08,0.0724885111288461,0.0511378350659033),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_8.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999995,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.48277311503641E-17,-1.06871463972545E-17,-0.707106781186547)))

# Visualization shape 
body_3_2_shape = chrono.ChVisualShapeModelFile() 
body_3_2_shape.SetFilename(shapes_dir +'body_3_2.obj') 
body_8.AddVisualShape(body_3_2_shape, chrono.ChFramed(chrono.ChVector3d(-5.55111512312578E-17,0.14679,0.12551), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_3_3_shape = chrono.ChVisualShapeModelFile() 
body_3_3_shape.SetFilename(shapes_dir +'body_3_3.obj') 
body_8.AddVisualShape(body_3_3_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.05261,0.12551), chrono.ChQuaterniond(0.707106781186548,3.73835945085112E-17,0.707106781186547,-1.86871695855872E-18)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_8.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999995,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-5.39835192531853E-17,2.48277311480301E-17,0.707106781186548)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_8.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.00500000000000006,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-5.39835192531853E-17,2.48277311480301E-17,0.707106781186548)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_8.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999995,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-5.39835192531853E-17,2.48277311480301E-17,0.707106781186548)))

# Visualization shape 
body_3_7_shape = chrono.ChVisualShapeModelFile() 
body_3_7_shape.SetFilename(shapes_dir +'body_3_7.obj') 
body_8.AddVisualShape(body_3_7_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(-4.16660120460961E-16,-2.63677968348465E-16,1,4.76768293758141E-15)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_8.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.00500000000000006,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-5.39835192531853E-17,2.48277311480301E-17,0.707106781186548)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_8.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.00500000000000006,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.48277311503641E-17,-1.06871463972545E-17,-0.707106781186547)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_8.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.00499999999999995,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.48277311503641E-17,-1.06871463972545E-17,-0.707106781186547)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_8.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.00500000000000006,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.48277311503641E-17,-1.06871463972545E-17,-0.707106781186547)))

# Visualization shape 
body_3_12_shape = chrono.ChVisualShapeModelFile() 
body_3_12_shape.SetFilename(shapes_dir +'body_3_12.obj') 
body_8.AddVisualShape(body_3_12_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.0558,0.12551), chrono.ChQuaterniond(0.838331738920779,3.13804834059278E-17,0.545160430990789,2.04031983438433E-17)))

# Auxiliary marker (coordinate system feature)
marker_8_1 = chrono.ChMarker()
marker_8_1.SetName('arm_steer_marker')
body_8.AddMarker(marker_8_1)
marker_8_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998685,-0.0143098000016786,-0.263410000000884),chrono.ChQuaterniond(0.500000000000002,-0.499999999999998,0.499999999999997,0.500000000000002)))

exported_items.append(body_8)



# Rigid body part
body_9 = chrono.ChBodyAuxRef()
body_9.SetName('hub_assem-1')
body_9.SetPos(chrono.ChVector3d(0.465441260098182,-0.00388421335620462,0.13790042883193))
body_9.SetRot(chrono.ChQuaterniond(0.994322390821007,-0.000139071129845315,-0.00129962045145294,-0.106401479115182))
body_9.SetMass(1.5598908069349)
body_9.SetInertiaXX(chrono.ChVector3d(0.00455731911417193,0.0021027534296609,0.00414576238789725))
body_9.SetInertiaXY(chrono.ChVector3d(0.000296279277479684,0.000301244020441802,0.000626930626183416))
body_9.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0870481233327876,0.072850189784672,0.0857992020333658),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_9.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0713531392165592,0.0218992234984526,0.132196545530042), chrono.ChQuaterniond(0.666388969328945,-0.233706445072318,0.668133245007216,0.234318172586962)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_9.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.10393587812052,-0.00766152532301644,0.132281719647764), chrono.ChQuaterniond(0.674333044626005,-0.209685254219403,0.676098113951778,0.210234106175032)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_9.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961949241651302,0.0165247077633611,0.125761461911144), chrono.ChQuaterniond(0.994322390821007,0.000139071129845315,0.00129962045145294,0.106401479115182)))

# Visualization shape 
body_4_4_shape = chrono.ChVisualShapeModelFile() 
body_4_4_shape.SetFilename(shapes_dir +'body_4_4.obj') 
body_9.AddVisualShape(body_4_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.128151564600374,0.165433452720356,0.0755948276627572), chrono.ChQuaterniond(-0.00101730857317256,0.627854897824528,0.778329312645782,-0.000820632295209696)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_9.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.113244780633865,0.0353364251146471,0.132306053929816), chrono.ChQuaterniond(0.672485001165168,-0.215538590789487,0.674245233230107,0.216102763875997)))

# Visualization shape 
body_4_6_shape = chrono.ChVisualShapeModelFile() 
body_4_6_shape.SetFilename(shapes_dir +'body_4_6.obj') 
body_9.AddVisualShape(body_4_6_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961426426015956,0.0165247077633606,0.14576139357698), chrono.ChQuaterniond(0.999999145822587,4.70054962440968E-15,0.00130704020480689,7.7339870702252E-18)))

# Auxiliary marker (coordinate system feature)
marker_9_1 = chrono.ChMarker()
marker_9_1.SetName('hub_steer_marker')
body_9.AddMarker(marker_9_1)
marker_9_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998676,-0.0218098000000489,0.263410000000884),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_9_2 = chrono.ChMarker()
marker_9_2.SetName('hub_drive_marker')
body_9.AddMarker(marker_9_2)
marker_9_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998676,0.0326901999999504,0.304660000000884),chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_9)



# Rigid body part
body_10 = chrono.ChBodyAuxRef()
body_10.SetName('arm_assembly-2')
body_10.SetPos(chrono.ChVector3d(0.374599999998677,0.0344001999999511,0.137900000000883))
body_10.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_10.SetMass(0.364051497440596)
body_10.SetInertiaXX(chrono.ChVector3d(0.00408204363389774,0.00104054206771479,0.00318444113837037))
body_10.SetInertiaXY(chrono.ChVector3d(-4.23413272321306e-11,-6.11651642363858e-10,-0.000719823333564868))
body_10.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-1.5922871557872e-08,0.0724885111288461,0.0511378350659033),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_10.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_2_shape = chrono.ChVisualShapeModelFile() 
body_3_2_shape.SetFilename(shapes_dir +'body_3_2.obj') 
body_10.AddVisualShape(body_3_2_shape, chrono.ChFramed(chrono.ChVector3d(0,0.14679,0.12551), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_3_3_shape = chrono.ChVisualShapeModelFile() 
body_3_3_shape.SetFilename(shapes_dir +'body_3_3.obj') 
body_10.AddVisualShape(body_3_3_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.05261,0.12551), chrono.ChQuaterniond(0.707106781186548,0,0.707106781186547,0)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_10.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_10.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_10.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_7_shape = chrono.ChVisualShapeModelFile() 
body_3_7_shape.SetFilename(shapes_dir +'body_3_7.obj') 
body_10.AddVisualShape(body_3_7_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(-6.12303176911189E-17,-8.14015851325628E-17,1,1.65030317669818E-27)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_10.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186547,-4.32963728535968E-17,-2.33403801826582E-27,0.707106781186548)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_10.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_10.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_10.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.53662117527136E-43,2.33402930250183E-27,-0.707106781186547)))

# Visualization shape 
body_3_12_shape = chrono.ChVisualShapeModelFile() 
body_3_12_shape.SetFilename(shapes_dir +'body_3_12.obj') 
body_10.AddVisualShape(body_3_12_shape, chrono.ChFramed(chrono.ChVector3d(0,-0.0558,0.12551), chrono.ChQuaterniond(0.838331738920779,0,0.545160430990789,0)))

# Auxiliary marker (coordinate system feature)
marker_10_1 = chrono.ChMarker()
marker_10_1.SetName('arm_steer_marker')
body_10.AddMarker(marker_10_1)
marker_10_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998677,-0.0143098000000489,0.263410000000883),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

exported_items.append(body_10)



# Rigid body part
body_11 = chrono.ChBodyAuxRef()
body_11.SetName('arm_assembly-4')
body_11.SetPos(chrono.ChVector3d(-4.39059433324836e-13,0.0344001999999939,-0.137900000000884))
body_11.SetRot(chrono.ChQuaterniond(4.92844550549504e-16,-2.77555756156281e-16,1,4.44029194545789e-15))
body_11.SetMass(0.364051497440596)
body_11.SetInertiaXX(chrono.ChVector3d(0.00408204363389774,0.00104054206771477,0.00318444113837038))
body_11.SetInertiaXY(chrono.ChVector3d(4.23413298999252e-11,-6.1165164375427e-10,0.000719823333564848))
body_11.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-1.5922871557872e-08,0.0724885111288461,0.0511378350659033),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_11.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-1.44170911167254E-17,1.40037966721206E-17,-0.707106781186547)))

# Visualization shape 
body_3_2_shape = chrono.ChVisualShapeModelFile() 
body_3_2_shape.SetFilename(shapes_dir +'body_3_2.obj') 
body_11.AddVisualShape(body_3_2_shape, chrono.ChFramed(chrono.ChVector3d(2.57869724376375E-18,0.14679,0.12551), chrono.ChQuaterniond(0.5,0.5,0.5,-0.5)))

# Visualization shape 
body_3_3_shape = chrono.ChVisualShapeModelFile() 
body_3_3_shape.SetFilename(shapes_dir +'body_3_3.obj') 
body_11.AddVisualShape(body_3_3_shape, chrono.ChFramed(chrono.ChVector3d(1.30753355245048E-17,-0.05261,0.12551), chrono.ChQuaterniond(0.707106781186548,3.94589586905534E-17,0.707106781186547,-3.90456642436136E-17)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_11.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.92925761838102E-17,1.44170911143914E-17,0.707106781186547)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_11.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.92925761838102E-17,1.44170911143914E-17,0.707106781186547)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_11.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.14239,0.09071), chrono.ChQuaterniond(0.707106781186548,-2.92925761838102E-17,1.44170911143914E-17,0.707106781186547)))

# Visualization shape 
body_3_7_shape = chrono.ChVisualShapeModelFile() 
body_3_7_shape.SetFilename(shapes_dir +'body_3_7.obj') 
body_11.AddVisualShape(body_3_7_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(-4.92844550549504E-16,-2.77555756156281E-16,1,4.44029194545789E-15)))

# Visualization shape 
body_3_4_shape = chrono.ChVisualShapeModelFile() 
body_3_4_shape.SetFilename(shapes_dir +'body_3_4.obj') 
body_11.AddVisualShape(body_3_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.14239,0.14031), chrono.ChQuaterniond(0.707106781186548,-2.92925761838102E-17,1.44170911143914E-17,0.707106781186547)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_11.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.00499999999999999,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-1.44170911167254E-17,1.40037966721206E-17,-0.707106781186547)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_11.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0.005,0.17059,0.09071), chrono.ChQuaterniond(0.707106781186548,-1.44170911167254E-17,1.40037966721206E-17,-0.707106781186547)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_11.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.005,0.17059,0.14031), chrono.ChQuaterniond(0.707106781186548,-1.44170911167254E-17,1.40037966721206E-17,-0.707106781186547)))

# Visualization shape 
body_3_12_shape = chrono.ChVisualShapeModelFile() 
body_3_12_shape.SetFilename(shapes_dir +'body_3_12.obj') 
body_11.AddVisualShape(body_3_12_shape, chrono.ChFramed(chrono.ChVector3d(7.63897669613422E-18,-0.0558,0.12551), chrono.ChQuaterniond(0.838331738920779,-3.03660873191405E-17,0.545160430990788,-1.9520131475355E-17)))

# Auxiliary marker (coordinate system feature)
marker_11_1 = chrono.ChMarker()
marker_11_1.SetName('arm_steer_marker')
body_11.AddMarker(marker_11_1)
marker_11_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-4.38927891660169E-13,-0.014309800000005,-0.263410000000884),chrono.ChQuaterniond(0.500000000000002,-0.499999999999998,0.499999999999997,0.500000000000002)))

exported_items.append(body_11)



# Rigid body part
body_12 = chrono.ChBodyAuxRef()
body_12.SetName('hub_assem-3')
body_12.SetPos(chrono.ChVector3d(0.283758739899181,-0.00388421335783412,-0.137900428831929))
body_12.SetRot(chrono.ChQuaterniond(0.00129962045144908,-0.106401479115183,0.994322390821007,0.000139071129855213))
body_12.SetMass(1.5598908069349)
body_12.SetInertiaXX(chrono.ChVector3d(0.00436080523071917,0.00230048447927597,0.00414454522173494))
body_12.SetInertiaXY(chrono.ChVector3d(0.000728725428031433,0.000534309901548285,-0.000448361570726465))
body_12.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0870481233327876,0.072850189784672,0.0857992020333658),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_12.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0713531392165592,0.0218992234984526,0.132196545530042), chrono.ChQuaterniond(0.666388969328945,-0.233706445072318,0.668133245007216,0.234318172586962)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_12.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.10393587812052,-0.00766152532301642,0.132281719647764), chrono.ChQuaterniond(0.674333044626005,-0.209685254219403,0.676098113951778,0.210234106175032)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_12.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961949241651301,0.0165247077633611,0.125761461911144), chrono.ChQuaterniond(0.994322390821007,0.000139071129845418,0.00129962045145291,0.106401479115182)))

# Visualization shape 
body_4_4_shape = chrono.ChVisualShapeModelFile() 
body_4_4_shape.SetFilename(shapes_dir +'body_4_4.obj') 
body_12.AddVisualShape(body_4_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.128151564600374,0.165433452720356,0.0755948276627571), chrono.ChQuaterniond(-0.00101730857317258,0.627854897824528,0.778329312645782,-0.000820632295209721)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_12.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.113244780633865,0.0353364251146471,0.132306053929816), chrono.ChQuaterniond(0.672485001165168,-0.215538590789487,0.674245233230107,0.216102763875997)))

# Visualization shape 
body_4_6_shape = chrono.ChVisualShapeModelFile() 
body_4_6_shape.SetFilename(shapes_dir +'body_4_6.obj') 
body_12.AddVisualShape(body_4_6_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961426426015956,0.0165247077633606,0.14576139357698), chrono.ChQuaterniond(0.999999145822587,4.72100700412701E-15,0.00130704020480689,1.29104006833423E-17)))

# Auxiliary marker (coordinate system feature)
marker_12_1 = chrono.ChMarker()
marker_12_1.SetName('hub_steer_marker')
body_12.AddMarker(marker_12_1)
marker_12_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998685,-0.0218098000016759,-0.263410000000884),chrono.ChQuaterniond(0.500000000000002,-0.499999999999993,0.499999999999998,0.500000000000008)))

# Auxiliary marker (coordinate system feature)
marker_12_2 = chrono.ChMarker()
marker_12_2.SetName('hub_drive_marker')
body_12.AddMarker(marker_12_2)
marker_12_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998685,0.0326901999983242,-0.304660000000884),chrono.ChQuaterniond(-4.85310576447961E-15,-6.03149133031534E-16,1,9.37203331434489E-15)))

exported_items.append(body_12)



# Rigid body part
body_13 = chrono.ChBodyAuxRef()
body_13.SetName('hub_assem-4')
body_13.SetPos(chrono.ChVector3d(0.0918664656424674,-0.00388421335615691,0.137900428831929))
body_13.SetRot(chrono.ChQuaterniond(0.994322390821008,-0.000139071129845742,-0.00129962045144819,-0.106401479115182))
body_13.SetMass(1.5598908069349)
body_13.SetInertiaXX(chrono.ChVector3d(0.00455731911417192,0.0021027534296609,0.00414576238789726))
body_13.SetInertiaXY(chrono.ChVector3d(0.000296279277479677,0.000301244020441806,0.000626930626183415))
body_13.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0870481233327876,0.072850189784672,0.0857992020333658),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_13.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.0713531392165592,0.0218992234984526,0.132196545530042), chrono.ChQuaterniond(0.666388969328945,-0.233706445072318,0.668133245007217,0.234318172586962)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_13.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.10393587812052,-0.00766152532301643,0.132281719647764), chrono.ChQuaterniond(0.674333044626005,-0.209685254219402,0.676098113951778,0.210234106175032)))

# Visualization shape 
body_4_3_shape = chrono.ChVisualShapeModelFile() 
body_4_3_shape.SetFilename(shapes_dir +'body_4_3.obj') 
body_13.AddVisualShape(body_4_3_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961949241651301,0.0165247077633611,0.125761461911144), chrono.ChQuaterniond(0.994322390821008,0.000139071129845742,0.00129962045144819,0.106401479115182)))

# Visualization shape 
body_4_4_shape = chrono.ChVisualShapeModelFile() 
body_4_4_shape.SetFilename(shapes_dir +'body_4_4.obj') 
body_13.AddVisualShape(body_4_4_shape, chrono.ChFramed(chrono.ChVector3d(-0.128151564600374,0.165433452720356,0.0755948276627571), chrono.ChQuaterniond(-0.00101730857317254,0.627854897824528,0.778329312645782,-0.000820632295209681)))

# Visualization shape 
body_4_1_shape = chrono.ChVisualShapeModelFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_13.AddVisualShape(body_4_1_shape, chrono.ChFramed(chrono.ChVector3d(-0.113244780633865,0.0353364251146472,0.132306053929816), chrono.ChQuaterniond(0.672485001165168,-0.215538590789487,0.674245233230107,0.216102763875997)))

# Visualization shape 
body_4_6_shape = chrono.ChVisualShapeModelFile() 
body_4_6_shape.SetFilename(shapes_dir +'body_4_6.obj') 
body_13.AddVisualShape(body_4_6_shape, chrono.ChFramed(chrono.ChVector3d(-0.0961426426015955,0.0165247077633606,0.14576139357698), chrono.ChQuaterniond(0.999999145822587,4.70120440901168E-15,0.00130704020480687,1.46320688999867E-17)))

# Auxiliary marker (coordinate system feature)
marker_13_1 = chrono.ChMarker()
marker_13_1.SetName('hub_steer_marker')
body_13.AddMarker(marker_13_1)
marker_13_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.00102520554296288,-0.0218098000000012,0.263410000000884),chrono.ChQuaterniond(0.500000000000003,-0.500000000000002,-0.499999999999998,-0.499999999999998)))

# Auxiliary marker (coordinate system feature)
marker_13_2 = chrono.ChMarker()
marker_13_2.SetName('hub_drive_marker')
body_13.AddMarker(marker_13_2)
marker_13_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.00102520554296288,0.0326901999999981,0.304660000000884),chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_13)



# Rigid body part
body_14 = chrono.ChBodyAuxRef()
body_14.SetName('screw_force_mounts-1')
body_14.SetPos(chrono.ChVector3d(5.55111512312578e-17,1.73472347597681e-18,0.0875))
body_14.SetRot(chrono.ChQuaterniond(0.707106781186548,0,-0.707106781186547,0))
body_14.SetMass(0.00242749331416924)
body_14.SetInertiaXX(chrono.ChVector3d(1.87975765320691e-05,1.86076275076408e-05,2.12080845460832e-07))
body_14.SetInertiaXY(chrono.ChVector3d(-2.76811875210074e-24,2.27606678031718e-21,-3.94448716333094e-40))
body_14.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0875,-0.00782020102033652,-1.77808754797091e-21),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_14_1_shape = chrono.ChVisualShapeModelFile() 
body_14_1_shape.SetFilename(shapes_dir +'body_14_1.obj') 
body_14.AddVisualShape(body_14_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_14_2_shape = chrono.ChVisualShapeModelFile() 
body_14_2_shape.SetFilename(shapes_dir +'body_14_1.obj') 
body_14.AddVisualShape(body_14_2_shape, chrono.ChFramed(chrono.ChVector3d(-0.175,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_14_1 = chrono.ChMarker()
marker_14_1.SetName('Coordinate System2')
body_14.AddMarker(marker_14_1)
marker_14_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(5.55111512312578E-17,-0.0127,0.0875),chrono.ChQuaterniond(0.707106781186548,0,-0.707106781186547,0)))

# Auxiliary marker (coordinate system feature)
marker_14_2 = chrono.ChMarker()
marker_14_2.SetName('Coordinate System2-2')
body_14.AddMarker(marker_14_2)
marker_14_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(3.40798322461791E-17,-0.0127,-0.0875),chrono.ChQuaterniond(0.707106781186548,0,-0.707106781186547,0)))

exported_items.append(body_14)




# Mate constraint: Parallel27 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_0 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_0 , SW name: cobra_4_1_pyMarkers - Copy ,  SW ref.type:4 (4)
link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.0447652371612743,-0.281923629727815,-0.253755907358352)
dA = chrono.ChVector3d(0,1,0)
cB = chrono.ChVector3d(0,0,0)
dB = chrono.ChVector3d(0,1,0)
link_1.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_1.SetName("Parallel27")
exported_items.append(link_1)


# Mate constraint: Parallel28 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_0 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_0 , SW name: cobra_4_1_pyMarkers - Copy ,  SW ref.type:4 (4)
link_2 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.0447652371612743,-0.281923629727815,-0.253755907358352)
dA = chrono.ChVector3d(1,0,0)
cB = chrono.ChVector3d(0,0,0)
dB = chrono.ChVector3d(1,0,0)
link_2.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_2.SetName("Parallel28")
exported_items.append(link_2)


# Mate constraint: Parallel29 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_0 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_0 , SW name: cobra_4_1_pyMarkers - Copy ,  SW ref.type:4 (4)
link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.0447652371612743,-0.281923629727815,-0.253755907358352)
dA = chrono.ChVector3d(0,0,1)
cB = chrono.ChVector3d(0,0,0)
dB = chrono.ChVector3d(0,0,1)
link_3.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_3.SetName("Parallel29")
exported_items.append(link_3)


# Mate constraint: Coincident199 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: hub_assem-1/Strut-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: arm_assembly-2/DS3225MG Servo 25Kg 4.8-6.8V-1 ,  SW ref.type:2 (2)
link_4 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.374599999998676,0.181190199999951,0.263410000000884)
cB = chrono.ChVector3d(0.374599999998677,0.181190199999951,0.263410000000883)
dA = chrono.ChVector3d(0,1,0)
dB = chrono.ChVector3d(1.62803170264902e-16,-1,-3.30081589457431e-27)
link_4.Initialize(body_9,body_10,False,cA,cB,dB)
link_4.SetDistance(0)
link_4.SetName("Coincident199")
exported_items.append(link_4)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.374599999998676,0.181190199999951,0.263410000000884)
dA = chrono.ChVector3d(0,1,0)
cB = chrono.ChVector3d(0.374599999998677,0.181190199999951,0.263410000000883)
dB = chrono.ChVector3d(1.62803170264902e-16,-1,-3.30081589457431e-27)
link_5.SetFlipped(True)
link_5.Initialize(body_9,body_10,False,cA,cB,dA,dB)
link_5.SetName("Coincident199")
exported_items.append(link_5)


# Mate constraint: Concentric5 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: hub_assem-1/Strut-2 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_10 , SW name: arm_assembly-2/bearings-1 ,  SW ref.type:1 (1)
link_6 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.374599999998676,-0.0218098000000489,0.263410000000884)
dA = chrono.ChVector3d(9.25185853854297e-17,-1,0)
cB = chrono.ChVector3d(0.374599999998677,-0.0143098000000489,0.263410000000883)
dB = chrono.ChVector3d(0,1,0)
link_6.SetFlipped(True)
link_6.Initialize(body_9,body_10,False,cA,cB,dA,dB)
link_6.SetName("Concentric5")
exported_items.append(link_6)

link_7 = chrono.ChLinkMateGeneric()
link_7.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.374599999998676,-0.0218098000000489,0.263410000000884)
cB = chrono.ChVector3d(0.374599999998677,-0.0143098000000489,0.263410000000883)
dA = chrono.ChVector3d(9.25185853854297e-17,-1,0)
dB = chrono.ChVector3d(0,1,0)
link_7.Initialize(body_9,body_10,False,cA,cB,dA,dB)
link_7.SetName("Concentric5")
exported_items.append(link_7)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: wheel_grouser-1/wheel_hub_2-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_9 , SW name: hub_assem-1/Wheel Hub_n2-1 ,  SW ref.type:1 (1)
link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.374599999998676,0.0326901999999493,0.288660000000884)
dA = chrono.ChVector3d(9.63118473862323e-15,9.5159016911713e-15,-1)
cB = chrono.ChVector3d(0.374599999998676,0.0326901999999504,0.304660000000884)
dB = chrono.ChVector3d(-9.54965273525232e-15,-9.517668771164e-15,1)
link_8.SetFlipped(True)
link_8.Initialize(body_5,body_9,False,cA,cB,dA,dB)
link_8.SetName("Concentric6")
exported_items.append(link_8)

link_9 = chrono.ChLinkMateGeneric()
link_9.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.374599999998676,0.0326901999999493,0.288660000000884)
cB = chrono.ChVector3d(0.374599999998676,0.0326901999999504,0.304660000000884)
dA = chrono.ChVector3d(9.63118473862323e-15,9.5159016911713e-15,-1)
dB = chrono.ChVector3d(-9.54965273525232e-15,-9.517668771164e-15,1)
link_9.Initialize(body_5,body_9,False,cA,cB,dA,dB)
link_9.SetName("Concentric6")
exported_items.append(link_9)


# Mate constraint: Coincident200 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: wheel_grouser-1/wheel_hub_2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_9 , SW name: hub_assem-1/Wheel Hub_n2-1 ,  SW ref.type:2 (2)
link_10 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.374599999998676,0.0326901999999492,0.304660000000884)
cB = chrono.ChVector3d(0.374599999998676,0.0326901999999504,0.304660000000884)
dA = chrono.ChVector3d(9.63118473862323e-15,9.5159016911713e-15,-1)
dB = chrono.ChVector3d(-9.54965273525232e-15,-9.517668771164e-15,1)
link_10.Initialize(body_5,body_9,False,cA,cB,dB)
link_10.SetDistance(0)
link_10.SetName("Coincident200")
exported_items.append(link_10)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.374599999998676,0.0326901999999492,0.304660000000884)
dA = chrono.ChVector3d(9.63118473862323e-15,9.5159016911713e-15,-1)
cB = chrono.ChVector3d(0.374599999998676,0.0326901999999504,0.304660000000884)
dB = chrono.ChVector3d(-9.54965273525232e-15,-9.517668771164e-15,1)
link_11.SetFlipped(True)
link_11.Initialize(body_5,body_9,False,cA,cB,dA,dB)
link_11.SetName("Coincident200")
exported_items.append(link_11)


# Mate constraint: Concentric7 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: arm_assembly-3/bearings-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_13 , SW name: hub_assem-4/Strut-2 ,  SW ref.type:2 (2)
link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.00102520554296289,-0.0143098000000013,0.263410000000884)
dA = chrono.ChVector3d(0,-1,0)
cB = chrono.ChVector3d(0.00102520554296286,-0.0218098000000012,0.263410000000884)
dB = chrono.ChVector3d(-9.25185853854297e-17,1,0)
link_12.SetFlipped(True)
link_12.Initialize(body_3,body_13,False,cA,cB,dA,dB)
link_12.SetName("Concentric7")
exported_items.append(link_12)

link_13 = chrono.ChLinkMateGeneric()
link_13.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.00102520554296289,-0.0143098000000013,0.263410000000884)
cB = chrono.ChVector3d(0.00102520554296286,-0.0218098000000012,0.263410000000884)
dA = chrono.ChVector3d(0,-1,0)
dB = chrono.ChVector3d(-9.25185853854297e-17,1,0)
link_13.Initialize(body_3,body_13,False,cA,cB,dA,dB)
link_13.SetName("Concentric7")
exported_items.append(link_13)


# Mate constraint: Coincident201 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: arm_assembly-3/DS3225MG Servo 25Kg 4.8-6.8V-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_13 , SW name: hub_assem-4/Strut-2 ,  SW ref.type:2 (2)
link_14 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.00102520554296286,0.181190199999999,0.263410000000884)
cB = chrono.ChVector3d(0.00102520554296286,0.181190199999999,0.263410000000884)
dA = chrono.ChVector3d(1.62803170264902e-16,-1,-3.30081589457431e-27)
dB = chrono.ChVector3d(0,1,0)
link_14.Initialize(body_3,body_13,False,cA,cB,dB)
link_14.SetDistance(0)
link_14.SetName("Coincident201")
exported_items.append(link_14)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.00102520554296286,0.181190199999999,0.263410000000884)
dA = chrono.ChVector3d(1.62803170264902e-16,-1,-3.30081589457431e-27)
cB = chrono.ChVector3d(0.00102520554296286,0.181190199999999,0.263410000000884)
dB = chrono.ChVector3d(0,1,0)
link_15.SetFlipped(True)
link_15.Initialize(body_3,body_13,False,cA,cB,dA,dB)
link_15.SetName("Coincident201")
exported_items.append(link_15)


# Mate constraint: Concentric8 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_8 , SW name: arm_assembly-1/bearings-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: hub_assem-3/Strut-2 ,  SW ref.type:2 (2)
link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.374599999998685,-0.0143098000016786,-0.263410000000884)
dA = chrono.ChVector3d(5.55111512312546e-16,-1,-9.5604786859114e-15)
cB = chrono.ChVector3d(0.374599999998685,-0.0218098000016759,-0.263410000000884)
dB = chrono.ChVector3d(-1.06622989799674e-15,1,1.87023790551577e-14)
link_16.SetFlipped(True)
link_16.Initialize(body_8,body_12,False,cA,cB,dA,dB)
link_16.SetName("Concentric8")
exported_items.append(link_16)

link_17 = chrono.ChLinkMateGeneric()
link_17.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.374599999998685,-0.0143098000016786,-0.263410000000884)
cB = chrono.ChVector3d(0.374599999998685,-0.0218098000016759,-0.263410000000884)
dA = chrono.ChVector3d(5.55111512312546e-16,-1,-9.5604786859114e-15)
dB = chrono.ChVector3d(-1.06622989799674e-15,1,1.87023790551577e-14)
link_17.Initialize(body_8,body_12,False,cA,cB,dA,dB)
link_17.SetName("Concentric8")
exported_items.append(link_17)


# Mate constraint: Coincident202 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_8 , SW name: arm_assembly-1/DS3225MG Servo 25Kg 4.8-6.8V-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: hub_assem-3/Strut-2 ,  SW ref.type:2 (2)
link_18 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.374599999998685,0.181190199998321,-0.263410000000883)
cB = chrono.ChVector3d(0.374599999998685,0.181190199998324,-0.263410000000881)
dA = chrono.ChVector3d(3.92308342047645e-16,-1,-9.5604786859081e-15)
dB = chrono.ChVector3d(-1.15874848338217e-15,1,1.87023790551577e-14)
link_18.Initialize(body_8,body_12,False,cA,cB,dB)
link_18.SetDistance(0)
link_18.SetName("Coincident202")
exported_items.append(link_18)

link_19 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.374599999998685,0.181190199998321,-0.263410000000883)
dA = chrono.ChVector3d(3.92308342047645e-16,-1,-9.5604786859081e-15)
cB = chrono.ChVector3d(0.374599999998685,0.181190199998324,-0.263410000000881)
dB = chrono.ChVector3d(-1.15874848338217e-15,1,1.87023790551577e-14)
link_19.SetFlipped(True)
link_19.Initialize(body_8,body_12,False,cA,cB,dA,dB)
link_19.SetName("Coincident202")
exported_items.append(link_19)


# Mate constraint: Concentric9 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_11 , SW name: arm_assembly-4/bearings-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: hub_assem-2/Strut-2 ,  SW ref.type:2 (2)
link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-4.38922332401567e-13,-0.014309800000005,-0.263410000000884)
dA = chrono.ChVector3d(6.10622663543809e-16,-1,-8.88087613422183e-15)
cB = chrono.ChVector3d(-4.38646988170552e-13,-0.0218098000000027,-0.263410000000884)
dB = chrono.ChVector3d(-3.90616302234214e-17,1,1.80776617633716e-14)
link_20.SetFlipped(True)
link_20.Initialize(body_11,body_4,False,cA,cB,dA,dB)
link_20.SetName("Concentric9")
exported_items.append(link_20)

link_21 = chrono.ChLinkMateGeneric()
link_21.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-4.38922332401567e-13,-0.014309800000005,-0.263410000000884)
cB = chrono.ChVector3d(-4.38646988170552e-13,-0.0218098000000027,-0.263410000000884)
dA = chrono.ChVector3d(6.10622663543809e-16,-1,-8.88087613422183e-15)
dB = chrono.ChVector3d(-3.90616302234214e-17,1,1.80776617633716e-14)
link_21.Initialize(body_11,body_4,False,cA,cB,dA,dB)
link_21.SetName("Concentric9")
exported_items.append(link_21)


# Mate constraint: Coincident203 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_11 , SW name: arm_assembly-4/DS3225MG Servo 25Kg 4.8-6.8V-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: hub_assem-2/Strut-2 ,  SW ref.type:2 (2)
link_22 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-4.39014156844581e-13,0.181190199999995,-0.263410000000882)
cB = chrono.ChVector3d(-4.38668656691417e-13,0.181190199999997,-0.263410000000881)
dA = chrono.ChVector3d(4.47819493278907e-16,-1,-8.88087613421853e-15)
dB = chrono.ChVector3d(-1.31580215608851e-16,1,1.80776617633716e-14)
link_22.Initialize(body_11,body_4,False,cA,cB,dB)
link_22.SetDistance(0)
link_22.SetName("Coincident203")
exported_items.append(link_22)

link_23 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-4.39014156844581e-13,0.181190199999995,-0.263410000000882)
dA = chrono.ChVector3d(4.47819493278907e-16,-1,-8.88087613421853e-15)
cB = chrono.ChVector3d(-4.38668656691417e-13,0.181190199999997,-0.263410000000881)
dB = chrono.ChVector3d(-1.31580215608851e-16,1,1.80776617633716e-14)
link_23.SetFlipped(True)
link_23.Initialize(body_11,body_4,False,cA,cB,dA,dB)
link_23.SetName("Coincident203")
exported_items.append(link_23)


# Mate constraint: Concentric10 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: wheel_grouser-4/wheel_hub_2-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_4 , SW name: hub_assem-2/Wheel Hub_n2-1 ,  SW ref.type:1 (1)
link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-4.38706255165849e-13,0.0326901999999972,-0.288660000000883)
dA = chrono.ChVector3d(-1.34468347783088e-16,-8.79609957776578e-15,1)
cB = chrono.ChVector3d(-4.38701262525158e-13,0.0326901999999974,-0.304660000000883)
dB = chrono.ChVector3d(1.58383786951885e-16,8.67599275199803e-15,-1)
link_24.SetFlipped(True)
link_24.Initialize(body_7,body_4,False,cA,cB,dA,dB)
link_24.SetName("Concentric10")
exported_items.append(link_24)

link_25 = chrono.ChLinkMateGeneric()
link_25.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-4.38706255165849e-13,0.0326901999999972,-0.288660000000883)
cB = chrono.ChVector3d(-4.38701262525158e-13,0.0326901999999974,-0.304660000000883)
dA = chrono.ChVector3d(-1.34468347783088e-16,-8.79609957776578e-15,1)
dB = chrono.ChVector3d(1.58383786951885e-16,8.67599275199803e-15,-1)
link_25.Initialize(body_7,body_4,False,cA,cB,dA,dB)
link_25.SetName("Concentric10")
exported_items.append(link_25)


# Mate constraint: Coincident204 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: wheel_grouser-4/wheel_hub_2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: hub_assem-2/Wheel Hub_n2-1 ,  SW ref.type:2 (2)
link_26 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-4.38704103672285e-13,0.0326901999999974,-0.304660000000883)
cB = chrono.ChVector3d(-4.38701262525158e-13,0.0326901999999974,-0.304660000000883)
dA = chrono.ChVector3d(-1.34468347783088e-16,-8.79609957776578e-15,1)
dB = chrono.ChVector3d(1.58383786951885e-16,8.67599275199803e-15,-1)
link_26.Initialize(body_7,body_4,False,cA,cB,dB)
link_26.SetDistance(0)
link_26.SetName("Coincident204")
exported_items.append(link_26)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-4.38704103672285e-13,0.0326901999999974,-0.304660000000883)
dA = chrono.ChVector3d(-1.34468347783088e-16,-8.79609957776578e-15,1)
cB = chrono.ChVector3d(-4.38701262525158e-13,0.0326901999999974,-0.304660000000883)
dB = chrono.ChVector3d(1.58383786951885e-16,8.67599275199803e-15,-1)
link_27.SetFlipped(True)
link_27.Initialize(body_7,body_4,False,cA,cB,dA,dB)
link_27.SetName("Coincident204")
exported_items.append(link_27)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_6 , SW name: wheel_grouser-3/wheel_hub_2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_13 , SW name: hub_assem-4/Wheel Hub_n2-1 ,  SW ref.type:2 (2)
link_28 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.00102520554296295,0.0326901999999975,0.36350062043445)
dA = chrono.ChVector3d(4.16622924069702e-17,9.67379006382285e-15,-1)
cB = chrono.ChVector3d(0.00102520554296291,0.0326901999999981,0.304660000000884)
dB = chrono.ChVector3d(4.16622923990423e-17,9.67379006382442e-15,-1)
link_28.Initialize(body_6,body_13,False,cA,cB,dA,dB)
link_28.SetName("Concentric11")
exported_items.append(link_28)

link_29 = chrono.ChLinkMateGeneric()
link_29.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.00102520554296295,0.0326901999999975,0.36350062043445)
cB = chrono.ChVector3d(0.00102520554296291,0.0326901999999981,0.304660000000884)
dA = chrono.ChVector3d(4.16622924069702e-17,9.67379006382285e-15,-1)
dB = chrono.ChVector3d(4.16622923990423e-17,9.67379006382442e-15,-1)
link_29.Initialize(body_6,body_13,False,cA,cB,dA,dB)
link_29.SetName("Concentric11")
exported_items.append(link_29)


# Mate constraint: Coincident205 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: wheel_grouser-3/wheel_hub_2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_13 , SW name: hub_assem-4/Wheel Hub_n2-1 ,  SW ref.type:2 (2)
link_30 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.00102520554296295,0.0326901999999981,0.304660000000884)
cB = chrono.ChVector3d(0.00102520554296291,0.0326901999999981,0.304660000000884)
dA = chrono.ChVector3d(4.16622924069702e-17,9.67379006382285e-15,-1)
dB = chrono.ChVector3d(-4.16622923990423e-17,-9.67379006382442e-15,1)
link_30.Initialize(body_6,body_13,False,cA,cB,dB)
link_30.SetDistance(0)
link_30.SetName("Coincident205")
exported_items.append(link_30)

link_31 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.00102520554296295,0.0326901999999981,0.304660000000884)
dA = chrono.ChVector3d(4.16622924069702e-17,9.67379006382285e-15,-1)
cB = chrono.ChVector3d(0.00102520554296291,0.0326901999999981,0.304660000000884)
dB = chrono.ChVector3d(-4.16622923990423e-17,-9.67379006382442e-15,1)
link_31.SetFlipped(True)
link_31.Initialize(body_6,body_13,False,cA,cB,dA,dB)
link_31.SetName("Coincident205")
exported_items.append(link_31)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: wheel_grouser-2/wheel_hub_2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: hub_assem-3/Wheel Hub_n2-1 ,  SW ref.type:2 (2)
link_32 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.374599999998685,0.0326901999983247,-0.363500620434449)
dA = chrono.ChVector3d(2.24108596615843e-16,-9.30125282518174e-15,1)
cB = chrono.ChVector3d(0.374599999998685,0.0326901999983242,-0.304660000000884)
dB = chrono.ChVector3d(2.23581514261285e-16,-9.30072390235511e-15,1)
link_32.Initialize(body_2,body_12,False,cA,cB,dA,dB)
link_32.SetName("Concentric12")
exported_items.append(link_32)

link_33 = chrono.ChLinkMateGeneric()
link_33.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.374599999998685,0.0326901999983247,-0.363500620434449)
cB = chrono.ChVector3d(0.374599999998685,0.0326901999983242,-0.304660000000884)
dA = chrono.ChVector3d(2.24108596615843e-16,-9.30125282518174e-15,1)
dB = chrono.ChVector3d(2.23581514261285e-16,-9.30072390235511e-15,1)
link_33.Initialize(body_2,body_12,False,cA,cB,dA,dB)
link_33.SetName("Concentric12")
exported_items.append(link_33)


# Mate constraint: Coincident206 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: wheel_grouser-2/wheel_hub_2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: hub_assem-3/Wheel Hub_n2-1 ,  SW ref.type:2 (2)
link_34 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.374599999998685,0.0326901999983242,-0.304660000000884)
cB = chrono.ChVector3d(0.374599999998685,0.0326901999983242,-0.304660000000884)
dA = chrono.ChVector3d(2.24108596615843e-16,-9.30125282518174e-15,1)
dB = chrono.ChVector3d(-2.23581514261285e-16,9.30072390235511e-15,-1)
link_34.Initialize(body_2,body_12,False,cA,cB,dB)
link_34.SetDistance(0)
link_34.SetName("Coincident206")
exported_items.append(link_34)

link_35 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.374599999998685,0.0326901999983242,-0.304660000000884)
dA = chrono.ChVector3d(2.24108596615843e-16,-9.30125282518174e-15,1)
cB = chrono.ChVector3d(0.374599999998685,0.0326901999983242,-0.304660000000884)
dB = chrono.ChVector3d(-2.23581514261285e-16,9.30072390235511e-15,-1)
link_35.SetFlipped(True)
link_35.Initialize(body_2,body_12,False,cA,cB,dA,dB)
link_35.SetName("Coincident206")
exported_items.append(link_35)


# Mate constraint: Concentric25 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/5537T868_T-Slotted Framing-2 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_3 , SW name: arm_assembly-3/Steering Arm-1 ,  SW ref.type:1 (1)
link_36 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.00102520554296285,0.117400199999999,0.134145200000884)
dA = chrono.ChVector3d(5.38482581824738e-16,8.15634772288052e-16,-1)
cB = chrono.ChVector3d(0.00102520554296285,0.117400199999999,0.125400000000884)
dB = chrono.ChVector3d(1.22460635382238e-16,-2.44327250170582e-17,1)
link_36.SetFlipped(True)
link_36.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_36.SetName("Concentric25")
exported_items.append(link_36)

link_37 = chrono.ChLinkMateGeneric()
link_37.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.00102520554296285,0.117400199999999,0.134145200000884)
cB = chrono.ChVector3d(0.00102520554296285,0.117400199999999,0.125400000000884)
dA = chrono.ChVector3d(5.38482581824738e-16,8.15634772288052e-16,-1)
dB = chrono.ChVector3d(1.22460635382238e-16,-2.44327250170582e-17,1)
link_37.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_37.SetName("Concentric25")
exported_items.append(link_37)


# Mate constraint: Concentric26 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/5537T868_T-Slotted Framing-4 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_11 , SW name: arm_assembly-4/Steering Arm-1 ,  SW ref.type:2 (2)
link_38 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-4.38921553673037e-13,0.117400199999995,-0.135699999998963)
dA = chrono.ChVector3d(-9.65870286624315e-16,-8.73511389791494e-15,1)
cB = chrono.ChVector3d(-4.39059065930796e-13,0.117400199999994,-0.125400000000884)
dB = chrono.ChVector3d(0,-2.44327250137578e-17,-1)
link_38.SetFlipped(True)
link_38.Initialize(body_1,body_11,False,cA,cB,dA,dB)
link_38.SetName("Concentric26")
exported_items.append(link_38)

link_39 = chrono.ChLinkMateGeneric()
link_39.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-4.38921553673037e-13,0.117400199999995,-0.135699999998963)
cB = chrono.ChVector3d(-4.39059065930796e-13,0.117400199999994,-0.125400000000884)
dA = chrono.ChVector3d(-9.65870286624315e-16,-8.73511389791494e-15,1)
dB = chrono.ChVector3d(0,-2.44327250137578e-17,-1)
link_39.Initialize(body_1,body_11,False,cA,cB,dA,dB)
link_39.SetName("Concentric26")
exported_items.append(link_39)


# Mate constraint: Concentric27 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/5537T868_T-Slotted Framing-6 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_8 , SW name: arm_assembly-1/Steering Arm-1 ,  SW ref.type:1 (1)
link_40 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.374599999998685,0.117400199998322,-0.135700000013348)
dA = chrono.ChVector3d(-7.21274276511585e-16,-9.36784210960477e-15,1)
cB = chrono.ChVector3d(0.374599999998685,0.11740019999832,-0.125400000000884)
dB = chrono.ChVector3d(0,-2.44327250137578e-17,-1)
link_40.SetFlipped(True)
link_40.Initialize(body_1,body_8,False,cA,cB,dA,dB)
link_40.SetName("Concentric27")
exported_items.append(link_40)

link_41 = chrono.ChLinkMateGeneric()
link_41.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.374599999998685,0.117400199998322,-0.135700000013348)
cB = chrono.ChVector3d(0.374599999998685,0.11740019999832,-0.125400000000884)
dA = chrono.ChVector3d(-7.21274276511585e-16,-9.36784210960477e-15,1)
dB = chrono.ChVector3d(0,-2.44327250137578e-17,-1)
link_41.Initialize(body_1,body_8,False,cA,cB,dA,dB)
link_41.SetName("Concentric27")
exported_items.append(link_41)


# Mate constraint: Concentric28 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/5537T868_T-Slotted Framing-8 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_10 , SW name: arm_assembly-2/Steering Arm-1 ,  SW ref.type:1 (1)
link_42 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.374599999998677,0.11740019999995,0.133225000003052)
dA = chrono.ChVector3d(4.07289327359778e-16,8.80349115125891e-15,-1)
cB = chrono.ChVector3d(0.374599999998677,0.117400199999951,0.125400000000883)
dB = chrono.ChVector3d(1.22460635382238e-16,-2.44327250170582e-17,1)
link_42.SetFlipped(True)
link_42.Initialize(body_1,body_10,False,cA,cB,dA,dB)
link_42.SetName("Concentric28")
exported_items.append(link_42)

link_43 = chrono.ChLinkMateGeneric()
link_43.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.374599999998677,0.11740019999995,0.133225000003052)
cB = chrono.ChVector3d(0.374599999998677,0.117400199999951,0.125400000000883)
dA = chrono.ChVector3d(4.07289327359778e-16,8.80349115125891e-15,-1)
dB = chrono.ChVector3d(1.22460635382238e-16,-2.44327250170582e-17,1)
link_43.Initialize(body_1,body_10,False,cA,cB,dA,dB)
link_43.SetName("Concentric28")
exported_items.append(link_43)


# Mate constraint: Coincident231 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1/Vertical Tubes-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: arm_assembly-1/Steering Arm-1 ,  SW ref.type:2 (2)
link_44 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.368266916397202,0.0231902000027926,-0.125400000000883)
cB = chrono.ChVector3d(0.412099999998685,0.0344001999983202,-0.125400000000884)
dA = chrono.ChVector3d(-5.39183362724218e-16,-3.20145585429192e-25,-1)
dB = chrono.ChVector3d(0,-2.03744416706092e-17,1)
link_44.Initialize(body_1,body_8,False,cA,cB,dB)
link_44.SetDistance(0)
link_44.SetName("Coincident231")
exported_items.append(link_44)

link_45 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.368266916397202,0.0231902000027926,-0.125400000000883)
dA = chrono.ChVector3d(-5.39183362724218e-16,-3.20145585429192e-25,-1)
cB = chrono.ChVector3d(0.412099999998685,0.0344001999983202,-0.125400000000884)
dB = chrono.ChVector3d(0,-2.03744416706092e-17,1)
link_45.SetFlipped(True)
link_45.Initialize(body_1,body_8,False,cA,cB,dA,dB)
link_45.SetName("Coincident231")
exported_items.append(link_45)


# Mate constraint: Parallel23 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1/Vertical Tubes-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: arm_assembly-1/Steering Arm-1 ,  SW ref.type:2 (2)
link_46 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.387299999999115,0.0231902000027926,-0.119033083600004)
dA = chrono.ChVector3d(1,5.39183362724218e-16,6.47020035448468e-14)
cB = chrono.ChVector3d(0.399599999998685,-0.184384053261738,-0.125400000000884)
dB = chrono.ChVector3d(1,0,-2.77988306607176e-16)
link_46.Initialize(body_1,body_8,False,cA,cB,dA,dB)
link_46.SetName("Parallel23")
exported_items.append(link_46)


# Mate constraint: Coincident232 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1/Vertical Tubes-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_11 , SW name: arm_assembly-4/Steering Arm-1 ,  SW ref.type:2 (2)
link_47 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.00633308360191363,0.0231902000027924,-0.125400000000883)
cB = chrono.ChVector3d(0.0374999999995609,0.0344001999999939,-0.125400000000884)
dA = chrono.ChVector3d(-5.39183362724217e-16,-1.07836672559671e-15,-1)
dB = chrono.ChVector3d(0,-2.03744416706092e-17,1)
link_47.Initialize(body_1,body_11,False,cA,cB,dB)
link_47.SetDistance(0)
link_47.SetName("Coincident232")
exported_items.append(link_47)

link_48 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.00633308360191363,0.0231902000027924,-0.125400000000883)
dA = chrono.ChVector3d(-5.39183362724217e-16,-1.07836672559671e-15,-1)
cB = chrono.ChVector3d(0.0374999999995609,0.0344001999999939,-0.125400000000884)
dB = chrono.ChVector3d(0,-2.03744416706092e-17,1)
link_48.SetFlipped(True)
link_48.Initialize(body_1,body_11,False,cA,cB,dA,dB)
link_48.SetName("Coincident232")
exported_items.append(link_48)


# Mate constraint: Parallel24 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1/Vertical Tubes-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_11 , SW name: arm_assembly-4/Steering Arm-1 ,  SW ref.type:2 (2)
link_49 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.0127000000008841,0.0231902000027924,-0.10636691639809)
dA = chrono.ChVector3d(-1,-5.39183362724218e-16,9.86076131526265e-32)
cB = chrono.ChVector3d(-0.025000000000439,-0.184384053260064,-0.125400000000884)
dB = chrono.ChVector3d(-1,0,0)
link_49.Initialize(body_1,body_11,False,cA,cB,dA,dB)
link_49.SetName("Parallel24")
exported_items.append(link_49)


# Mate constraint: Coincident233 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1/Vertical Tubes-4 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: arm_assembly-3/Steering Arm-1 ,  SW ref.type:2 (2)
link_50 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.00955040000367915,0.0231902000027924,0.125400000000884)
cB = chrono.ChVector3d(-0.0364747944570371,0.0344001999999987,0.125400000000884)
dA = chrono.ChVector3d(-1.07836672480815e-15,-1.07836672480814e-15,1)
dB = chrono.ChVector3d(-1.22460635382238e-16,-2.03744416673088e-17,-1)
link_50.Initialize(body_1,body_3,False,cA,cB,dB)
link_50.SetDistance(0)
link_50.SetName("Coincident233")
exported_items.append(link_50)

link_51 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.00955040000367915,0.0231902000027924,0.125400000000884)
dA = chrono.ChVector3d(-1.07836672480815e-15,-1.07836672480814e-15,1)
cB = chrono.ChVector3d(-0.0364747944570371,0.0344001999999987,0.125400000000884)
dB = chrono.ChVector3d(-1.22460635382238e-16,-2.03744416673088e-17,-1)
link_51.SetFlipped(True)
link_51.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_51.SetName("Coincident233")
exported_items.append(link_51)


# Mate constraint: Parallel25 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1/Vertical Tubes-4 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: arm_assembly-3/Steering Arm-1 ,  SW ref.type:2 (2)
link_52 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.0127000000008841,0.0231902000027924,0.119033083600884)
dA = chrono.ChVector3d(-1,5.39183362404073e-16,-1.07836672512829e-15)
cB = chrono.ChVector3d(-0.0239747944570371,-0.184384053260059,0.125400000000884)
dB = chrono.ChVector3d(-1,-1.6280317026535e-16,4.00448941989414e-16)
link_52.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_52.SetName("Parallel25")
exported_items.append(link_52)


# Mate constraint: Coincident234 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1/Vertical Tubes-3 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: arm_assembly-2/Steering Arm-1 ,  SW ref.type:2 (2)
link_53 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.380933083598232,0.0231902000027923,0.125400000000884)
cB = chrono.ChVector3d(0.337099999998677,0.0344001999999511,0.125400000000883)
dA = chrono.ChVector3d(4.6841850577209e-25,4.6841850577209e-25,1)
dB = chrono.ChVector3d(-1.22460635382238e-16,-2.03744416673088e-17,-1)
link_53.Initialize(body_1,body_10,False,cA,cB,dB)
link_53.SetDistance(0)
link_53.SetName("Coincident234")
exported_items.append(link_53)

link_54 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.380933083598232,0.0231902000027923,0.125400000000884)
dA = chrono.ChVector3d(4.6841850577209e-25,4.6841850577209e-25,1)
cB = chrono.ChVector3d(0.337099999998677,0.0344001999999511,0.125400000000883)
dB = chrono.ChVector3d(-1.22460635382238e-16,-2.03744416673088e-17,-1)
link_54.SetFlipped(True)
link_54.Initialize(body_1,body_10,False,cA,cB,dA,dB)
link_54.SetName("Coincident234")
exported_items.append(link_54)


# Mate constraint: Parallel26 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1/Vertical Tubes-3 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: arm_assembly-2/Steering Arm-1 ,  SW ref.type:2 (2)
link_55 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.387299999999116,0.0231902000027923,0.122250400001766)
dA = chrono.ChVector3d(1,-5.39183362404072e-16,0)
cB = chrono.ChVector3d(0.399599999998677,-0.184384053260107,0.125400000000883)
dB = chrono.ChVector3d(1,1.6280317026535e-16,-1.22460635382238e-16)
link_55.Initialize(body_1,body_10,False,cA,cB,dA,dB)
link_55.SetName("Parallel26")
exported_items.append(link_55)


# Mate constraint: Coincident245 [MateCoincident] type:0 align:2 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1/Frame Top-Bottom-1/Front-Back Side Tube-1 ,  SW ref.type:6 (6)
#   Entity 1: C::E name: body_0 , SW name: screw_force_mounts-1 ,  SW ref.type:4 (4)
link_56 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(5.54096623275982e-17,0.0104902000008788,0)
cB = chrono.ChVector3d(4.47954917387185e-17,1.73472347597681e-18,0)
dB = chrono.ChVector3d(1.22464679914735e-16,0,1)
link_56.Initialize(body_1,body_14,False,cA,cB,dB)
link_56.SetDistance(0)
link_56.SetName("Coincident245")
exported_items.append(link_56)


# Mate constraint: Coincident246 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1/Frame Top-Bottom-1/Front-Back Side Tube-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_14 , SW name: screw_force_mounts-1/1_4-20_screw-2 ,  SW ref.type:2 (2)
link_57 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.00434339999808644,-1.73472347597681e-18,0.1)
cB = chrono.ChVector3d(3.40798322461791e-17,1.73472347597681e-18,-0.0875)
dA = chrono.ChVector3d(8.13891333652105e-16,1,0)
dB = chrono.ChVector3d(0,-1,0)
link_57.Initialize(body_1,body_14,False,cA,cB,dB)
link_57.SetDistance(0)
link_57.SetName("Coincident246")
exported_items.append(link_57)

link_58 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.00434339999808644,-1.73472347597681e-18,0.1)
dA = chrono.ChVector3d(8.13891333652105e-16,1,0)
cB = chrono.ChVector3d(3.40798322461791e-17,1.73472347597681e-18,-0.0875)
dB = chrono.ChVector3d(0,-1,0)
link_58.SetFlipped(True)
link_58.Initialize(body_1,body_14,False,cA,cB,dA,dB)
link_58.SetName("Coincident246")
exported_items.append(link_58)


# Mate constraint: Coincident247 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_0 , SW name: Assem6^cobra_4_1_pyMarkers - Copy-1/Frame Assy-1/Frame Top-Bottom-1/Front-Back Side Tube-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_0 , SW name: screw_force_mounts-1 ,  SW ref.type:4 (4)
link_59 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(5.55111512312578e-17,0.0104902000008788,-0.0746)
cB = chrono.ChVector3d(5.55111512312578e-17,1.73472347597681e-18,0.0875)
dA = chrono.ChVector3d(1,0,0)
dB = chrono.ChVector3d(-1,0,1.22464679914735e-16)
link_59.Initialize(body_1,body_14,False,cA,cB,dB)
link_59.SetDistance(0)
link_59.SetName("Coincident247")
exported_items.append(link_59)

link_60 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(5.55111512312578e-17,0.0104902000008788,-0.0746)
dA = chrono.ChVector3d(1,0,0)
cB = chrono.ChVector3d(5.55111512312578e-17,1.73472347597681e-18,0.0875)
dB = chrono.ChVector3d(-1,0,1.22464679914735e-16)
link_60.SetFlipped(True)
link_60.Initialize(body_1,body_14,False,cA,cB,dA,dB)
link_60.SetName("Coincident247")
exported_items.append(link_60)


# Auxiliary marker (coordinate system feature)
marker_0_1 = chrono.ChMarker()
marker_0_1.SetName('steer_arm_1')
body_0.AddMarker(marker_0_1)
marker_0_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998677,-0.0143098000000489,0.263410000000883),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_2 = chrono.ChMarker()
marker_0_2.SetName('steer_arm_2')
body_0.AddMarker(marker_0_2)
marker_0_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.00102520554296289,-0.0143098000000012,0.263410000000884),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_3 = chrono.ChMarker()
marker_0_3.SetName('steer_arm_3')
body_0.AddMarker(marker_0_3)
marker_0_3.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998685,-0.0143098000016786,-0.263410000000884),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_4 = chrono.ChMarker()
marker_0_4.SetName('steer_arm_4')
body_0.AddMarker(marker_0_4)
marker_0_4.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-4.38854993558744E-13,-0.014309800000005,-0.263410000000884),chrono.ChQuaterniond(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_5 = chrono.ChMarker()
marker_0_5.SetName('steer_hub_1')
body_0.AddMarker(marker_0_5)
marker_0_5.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998676,-0.0218098000000489,0.263410000000884),chrono.ChQuaterniond(-0.5,0.5,0.5,0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_6 = chrono.ChMarker()
marker_0_6.SetName('steer_hub_2')
body_0.AddMarker(marker_0_6)
marker_0_6.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.00102520554296286,-0.0218098000000012,0.263410000000884),chrono.ChQuaterniond(-0.5,0.5,0.5,0.5)))

# Auxiliary marker (coordinate system feature)
marker_0_7 = chrono.ChMarker()
marker_0_7.SetName('steer_hub_3')
body_0.AddMarker(marker_0_7)
marker_0_7.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998686,-0.021809800001676,-0.263410000000884),chrono.ChQuaterniond(0.500000000000007,-0.499999999999997,-0.499999999999993,-0.500000000000002)))

# Auxiliary marker (coordinate system feature)
marker_0_8 = chrono.ChMarker()
marker_0_8.SetName('steer_hub_4')
body_0.AddMarker(marker_0_8)
marker_0_8.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-4.38841277199862E-13,-0.0218098000000022,-0.263410000000885),chrono.ChQuaterniond(0.500000000000007,-0.499999999999998,-0.499999999999993,-0.500000000000002)))

# Auxiliary marker (coordinate system feature)
marker_0_9 = chrono.ChMarker()
marker_0_9.SetName('drive_hub_1')
body_0.AddMarker(marker_0_9)
marker_0_9.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998676,0.0326901999999504,0.304660000000884),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_10 = chrono.ChMarker()
marker_0_10.SetName('drive_hub_2')
body_0.AddMarker(marker_0_10)
marker_0_10.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.00102520554296288,0.0326901999999981,0.304660000000884),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_11 = chrono.ChMarker()
marker_0_11.SetName('drive_hub_3')
body_0.AddMarker(marker_0_11)
marker_0_11.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998686,0.0326901999983241,-0.304660000000884),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_12 = chrono.ChMarker()
marker_0_12.SetName('drive_hub_4')
body_0.AddMarker(marker_0_12)
marker_0_12.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-4.38863867396766E-13,0.0326901999999979,-0.304660000000884),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_13 = chrono.ChMarker()
marker_0_13.SetName('drive_wheel_1')
body_0.AddMarker(marker_0_13)
marker_0_13.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998676,0.0326901999999493,0.304660000000884),chrono.ChQuaterniond(0.996515638938112,4.3525550483416E-15,-5.34897499187557E-15,0.0834061229872693)))

# Auxiliary marker (coordinate system feature)
marker_0_14 = chrono.ChMarker()
marker_0_14.SetName('drive_wheel_2')
body_0.AddMarker(marker_0_14)
marker_0_14.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.00102520554296295,0.0326901999999981,0.304660000000884),chrono.ChQuaterniond(0.999650404071471,4.83872123341665E-15,-3.02512959443703E-16,0.0264399251085184)))

# Auxiliary marker (coordinate system feature)
marker_0_15 = chrono.ChMarker()
marker_0_15.SetName('drive_wheel_3')
body_0.AddMarker(marker_0_15)
marker_0_15.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.374599999998686,0.0326901999983241,-0.304660000000884),chrono.ChQuaterniond(0.999816178919164,4.65191995946034E-15,2.28667013718492E-17,0.0191731158521873)))

# Auxiliary marker (coordinate system feature)
marker_0_16 = chrono.ChMarker()
marker_0_16.SetName('drive_wheel_4')
body_0.AddMarker(marker_0_16)
marker_0_16.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-4.38923989859672E-13,0.0326901999999979,-0.304660000000884),chrono.ChQuaterniond(0.999472744354863,4.39354786867565E-15,-2.09998822109536E-16,0.0324689588955277)))

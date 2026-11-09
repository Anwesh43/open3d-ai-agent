from tools.three3d_tools import addBox, addCustomShape, addCylinder, addSphere, render 
from models.shapes_config import BoxShape, CylinderConfig 
addBox(boxConfig=BoxShape(width = 1, height = 1, depth = 1, x = 2, y = 0, z = 0, rotationXInRadians  = 0, rotationYInRadians = 0, rotationZInRadians  = 3.14 / 4, colorX  = 0, colorY = 1, colorZ = 0 ))
addCylinder(cylinderConfig = CylinderConfig(radius = 2, height = 2,  x = 0, y = 2, z = 0, rotationXInRadians  = 3.14 / 2, rotationYInRadians = 0, rotationZInRadians  = 3.14 / 4, colorX  = 0, colorY = 1, colorZ = 0 ))
render()



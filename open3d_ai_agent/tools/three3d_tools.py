from wrappers.three3d_wrapper import Three3dWrapper 
from models.shapes_config import CylinderConfig, SphereConfig, BoxShape, CustomShapesConfig 

three3DWrapper = Three3dWrapper()

def addCylinder(cylinderConfig : CylinderConfig):
    print(f"Calling addCylinder tool")
    return three3DWrapper.addCylinder(cylinderConfig=cylinderConfig)

def addSphere(sphereConfig : SphereConfig):
    print(f"Calling addSphere tool")
    return three3DWrapper.addSphere(sphereConfig=sphereConfig)

def addBox(boxConfig : BoxShape):
    print(f"Calling addBox tool")
    return three3DWrapper.addBox(boxConfig=boxConfig)

def addCustomShape(customShapeConfig : CustomShapesConfig):
    print(f"Calling addCustomShape tool")
    return three3DWrapper.addCustomShape(customShapeConfig=customShapeConfig)

def render():
    print(f"Calling render tool")
    return three3DWrapper.render()

def getTools():
    return [
        addSphere, 
        addBox, 
        addCustomShape,
        addCylinder 
    ]
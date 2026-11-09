import open3d as o3d
import numpy as np 
from models.shapes_config import BoxShape, SphereConfig, CylinderConfig, CustomShapesConfig 
class Three3dWrapper:
    def __init__(self):
        self.shapes = []

    def addBox(self, boxConfig : BoxShape):
        boxShape = o3d.geometry.TriangleMesh.create_box(width = boxConfig.width, height = boxConfig.height, depth = boxConfig.depth)
        boxShape.translate([boxConfig.x, boxConfig.y, boxConfig.z])
        boxShape.rotate([boxConfig.rotationXInRadians, boxConfig.rotationYInRadians, boxConfig.rotationZInRadians])
        boxShape.compute_vertex_normals()
        boxShape.paint_uniform_color([boxConfig.colorX, boxConfig.colorY, boxConfig.colorZ])
        self.shapes.append(boxShape)

    def addSphere(self, sphereConfig : SphereConfig):
        sphereShape = o3d.geometry.TriangleMesh.create_sphere(radius = sphereConfig.radius, resolution = sphereConfig.resolution)
        sphereShape.translate([sphereConfig.x, sphereConfig.y, sphereConfig.z])
        sphereShape.rotate([sphereConfig.rotationXInRadians, sphereConfig.rotationYInRadians, sphereConfig.rotationZInRadians])
        sphereShape.compute_vertex_normals()
        sphereShape.paint_uniform_color([sphereConfig.colorX, sphereConfig.colorY, sphereConfig.colorZ])
        self.shapes.append(sphereShape)
    
    def addCylinder(self, cylinderConfig : CylinderConfig):
        cylinderShape = o3d.geometry.TriangleMesh.create_cylinder(radius = cylinderConfig.radius, height = cylinderConfig.height)
        cylinderShape.translate([cylinderConfig.x, cylinderConfig.y, cylinderConfig.z])
        cylinderShape.rotate([cylinderConfig.rotationXInRadians, cylinderConfig.rotationYInRadians, cylinderConfig.rotationZInRadians])
        cylinderShape.compute_vertex_normals()
        cylinderShape.paint_uniform_color([cylinderConfig.colorX, cylinderConfig.colorY, cylinderConfig.colorZ])
        self.shapes.append(cylinderShape)    

    def addCustomShape(self, customShapeConfig : CustomShapesConfig):
        customShape = o3d.geometry.TriangleMesh()
        customShape.vertices = o3d.utility.Vector3dVector(customShapeConfig.vertices)
        customShape.triangles = o3d.utility.Vector3iVector(customShapeConfig.triangles)
        customShape.translate([customShapeConfig.x, customShapeConfig.y, customShapeConfig.z])
        customShape.rotate([customShapeConfig.rotationXInRadians, customShapeConfig.rotationYInRadians, customShapeConfig.rotationZInRadians])
        customShape.compute_vertex_normals()
        customShape.paint_uniform_color([customShapeConfig.colorX, customShapeConfig.colorY, customShapeConfig.colorZ])
        self.shapes.append(customShape)    

    def render(self):
        o3d.visualization.draw_geometries(self.shapes)
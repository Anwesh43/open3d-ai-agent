import open3d as o3d
import numpy as np 
from models.shapes_config import BoxShape, SphereConfig, CylinderConfig, CustomShapesConfig 
class Three3dWrapper:
    def __init__(self):
        self.shapes = []

    def _handleSuccess(self, shape : str):
        return {
            "status": "success",
            "message": f"Added shape {shape}"
        }

    def addBox(self, boxConfig : BoxShape):
        boxShape = o3d.geometry.TriangleMesh.create_box(width = boxConfig.width, height = boxConfig.height, depth = boxConfig.depth)
        boxShape.translate([boxConfig.x, boxConfig.y, boxConfig.z])
        angles = np.radians([boxConfig.rotationXInRadians, boxConfig.rotationYInRadians, boxConfig.rotationZInRadians]).astype(np.float64)
        boxShape.rotate(boxShape.get_rotation_matrix_from_xyz(angles))
        boxShape.compute_vertex_normals()
        boxShape.paint_uniform_color([boxConfig.colorX, boxConfig.colorY, boxConfig.colorZ])
        self.shapes.append(boxShape)
        return self._handleSuccess("box")

    def addSphere(self, sphereConfig : SphereConfig):
        sphereShape = o3d.geometry.TriangleMesh.create_sphere(radius = sphereConfig.radius, resolution = sphereConfig.resolution)
        sphereShape.translate([sphereConfig.x, sphereConfig.y, sphereConfig.z])
        angles = np.radians([sphereConfig.rotationXInRadians, sphereConfig.rotationYInRadians, sphereConfig.rotationZInRadians]).astype(np.float64)
        sphereShape.rotate(sphereShape.get_rotation_matrix_from_xyz(angles))
        sphereShape.compute_vertex_normals()
        sphereShape.paint_uniform_color([sphereConfig.colorX, sphereConfig.colorY, sphereConfig.colorZ])
        self.shapes.append(sphereShape)
        return self._handleSuccess("sphere")
    
    def addCylinder(self, cylinderConfig : CylinderConfig):
        cylinderShape = o3d.geometry.TriangleMesh.create_cylinder(radius = cylinderConfig.radius, height = cylinderConfig.height, resolution = 100, split = 4)
        cylinderShape.translate([cylinderConfig.x, cylinderConfig.y, cylinderConfig.z])
        angles = np.radians([cylinderConfig.rotationXInRadians, cylinderConfig.rotationYInRadians, cylinderConfig.rotationZInRadians]).astype(np.float64)
        cylinderShape.rotate(cylinderShape.get_rotation_matrix_from_xyz(angles))
        cylinderShape.compute_vertex_normals()
        cylinderShape.paint_uniform_color([cylinderConfig.colorX, cylinderConfig.colorY, cylinderConfig.colorZ])
        self.shapes.append(cylinderShape)  
        return self._handleSuccess("cylinder")  

    def addCustomShape(self, customShapeConfig : CustomShapesConfig):
        customShape = o3d.geometry.TriangleMesh()
        customShape.vertices = o3d.utility.Vector3dVector([[vertex.x, vertex.y, vertex.z] for vertex in customShapeConfig.vertices])
        customShape.triangles = o3d.utility.Vector3iVector([[triangle.x, triangle.y, triangle.z] for triangle in customShapeConfig.triangles])
        customShape.translate([customShapeConfig.x, customShapeConfig.y, customShapeConfig.z])
        angles = np.radians([customShapeConfig.rotationXInRadians, customShapeConfig.rotationYInRadians, customShapeConfig.rotationZInRadians]).astype(np.float64)
        customShape.rotate(customShape.get_rotation_matrix_from_xyz(angles))
        customShape.compute_vertex_normals()
        customShape.paint_uniform_color([customShapeConfig.colorX, customShapeConfig.colorY, customShapeConfig.colorZ])
        self.shapes.append(customShape)    
        return self._handleSuccess("customshape")

    def render(self):
        o3d.visualization.draw_geometries(self.shapes, zoom=0.7, front=[1, 1, 0.8], lookat=[0, 0, 0], up=[0, 0, 1])
        return self._handleSuccess("rendered all")
from pydantic import BaseModel, Field 
from typing import List 

class BoxShape(BaseModel):
    width : float = Field(default = 1.0, gt = 0)
    height : float = Field(default = 1.0, gt = 0)
    depth : float = Field(default = 1.0, gt = 0)
    x : int 
    y : int 
    z : int 
    rotationXInRadians : float
    rotationYInRadians : float
    rotationZInRadians : float
    colorX : float 
    colorY : float 
    colorZ : float 


class SphereConfig(BaseModel):
    radius : float
    resolution : int 
    x : int 
    y : int 
    z : int 
    rotationXInRadians : float
    rotationYInRadians : float
    rotationZInRadians : float
    colorX : float 
    colorY : float 
    colorZ : float 

class CylinderConfig(BaseModel):
    radius : float 
    height : float 
    x : int 
    y : int 
    z : int 
    rotationXInRadians : float
    rotationYInRadians : float
    rotationZInRadians : float
    colorX : float 
    colorY : float 
    colorZ : float 

class Point3DTriangle(BaseModel):
    x : int 
    y : int 
    z : int 

class Point3DVertex(BaseModel):
    x : float
    y : float 
    z : float 

class CustomShapesConfig(BaseModel):
    vertices: List[Point3DVertex]
    triangles : List[Point3DTriangle]
    x : int 
    y : int 
    z : int 
    rotationXInRadians : float
    rotationYInRadians : float
    rotationZInRadians : float
    colorX : float 
    colorY : float 
    colorZ : float   
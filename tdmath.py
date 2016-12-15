import math

def vectorCrossProduct(vec_one,vec_two): # Cross Product
    cp = (vec_one[1] * vec_two[2] - vec_one[2] * vec_two[1],
          vec_one[2] * vec_two[0] - vec_one[0] * vec_two[2],
          vec_one[0] * vec_two[1] - vec_one[1] * vec_two[0])
    return cp

def vectorAdd(vec_one,vec_two): # Vector Addition
    va = (vec_one[0] + vec_two[0],
          vec_one[1] + vec_two[1],
          vec_one[2] + vec_two[2])
    return va

def vectorSub(vec_one,vec_two): # Vector Substraction
    vs = (vec_one[0] - vec_two[0],
          vec_one[1] - vec_two[1],
          vec_one[2] - vec_two[2])
    return vs

def dotProduct(point,mod_matrix): # Dot product/multiplikation 
    dp = []
    for tupl in mod_matrix:
        dp.append(tupl[0] * point[0]
                  + tupl[1] * point[1]
                  + tupl[2] * point[2]
                  + tupl[3] * point[3])

    return dp

def vectorVectorAngle(vec_one, vec_two): # Angle between vectors
    angle = math.acos((vec_one[0]*vec_two[0]+vec_one[1]*vec_two[1]+vec_one[2]*vec_two[2])
            /((math.sqrt(math.pow(vec_one[0],2)+math.pow(vec_one[1],2)+math.pow(vec_one[2],2)))
                *(math.sqrt(math.pow(vec_two[0],2)+math.pow(vec_two[1],2)+math.pow(vec_two[2],2)))))
    return angle

def zInTriangle(a,b,c,point): # Finds Z for point in triangle
        # make two vectors with two sides of the triangle
        v1 = [n - m for n,m in zip(a,b)]
        v2 = [n - m for n,m in zip(a,c)]
        
        # calculate the crossproduct of the two vectors
        n = [(v1[1]*v2[2]- v1[2]*v2[1]),
        (v1[2]*v2[0]- v1[0]*v2[2]),
        (v1[0]*v2[1]- v1[1]*v2[0])]

        #dot product of n and a
        k = sum([f * e for f,e in zip(n,a)])

        # calculate the Z of the point
        z = 1/n[2]*(k - n[0]*point[0]-n[1]*point[1])

        return z
    
print(zInTriangle((0,0,0),(5,0,0),(0,5,0),(2,2,0)))
    

# check if inside triangle
def pointInTriangle(a, b, c, point):
	denominator = ((b[1] - c[1])*(a[0] - c[0]) + (c[0] - b[0])*(a[1] - c[1]))
	an = ((b[1] - c[1])*(point[0] - c[0]) + (c[0] - b[0])*(point[1] - c[1])) / denominator
	bn = ((c[1] - a[1])*(point[0] - c[0]) + (a[0] - c[0])*(point[1] - c[1])) / denominator
	cn = 1 - an - bn;
	
	if 0 <= an and an <= 1 and 0 <= bn and bn <= 1 and 0 <= cn and cn <= 1:
		its = True
	else: 
		its = False

	return its


def axisRotation(matrix,rx,ry,rz): # Rotates coordinates around the axis XYZ

    X = (
         (1,0,0,0),
         (0,math.cos(rx),-math.sin(rx),0),
         (0,math.sin(rx),math.cos(rx),0),
         (0,0,0,1)
        )

    Y = (
         (math.cos(ry),0,math.sin(ry),0),
         (0,1,0,0),
         (-math.sin(ry),0,math.cos(ry),0),
         (0,0,0,1)
        )

    Z = (
         (math.cos(rz),-math.sin(rz),0,0),
         (math.sin(rz),math.cos(rz),0,0),
         (0,0,1,0),
         (0,0,0,1)
        )

    rxy = [dotProduct(xyz,X) for xyz in Y]
    rxyz = [dotProduct(xyz,Z) for xyz in rxy]
    mod = [dotProduct(xyz,rxyz) for xyz in matrix]

    return mod

def scale(matrix,scale): # Scales coordinates, the object get bigger or smaller, from origo!

    S = (
         (scale,0,0,0),
         (0,scale,0,0),
         (0,0,scale,0),
         (0,0,0,1)
        )

    mod = [dotProduct(xyz,S) for xyz in matrix]

    return mod

def translationMatrix(matrix,dx,dy,dz): # Moves coordinates around, 'd' is delta.

    TM = (
          (1,0,0,dx),
          (0,1,0,dy),
          (0,0,1,dz),
          (0,0,0,1)
         )

    mod = [dotProduct(xyz,TM) for xyz in matrix]

    return mod

def wDivide(matrix): # Divide by W
    wd = []
    for point in matrix:
        wd.append((point[0] / point[3], point[1] / point[3], point[2] / point[3], point[3] / point[3]))

    return wd


def projectionMatrix(d,dx,dy,dz,rx,ry,rz,matrix): # d is the angle of view, xyz position, xyz rotation, world. 

    # A pinhole projection, infinit space
    PM = (
          (1,0,0,0),
          (0,1,0,0),
          (0,0,1,0),
          (0,0,1/d,0)
         )

    MatrixM = translationMatrix(matrix,-1*dx,-1*dy,-1*dz)
    MatrixR = axisRotation(MatrixM,rx,ry,rz)
    cam = [dotProduct(xyz,PM) for xyz in MatrixR]

    print(cam)

    # Clip points with negative Z
    cam = [point for point in cam if point[2] > 0]

    if len(cam) > 0:
        wcam = wDivide(cam)
    else:
        wcam = []

    return wcam

##def blender(light,objects,camera): # sets up the world an objects for the camera.
##
##    def transformToWorld(oneObject):
##        ob1 = axisRotation(oneObject,rx,ry,rz)
##        ob2 =translationMatrix(ob1,dx,dy,dz)
##        
##    
##    def checkObjectVisibility():
##
##        if
##
##        return desition
##
##    def createObject():
##        if 
##
##    world = 


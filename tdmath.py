import math

def vectorCross(vec_one,vec_two):
    cp = (vec_one[1] * vec_two[2] - vec_one[2] * vec_two[1],
          vec_one[2] * vec_two[0] - vec_one[0] * vec_two[2],
          vec_one[0] * vec_two[1] - vec_one[1] * vec_two[0])
    return cp

def vectorAdd(vec_one,vec_two):
    va = (vec_one[0] + vec_two[0], vec_one[1] + vec_two[1], vec_one[2] + vec_two[2])
    return va

def vectorSub(vec_one,vec_two):
    vs = (vec_one[0] - vec_two[0], vec_one[1] - vec_two[1], vec_one[2] - vec_two[2])
    return vs

def dotProduct(point,mod_matrix): # Dot product
    dp = []
    for tupl in mod_matrix:
        dp.append(tupl[0] * point[0] + tupl[1] * point[1] + tupl[2] * point[2] + tupl[3] * point[3])

    return dp

def wDivide(matrix): # Divide by W
    wd = []
    for point in matrix:
        wd.append((point[0] / point[3], point[1] / point[3], point[2] / point[3], point[3] / point[3]))

    return wd

def vectorVectorAngle(vector1, vector2):
    angle = math.acos()(ARCCOS((vector1[0]*vector2[0]+vector1[1]*vector2[1]+vector1[2]*vector2[2])
            /((math.sqrt(vector1[0]^2+vector1[1]^2+vector1[2]^2))*(math.sqrt(vector2[0]^2+vector2[1]^2+vector2[2]^2)))))
    return angle

def axisRotation(matrix,rx,ry,rz):

    Z = (
         (math.cos(rz),-math.sin(rz),0,0),
         (math.sin(rz),math.cos(rz),0,0),
         (0,0,1,0),
         (0,0,0,1)
        )

    Y = (
         (math.cos(ry),0,math.sin(ry),0),
         (0,1,0,0),
         (-math.sin(ry),0,math.cos(ry),0),
         (0,0,0,1)
        )

    X = (
         (1,0,0,0),
         (0,math.cos(rx),-math.sin(rx),0),
         (0,math.sin(rx),math.cos(rx),0),
         (0,0,0,1)
        )

    rxy = [dotProduct(xyz,X) for xyz in Y]
    rxyz = [dotProduct(xyz,Z) for xyz in rxy]
    mod = [dotProduct(xyz,rxyz) for xyz in matrix]

    return mod

def scale(matrix,scale):

    S = (
         (scale,0,0,0),
         (0,scale,0,0),
         (0,0,scale,0),
         (0,0,0,1)
        )

    mod = [dotProduct(xyz,S) for xyz in matrix]

    return mod

def translationMatrix(dx,dy,dz,matrix): # d is delta

    TM = (
          (1,0,0,dx),
          (0,1,0,dy),
          (0,0,1,dz),
          (0,0,0,1)
         )

    mod = [dotProduct(xyz,TM) for xyz in matrix]

    return mod


def projectionMatrix(d,dx,dy,dz,rx,ry,rz,matrix): # d is angle? x,y,z position 

    PM = (
          (1,0,0,0),
          (0,1,0,0),
          (0,0,1,0),
          (0,0,1/d,0)
         )

    MatrixM = translationMatrix(-1*dx,-1*dy,-1*dz,matrix)
    MatrixR = axisRotation(MatrixM,rx,ry,rz)
    cam = [dotProduct(xyz,PM) for xyz in MatrixR]
    
    wcam = wDivide(cam)

    return wcam



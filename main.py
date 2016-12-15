import tdmath
import math
from tkinter import *

rotateObjZ = 0
rotateObjY = 0
rotateObjX = 0

rotateCamZ = math.pi/2
rotateCamY = 0
rotateCamX = 0

shape = [(0,-20,0,1),(20,-20,0,1),(10,-10,0,1),(0,-20,0,1),(0,-10,0,1),(20,-10,0,1)
         ,(0,0,0,1),(20,0,0,1),(0,0,0,1),(20,10,0,1),(0,20,0,1)]

def RotObjX():
    global rotateObjX
    rotateObjX = rotateObjX + (math.pi/40)
    if rotateObjX > (math.pi * 2):
        rotateObjX = rotateObjX - (math.pi * 2)
    Draw3D()

def RotObjY():
    global rotateObjY
    rotateObjY = rotateObjY + (math.pi/40)
    if rotateObjY > (math.pi * 2):
        rotateObjY = rotateObjY - (math.pi * 2)
    Draw3D()

def RotObjZ():
    global rotateObjZ
    rotateObjZ = rotateObjZ + (math.pi/40)
    if rotateObjZ > (math.pi * 2):
        rotateObjZ = rotateObjZ - (math.pi * 2)
    Draw3D()

def RotCamX():
    global rotateCamX
    rotateCamX = rotateCamX + (math.pi/40)
    if rotateCamX > (math.pi * 2):
        rotateCamX = rotateCamX - (math.pi * 2)
    Draw3D()

def RotCamY():
    global rotateCamY
    rotateCamY = rotateCamY + (math.pi/40)
    if rotateCamY > (math.pi * 2):
        rotateCamY = rotateCamY - (math.pi * 2)
    Draw3D()

def RotCamZ():
    global rotateCamZ
    rotateCamZ = rotateCamZ + (math.pi/40)
    if rotateCamZ > (math.pi * 2):
        rotateCamZ = rotateCamZ - (math.pi * 2)
    Draw3D()

def Refresher():
    RotObjX()
    RotCamZ()
    root.after(100, Refresher)
    
def Draw3D():
    
    global rotateObjX
    global rotateObjY
    global rotateObjZ
    
    global rotateCamX
    global rotateCamY
    global rotateCamZ

    draw.delete(ALL)
    draw.configure(background='white')

    # Transform objects
    matrix = tdmath.axisRotation(shape,rotateObjX,rotateObjY,rotateObjZ) # Rotate Shape

    # Objects to world
    matrix = tdmath.translationMatrix(matrix,200,200,50) # Put in world

    # Camera view perspective
    matrix = tdmath.projectionMatrix(50,200,200,0,rotateCamX,rotateCamY,rotateCamZ,matrix) # Camera angle xyz xyzrotation world
    
    # Adapt to screen
    matrix = tdmath.translationMatrix(matrix,200,200,0)
    

    if len(matrix) > 0:
        polyg = []
        for point in matrix:
           polyg.append(point[0])
           polyg.append(point[1])


        draw.create_polygon(polyg,fill='',outline='black')
    else:
        pass
    
    matrix = []


root = Tk()
root.title("3D_Test")

var1 = StringVar()

label2 = Label(root, text="3D", bg="black", fg="white")
draw = Canvas(root, width=400, height=400)
button1 = Button(root, text="ObjX", command=RotObjX)
button2 = Button(root, text="ObjY", command=RotObjY)
button3 = Button(root, text="ObjZ", command=RotObjZ)

button4 = Button(root, text="CamX", command=RotCamX)
button5 = Button(root, text="CamY", command=RotCamY)
button6 = Button(root, text="CamZ", command=RotCamZ)

label2.grid(row=0, column=0, columnspan=2, sticky=W+E)
draw.grid(row=1, column=0, columnspan=2, sticky=W+E)
button1.grid(row=2, column=0, columnspan=1, sticky=W+E)
button2.grid(row=3, column=0, columnspan=1, sticky=W+E)
button3.grid(row=4, column=0, columnspan=1, sticky=W+E)

button4.grid(row=2, column=1, columnspan=2, sticky=W+E)
button5.grid(row=3, column=1, columnspan=2, sticky=W+E)
button6.grid(row=4, column=1, columnspan=2, sticky=W+E)

Draw3D()
Refresher()
root.mainloop()

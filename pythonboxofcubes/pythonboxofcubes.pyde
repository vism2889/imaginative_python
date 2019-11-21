# Python conversion 'box of cubes sketch'


offset = 200

def setup():
    size(900,720,P3D)
    
def draw():
    background(0)
    translate(width/2, height/2, -offset)
    rotateX(frameCount * .01)
    for x in range(-offset,offset,50):
        for y in range(-offset,offset,50):
            for z in range(-offset,offset,50):
                pushMatrix()
                translate(x,y,z)
                fill(colorFromOffset(x),colorFromOffset(y),colorFromOffset(z))
                box(30)
                popMatrix() 
                                       
def colorFromOffset(offset_c):
    return ((offset_c + offset)/(2.8*offset)* 255)

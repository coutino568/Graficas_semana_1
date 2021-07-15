

from gl import Renderer

width = 1920
height = 1080


myRenderer = Renderer(width, height)
myRenderer.glViewPort(100,100,1700,800)
myRenderer.glColor(0.2,0.8,0.7)


def drawflag():
    for x in range(int(width/3)):
        myRenderer.glColor(0,0.47,0.7)
        for y in range(height):
            myRenderer.glVertex(x, y)

    for x in range(int(width/3)):
        myRenderer.glColor(0,0.47,0.7)
        for y in range(height):
            myRenderer.glVertex(x+int(2*width/3), y)
    


drawflag()
#myRenderer.show()
myRenderer.glFinish("output.bmp")
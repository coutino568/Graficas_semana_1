

from gl import Renderer

windoWidth = 960
windowHeight = 540
viewportWidth= windoWidth*3/4
viewportHeight= windowHeight *3/4
viewportX=windoWidth/10
viewportY=windowHeight/10



myRenderer = Renderer(windoWidth, windowHeight)
myRenderer.glViewPort(viewportX,viewportY,viewportWidth,viewportHeight)



def drawflag():
    for x in range(int(viewportWidth/3)):
        myRenderer.glColor(0,0.47,0.7)
        for y in range(int(viewportHeight)):
            myRenderer.glVertex(viewportX+x, viewportY+y)

    for x in range(int(viewportWidth/3)):
        myRenderer.glColor(0,0.47,0.7)
        for y in range(int(viewportHeight)):
            myRenderer.glVertex(viewportX+x+int(2*viewportWidth/3), viewportY+y)
    
#miwate flag
myRenderer.glColor(0.2,0.8,0.7)
drawflag()


#normalized dot
myRenderer.glColor(0,0,0)
myRenderer.glVertexNormalized(0,0)


#myRenderer.show()
myRenderer.glFinish("output.bmp")
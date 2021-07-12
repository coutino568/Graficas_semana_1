

from gl import Renderer

width = 16
height = 10

# def render(filename):
#     with open(filename, "wb") as file :
    


myRenderer = Renderer(width, height)

myRenderer.glVertex(0,1)

myRenderer.show()

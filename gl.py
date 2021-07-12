import struct

def char(c):
    # used to reduce it to 1 byte

    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # used to reduce it to 2 byte
    return struct.pack('=h',w)

def dword(d):
    # used to reduce it to 4 byte
    return struct.pack('=l',d)

def color(r ,g ,b ):
    #takes input from 0 to 1
    return bytes ([ int(b *255), int(g *255), int(r*255)])



class Renderer(object):
    def __init__(self,width , height):
        
        # self.bgColor = color(1,1,1)
        # self.mainColor = color(0,0,0)
        self.bgColor = 0
        self.mainColor = 1
        self.glCreateWindow( width, height)

    def glInit(self):
        pass

    def glCreateWindow (self, width, height):
        self.width =width
        self.height = height
        self.glClear()    
    

    def glViewPort(self, width, height):
        pass


    def pickForegroundColor( self, r,g,b):
        self.mainColor = color(r,g,b)

    def glClear(self):
        # print (self.mainColor)
        self.matrix = [[self.bgColor for x in range(self.width)] for y in range(self.height)]
        # print ( " width " + str(self.width))
        # print ( " height " + str(self.height))
        # for x in range(self.width ) :
        #     for y in range(self.height):
        #         self.matrix[y][x] = self.bgColor


    def glClearColor (self, r,g,b):
        self.mainColor = color(r,g,b)

    def glVertex(self,x,y):
        print("glVertex")
        self.matrix[y][x] = 1

    def show(self):
        for x in range(self.height):
            print(self.matrix[x])



    def glColor(self):
        pass


    
    def glFinish(self):
        pass

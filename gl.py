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
        self.black = color(0,0,0)
        self.bgColor = color(0,0,0)
        self.viewportBgColor = color(1,1,1)
        self.mainColor = color(0,0,0)
        self.glCreateWindow( width, height)
        self.glViewPort(0,0,self.width,self.height)
        



    def glCreateWindow (self, width, height):
        self.width =width
        self.height = height
        self.glClear()    
    

    def glViewPort(self, x = 0, y=0, width=1, height = 1):
        self.viewportW =width
        self.viewportH = height
        self.viewportX = x
        self.viewportY = y
        print("Viewport is defined from : " + str(x) + " , " + str(y) )
        print("To :  " + str(x+width) + " , " + str(y+height) )
        self.glClearviewport()




    def pickForegroundColor( self, r,g,b):
        self.mainColor = color(r,g,b)

    def glClear(self):
        self.matrix = [[self.bgColor for x in range(self.width)] for y in range(self.height)]
        


    def glClearviewport(self):

        for x in range (self.viewportX, self.viewportX+ self.viewportW):
            for y in range (self.viewportY, self.viewportY+self.viewportH):
                self.matrix[y][x] = self.viewportBgColor

        


    def glClearColor (self, r,g,b):
        self.bgColor = color(r,g,b)

    def glVertex(self,x,y):
        if (x>= self.viewportX and x <= (self.viewportX+self.viewportW)  and   y>= self.viewportY and y <= self.viewportY+self.viewportH) :
            self.matrix[y][x] = self.mainColor
        # else :
        #     print("point out of viewport")


    def glColor(self, r,g,b):
        self.mainColor = color(r,g,b)


    
    def glFinish(self,filename):
        with open(filename, "wb") as file:
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.matrix[y][x])



    def show(self):
        for x in range(self.height):
            print(self.matrix[x])
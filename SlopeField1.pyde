from slider import Slider

'''Grid for graphing'''



sliderx = Slider(-3.0,3.0,2)
slidery = Slider(-3.0,3.0,1)

def setup():
    size(600,600)
    sliderx.position(20,20)
    slidery.position(20,50)
    
rangex = 10.0
rangey = 10.0

z = (.1,.1)
pointList = []

def draw():
    global z,c1,c2
    background(255)
    c1 = sliderx.value()
    c2 = slidery.value()
    sliderx.label = "c1"
    slidery.label = "c2"
    grid()
    for x in arange(-10.0,11,1): #change last number to decimal for denser field
        for y in arange(-10.0,11,1):
            m,b = slopept([x,y],fprime)
            tick(x,y,m,b)


def fprime(x,y): 
    '''The Differential Equation'''
    global c1,c2
    return c1*x + c2*y

def slopept(p,fprime):
    '''returns slope and yint of lin through point'''
    slope = fprime(p[0],p[1])
    yint = -slope*p[0] + p[1]
    return slope, yint

def f(x,m,b):
    '''line through (x,y)'''
    return m*x + b

def tick(x,y,m,b):
    '''makes the tick at (x,y)'''
    global xscl, yscl
    pushMatrix()
    translate(x*xscl,y*yscl) #go to the (x,y) point
    rotate(-atan(m))
    stroke(255,0,0) #red function
    line(-0.25*xscl,0,0.25*xscl,0)
    popMatrix()
    
def grid():
    global xscl, yscl
    xscl = float(width)/rangex
    yscl = float(-height)/rangey
    translate(width/2,height/2)
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(-10,11):
        line(i*xscl,-10*yscl,i*xscl,10*yscl)
        line(-10*xscl,i*yscl, 10*xscl,i*yscl)
        
    stroke(0) #black axes
    line(0,-10*yscl,0,10*yscl)
    line(-10*xscl,0, 10*xscl,0)
    #graphFunction()
    strokeWeight(1)


def arange(start,stop,step):
    '''DIY version of arange'''
    output = []
    x = start
    while x < stop:
        output.append(x)
        x += step
    return output
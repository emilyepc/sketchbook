def setup():
    global y
    size(500, 500)
    y = height / 2
    colorMode(HSB)
    
w = 50
hw = w / 2
#hw means half width
x = hw
y = 0
xdir = 1

def draw():
    global x
    global xdir
    background(0)
    noStroke()
    fill(x / 2, 255, 255);
    circle(x, y, w);
    x = x + xdir
    
    println("x: "
    
    if x == width:
        xdir = -1 #minus 1 makes it stop at the end has a semi circle. plus 1 makes it continue to go off the screen
    
    
#one equals is an assignment and two equals is called an equality operator

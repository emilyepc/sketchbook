def setup():
    global cx
    global cy
    global r
    global theta
    global px
    global c
    global py
    size(500, 500)
    cx = width / 2
    cy = height / 2
    px = cx
    py = cy
    background(0)
    colorMode(HSB)
    
    
cx = 0
cy = 0
r = 10
c = 1
theta = 0
#centre x = cx

px = 0
py = 0

def draw():
    global cx
    global cy
    global r
    global theta
    global px 
    global py
    global c
    x = cx - sin(theta) * r
    y = cy + cos(theta) * r
    
    stroke(c, 180, 255)
    line(px, py, x, y)
    circle(x, y, 10)
    
    r = r + 2
    c = (c + 1) % 256
#% means modulus, so it means it will repeat
    theta = theta + 0.2
    

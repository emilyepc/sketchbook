def setup(): 
    global x
    global y
    global a
    global b
    size(500, 500)
    colorMode(HSB)
    background(160, 255, 200)
    x = width / 2
    y = height / 2
    a = width / 2
    b = height / 2
    noStroke()

    
x = 1
y = 1
#when doing colour change, y in the hue value of HSB will be a descending wheel so changing colour every frame

    
def draw():
    global x
    global y
    fill(255, 255, 255)
    ellipse(250, 250, 150, 100)
    fill(y, 255, 255)
    circle(x, y, 80)
    circle(x, x, 80)
    circle(y, y, 80)
    circle(y, x, 80)
    x = x + 1
    y = y - 1
    
    
    
    

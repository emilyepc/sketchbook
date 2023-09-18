def setup():
    colorMode(HSB)#not v.
    background(255, 255, 255)#255 is white, in RGB
    size(500, 700)


def draw():
    
    fill(40, 255, 255)
    ellipse(240, 350, 400, 500)
    fill(130, 255, 255)
    triangle(30, 500, 250, 30, 460, 500)
    fill(255, 0, 230)
    ellipse(248, 320, 250, 177)
    fill(0)
    ellipse(mouseX, mouseY, 100, 100)

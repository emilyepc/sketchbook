def setup():
    size(500, 500)#use 8bits to store a bit, colours represented. RGBA. A(alpha)
    colorMode(HSB)
    #or colorMode(RGB). can switch between them in code. one of the three main coding principles=sequence
    #sequence of characters in programming is called a string
    #two types of variables are global and local. local stays inside the function. if its about the variable it's called the scope. so you would say a 'globalscope'
    
def draw():
    #Greyscale
    #RGBA
    #HSB better colour mode
    background(0)
    #the decimal turns them into 'floats'
    f = 10.0
    g = 20.0
    h = 5.0
    
    f = f + 1
    #or f += 1
    #subtracting
    g -= 30
    g = g - 27
    #multipying
    g = f * h
    #dividing
    g = f/h
    h = h/2.5
    
    #f =pow(g, 2)
    
    h = h - 7
    g += f
    f += g
    h = f - (g + 5)
    
    println("f: " + str(f))
    println("g: " + str(g))
    println("h: " + str(h))
    
#str converts into a character type
    
    stroke(80, 255, 255);
    line(mouseX, 10, 100, mouseY) #operator
    #rect can use 8 parameters if u want to have a curved line
    #processingmode has all the common code parameters
    #codingtrain does vids online
    #programming language called ALGOL(spelling might be wrong)
    #square brackets are arrays
    rectMode(CORNER)
    rect(20, 20, 50, 100)#second two are the width and the height of this
    circle(100, mouseY, 5)
    fill(90, mouseX / 2, 255)
    ellipse(200, 200, 100, 80)#last two are width and height
    point(90, 100)

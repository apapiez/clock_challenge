  
def setup():
    size(300, 350)

def draw():
    background(0, 0, 0)
    s = second()  # Values from 0 - 59
    m = minute()  # Values from 0 - 59
    h = hour()  # Values from 0 - 23
    
    stroke(209, 35, 35)
    strokeWeight(2)
    fill(0, 0, 0)
    rect(0, 350, 99, -(h*10)) #(X, Y, Xsize, Ysize)
    textSize(32)
    fill(209, 35, 35)
    text(h, 30, (350 - ((h*10)+2)))
    
    stroke(55, 67, 176)
    strokeWeight(2)
    fill(25, 47, 156)
    rect(101, 350, 99, -(m*5))
    textSize(32)
    fill(55, 67, 176)
    text(m, 130, (350 - ((m*5)+2)))
    
    stroke(29, 146, 53)
    strokeWeight(2)
    fill(0, 0, 0)
    rect(202, 350, 99, -(s*5))
    textSize(32)
    fill(29, 146, 53)
    text(s, 230, (350 - ((s*5)+2)))

"""
    stroke(209, 35, 35)
    fill(255, 255, 255)
    rect(0, 0, s, 33)
    
    stroke(55, 67, 176)
    fill(255, 255, 255)
    rect(0, 34, m, 33)
    
    stroke(29, 146, 53)
    fill(255, 255, 255)
    rect(0, 67, h, 65)
"""
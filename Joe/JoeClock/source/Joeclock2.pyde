  
def setup(): #__Init__ for processing
    size(302, 350) #Size of frame
    global MeImg, LandImg, AlexImg, Sun, Moon #Cheeky globals due to lack of class (Because it's a proof of concept not a script and we all know how classes look)
    LandImg = loadImage("Landy.png") #Open pngs
    MeImg = loadImage("Me.png")
    AlexImg = loadImage("Alex.png")
    Moon = loadImage("Moon.png")
    Sun = loadImage("Sun.png")
    
def draw():
    background(0, 0, 0) #Incase of disaster, include background (Also prerenders black)
    s = second()  # Values from 0 - 59
    m = minute()  # Values from 0 - 59
    h = hour()  # Values from 0 - 23  
    
    if h > 5 and h < 9: #6, 7, 8am
        background(220, 146, 17)
        image(Sun, (((((float(h)*60)+m)-420) / 660) * 290), 0) #Move sun from right to let during day hours
        image(Moon, ((((((float(h)+24)*60)+m)-1080) / 1740) * 600), 0) #Move Moon right to left during night hours
        print("Dawn", h)
    
    elif h < 18 and h > 8: #Between 9am to 6pm
        background(17, 126, 220)
        image(Sun, (((((float(h)*60)+m)-420) / 660) * 290), 0)
        print("Day", h)
    
    elif h > 17 and h < 21: # 6, 7, 8pm (18, 19, 20)
        background(220, 146, 17)
        image(Moon, ((((float((h)*60)+m)-1080) / 1740) * 600), 0)
        image(Sun, (((((float(h)*60)+m)-420) / 660) * 290), 0)
        print("Dusk", h)
        
    elif h < 6: #Early hours
        background(0, 0, 0)
        print((((((float(h)+24)*60)+m)-1080) / 1740) * 600) #NOT THIS
        image(Moon, ((((((float(h)+24)*60)+m)-1080) / 1740) * 600), 0)
        print("Wee hours", h)
        
    else: #All remaining hours (I.e. nighttime)
        background(0, 0, 0)
        image(Moon, (((((float(h)*60)+m)-1080) / 1740) * 600), 0)
        print("Evening", h)
        
        
        
    stroke(209, 35, 35) #Box boarder
    strokeWeight(2) #Box boarder linesize
    fill(179, 145, 125) #Box inner colour
    rect(0, 350, 99, -(h*10)) #draw rectangle (X, Y, Xsize, Ysize)
    textSize(32) #Text size
    fill(255, 255, 255) #Text colour
    text(h, 30, (350 - ((h*10)+2))) #Text (Message, X, Y)
    image(LandImg, 30, (350 - ((h*10)-5)), LandImg.width / 2, LandImg.height / 2) #Cheeky Landy
    
    stroke(55, 67, 176) #See above
    strokeWeight(2)
    fill(145, 125, 179)
    rect(101, 350, 99, -(m*5))
    textSize(32)
    fill(255, 255, 255)
    text(m, 130, (350 - ((m*5)+2)))
    image(AlexImg, 130, (350 - ((m*5)-5)), AlexImg.width / 2, AlexImg.height / 2) #Cheeky Alex
    
    stroke(29, 146, 53) #See above
    strokeWeight(2)
    fill(125, 179, 145)
    rect(202, 350, 99, -(s*5))
    textSize(32)
    fill(255, 255, 255)
    text(s, 230, (350 - ((s*5)+2)))
    image(MeImg, 230, (350 - ((s*5)-5))) #HELL YEAH, IT's GREAT TO BE THE KING
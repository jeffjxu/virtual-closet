from tkinter import * 
from CVStuff import *
from OOPy import *
####################################
# customize these functions
####################################

def init(data):
    data.iconWidth = data.width/3
    data.iconHeight = data.height/3
    data.margin = data.width/10
    data.hasStarted = False
    data.startWebcam = False
    data.AELogo = PhotoImage(file="AELogo.png")
    data.AFLogo = PhotoImage(file="AFLogo.png")
    data.NikeLogo = PhotoImage(file="NikeLogo.png")
    data.SLogo = PhotoImage(file="SupremeLogo.png")
    data.textSize = data.width//25
    data.runAE = False
    data.runAF = False
    data.runNike = False
    data.runSupreme = False
    data.menuMargin = data.width/20
    data.menuCellWidth = (data.width-data.menuMargin*2)/3
    data.menuCellHeight = (data.height-data.menuMargin*2)/3
    data.AEBrown = rgbString(191, 175, 155)
    data.AFMaroon = rgbString(88, 36, 40)
    data.NikeRed = rgbString(215, 31, 23)
    data.SupremeRed = rgbString(237, 28, 36)
    data.Glasses = Glasses(data)
    resizeImage(data)

def mousePressed(event, data):
    #when the user start the app by clicking on a brand
    if data.hasStarted == False:
        if event.x > data.margin and event.x < data.margin+data.iconWidth and \
        event.y > data.margin and event.y < data.margin+data.iconHeight:
            print("Run American Eagle")
            data.hasStarted = True
            data.runAE = True
        elif event.x > data.width-data.margin-data.iconWidth and \
        event.x < data.width-data.margin and event.y > data.margin and \
        event.y < data.margin+data.iconHeight:
            print("Run Abercrombie & Fitch")
            data.hasStarted = True
            data.runAF = True
        elif event.x > data.margin and event.x < data.margin+data.iconWidth and \
        event.y > data.height-data.margin-data.iconHeight and \
        event.y < data.height-data.margin:
            print("Run Nike")
            data.hasStarted = True
            data.runNike = True
        elif event.x > data.width-data.margin-data.iconWidth and event.x < data.width-data.margin \
        and event.y > data.height-data.margin-data.iconHeight and event.y < data.height-data.margin:
            print("Run Supreme")
            data.hasStarted = True
            data.runSupreme = True
    #check for mousePressed in clothes menu
    if data.runAE or data.runAF or data.runNike or data.runSupreme:
        for row in range(3):
            for col in range(3):
                if event.x > data.menuMargin+data.menuCellWidth*col and \
                event.x < data.menuMargin+data.menuCellWidth*(col+1) and \
                event.y > data.menuMargin+data.menuCellHeight*row and \
                event.y < data.menuMargin+data.menuCellHeight*(row+1):
                    data.startWebcam = True

def runWebcam(data):
    if data.startWebcam:
        runCV()

def keyPressed(event, data):
    if data.hasStarted:
        #press r to restart
        if event.keysym == "r":
            print("Restart")
            init(data)
        elif event.keysym == "s":
            runWebcam(data)

def timerFired(data):
    pass

#get color from rgb string
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

#resize image to fit the icons
def resizeImage(data):
    #first enlarge the image by the size of the icon
    data.AELogo = data.AELogo.zoom(int(data.iconWidth)//100, int(data.iconHeight)//100)
    #then shrink the image by the size the original image
    data.AELogo = data.AELogo.subsample(data.AELogo.width()//100, data.AELogo.height()//100)
    data.AFLogo = data.AFLogo.zoom(int(data.iconWidth)//100, int(data.iconHeight)//100)
    data.AFLogo = data.AFLogo.subsample(data.AFLogo.width()//120, data.AFLogo.height()//120)
    data.NikeLogo = data.NikeLogo.zoom(int(data.iconWidth)//50, int(data.iconHeight)//50)
    data.NikeLogo = data.NikeLogo.subsample(data.NikeLogo.width()//120, data.NikeLogo.height()//120)
    data.SLogo = data.SLogo.zoom(int(data.iconWidth)//50, int(data.iconHeight)//50)
    data.SLogo = data.SLogo.subsample(data.SLogo.width()//120, data.SLogo.height()//120)
    
def drawScreen(canvas, data):
    #create the square icon backgrounds
    canvas.create_rectangle(0, 0, data.width, data.height, fill="dark slate blue", width=0)
    canvas.create_rectangle(data.margin, data.margin, 
        data.margin + data.iconWidth, data.margin + data.iconHeight, fill=data.AEBrown, width=0)
    canvas.create_rectangle(data.width-data.margin-data.iconWidth, data.margin,
        data.width-data.margin, data.margin+data.iconHeight, fill=data.AFMaroon, width=0)
    canvas.create_rectangle(data.margin, data.height-data.margin-data.iconHeight,
        data.margin+data.iconWidth, data.height-data.margin, fill="Black", width=0)
    canvas.create_rectangle(data.width-data.margin-data.iconWidth, data.height-data.margin-data.iconHeight,
        data.width-data.margin, data.height-data.margin, fill=data.SupremeRed, width=0)
    #create the logos for each brand
    canvas.create_image(data.margin+data.iconWidth/2, data.margin+data.iconHeight/2, 
        image=data.AELogo)
    canvas.create_image(data.width-data.margin-data.iconWidth/2, data.margin+data.iconHeight/2, 
        image=data.AFLogo)
    canvas.create_image(data.margin+data.iconWidth/2, data.height-data.margin-data.iconHeight/2,
        image=data.NikeLogo)
    canvas.create_image(data.width-data.margin-data.iconWidth/2, data.height-data.margin-data.iconHeight/2,
        image=data.SLogo)
    #create instruction texts
    canvas.create_text(data.width/2, data.margin/2, text="Welcome to 15-112 Virtual Closet!", font="Verdana %d" % data.textSize, fill="lime green")
    canvas.create_text(data.width/2, data.height/2, text="Select a Brand to Begin", font="Verdana %d" % data.textSize, fill="lime green")
    
#draw the menu background based on the color of the company
def drawMenuBoard(canvas, data, company):
    if company == "AE":
        background = data.AEBrown
    canvas.create_rectangle(0, 0, data.width, data.height, fill="dark slate blue")
    for row in range(3):
        for col in range(3):
            canvas.create_rectangle(data.menuMargin+data.menuCellWidth*col,
            data.menuMargin+data.menuCellHeight*row,
            data.menuMargin+data.menuCellWidth*(col+1),
            data.menuMargin+data.menuCellHeight*(row+1), fill=background, width=5)
        
#for now this function loops over the boxes to only draw the glasses
#in the future it will draw from a list of clothes
def drawClothes(canvas, data):
    for row in range(3):
        for col in range(3):
            '''canvas.create_image(data.menuCellWidth*col+data.menuCellWidth/2, 
            data.menuCellHeight*row+data.menuCellHeight/2, image=data.Glasses.returnImage(data))'''
            canvas.create_text(data.menuMargin+data.menuCellWidth*col+data.menuCellWidth/2, 
            data.menuMargin+data.menuCellHeight*row+data.menuCellHeight/2, text="Clothing Here", 
            font="Verdana 10", fill="Black")
    
def redrawAll(canvas, data):
    if data.hasStarted == False:
        drawScreen(canvas, data)
    else:
        if data.runAE:
            drawMenuBoard(canvas, data, "AE")
            drawClothes(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 500)
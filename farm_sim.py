from graphics import *
from functions import *

def main():
    '''
    another way of setting the window size. would make it work better with bigger screens
    but the ui would need to be handled differently
    win_x = 1000
    win_y = 800
    '''
    
    win = GraphWin("Farm", 1280, 800)
    
    #Creating and drawing the boxes. (0,0) is in the top left, not bottom left
    exit = Text(Point(50, 765), "Exit")
    exit.setSize(30)
    exit_box = Rectangle(Point(15, 745), Point(85, 785))
    
    exit.draw(win)
    exit_box.draw(win)
    
    plot = Rectangle(Point(40, 40), Point(120, 120))
    #Center letter used to indicate what is being grown
    plot_type = Text(plot.getCenter(), "p")
    
    plot.draw(win)
    plot_type.draw(win)
    
    end = False
    while end == False:
        click = win.getMouse()
        
        #End program if the exit box is clicked on
        if in_box(Point(15, 745), Point(85, 785), click) == True:
                  end = True
    
        #Change box color to show that the crop has been watered
        elif in_box(Point(40, 40), Point(120, 120), click) == True:
            plot.setFill("sky blue")
    win.close()
    
main()

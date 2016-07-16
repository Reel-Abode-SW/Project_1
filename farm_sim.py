from graphics import *
from functions import *

def main():
    '''
    another way of setting the window size. would make it work better with bigger screens
    but the ui would need to be handled differently
    win_x = 1000
    win_y = 800
    '''
    #Gameplay variables
    mun=0; #money
    actions_per_day=5; #testing this thing
    crop_watered=False;
    plot_count=3; #0-based number of plots (so 4 plots)
    
    #Window setup
    win = GraphWin("Farm", 1280, 800);
    
    #Creating and drawing the boxes. (0,0) is in the top left, not bottom left
    next = Text(Point(1200, 50), "Next Day");
    next.setSize(30);
    next_box = Rectangle(Point(1116, 28), Point(1285, 72));
    next.draw(win); #Draw
    next_box.draw(win);
    
    exit = Text(Point(50, 765), "Exit");
    exit.setSize(30);
    exit_box = Rectangle(Point(0, 743), Point(87, 787));
    exit.draw(win); #Draw
    exit_box.draw(win);
    
    i=0;
    plot=[0,0,0,0];
    while i<plot_count:
        plot[i] = Rectangle(Point(40+i, 40+(i)), Point(120+(i), 120+(i)));
        #Center letter used to indicate what is being grown
        plot_type = Text(plot[i].getCenter(), "p");
        plot[i].draw(win);
        plot_type.draw(win);
        i+=0;
    
    end = False;
    while end == False:
        click = win.getMouse();
        plot_click=(in_box(Point(40, 40), Point(120, 120), click));
        
        #End program if the exit box is clicked on
        if in_box(Point(15, 745), Point(85, 785), click) == True:
            end = True;
        
        #Change box color to show that the crop has been watered
        if crop_watered == True:
            plot[0].setFill("sky blue");
        if crop_watered == False:
            plot[0].setFill("white");
            
    win.close()
    
main()

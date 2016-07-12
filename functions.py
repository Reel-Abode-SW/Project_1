def in_box(top_left, lower_right, click):
   '''
   Purpose:  
    to test a point to see if it is in a box defined by two other points (upper right and lower left) 
    Pre-conditions:  two points that define the box, a third point
    Post-conditions:  True if point3 is inside the box,False if not
   '''
   #initialize flag
   box_click = False

   #if the point's X is inside the other points' X's and
   #the point's Y is inside the other points' Y'
   if (top_left.getX() < click.getX() < lower_right.getX()) and (top_left.getY() < click.getY() < lower_right.getY()):
      #flag is set True
      box_click = True

   #return the flag
   return box_click
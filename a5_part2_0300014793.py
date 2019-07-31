#Family name: Aidan Charles
# Student number:  0300014793
# Course: IT1 1120
# Assignment Number 5 part 2
class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord
    def getx (self):
        '''(Point)->int
        Returns a int representing the x coordinate of a point'''
        return (self.x)
    
    def gety (self):
        '''(Point)->int
        Returns a int representing the y coordinate of a point'''
        return (self.y)

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle(Point):
    'class that represents a rectangle in the plane'
    def __init__(self, blP, trP, color="clear"):
        ''' (Rectangle,Point, Point,String) -> None
        initialize Rectangles bottom left and top right points as well as the color of the rectangle'''
        self.blP= blP
        self.trP = trP
        self.c = color
        

    def get_bottom_left(self):
        '''(Rectangle)->Point
        Returns the bottom left point of the rectangle'''
        return (self.blP)

    def get_top_right(self):
        '''(Rectangle)->Point
        Returns the top right point of the rectangle'''
        return(self.trP)
    
    def get_color(self):
        '''(Rectangle)->Point
        Returns color of the rectangle'''
        return (self.c)
    
    def reset_color(self,color):
         ''' (Rectangle,String)->None
         Resets the color of the rectangle'''
         self.c=color
        
    def get_perimeter(self):
        '''(Rectangle)->Number 
        Returns the perimeter of the rectangle  
        '''
        xT=self.trP.getx()-self.blP.getx()
        yT=self.trP.gety()-self.blP.gety()
        ans= 2*xT+2*yT
        return (ans)
    
    def get_area(self):
        '''(Rectangle)->Number
        Returns the area of the rectangle  
        '''        
        xT=self.trP.getx()-self.blP.getx()
        yT=self.trP.gety()-self.blP.gety()
        ans=xT*yT
        return(ans)
    
    def move (self,dx,dy):
        '''(Rectangle,number,number)->None
        changes the x and y coordinates of both the bottom left and top right points of the rectangle by factors of dx and dy this in turn moves the rectangle by dx, dy'''
        self.blP.move(dx,dy)
        self.trP.move(dx,dy)
        
    def intersects(self,rec):
        '''(Rectangle)->boolean
        Returns true if the two rectangles share a point in common otherwise it returns false  
        ''' 
        
        maxXR=max (self.trP.getx(),rec.trP.getx())
        maxYR=max (self.trP.gety(),rec.trP.gety())
        
        maxXL=max (self.blP.getx(),rec.blP.getx())
        maxYL=max (self.blP.gety(),rec.blP.gety())

        checkX=min (self.trP.getx(),rec.trP.getx())
        checkY=min (self.trP.gety(),rec.trP.gety())
        return (checkX>=maxXL and checkX<=maxXR and checkY>=maxYL and checkY<=maxYR)

    def contains(self,x,y):
        '''(Rectangle,Number,Number)->boolean
        Returns true if te point given is within the rectangles bounderies in other words if the rectangle contains the point
        '''
        return (min(self.trP.getx(),self.blP.getx()))<=x and max(self.trP.getx(),self.blP.getx())>=x and min(self.trP.gety(),self.blP.gety())<=y and max(self.trP.gety(),self.blP.gety())>=y
    

    def __eq__(self, other):
        '''(Rectangle,Rectangle)->bool
        Returns True if self and other are the same points'''
        return self.blP == other.blP and self.trP == other.trP and self.c == other.c
    
    def __repr__(self):
        '''(Rectangle)->str
        Returns canonical string representation Rectangle(bottom left point, top right point, color)'''
        return "Rectangle("+str(self.blP)+","+str(self.trP)+",'"+str(self.c)+"')"
    
    def __str__(self):
        '''(Rectangle)->str
        Returns nice string representation Rectangle(bottom left point, top right point, color).
        In this case we chose the same representation as in __repr__'''
        return 'I am a '+self.get_color()+" rectangle with bottom left corner at "+str(self.blP)+ " and top right corner at "+str(self.trP)+"."

class Canvas(Rectangle):
    'class that represents a collection of rectangles all found on a plane'
    
    def __init__(self):
        ''' (Canvas) -> None
        initialize Canvas which is a collection of rectangles in a list'''
        self.col=[]  

    def add_one_rectangle(self,Rect):
        '''(Canvas,Rectangle)->None
        This method simply adds a rectangle to the collection of rectangles found on the canvas 
        ''' 
        self.col.append(Rect)

    def count_same_color(self,color):
        '''(Canvas, String)->int
        Returns a integer that holds the number of rectangles that share the same color as the one specified in the method call 
        ''' 
        if len(self.col)==0:
            return(0)
        else:
            count=0
            for i in range (len(self.col)):
                if self.col[i].get_color().lower()==color.lower():
                    count+=1

            return(count)

    def total_perimeter (self):
        '''(Canvas)->integer
        Returns integer that holds the sum of the perimeters of all the rectangles in the canvas object  
        ''' 
        total=0
        for i in range (len(self.col)):
            total+=self.col[i].get_perimeter()

        return (total)
    
    def min_enclosing_rectangle (self):
        '''(Canvas)->Rectangle
        Returns the smallest rectangle that would enclose all the rectangles in the collection of rectangles found in the Canvas object   
        ''' 
        minX=self.col[0].get_bottom_left().getx() 
        minY=self.col[0].get_bottom_left().gety() 
        maxX=self.col[0].get_top_right().getx() 
        maxY=self.col[0].get_top_right().gety()

        for i in range (1,len(self.col)):
            if self.col[i].get_bottom_left().getx()<minX:
                minX=self.col[i].get_bottom_left().getx()
                
            if self.col[i].get_bottom_left().gety()<minY:
                minY=self.col[i].get_bottom_left().gety()
                
            if self.col[i].get_top_right().getx()>maxX:
                maxX=self.col[i].get_top_right().getx()

            if self.col[i].get_top_right().gety()>maxY:
                maxY=self.col[i].get_top_right().gety()

        return (Rectangle(Point(minX,minY), Point(maxX,maxY), color="red"))

    def common_point(self):
        '''(Canvas)->Boolean
        Returns True if all the rectangles in the canvas share at least one point in common otherwise it returns false    
        '''
        for i in range (len(self.col)-1):
            for j in range (1,len(self.col)-1):
                if not(self.col[i].intersects(self.col[j])):
                    return(False)
            
        return (True)                
            
    
    def __repr__(self):
        '''(Canvas)->str
        Returns canonical string representation the Canvas object which is a collection of rectangles'''
        return "Canvas("+str(self.col)+")"

    def __len__(self):
        '''(Canvas)->integer 
        Returns integer that represent the total number of elements in the collection of rectangles found in the canvas object'''
        return(len(self.col))
            


            
            
        
                
                
        
       

    
    


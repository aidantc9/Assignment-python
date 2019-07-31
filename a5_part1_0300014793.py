#Family name: Aidan Charles
# Student number:  0300014793
# Course: IT1 1120
# Assignment Number 5 part 1

#1a)

def largest_34(a):
    '''(list)->int
    Preconditions:List contains at least four elements, all the elements are unique and the elements are intergers
    This functions returns the sum of the thrid and fourth largest numbers in a list  
    '''
    a.sort()
    ans= a[len(a)-4] + a[len(a)-3]

    return (ans)




#1b)

def largest_third(a):
    '''(list)->int
    Preconditions:List contains at least three elements,all the elements are unique and the elements are intergers
    This functions returns the sum of len(a)//3 elements in a list this translates to the sum of of one third of elements noting that that one third is inluding the largest numbers
    '''
    numE= len (a)//3
    a.sort()
    ans=0
    for i in range (1,numE+1):
        ans+=a[len(a)-i]

    return (ans)


#1c)

def third_at_least(a):
    '''(list)->bolean
    Preconditions:List contains at least four elements and the elements are intergers 
    This functions returns true if there is a element in the list that appears at least len(a)//3 + 1 times or about one third the total length of the list. If the list does not have a element that appears that many it returns false
    '''
    a.sort()
    check=len(a)//3 + 1
    f=a[0]
    count=0
    for i in range (len(a)):
        if (f==a[i]):
            count+=1
        if count>=check:
            return (a[i])
        if (f!=a[i]):
            f=a[i]
            count=0
    return (None)

        
#1d)

def sum_tri(a,x):
    '''(list,int)->boolean
    Preconditions:all elements in the list are integers 
    This functions returns true if 3 elements in the list can be summed up to for a integer "x" otherwise it returns false  
    '''
    
    a.sort()
    for i in range (len(a)):
        j=0
        k=len(a)-1

        while (j<=k):
            if a[i]+a[j]+a[k]==x:
                return True
            if (x-a[i])>a[j]+a[k]:
                j+=1
            else:
                k-=1
    return(False)

          
            
        
            
        
        


    

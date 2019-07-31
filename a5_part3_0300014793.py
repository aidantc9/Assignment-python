#Family name: Aidan Charles
# Student number:  0300014793
# Course: IT1 1120
# Assignment Number 5 part 3
def digit_sum(n):
    '''(int)->int
    Preconditions:obviously integers are required 
    This functions returns the sum of each digit in a number   
    '''
    n=str(n)
    if len(n)==1:
        return (n)

    else:
        return (int(digit_sum(n[:len(n)-1]))+int(n[len(n)-1]))


def digital_root(n):
    '''(int)->int
    Preconditions:obviously integers are required 
    This functions returns the sum of each digit in a number and it will continue to return this sum untill it reaches a single digit number   
    '''
    n=str(n)
    if len(n)==1:
        n=int(n)
        return (n)
    else:
        return digital_root(digit_sum(n))



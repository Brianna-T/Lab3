"""
Course CS2301 MW 1:30-2:50pm
Instructor:Fuentes, Olac
Tovar, Brianna
Date of last modification: 3/10/2019
3rd Lab
This lab is over creating Binary Search Trees, returning a list of their elements and
printing them.

Honesty Statement:
    Academic dishonesty includes but is not limited to cheating, plagiarism and collusion. Cheating may involve
copying from or providing information to another student, possessing unauthorized materials during a test, or
falsifying data (for example program outputs) in laboratory reports. Plagiarism occurs when someone
represents the work or ideas of another person as his/her own. Collusion involves collaborating with another
person to commit an academically dishonest act. Professors are required to - and will - report academic
dishonesty and any other violation of the Standards of Conduct to the Dean of Students.
    I herby state hereby this code is mine and mine alone.
"""
class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right   
        
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
    
#def PrintFigure(T): #I was not able to complete this method
#    return None

    
def IterativeSearch(T,k): #repeated search, looks left and looks right repeatedly
    #everytime its returning back its own method, needs fixing since returns None
    if T is None:
        return T
    if T.item>k:
        return IterativeSearch(T.left,k)
    if T.item<k:
        return IterativeSearch(T.right,k)
       
def Balanced(T,A): #inserting list without calling Insert method, needs to be fixed
    #since its not returning a balanced BST
    if T == None:
        T =  BST(A)
    elif T.item > A.head:
        T.left = Balanced(T.left,A.next)
    else:
        T.right = Balanced(T.right,A.next)
    return T

def Extraction(T,List):#creating a new list, comparing the item to either put
    #the item at the beginning of the list (head) or to the next, needs to be fixed
    #since it keeps returning None
    B=List()
    if T is None or B.head is None:
        return None
    while T is not None:
        if T.item>B.head:
            B.head=T.left
        if T.item<B.head:
            B.next=T.right
        return Extraction(T, B.next)
    

def DepthNum(T):#start by getting the largest item, printing its depth, then 
    #using that depth to go backwards until reaching depth 0, each time returning
    #the depth and its items
    if T is None:
        return T
    depth=Largest(T)
    print(Find(T,depth))
    return depth-1, DepthNum(T.item)
    
    
# Code to test the functions above
T = None
A=List()
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T,a)
    
InOrder(T)
print()
InOrderD(T,'')
print()

print(SmallestL(T).item)
print(Smallest(T).item)

print(IterativeSearch(T,90))
print(Balanced(T,A))
print(Extraction(T,List))
print(DepthNum(T))

#commented out since this was not part of my code, only used for certain checks
"""
FindAndPrint(T,40)
FindAndPrint(T,110)
"""
"""
n=60
print('Delete',n,'Case 1, deleted node is a leaf')
T = Delete(T,n) #Case 1, deleted node is a leaf
InOrderD(T,'')
print('####################################')

n=90      
print('Delete',n,'Case 2, deleted node has one child')      
T = Delete(T,n) #Case 2, deleted node has one child
InOrderD(T,'')
print('####################################')

n=70      
print('Delete',n,'Case 3, deleted node has two children') 
T = Delete(T,n) #Case 3, deleted node has two children
InOrderD(T,'')

n=40      
print('Delete',n,'Case 3, deleted node has two children') 
T = Delete(T,n) #Case 3, deleted node has two children
InOrderD(T,'')
"""
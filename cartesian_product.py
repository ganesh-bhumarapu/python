from itertools import product #import product function from itertools
l1=input().split() # reads input from user .split()-> splits the input string into a list of string based on spaces
l2=input().split()

l1=list(map(int, l1)) #converting elements to integers for multiplication
l2=list(map(int, l2))

cartesian_product=product(l1,l2)
for pair in cartesian_product: # printing the cartesian product
    print(pair, end=' ') # end is used for printing the pairs in same line
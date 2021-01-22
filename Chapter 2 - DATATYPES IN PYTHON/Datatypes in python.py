# Built-in Data Type
# None Type
# Numeric Type
# Sequences 
# Sets
# Mapping


#NUMERIC DATATYPE

# int 
# float
# complex

# Int Datatype Examples
a = 15 # a is called int type variable
print(a) 

b = -25
print(b) 

c = 9845762578456
print(c)

# Float Datatype Example
d = 0.5
print(d)

e = -3.54766
print(e)

f = 290.1525
print(f)

# Complex Datatype Example
g1 = 2.5+2.5j 
g2 = 3.0-0.5j
g3 = g1 + g2 
print("Sum= ", g3)

# Bool Datatype 
a = 10 
b = 20 
if (a<b): # True 
    print("python") # display python

# SEQUENCE IN PYTHON

# str 
# bytes
# bytearray
# list
# tuple 
# range 

# str (string type)
my_str = "Python" # here str in name of string type variable
print(my_str) 
my_str = 'Python' # we can write str inside """"(triple double quotes)
print(my_str)

# bytes Datatype
elements = [10, 25, 0, 45 , 255, 10] # this is a list of bytes numbers
x = bytes(elements) # convert the list into bytes array 
print(x[0]) # display 0 element, i.e 10

# A python program to create a byte type array read and display the element of the array 
# program to understand bytes type array 
elements = [10, 20, 35, 40 ,0, 15] # create a list bytes numbers 
x = bytes(elements) # convert the list into bytes type array 
for i in x: 
    print(i) # retrieve elements from x using for loop and display 


# bytearray Datatype
elements = [10, 25, 35, 40, 0, 15] # this is a list of byte numbers
x = bytearray(elements) # convert the list into bytearray type array 
print(x[0]) # display 0 element, i.e 10

# Another bytearray datatype example
# A Python program to create a bytearray type array retrieve element

# program to understand bytearray type array 
elements = [10, 20, 0, 40, 15] # create a list of bytes numbers
x = bytearray(elements) # convert the list into bytearray type array 
x[0] = 88 # modify the first two elements of x 
x[1] = 99

for i in x: # retrieve elements from x using for loop and display 
    print(i)

# list Datatype
list = [10, -30, 25.5, 'roshan', 'bala']
print(list)
print(list[0])
print(list[1:3])
print(list[-2])
print(list * 2)

# tuple Datatype
list = (10, -30, 25.5, 'roshan', 'bala')
print(list)
print(list[0])
print(list[1:3])
print(list[-2])
print(list * 2)

# range Datatype
lst = list(range(10))
print(lst) 

# set Datatype
b = {10, 20, 30, 20, 50}
print(b) # may display {50, 10, 20, 30}

# Another example 
ch = set("Python")
print(ch) # may display {'P', 'y', 't', 'h', 'o', 'n'}

# Another example
lst = [1, 2, 5, 4, 3]
s = set(lst)
print(s) # may display {1, 2, 3, 4, 5, 50, 60}

# forzenset Datatype 
s = {50, 60, 70, 80, 90}
print(s) # may display {80, 90, 50, 60, 70}
fs = frozenset(s) # create frozenset fs
print(fs) # may display frozenset ({80, 90, 50, 60, 70})

# mapping Datatype
d = {10: 'roshan', 11: 'bala', 12:'kaju', 13:'gavu', 14:'samju'}
print(d)
print(d[11])
print(d.keys())
print(d.values())
d [10] = 'hareesh'
print(d)
del d[11]
print(d)


######################################### END #############################################
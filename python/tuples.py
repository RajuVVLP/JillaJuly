#Tuples are READ ONLY. 
#() infers tuples.
#Tuples are required when you wanted to create a service which should act like a read only

shape = (3,4,6)
print(type(shape))

#access tuple elements by slicing
print(shape[0])
print(shape[0:3])
print(shape[2:3])

shape[2] = 100
print(shape)

shape2 = (10, 20, (40,50), True)
len(shape2)


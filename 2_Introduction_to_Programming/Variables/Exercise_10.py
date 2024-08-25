# Assume that obj already has a value of 42 when the code 
# below starts running. Which of the subsequent statements 
# reassign the variable? Which statements mutate the value 
# of the object that obj references? Which statements do neither? 
# If necessary, you can read the documentation.

obj = 'ABcd' #this reassigns the variable
obj.upper() #this does neither, just prints in all caps
obj = obj.lower() #this reassigns the variable
print(len(obj)) #this does neither
obj = list(obj) #this reassigns the variable
obj.pop() #pop removes removes an element at a specified position. No position
#is specified here so it removes the default value with index -1 which is d
#this is mutation.
obj[2] = 'X' #the variable has been mutated.
obj.sort() #the variable has been mutated.
set(obj) # this does neither
obj = tuple(obj) #the variable has been reassigned.


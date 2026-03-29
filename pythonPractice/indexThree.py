# Create a Python function that 
# takes a sequence of comma-separated numbers as input and
#  generates both a list and a tuple containing those numbers.

# convert_input_to_list_and_tuple("3,6,5,3,2,8")
# (['3', '6', '5', '3', '2', '8'], ('3', '6', '5', '3', '2', '8'))

def  convert_input_to_list_and_tuple(a):
    Tuple = tuple(a.split(",")) 
    List = list(a.split(","))    
    newList, newTuple = list(List), tuple(Tuple)   
    converted = tuple([newList, newTuple])
    print(converted)




# call function 
convert_input_to_list_and_tuple("3,6,5,3,2,8")
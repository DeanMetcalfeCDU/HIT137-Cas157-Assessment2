# https://github.com/DeanMetcalfeCDU/HIT137-Cas157-Assessment2
# Created by Group 157 (Adrian Voljak & Dean Metcalfe)

# Detected Errors turned into comments, new code added where necessary

global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    #global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    '''while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1'''
    numbers = [num for num in numbers if num % 2 != 0]

    return numbers

#my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
my_set = {1, 2, 3, 4, 5}
#result = process_numbers(numbers=my_set)
result = process_numbers()

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

#modify_dict(5)
modify_dict()

def update_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)
    #i += 1

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")

# if 5 not in my_dict:
if 'key5' OR 'value5' not in my_dict:
    print("key5 or value5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)

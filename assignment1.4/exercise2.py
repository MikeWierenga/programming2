import numpy as np
def apply_to_data(data, method):
    new_data = [data*2 for data in data]
    return new_data

# print(apply_to_data([1,2,3,4,5], method=2))

def enhanced_apply_function_to_data(data, *methods):
    for method in methods:
        print(method(data))

def test_function(data):
    return [data**2 for data in data]

def another_test_function(data):
    return [data*2 for data in data]

enhanced_apply_function_to_data([1,2,3,4,5], test_function, another_test_function)

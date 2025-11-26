# test_code.py
# Some code with intentional issues for testing

def add_numbers(x,y):
   z=x+y  # poor spacing and variable naming
   return z
def process_data(data):
    # no type hints, no error handling
    result = []
    for i in data:
        result.append(i*2)
    return result

# global variable without proper naming convention
temp_var = 100

# function missing docstring and proper parameter validation
def calculate_average(nums):
    return sum(nums)/len(nums)  # no error handling for empty list
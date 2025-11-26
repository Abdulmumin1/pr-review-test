# Sample Python file with some intentional issues

def calculate(num1,num2,type):
    """Function to perform basic math operations"""
    # No input validation
    if type=='add':
        result=num1+num2
    elif type=='subtract':
        result=num1-num2
    elif type=='multiply':
        result=num1*num2
    elif type=='divide':
        result=num1/num2    # No division by zero check
    return result

def process_list(list_data):
    # Inefficient list processing
    result_list = []
    for item in list_data:
        if item in result_list:
            continue
        result_list.append(item)
    return result_list

# Global variable usage
global_config = {
    "debug": True,
    "max_items": 100
}

def main():
    # Unused import
    import json
    
    # Hardcoded values
    numbers = [1, 2, 3, 4, 5]
    
    # No error handling
    result = calculate(10, 0, 'divide')
    print(f"Result: {result}")

if __name__ == '__main__':
    main()

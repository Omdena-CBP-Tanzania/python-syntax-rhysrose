def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"

    pass

def conditional_check(number):

    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"
    pass

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
    pass

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    total_sum = sum(numbers)
    max_number = max(numbers)
    min_number = min(numbers)
    return (total_sum, max_number, min_number)
    pass

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    # Create a list to store names of students with scores > 80
    high_scorers = [name for name, score in students_dict.items() if score > 80]
    return high_scorers
    pass

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
     # Convert lists to sets and find the intersection
    common_elements = set(list1) & set(list2)
    return common_elements
    pass

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    # Perform arithmetic operations
    results = {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b if b != 0 else "undefined",  # Handle division by zero
        "modulus": a % b if b != 0 else "undefined",   # Handle modulus by zero
        "floor_division": a // b if b != 0 else "undefined",  # Floor division
        "exponential": a ** b  # Exponential operation
    }
    return results
    pass

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    # Perform logical operations
    results = {
        "and": x and y,  # Logical AND
        "or": x or y,    # Logical OR
        "not_x": not x,  # Logical NOT for x
        "not_y": not y,  # Logical NOT for y,
        "xor": (x and not y) or (not x and y)  # Logical XOR
    }
    return results
    pass

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    # Perform bitwise operations
    results = {
        "and": a & b,          # Bitwise AND
        "or": a | b,           # Bitwise OR
        "xor": a ^ b,          # Bitwise XOR
        "not_a": ~a,           # Bitwise NOT for a
        "not_b": ~b,           # Bitwise NOT for b
        "left_shift_a": a << 1,  # Left shift a by 1 bit
        "left_shift_b": b << 1,  # Left shift b by 1 bit
        "right_shift_a": a >> 1, # Right shift a by 1 bit
        "right_shift_b": b >> 1  # Right shift b by 1 bit
    }
    return results
    pass
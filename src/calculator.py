import math
from typing import List, Union, Tuple
from collections import Counter

def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    return x + y

def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
    Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def fun4(x, y, z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    Raises:
        ValueError: If any input is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
        raise ValueError("All inputs must be numbers.")
    
    total_sum = x + y + z
    return total_sum

def fun5(x, y):
    """
    Divides two numbers with zero-division handling.
    Args:
        x (int/float): Dividend.
        y (int/float): Divisor.
    Returns:
        float: Quotient of x divided by y.
    Raises:
        ValueError: If x or y is not a number.
        ZeroDivisionError: If y is zero.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def fun6(base, exponent):
    """
    Raises a base to the power of an exponent with overflow protection.
    Args:
        base (int/float): Base number.
        exponent (int/float): Exponent.
    Returns:
        float: Result of base^exponent.
    Raises:
        ValueError: If inputs are not numbers or result would be too large.
        OverflowError: If result exceeds maximum float value.
    """
    if not (isinstance(base, (int, float)) and isinstance(exponent, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    # Check for potential overflow
    if abs(base) > 1 and exponent > 100:
        raise OverflowError("Result would be too large to compute safely.")
    
    try:
        result = base ** exponent
        if math.isinf(result):
            raise OverflowError("Result exceeds maximum float value.")
        return result
    except OverflowError:
        raise OverflowError("Result exceeds maximum float value.")

def fun7(n):
    """
    Calculates factorial of a non-negative integer.
    Args:
        n (int): Non-negative integer.
    Returns:
        int: Factorial of n.
    Raises:
        ValueError: If n is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fun8(numbers: List[Union[int, float]]):
    """
    Calculates statistical measures of a list of numbers.
    Args:
        numbers (List[int/float]): List of numbers.
    Returns:
        dict: Dictionary containing mean, median, mode, std_dev, and variance.
    Raises:
        ValueError: If list is empty or contains non-numeric values.
    """
    if not numbers:
        raise ValueError("List cannot be empty.")
    
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements must be numbers.")
    
    # Mean
    mean = sum(numbers) / len(numbers)
    
    # Median
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2 if n % 2 == 0 else sorted_nums[n//2]
    
    # Mode (most frequent value)
    counts = Counter(numbers)
    mode = counts.most_common(1)[0][0]
    
    # Variance and Standard Deviation
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'std_dev': std_dev,
        'variance': variance,
        'count': len(numbers)
    }

def fun9(n):
    """
    Generates the first n numbers in the Fibonacci sequence.
    Args:
        n (int): Number of Fibonacci numbers to generate.
    Returns:
        List[int]: First n Fibonacci numbers.
    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence

def fun10(coefficients: List[Union[int, float]], x):
    """
    Evaluates a polynomial at a given point using Horner's method.
    Args:
        coefficients (List[int/float]): Polynomial coefficients [a0, a1, a2, ...] for a0 + a1*x + a2*x^2 + ...
        x (int/float): Point at which to evaluate the polynomial.
    Returns:
        float: Value of polynomial at x.
    Raises:
        ValueError: If coefficients is empty or contains non-numeric values, or x is not numeric.
    """
    if not coefficients:
        raise ValueError("Coefficients list cannot be empty.")
    
    if not all(isinstance(c, (int, float)) for c in coefficients):
        raise ValueError("All coefficients must be numbers.")
    
    if not isinstance(x, (int, float)):
        raise ValueError("x must be a number.")
    
    # Horner's method for efficient polynomial evaluation
    result = coefficients[-1]  # Start with highest degree coefficient
    for i in range(len(coefficients) - 2, -1, -1):
        result = result * x + coefficients[i]
    
    return result

def fun11(a, b, c):
    """
    Solves a quadratic equation ax^2 + bx + c = 0.
    Args:
        a (int/float): Coefficient of x^2.
        b (int/float): Coefficient of x.
        c (int/float): Constant term.
    Returns:
        Tuple: (root1, root2) or (root,) for repeated root, or None for no real roots.
    Raises:
        ValueError: If a is zero (not quadratic) or inputs are not numeric.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise ValueError("All coefficients must be numbers.")
    
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        # One repeated real root
        root = -b / (2*a)
        return (root,)
    else:
        # No real roots (complex roots)
        return None

def fun12(matrix1: List[List[Union[int, float]]], matrix2: List[List[Union[int, float]]]):
    """
    Multiplies two matrices.
    Args:
        matrix1 (List[List[int/float]]): First matrix.
        matrix2 (List[List[int/float]]): Second matrix.
    Returns:
        List[List[float]]: Product of matrix1 and matrix2.
    Raises:
        ValueError: If matrices are invalid or incompatible for multiplication.
    """
    # Validate inputs
    if not matrix1 or not matrix2:
        raise ValueError("Matrices cannot be empty.")
    
    # Check if matrices are rectangular and contain only numbers
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    for row in matrix1:
        if len(row) != cols1 or not all(isinstance(x, (int, float)) for x in row):
            raise ValueError("Matrix1 must be rectangular and contain only numbers.")
    
    for row in matrix2:
        if len(row) != cols2 or not all(isinstance(x, (int, float)) for x in row):
            raise ValueError("Matrix2 must be rectangular and contain only numbers.")
    
    # Check compatibility for multiplication
    if cols1 != rows2:
        raise ValueError(f"Cannot multiply {rows1}x{cols1} matrix with {rows2}x{cols2} matrix.")
    
    # Perform matrix multiplication
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            dot_product = sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1))
            row.append(dot_product)
        result.append(row)
    
    return result
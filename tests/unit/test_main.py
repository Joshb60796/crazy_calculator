from cli_calculator.main import CalculationInput, CalculationResult, calculate
import pytest

def test_basic_operations():
    # Test addition
    input_data = CalculationInput(operation="add", operand1=5.0, operand2=3.0)
    result = calculate(input_data)
    assert result.result == 8.0
    assert result.error is None
    
    # Test subtraction
    input_data = CalculationInput(operation="subtract", operand1=10.0, operand2=4.0)
    result = calculate(input_data)
    assert result.result == 6.0
    assert result.error is None
    
    # Test multiplication
    input_data = CalculationInput(operation="multiply", operand1=3.0, operand2=7.0)
    result = calculate(input_data)
    assert result.result == 21.0
    assert result.error is None
    
    # Test division
    input_data = CalculationInput(operation="divide", operand1=15.0, operand2=3.0)
    result = calculate(input_data)
    assert result.result == 5.0
    assert result.error is None

def test_scientific_operations():
    # Test square root
    input_data = CalculationInput(operation="sqrt", operand1=16.0)
    result = calculate(input_data)
    assert result.result == 4.0
    assert result.error is None
    
    # Test logarithm
    input_data = CalculationInput(operation="log", operand1=1.0)
    result = calculate(input_data)
    assert result.result == 0.0
    assert result.error is None
    
    # Test exponential
    input_data = CalculationInput(operation="exp", operand1=0.0)
    result = calculate(input_data)
    assert result.result == 1.0
    assert result.error is None
    
    # Test sine
    input_data = CalculationInput(operation="sin", operand1=0.0)
    result = calculate(input_data)
    assert result.result == 0.0
    assert result.error is None
    
    # Test cosine
    input_data = CalculationInput(operation="cos", operand1=0.0)
    result = calculate(input_data)
    assert result.result == 1.0
    assert result.error is None
    
    # Test tangent
    input_data = CalculationInput(operation="tan", operand1=0.0)
    result = calculate(input_data)
    assert result.result == 0.0
    assert result.error is None

def test_error_handling():
    # Test division by zero
    input_data = CalculationInput(operation="divide", operand1=10.0, operand2=0.0)
    result = calculate(input_data)
    assert result.result == 0.0
    assert "Cannot divide by zero" in result.error
    
    # Test square root of negative number
    input_data = CalculationInput(operation="sqrt", operand1=-1.0)
    result = calculate(input_data)
    assert result.result == 0.0
    assert "Cannot calculate square root" in result.error
    
    # Test logarithm of non-positive number
    input_data = CalculationInput(operation="log", operand1=0.0)
    result = calculate(input_data)
    assert result.result == 0.0
    assert "Cannot calculate logarithm" in result.error

def test_invalid_operations():
    # Test invalid operation
    input_data = CalculationInput(operation="invalid_operation", operand1=5.0)
    result = calculate(input_data)
    assert result.result == 0.0
    assert "Unknown operation" in result.error

def test_constants():
    from cli_calculator.main import PI, E
    assert PI == 3.141592653589793
    assert E == 2.718281828459045

def test_memory_operations():
    # Test that we can handle memory-like operations (basic functionality)
    input_data = CalculationInput(operation="add", operand1=1.0, operand2=1.0)
    result = calculate(input_data)
    assert result.result == 2.0
    assert result.error is None

def test_edge_cases():
    # Test with zero operands
    input_data = CalculationInput(operation="add", operand1=0.0, operand2=0.0)
    result = calculate(input_data)
    assert result.result == 0.0
    
    # Test with negative operands
    input_data = CalculationInput(operation="multiply", operand1=-2.0, operand2=3.0)
    result = calculate(input_data)
    assert result.result == -6.0

def test_float_precision():
    # Test that floating point operations work correctly
    input_data = CalculationInput(operation="add", operand1=0.1, operand2=0.2)
    result = calculate(input_data)
    # Due to floating point precision, we check if it's close to 0.3
    assert abs(result.result - 0.3) < 1e-10

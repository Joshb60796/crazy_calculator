from cli_calculator.input_handler import InputHandler, OperationType, CalculationResult
import pytest

def test_basic_arithmetic_operations():
    # Test addition
    result = InputHandler.parse_input("2 + 3")
    assert result[0] == OperationType.ADD
    assert result[1] == 2.0
    assert result[2] == 3.0
    
    # Test subtraction
    result = InputHandler.parse_input("5 - 2")
    assert result[0] == OperationType.SUBTRACT
    assert result[1] == 5.0
    assert result[2] == 2.0
    
    # Test multiplication
    result = InputHandler.parse_input("4 * 6")
    assert result[0] == OperationType.MULTIPLY
    assert result[1] == 4.0
    assert result[2] == 6.0
    
    # Test division
    result = InputHandler.parse_input("10 / 2")
    assert result[0] == OperationType.DIVIDE
    assert result[1] == 10.0
    assert result[2] == 2.0
    
    # Test power
    result = InputHandler.parse_input("2 ** 3")
    assert result[0] == OperationType.POWER
    assert result[1] == 2.0
    assert result[2] == 3.0
    
    # Test modulo
    result = InputHandler.parse_input("10 % 3")
    assert result[0] == OperationType.MODULO
    assert result[1] == 10.0
    assert result[2] == 3.0

def test_unary_operations():
    # Test sqrt
    result = InputHandler.parse_input("sqrt 9")
    assert result[0] == OperationType.SQRT
    assert result[1] == 9.0
    assert result[2] is None
    
    # Test log
    result = InputHandler.parse_input("log 10")
    assert result[0] == OperationType.LOG
    assert result[1] == 10.0
    assert result[2] is None
    
    # Test exp
    result = InputHandler.parse_input("exp 1")
    assert result[0] == OperationType.EXP
    assert result[1] == 1.0
    assert result[2] is None
    
    # Test sin
    result = InputHandler.parse_input("sin 0")
    assert result[0] == OperationType.SIN
    assert result[1] == 0.0
    assert result[2] is None
    
    # Test cos
    result = InputHandler.parse_input("cos 0")
    assert result[0] == OperationType.COS
    assert result[1] == 0.0
    assert result[2] is None
    
    # Test tan
    result = InputHandler.parse_input("tan 0")
    assert result[0] == OperationType.TAN
    assert result[1] == 0.0
    assert result[2] is None

def test_invalid_inputs():
    # Test invalid operation
    with pytest.raises(ValueError, match="Invalid input"):
        InputHandler.parse_input("invalid")
    
    # Test invalid operands
    with pytest.raises(ValueError, match="Invalid operands"):
        InputHandler.parse_input("2 * abc")
    
    # Test missing operand for unary operation
    with pytest.raises(ValueError, match="Missing operand"):
        InputHandler.parse_input("sqrt")

def test_whitespace_handling():
    # Test with whitespace
    result = InputHandler.parse_input("  2 + 3  ")
    assert result[0] == OperationType.ADD
    assert result[1] == 2.0
    assert result[2] == 3.0

def test_single_number():
    # Test single number input
    result = InputHandler.parse_input("5")
    assert result[0] == OperationType.ADD
    assert result[1] == 5.0
    assert result[2] is None

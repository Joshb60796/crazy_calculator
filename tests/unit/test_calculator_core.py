from cli_calculator.calculator_core import CalculatorCore, CalculationResult, MemoryState, CalculatorError
import pytest

def test_calculation_result_model():
    """Test CalculationResult model."""
    result = CalculationResult(value=5.0, expression="2 + 3")
    assert result.value == 5.0
    assert result.expression == "2 + 3"

def test_memory_state_model():
    """Test MemoryState model."""
    memory = MemoryState(value=10.0, history=["2 + 3 = 5"])
    assert memory.value == 10.0
    assert memory.history == ["2 + 3 = 5"]

def test_calculator_core_initialization():
    """Test calculator core initialization."""
    calc = CalculatorCore()
    assert calc.memory.value == 0.0
    assert calc.memory.history == []
    assert calc.constants['pi'] == pytest.approx(3.141592653589793)
    assert calc.constants['e'] == pytest.approx(2.718281828459045)

def test_basic_arithmetic_operations():
    """Test basic arithmetic operations."""
    calc = CalculatorCore()
    
    # Test addition
    result = calc.calculate('+', 2, 3)
    assert result.value == 5.0
    assert result.expression == "2.0 + 3.0"
    
    # Test subtraction
    result = calc.calculate('-', 10, 4)
    assert result.value == 6.0
    assert result.expression == "10.0 - 4.0"
    
    # Test multiplication
    result = calc.calculate('*', 3, 7)
    assert result.value == 21.0
    assert result.expression == "3.0 * 7.0"
    
    # Test division
    result = calc.calculate('/', 15, 3)
    assert result.value == 5.0
    assert result.expression == "15.0 / 3.0"
    
    # Test exponentiation
    result = calc.calculate('**', 2, 3)
    assert result.value == 8.0
    assert result.expression == "2.0 ** 3.0"

def test_invalid_operations():
    """Test invalid operations raise appropriate errors."""
    calc = CalculatorCore()
    
    # Test division by zero
    with pytest.raises(CalculatorError, match="Division by zero"):
        calc.calculate('/', 10, 0)
    
    # Test unsupported operation
    with pytest.raises(CalculatorError, match="Unsupported operation"):
        calc.calculate('mod', 10, 3)
    
    # Test binary operation with missing operand
    with pytest.raises(CalculatorError, match="Binary operations require two operands"):
        calc.calculate('+', 5)

def test_unary_operations():
    """Test unary mathematical operations."""
    calc = CalculatorCore()
    
    # Test square root
    result = calc.calculate('sqrt', 16)
    assert result.value == 4.0
    assert result.expression == "sqrt(16.0)"
    
    # Test invalid square root
    with pytest.raises(CalculatorError, match="Cannot calculate square root of negative number"):
        calc.calculate('sqrt', -4)
    
    # Test logarithm
    result = calc.calculate('log', 10)
    assert result.value == pytest.approx(2.302585092994046)
    assert result.expression == "log(10.0)"
    
    # Test invalid logarithm
    with pytest.raises(CalculatorError, match="Cannot calculate logarithm of non-positive number"):
        calc.calculate('log', 0)
    
    # Test exponential
    result = calc.calculate('exp', 1)
    assert result.value == pytest.approx(2.718281828459045)
    assert result.expression == "exp(1.0)"
    
    # Test trigonometric functions
    result = calc.calculate('sin', 0)
    assert result.value == 0.0
    assert result.expression == "sin(0.0)"
    
    result = calc.calculate('cos', 0)
    assert result.value == 1.0
    assert result.expression == "cos(0.0)"
    
    result = calc.calculate('tan', 0)
    assert result.value == 0.0
    assert result.expression == "tan(0.0)"

def test_memory_operations():
    """Test memory operations."""
    calc = CalculatorCore()
    
    # Test memory store
    calc.memory_store(42.0)
    assert calc.memory_recall() == 42.0
    
    # Test memory clear
    calc.memory_clear()
    assert calc.memory_recall() == 0.0
    
    # Test memory add
    calc.memory_store(10.0)
    calc.memory_add(5.0)
    assert calc.memory_recall() == 15.0
    
    # Test memory subtract
    calc.memory_subtract(3.0)
    assert calc.memory_recall() == 12.0

def test_constants():
    """Test constants retrieval."""
    calc = CalculatorCore()
    constants = calc.get_constants()
    assert 'pi' in constants
    assert 'e' in constants
    assert constants['pi'] == pytest.approx(3.141592653589793)
    assert constants['e'] == pytest.approx(2.718281828459045)

def test_history():
    """Test calculation history."""
    calc = CalculatorCore()
    
    calc.calculate('+', 2, 3)
    calc.calculate('*', 4, 5)
    
    history = calc.get_history()
    assert len(history) == 2
    assert history[0] == "2.0 + 3.0"
    assert history[1] == "4.0 * 5.0"

def test_invalid_operand_types():
    """Test that invalid operand types raise errors."""
    calc = CalculatorCore()
    
    with pytest.raises(CalculatorError, match="Invalid operand type"):
        calc.calculate('+', "invalid", 5)
    
    with pytest.raises(CalculatorError, match="Invalid operand type"):
        calc.calculate('sqrt', [1, 2, 3])

from cli_calculator.scientific_functions import ScientificFunctions, ScientificFunctionResult, ScientificFunctionInput

def test_scientific_functions_basic_operations():
    """Test basic scientific function operations."""
    # Test square root
    result = ScientificFunctions.execute_operation('sqrt', 16)
    assert result.success is True
    assert result.operation == 'sqrt'
    assert result.input_value == 16
    assert result.result == 4.0
    
    # Test invalid sqrt
    result = ScientificFunctions.execute_operation('sqrt', -4)
    assert result.success is False
    assert "negative" in result.error_message.lower()
    
    # Test logarithm
    result = ScientificFunctions.execute_operation('log', 10)
    assert result.success is True
    assert abs(result.result - 2.302585) < 1e-5
    
    # Test log base 10
    result = ScientificFunctions.execute_operation('log10', 100)
    assert result.success is True
    assert result.result == 2.0
    
    # Test exponential
    result = ScientificFunctions.execute_operation('exp', 1)
    assert result.success is True
    assert abs(result.result - 2.718281) < 1e-5

def test_trigonometric_functions():
    """Test trigonometric functions."""
    # Test sine
    result = ScientificFunctions.execute_operation('sin', 0)
    assert result.success is True
    assert abs(result.result) < 1e-10
    
    # Test cosine
    result = ScientificFunctions.execute_operation('cos', 0)
    assert result.success is True
    assert result.result == 1.0
    
    # Test tangent
    result = ScientificFunctions.execute_operation('tan', 0)
    assert result.success is True
    assert abs(result.result) < 1e-10

def test_inverse_trigonometric_functions():
    """Test inverse trigonometric functions."""
    # Test arcsine
    result = ScientificFunctions.execute_operation('asin', 0)
    assert result.success is True
    assert abs(result.result) < 1e-10
    
    # Test invalid arcsine
    result = ScientificFunctions.execute_operation('asin', 2)
    assert result.success is False
    assert "between" in result.error_message.lower()
    
    # Test arccosine
    result = ScientificFunctions.execute_operation('acos', 1)
    assert result.success is True
    assert result.result == 0.0
    
    # Test invalid arccosine
    result = ScientificFunctions.execute_operation('acos', 2)
    assert result.success is False
    assert "between" in result.error_message.lower()
    
    # Test arctangent
    result = ScientificFunctions.execute_operation('atan', 0)
    assert result.success is True
    assert abs(result.result) < 1e-10

def test_hyperbolic_functions():
    """Test hyperbolic functions."""
    # Test sinh
    result = ScientificFunctions.execute_operation('sinh', 0)
    assert result.success is True
    assert abs(result.result) < 1e-10
    
    # Test cosh
    result = ScientificFunctions.execute_operation('cosh', 0)
    assert result.success is True
    assert result.result == 1.0
    
    # Test tanh
    result = ScientificFunctions.execute_operation('tanh', 0)
    assert result.success is True
    assert abs(result.result) < 1e-10

def test_constants():
    """Test constants retrieval."""
    constants = ScientificFunctions.get_constants()
    assert 'pi' in constants
    assert 'e' in constants
    assert abs(constants['pi'] - 3.141592) < 1e-5
    assert abs(constants['e'] - 2.718281) < 1e-5

def test_supported_operations():
    """Test supported operations retrieval."""
    operations = ScientificFunctions.get_supported_operations()
    assert 'sqrt' in operations
    assert 'log' in operations
    assert 'sin' in operations
    assert 'cos' in operations
    assert 'tan' in operations
    assert 'asin' in operations
    assert 'acos' in operations
    assert 'atan' in operations
    assert 'sinh' in operations
    assert 'cosh' in operations
    assert 'tanh' in operations

def test_unsupported_operation():
    """Test handling of unsupported operations."""
    result = ScientificFunctions.execute_operation('unsupported_op', 5)
    assert result.success is False
    assert "unsupported" in result.error_message.lower()

def test_logarithm_with_base():
    """Test logarithm with custom base."""
    result = ScientificFunctions.execute_operation('log', 8, 2)
    assert result.success is True
    assert abs(result.result - 3.0) < 1e-10  # log base 2 of 8 = 3

def test_logarithm_invalid_base():
    """Test logarithm with invalid base."""
    result = ScientificFunctions.execute_operation('log', 10, 0)
    assert result.success is False
    assert "positive" in result.error_message.lower()

from cli_calculator.output_formatter import CalculationResult, format_result
import pytest

def test_format_result_with_small_number():
    """Test formatting of very small numbers."""
    result = format_result(1e-9)
    assert result == "1e-9"

def test_format_result_with_large_number():
    """Test formatting of very large numbers."""
    result = format_result(1e10)
    assert result == "1e+10"

def test_format_result_with_zero():
    """Test formatting of zero."""
    result = format_result(0)
    assert result == "0"

def test_format_result_with_positive_number():
    """Test formatting of positive numbers."""
    result = format_result(42.0)
    assert result == "42"

def test_format_result_with_negative_number():
    """Test formatting of negative numbers."""
    result = format_result(-42.0)
    assert result == "-42"

def test_format_result_with_decimal():
    """Test formatting of decimal numbers."""
    result = format_result(3.14159)
    assert result == "3.14159"

def test_format_result_with_none_value():
    """Test formatting of None values."""
    result = format_result(None)
    assert result == "None"

def test_format_result_with_nan():
    """Test formatting of NaN values."""
    result = format_result(float('nan'))
    assert result == "NaN"

def test_format_result_with_infinity():
    """Test formatting of infinity values."""
    result = format_result(float('inf'))
    assert result == "Infinity"
    
def test_format_result_with_negative_infinity():
    """Test formatting of negative infinity values."""
    result = format_result(float('-inf'))
    assert result == "-Infinity"

def test_calculation_result_model():
    """Test the CalculationResult model."""
    # Test with valid values
    result = CalculationResult(value=42.0)
    assert result.value == 42.0
    
    # Test with string value
    result = CalculationResult(value="42.0")
    assert result.value == 42.0
    
    # Test with None value
    result = CalculationResult(value=None)
    assert result.value is None
    
    # Test with error
    result = CalculationResult(value=42.0, error="Division by zero")
    assert result.value == 42.0
    assert result.error == "Division by zero"

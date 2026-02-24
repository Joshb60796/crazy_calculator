import pytest
from cli_calculator.output_formatter import CalculationResult, format_result

def test_format_result_with_small_number():
    """Test formatting of very small numbers."""
    result = CalculationResult(value=1e-9)
    formatted = format_result(result)
    assert formatted == "1e-9"

def test_format_result_with_large_number():
    """Test formatting of very large numbers."""
    result = CalculationResult(value=1e10)
    formatted = format_result(result)
    assert formatted == "1e+10"

def test_format_result_with_zero():
    """Test formatting of zero."""
    result = CalculationResult(value=0)
    formatted = format_result(result)
    assert formatted == "0"

def test_format_result_with_integer():
    """Test formatting of integers."""
    result = CalculationResult(value=42)
    formatted = format_result(result)
    assert formatted == "42"

def test_format_result_with_float():
    """Test formatting of floats."""
    result = CalculationResult(value=3.14159)
    formatted = format_result(result)
    assert formatted == "3.14159"

def test_format_result_with_negative():
    """Test formatting of negative numbers."""
    result = CalculationResult(value=-42.5)
    formatted = format_result(result)
    assert formatted == "-42.5"

def test_format_result_with_none_value():
    """Test formatting of None values."""
    result = CalculationResult(value=None)
    formatted = format_result(result)
    assert formatted == "No result"

def test_format_result_with_nan():
    """Test formatting of NaN values."""
    result = CalculationResult(value=float('nan'))
    formatted = format_result(result)
    assert formatted == "NaN"

def test_format_result_with_infinity():
    """Test formatting of infinity values."""
    result = CalculationResult(value=float('inf'))
    formatted = format_result(result)
    assert formatted == "Infinity"

def test_format_result_with_negative_infinity():
    """Test formatting of negative infinity values."""
    result = CalculationResult(value=float('-inf'))
    formatted = format_result(result)
    assert formatted == "-Infinity"

def test_format_result_with_message():
    """Test formatting with message."""
    result = CalculationResult(value=100, message="Calculation complete")
    formatted = format_result(result)
    assert formatted == "100"

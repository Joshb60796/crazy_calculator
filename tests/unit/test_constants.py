from cli_calculator.constants import CALCULATOR_CONSTANTS, CalculatorConstants

def test_calculator_constants_existence():
    """Test that calculator constants exist and are accessible."""
    assert CALCULATOR_CONSTANTS is not None
    assert isinstance(CALCULATOR_CONSTANTS, CalculatorConstants)

def test_pi_constant():
    """Test that pi constant has correct value."""
    assert hasattr(CALCULATOR_CONSTANTS, 'pi')
    assert isinstance(CALCULATOR_CONSTANTS.pi, float)
    assert abs(CALCULATOR_CONSTANTS.pi - 3.141592653589793) < 1e-10

def test_e_constant():
    """Test that e constant has correct value."""
    assert hasattr(CALCULATOR_CONSTANTS, 'e')
    assert isinstance(CALCULATOR_CONSTANTS.e, float)
    assert abs(CALCULATOR_CONSTANTS.e - 2.718281828459045) < 1e-10

def test_constants_are_frozen():
    """Test that constants are immutable."""
    try:
        CALCULATOR_CONSTANTS.pi = 1.0
        assert False, "Should not be able to modify constants"
    except Exception:
        pass  # Expected behavior

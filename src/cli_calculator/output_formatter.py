from typing import Union, Optional
from pydantic import BaseModel, Field, field_validator
import math

class CalculationResult(BaseModel):
    """Model representing a calculation result with value and optional message."""
    value: Union[float, int, None] = Field(..., description="The calculation result value")
    message: Optional[str] = Field(None, description="Optional message associated with the result")

    @field_validator('value', mode='before')
    @classmethod
    def validate_value(cls, v):
        """Validate and convert value to appropriate type."""
        if v is None:
            return None
        # Convert to float if it's a string representation of a number
        if isinstance(v, str):
            try:
                return float(v)
            except ValueError:
                return v
        return v

def format_result(result: CalculationResult) -> str:
    """
    Format a calculation result for display.
    
    Args:
        result: The calculation result to format
        
    Returns:
        Formatted string representation of the result
    """
    if result.value is None:
        return "No result"
    
    # Handle special cases
    if math.isnan(result.value):
        return "NaN"
    if math.isinf(result.value):
        return "Infinity" if result.value > 0 else "-Infinity"
    
    # Format based on value type and magnitude
    if result.value == 0:
        return "0"
    
    # For very small or very large numbers, use scientific notation
    abs_value = abs(result.value)
    if abs_value < 1e-9 or abs_value >= 1e10:
        # Use scientific notation with proper formatting
        formatted = f"{result.value:.1e}"
        # Remove unnecessary trailing zeros and decimal points
        if 'e' in formatted:
            # Split into mantissa and exponent
            mantissa, exponent = formatted.split('e')
            # Remove trailing zeros from mantissa
            mantissa = mantissa.rstrip('0').rstrip('.')
            # Format exponent without '+' if positive
            exp_sign = '+' if exponent.startswith('+') else ''
            exp_value = exponent.lstrip('+')
            return f"{mantissa}e{exp_sign}{exp_value}"
        return formatted
    
    # For regular numbers, use standard formatting
    if isinstance(result.value, int) or (isinstance(result.value, float) and result.value.is_integer()):
        return str(int(result.value))
    else:
        # Remove trailing zeros from decimal numbers
        formatted = f"{result.value:g}"
        return formatted

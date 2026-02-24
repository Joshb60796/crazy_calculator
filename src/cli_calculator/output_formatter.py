from typing import Union, Optional
from pydantic import BaseModel, Field, field_validator
import math

class CalculationResult(BaseModel):
    """Model representing a calculation result with value and optional error."""
    value: Optional[Union[float, int]] = Field(default=None)
    error: Optional[str] = Field(default=None)

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

def format_result(value: Union[float, int, None]) -> str:
    """
    Format a calculation result for display.
    
    Args:
        value: The numerical value to format
        
    Returns:
        Formatted string representation of the value
    """
    if value is None:
        return "None"
    
    if math.isnan(value):
        return "NaN"
    
    if math.isinf(value):
        return "Infinity" if value > 0 else "-Infinity"
    
    # Handle zero specially
    if value == 0.0:
        return "0"
    
    # Use scientific notation for very small or very large numbers
    abs_value = abs(value)
    if abs_value < 1e-9 or abs_value >= 1e10:
        # Format with scientific notation, removing unnecessary zeros and plus signs
        formatted = f"{value:.2e}"
        # Remove trailing zeros and unnecessary plus signs
        if 'e' in formatted:
            mantissa, exponent = formatted.split('e')
            # Remove trailing zeros from mantissa
            mantissa = mantissa.rstrip('0').rstrip('.')
            # Remove unnecessary plus sign from exponent
            exponent = exponent.lstrip('+')
            return f"{mantissa}e{exponent}"
        return formatted
    
    # For regular numbers, use standard formatting
    formatted = f"{value:.10g}"
    # Remove trailing zeros and decimal point if not needed
    if '.' in formatted:
        formatted = formatted.rstrip('0').rstrip('.')
    return formatted

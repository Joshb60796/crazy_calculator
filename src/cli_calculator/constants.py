from pydantic import BaseModel, Field
from typing import Dict, Any

class CalculatorConstants(BaseModel):
    """Model for calculator constants."""
    pi: float = Field(default=3.141592653589793, description="Mathematical constant pi")
    e: float = Field(default=2.718281828459045, description="Euler's number")
    
    class Config:
        frozen = True  # Constants should be immutable

# Global instance of calculator constants
CALCULATOR_CONSTANTS = CalculatorConstants()

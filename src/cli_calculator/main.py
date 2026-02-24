from pydantic import BaseModel, Field, field_validator
from typing import Optional
import math

class CalculationInput(BaseModel):
    operation: str = Field(..., description="The mathematical operation to perform")
    operand1: float = Field(..., description="First operand")
    operand2: Optional[float] = Field(None, description="Second operand (optional)")

class CalculationResult(BaseModel):
    result: float = Field(..., description="The result of the calculation")
    error: Optional[str] = Field(None, description="Error message if calculation failed")

def calculate(input_data: CalculationInput) -> CalculationResult:
    """
    Perform a mathematical calculation based on the input data.
    
    Args:
        input_data: CalculationInput object containing operation and operands
        
    Returns:
        CalculationResult object with result or error message
    """
    try:
        # Handle operations that require one operand
        if input_data.operation == 'sqrt':
            if input_data.operand1 < 0:
                return CalculationResult(result=0.0, error="Cannot calculate square root of negative number")
            return CalculationResult(result=math.sqrt(input_data.operand1))
        elif input_data.operation == 'log':
            if input_data.operand1 <= 0:
                return CalculationResult(result=0.0, error="Cannot calculate logarithm of non-positive number")
            return CalculationResult(result=math.log(input_data.operand1))
        elif input_data.operation == 'exp':
            return CalculationResult(result=math.exp(input_data.operand1))
        elif input_data.operation == 'sin':
            return CalculationResult(result=math.sin(input_data.operand1))
        elif input_data.operation == 'cos':
            return CalculationResult(result=math.cos(input_data.operand1))
        elif input_data.operation == 'tan':
            return CalculationResult(result=math.tan(input_data.operand1))
        
        # Handle operations that require two operands
        elif input_data.operation == 'add':
            return CalculationResult(result=input_data.operand1 + input_data.operand2)
        elif input_data.operation == 'subtract':
            return CalculationResult(result=input_data.operand1 - input_data.operand2)
        elif input_data.operation == 'multiply':
            return CalculationResult(result=input_data.operand1 * input_data.operand2)
        elif input_data.operation == 'divide':
            if input_data.operand2 == 0:
                return CalculationResult(result=0.0, error="Cannot divide by zero")
            return CalculationResult(result=input_data.operand1 / input_data.operand2)
        
        # Handle invalid operations
        else:
            return CalculationResult(result=0.0, error=f"Unknown operation: {input_data.operation}")
            
    except Exception as e:
        return CalculationResult(result=0.0, error=str(e))

# Constants
PI = math.pi
E = math.e

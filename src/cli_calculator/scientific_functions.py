from typing import Union, Dict, Any
from pydantic import BaseModel, Field, validator
import math

class ScientificFunctionInput(BaseModel):
    """Input model for scientific function operations."""
    operation: str = Field(..., description="The scientific operation to perform")
    value: float = Field(..., description="The input value for the operation")
    base: float = Field(None, description="Base for logarithmic operations")

class ScientificFunctionResult(BaseModel):
    """Output model for scientific function operations."""
    operation: str
    input_value: float
    result: float
    success: bool = True
    error_message: str = None

class ScientificFunctions:
    """A class to handle scientific mathematical operations."""
    
    # Constants
    PI = math.pi
    E = math.e
    
    # Supported operations
    SUPPORTED_OPERATIONS = {
        'sqrt', 'log', 'log10', 'exp', 'sin', 'cos', 'tan', 
        'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh'
    }
    
    @classmethod
    def execute_operation(cls, operation: str, value: float, base: float = None) -> ScientificFunctionResult:
        """
        Execute a scientific mathematical operation.
        
        Args:
            operation: The name of the operation to perform
            value: The input value
            base: Base for logarithmic operations (optional)
            
        Returns:
            ScientificFunctionResult containing the result of the operation
        """
        try:
            if operation not in cls.SUPPORTED_OPERATIONS:
                raise ValueError(f"Unsupported operation: {operation}")
            
            if operation == 'sqrt':
                if value < 0:
                    raise ValueError("Cannot calculate square root of negative number")
                result = math.sqrt(value)
                
            elif operation == 'log':
                if value <= 0:
                    raise ValueError("Cannot calculate logarithm of non-positive number")
                if base is not None and base <= 0:
                    raise ValueError("Logarithm base must be positive")
                if base is None:
                    result = math.log(value)
                else:
                    result = math.log(value, base)
                    
            elif operation == 'log10':
                if value <= 0:
                    raise ValueError("Cannot calculate logarithm of non-positive number")
                result = math.log10(value)
                
            elif operation == 'exp':
                result = math.exp(value)
                
            elif operation == 'sin':
                result = math.sin(value)
                
            elif operation == 'cos':
                result = math.cos(value)
                
            elif operation == 'tan':
                result = math.tan(value)
                
            elif operation == 'asin':
                if value < -1 or value > 1:
                    raise ValueError("Arc sine input must be between -1 and 1")
                result = math.asin(value)
                
            elif operation == 'acos':
                if value < -1 or value > 1:
                    raise ValueError("Arc cosine input must be between -1 and 1")
                result = math.acos(value)
                
            elif operation == 'atan':
                result = math.atan(value)
                
            elif operation == 'sinh':
                result = math.sinh(value)
                
            elif operation == 'cosh':
                result = math.cosh(value)
                
            elif operation == 'tanh':
                result = math.tanh(value)
                
            else:
                raise ValueError(f"Unsupported operation: {operation}")
                
            return ScientificFunctionResult(
                operation=operation,
                input_value=value,
                result=result
            )
            
        except Exception as e:
            return ScientificFunctionResult(
                operation=operation,
                input_value=value,
                result=0.0,
                success=False,
                error_message=str(e)
            )
    
    @classmethod
    def get_supported_operations(cls) -> list:
        """Get list of supported scientific operations."""
        return list(cls.SUPPORTED_OPERATIONS)
    
    @classmethod
    def get_constants(cls) -> Dict[str, float]:
        """Get dictionary of mathematical constants."""
        return {
            'pi': cls.PI,
            'e': cls.E
        }

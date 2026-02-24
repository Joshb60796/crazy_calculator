from typing import Optional, Union
from pydantic import BaseModel, Field, validator
import math

class CalculationResult(BaseModel):
    """Model representing the result of a calculation."""
    value: float = Field(..., description="The result of the calculation")
    expression: str = Field(..., description="The expression that was calculated")

class MemoryState(BaseModel):
    """Model representing the calculator's memory state."""
    value: float = Field(0.0, description="The current memory value")
    history: list = Field(default_factory=list, description="Calculation history")

class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass

class CalculatorCore:
    """Core calculator implementation with advanced mathematical functions."""
    
    def __init__(self):
        self.memory = MemoryState()
        self.constants = {
            'pi': math.pi,
            'e': math.e
        }
    
    def _validate_operand(self, operand: Union[int, float]) -> float:
        """Validate and convert operand to float."""
        if isinstance(operand, (int, float)):
            return float(operand)
        raise CalculatorError(f"Invalid operand type: {type(operand)}")
    
    def _validate_operation(self, operation: str) -> str:
        """Validate that the operation is supported."""
        supported_operations = ['+', '-', '*', '/', '**', 'sqrt', 'log', 'exp', 'sin', 'cos', 'tan']
        if operation not in supported_operations:
            raise CalculatorError(f"Unsupported operation: {operation}")
        return operation
    
    def calculate(self, operation: str, operand1: Union[int, float], operand2: Optional[Union[int, float]] = None) -> CalculationResult:
        """
        Perform a calculation with the given operation and operands.
        
        Args:
            operation: The mathematical operation to perform
            operand1: The first operand
            operand2: The second operand (optional for unary operations)
            
        Returns:
            CalculationResult containing the result and expression
            
        Raises:
            CalculatorError: If operation is invalid or calculation fails
        """
        operation = self._validate_operation(operation)
        operand1 = self._validate_operand(operand1)
        
        if operation in ['+', '-', '*', '/', '**']:
            if operand2 is None:
                raise CalculatorError("Binary operations require two operands")
            operand2 = self._validate_operand(operand2)
            
        try:
            if operation == '+':
                result = operand1 + operand2
            elif operation == '-':
                result = operand1 - operand2
            elif operation == '*':
                result = operand1 * operand2
            elif operation == '/':
                if operand2 == 0:
                    raise CalculatorError("Division by zero")
                result = operand1 / operand2
            elif operation == '**':
                result = operand1 ** operand2
            elif operation == 'sqrt':
                if operand1 < 0:
                    raise CalculatorError("Cannot calculate square root of negative number")
                result = math.sqrt(operand1)
            elif operation == 'log':
                if operand1 <= 0:
                    raise CalculatorError("Cannot calculate logarithm of non-positive number")
                result = math.log(operand1)
            elif operation == 'exp':
                result = math.exp(operand1)
            elif operation == 'sin':
                result = math.sin(operand1)
            elif operation == 'cos':
                result = math.cos(operand1)
            elif operation == 'tan':
                result = math.tan(operand1)
            else:
                raise CalculatorError(f"Unsupported operation: {operation}")
                
            expression = self._build_expression(operation, operand1, operand2)
            self.memory.history.append(expression)
            return CalculationResult(value=result, expression=expression)
            
        except Exception as e:
            raise CalculatorError(f"Calculation failed: {str(e)}")
    
    def _build_expression(self, operation: str, operand1: float, operand2: Optional[float] = None) -> str:
        """Build a string representation of the calculation."""
        if operation in ['+', '-', '*', '/', '**']:
            return f"{operand1} {operation} {operand2}"
        else:
            if operand2 is None:
                return f"{operation}({operand1})"
            else:
                return f"{operation}({operand1}, {operand2})"
    
    def memory_store(self, value: Union[int, float]) -> None:
        """Store a value in memory."""
        self.memory.value = self._validate_operand(value)
    
    def memory_recall(self) -> float:
        """Recall the value from memory."""
        return self.memory.value
    
    def memory_clear(self) -> None:
        """Clear the memory."""
        self.memory.value = 0.0
    
    def memory_add(self, value: Union[int, float]) -> None:
        """Add a value to memory."""
        self.memory.value += self._validate_operand(value)
    
    def memory_subtract(self, value: Union[int, float]) -> None:
        """Subtract a value from memory."""
        self.memory.value -= self._validate_operand(value)
    
    def get_constants(self) -> dict:
        """Get all available constants."""
        return self.constants.copy()
    
    def get_history(self) -> list:
        """Get calculation history."""
        return self.memory.history.copy()

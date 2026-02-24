from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional, List
import math

class CalculationInput(BaseModel):
    """
    Represents the input for a calculation operation.
    """
    operand1: Optional[float] = Field(default=None, description="First operand for the calculation")
    operand2: Optional[float] = Field(default=None, description="Second operand for the calculation")
    number: Optional[float] = Field(default=None, description="Single number for the calculation")
    operation: str = Field(..., description="The operation to perform")
    
    @field_validator('operation')
    def validate_operation(cls, v):
        valid_operations = [
            'add', 'subtract', 'multiply', 'divide', 'sqrt', 'prime', 'ln', 'log', 
            'power', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'exp', 'inverse'
        ]
        if v not in valid_operations:
            raise ValueError(f"Invalid operation: {v}. Must be one of {valid_operations}")
        return v

class CalculationResult(BaseModel):
    """
    Represents the result of a calculation operation.
    """
    operation: str = Field(..., description="The operation that was performed")
    operand1: Optional[float] = Field(default=None, description="First operand used")
    operand2: Optional[float] = Field(default=None, description="Second operand used")
    number: Optional[float] = Field(default=None, description="Single number used")
    result: float = Field(..., description="The result of the calculation")
    timestamp: str = Field(..., description="Timestamp of when the calculation was performed")

class MemoryOperation(BaseModel):
    """
    Represents a memory operation.
    """
    operation: str = Field(..., description="The memory operation to perform")
    value: Optional[float] = Field(default=None, description="Value to store or retrieve")
    
    @field_validator('operation')
    def validate_memory_operation(cls, v):
        valid_operations = ['store', 'recall', 'clear', 'add', 'subtract']
        if v not in valid_operations:
            raise ValueError(f"Invalid memory operation: {v}. Must be one of {valid_operations}")
        return v

class MemoryState(BaseModel):
    """
    Represents the current state of memory.
    """
    value: float = Field(default=0.0, description="Current memory value")
    operations: List[MemoryOperation] = Field(default_factory=list, description="List of memory operations performed")

class CalculatorConfig(BaseModel):
    """
    Configuration for the calculator.
    """
    precision: int = Field(default=10, ge=1, le=15, description="Decimal precision for calculations")
    use_memory: bool = Field(default=True, description="Whether to enable memory functionality")
    use_trigonometry: bool = Field(default=True, description="Whether to enable trigonometric functions")
    use_logarithms: bool = Field(default=True, description="Whether to enable logarithmic functions")
    use_constants: bool = Field(default=True, description="Whether to enable mathematical constants")

class CalculatorState(BaseModel):
    """
    Represents the current state of the calculator.
    """
    current_value: float = Field(default=0.0, description="Current value in calculator")
    memory: MemoryState = Field(default_factory=MemoryState, description="Current memory state")
    config: CalculatorConfig = Field(default_factory=CalculatorConfig, description="Calculator configuration")
    history: List[CalculationResult] = Field(default_factory=list, description="Calculation history")

class CalculationError(BaseModel):
    """
    Represents an error that occurred during a calculation.
    """
    operation: str = Field(..., description="The operation that failed")
    error_type: str = Field(..., description="Type of error that occurred")
    message: str = Field(..., description="Error message")
    timestamp: str = Field(..., description="Timestamp of when the error occurred")

class CalculatorRequest(BaseModel):
    """
    Represents a request to perform a calculation.
    """
    input_data: CalculationInput = Field(..., description="The input data for the calculation")
    config: Optional[CalculatorConfig] = Field(default=None, description="Optional configuration override")

class CalculatorResponse(BaseModel):
    """
    Represents a response from the calculator.
    """
    success: bool = Field(..., description="Whether the calculation was successful")
    result: Optional[CalculationResult] = Field(default=None, description="The calculation result if successful")
    error: Optional[CalculationError] = Field(default=None, description="Error information if calculation failed")
    history: List[CalculationResult] = Field(default_factory=list, description="Updated calculation history")

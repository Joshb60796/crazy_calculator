from enum import Enum
from typing import Union, Tuple
from pydantic import BaseModel, Field
from dataclasses import dataclass

class OperationType(str, Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    POWER = "**"
    MODULO = "%"
    SQRT = "sqrt"
    LOG = "log"
    EXP = "exp"
    SIN = "sin"
    COS = "cos"
    TAN = "tan"

class CalculationResult(BaseModel):
    """Model for calculation results."""
    value: float = Field(description="The result of the calculation")
    operation: OperationType = Field(description="The operation performed")

class InputHandler:
    """Handles parsing of input strings for the calculator."""
    
    @staticmethod
    def parse_input(input_str: str) -> Tuple[OperationType, Union[float, None], Union[float, None]]:
        """
        Parse input string and return operation type and operands.
        
        Args:
            input_str: String input from user
            
        Returns:
            Tuple of (operation_type, operand1, operand2)
            
        Raises:
            ValueError: If input is invalid
        """
        # Remove whitespace
        input_str = input_str.strip()
        
        # Handle unary operations (sqrt, log, exp, sin, cos, tan)
        if input_str.startswith(('sqrt', 'log', 'exp', 'sin', 'cos', 'tan')):
            # Find the operation type
            for op in OperationType:
                if input_str.startswith(op.value):
                    if op.value in ['sqrt', 'log', 'exp', 'sin', 'cos', 'tan']:
                        # Extract the operand (everything after the operation)
                        operand_str = input_str[len(op.value):].strip()
                        if not operand_str:
                            raise ValueError(f"Missing operand for {op.value}")
                        try:
                            operand = float(operand_str)
                            return op, operand, None
                        except ValueError:
                            raise ValueError(f"Invalid operand for {op.value}: {operand_str}")
        
        # Handle binary operations
        # Check for power operation first (since it's two characters)
        if "**" in input_str:
            parts = input_str.split("**", 1)
            if len(parts) != 2:
                raise ValueError("Invalid power operation")
            operand1_str, operand2_str = parts
            try:
                operand1 = float(operand1_str.strip())
                operand2 = float(operand2_str.strip())
                return OperationType.POWER, operand1, operand2
            except ValueError:
                raise ValueError(f"Invalid operands for {OperationType.POWER}: {operand1_str}, {operand2_str}")
        
        # Check for other binary operations
        operations = ['+', '-', '*', '/', '%']
        for op in operations:
            if op in input_str:
                parts = input_str.split(op, 1)
                if len(parts) != 2:
                    continue
                operand1_str, operand2_str = parts
                try:
                    operand1 = float(operand1_str.strip())
                    operand2 = float(operand2_str.strip())
                    return OperationType(op), operand1, operand2
                except ValueError:
                    raise ValueError(f"Invalid operands for {op}: {operand1_str}, {operand2_str}")
        
        # If no operation found, try to parse as a single number
        try:
            return OperationType.ADD, float(input_str), None
        except ValueError:
            raise ValueError(f"Invalid input: {input_str}")

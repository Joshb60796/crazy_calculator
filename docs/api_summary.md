# CLI Calculator API Summary

## Overview
A command-line calculator with advanced mathematical functions, memory capabilities, and support for constants.

## Modules

### cli_calculator.main
- **`main()`**: Entry point for the calculator application.

### cli_calculator.calculator_core
- **`CalculatorCore`**: Core calculator logic with basic arithmetic operations.
  - `add(a: float, b: float) -> float`
  - `subtract(a: float, b: float) -> float`
  - `multiply(a: float, b: float) -> float`
  - `divide(a: float, b: float) -> float`
  - `power(base: float, exponent: float) -> float`
  - `modulo(a: float, b: float) -> float`

### cli_calculator.memory_manager
- **`MemoryManager`**: Manages calculator memory operations.
  - `store(value: float) -> None`
  - `recall() -> float`
  - `clear() -> None`
  - `get_memory() -> float`

### cli_calculator.scientific_functions
- **`ScientificFunctions`**: Provides advanced mathematical functions.
  - `sqrt(x: float) -> float`
  - `log(x: float, base: float = math.e) -> float`
  - `exp(x: float) -> float`
  - `sin(x: float) -> float`
  - `cos(x: float) -> float`
  - `tan(x: float) -> float`
  - `asin(x: float) -> float`
  - `acos(x: float) -> float`
  - `atan(x: float) -> float`
  - `pi() -> float`
  - `e() -> float`

### cli_calculator.input_handler
- **`InputHandler`**: Handles user input parsing and validation.
  - `parse_expression(expression: str) -> list`
  - `validate_input(input_str: str) -> bool`

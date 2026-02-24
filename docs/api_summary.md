# CLI Calculator API Summary

## Overview
A command-line calculator with advanced mathematical functions including basic arithmetic, scientific operations, memory capabilities, and support for mathematical constants.

## Modules

### cli_calculator.main
- **`main()`**: Entry point for the calculator application
- **`run()`**: Main execution loop for the calculator

### cli_calculator.calculator_core
- **`Calculator()`**: Core calculator class for performing arithmetic operations
- **`OperationResult`**: Pydantic model for operation results

### cli_calculator.memory_manager
- **`MemoryManager()`**: Manages calculator memory operations
- **`MemoryOperation`**: Pydantic model for memory operations

### cli_calculator.scientific_functions
- **`ScientificCalculator()`**: Scientific calculator with advanced functions
- **`ScientificFunction`**: Pydantic model for scientific functions

### cli_calculator.input_handler
- **`InputHandler()`**: Handles user input parsing and validation
- **`ParsedInput`**: Pydantic model for parsed input data

### cli_calculator.output_formatter
- **`OutputFormatter()`**: Formats calculation results for display
- **`FormattedOutput`**: Pydantic model for formatted output

### cli_calculator.constants
- **`Constants`**: Class containing mathematical constants (pi, e)
- **`Constant`**: Pydantic model for mathematical constants

## Key Features
- Basic arithmetic operations (+, -, *, /, ^)
- Scientific functions (sqrt, log, exp, sin, cos, tan)
- Memory operations (M+, M-, MR, MC)
- Support for mathematical constants (π, e)
- Error handling for invalid operations
- Command-line interface with user-friendly output

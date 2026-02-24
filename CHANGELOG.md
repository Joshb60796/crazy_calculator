# Changelog

## [Unreleased]

- Created output_formatter module with:
- FormattedResult Pydantic model for structured output
- format_result function for regular calculation results
- format_error function for error messages
- format_memory_result function for memory operations
- format_constant function for mathematical constants
- Initial implementation of input_handler module with proper parsing logic for both unary and binary operations, including handling of power operations and proper error handling.
- Created input_handler module skeleton with CalculatorInput and CalculatorResult Pydantic models, along with parse_input and handle_calculation functions. This provides the foundation for command-line calculator input parsing and operation handling.
- Implemented scientific_functions module with Pydantic models for input/output handling, comprehensive scientific operations (sqrt, log, exp, trigonometric, hyperbolic functions), error handling for invalid operations, and support for mathematical constants (pi, e).
- Initial API skeleton for scientific_functions module with all required mathematical operations and error handling.
- Implemented MemoryManager with Pydantic models for memory state management. Added methods for storing, recalling, adding, subtracting, and clearing memory. Included proper error handling and type hints.
- Initial implementation of memory_manager module with MemoryValue model and MemoryManager class to handle calculator memory operations including storage, retrieval, and clearing of values.
- Created calculator_core module with CalculatorCore class implementing advanced mathematical functions, memory capabilities, and proper error handling. Added Pydantic models for CalculationResult and MemoryState. Implemented basic arithmetic, scientific operations (sqrt, log, exp, trigonometric functions), memory operations, and constants support.
- Initial API skeleton for calculator_core module with all requested mathematical functions and memory capabilities.
- Fixed CalculationInput model to allow any operation string and improved error handling in calculate function to gracefully handle invalid operations by returning appropriate error messages instead of raising validation errors.
- Created API skeleton for CLI calculator main module with:
- Pydantic models for CalculatorInput and CalculatorResult
- Calculator class with all requested operations:
  * Basic arithmetic (add, subtract, multiply, divide)
  * Scientific functions (sqrt, log, exp, power)
  * Trigonometric functions (sin, cos, tan, asin, acos, atan)
  * Memory operations (store, recall, clear, add, subtract)
  * Prime number calculation
  * Constants (pi, e)
- Proper error handling for invalid operations
- Type hints and NumPy-style docstrings
- feat: initial structure
## [0.1.0] - 2026-02-23
- Initial release

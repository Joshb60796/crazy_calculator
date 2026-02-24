# CLI Calculator

A powerful command-line calculator with advanced mathematical functions including basic arithmetic, scientific operations, memory capabilities, and support for mathematical constants.

## Features

- **Basic Arithmetic**: Addition (+), subtraction (-), multiplication (*), division (/), exponentiation (^)
- **Scientific Functions**: Square root (sqrt), natural logarithm (ln), common logarithm (log), exponential (exp), sine (sin), cosine (cos), tangent (tan)
- **Inverse Trigonometric**: Arc sine (asin), arc cosine (acos), arc tangent (atan)
- **Memory Operations**: Memory store (M+), memory recall (MR), memory clear (MC)
- **Mathematical Constants**: π (pi), e (Euler's number)
- **Special Functions**: Reciprocal (1/x), factorial (!)

## Installation

```bash
pip install cli_calculator
```

## Usage

### Interactive Mode

Run the calculator in interactive mode:

```bash
python -m cli_calculator
```

### Command Line Operations

You can also perform calculations directly from the command line:

```bash
python -m cli_calculator "2 + 3"
python -m cli_calculator "sqrt(16)"
python -m cli_calculator "sin(pi/2)"
```

### Supported Operations

#### Basic Arithmetic
- `2 + 3` → 5
- `10 - 4` → 6
- `5 * 6` → 30
- `20 / 4` → 5
- `2 ^ 3` → 8

#### Scientific Functions
- `sqrt(16)` → 4
- `ln(2.71828)` → 1
- `log(100)` → 2
- `exp(1)` → 2.71828
- `sin(pi/2)` → 1
- `cos(0)` → 1
- `tan(pi/4)` → 1

#### Inverse Trigonometric
- `asin(1)` → π/2
- `acos(0)` → π/2
- `atan(1)` → π/4

#### Memory Operations
- `M+ 5` → Store 5 in memory
- `MR` → Recall memory value
- `MC` → Clear memory

#### Constants
- `pi` → 3.14159...
- `e` → 2.71828...

## Examples

```bash
$ python -m cli_calculator
CLI Calculator
Enter calculations (type 'quit' to exit):
> 2 + 3
Result: 5.0
> sqrt(16)
Result: 4.0
> sin(pi/2)
Result: 1.0
> M+ 10
Memory stored: 10.0
> MR
Memory recall: 10.0
> quit
Goodbye!
```

## Error Handling

The calculator handles various error conditions gracefully:
- Division by zero
- Invalid mathematical operations
- Unsupported functions
- Syntax errors in input

## License

MIT

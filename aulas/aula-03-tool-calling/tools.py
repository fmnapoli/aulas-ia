"""Custom tools for the agent: calculator and unit converter."""

from agno.tools import tool


@tool
def calculate(expression: str) -> str:
    """Evaluate a math expression and return the result.

    Args:
        expression: A mathematical expression to evaluate. Example: '2 + 3 * 4'

    Returns:
        The result of the calculation or an error message.
    """
    allowed_names = {
        "abs": abs,
        "round": round,
        "min": min,
        "max": max,
        "pow": pow,
        "int": int,
        "float": float,
    }
    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return f"Result of '{expression}' = {result}"
    except ZeroDivisionError:
        return "Error: division by zero"
    except Exception as e:
        return f"Error evaluating '{expression}': {e}"


@tool
def convert_temperature(value: float, from_unit: str, to_unit: str) -> str:
    """Convert temperature between Celsius (C), Fahrenheit (F), and Kelvin (K).

    Args:
        value: The temperature value to convert.
        from_unit: Source unit — one of 'C', 'F', or 'K'.
        to_unit: Target unit — one of 'C', 'F', or 'K'.

    Returns:
        The converted temperature as a formatted string.
    """
    from_unit = from_unit.upper().strip()
    to_unit = to_unit.upper().strip()

    valid_units = {"C", "F", "K"}
    if from_unit not in valid_units or to_unit not in valid_units:
        return f"Error: units must be one of {valid_units}. Got from='{from_unit}', to='{to_unit}'."

    if from_unit == to_unit:
        return f"{value}°{to_unit} (same unit, no conversion needed)"

    # Convert to Celsius first (intermediate step)
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    else:  # K
        celsius = value - 273.15

    # Convert from Celsius to target
    if to_unit == "C":
        result = celsius
    elif to_unit == "F":
        result = celsius * 9 / 5 + 32
    else:  # K
        result = celsius + 273.15

    return f"{value}°{from_unit} = {result:.2f}°{to_unit}"

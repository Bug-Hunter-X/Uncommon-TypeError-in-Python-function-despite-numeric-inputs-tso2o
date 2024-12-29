def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except TypeError:
        return "Error: x and y must be numbers"
except ZeroDivisionError:
    return "Error: Cannot divide by zero"
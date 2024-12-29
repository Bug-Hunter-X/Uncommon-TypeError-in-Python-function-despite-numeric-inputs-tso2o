def function_with_uncommon_error_solution(x, y):
    try:
        x = float(x)
        y = float(y)
        result = x / y
        return result
    except TypeError:
        return "Error: x and y must be numbers"
except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except ValueError:
        return "Error: Invalid input type" 
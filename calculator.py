
def calculate(a, b, operator):
    """
    执行基础的四则运算。

    Args:
        a (float/int): 第一个操作数。
        b (float/int): 第二个操作数。
        operator (str): 运算符 ('+', '-', '*', '/')。

    Returns:
        float: 计算结果。

    Raises:
        ValueError: 如果运算符无效。
        ZeroDivisionError: 如果尝试除以零。
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ZeroDivisionError("错误：除数不能为零")
        return a / b
    else:
        raise ValueError(f"错误：不支持的运算符 '{operator}'")

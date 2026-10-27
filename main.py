# -*- coding: utf-8 -*-
from calculator import calculate

def main():
    print("欢迎使用简易计算器！(输入 'q' 退出)")
    while True:
        try:
            expr = input("\n请输入表达式 (例如: 1 + 2): ")
            if expr.lower() == 'q':
                print("再见！")
                break
            
            parts = expr.split()
            if len(parts) != 3:
                print("格式错误，请按 '数字 运算符 数字' 的格式输入。")
                continue
            
            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])
            
            result = calculate(a, b, operator)
            print(f"结果: {result}")
            
        except ZeroDivisionError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"发生未知错误: {e}")

if __name__ == "__main__":
    main()

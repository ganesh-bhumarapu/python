def perform_division(a, b):
    try:
        result = a // b
        print(result)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print(f"Error Code: {e}")

T = int(input().strip())
for _ in range(T):
    try:
        a, b = input().strip().split()
        a = int(a)
        b = int(b)
        perform_division(a, b)
    except ValueError as e:
        print(f"Error Code: {e}")
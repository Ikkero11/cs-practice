def main():
    a = float(input("Введите первое число: "))
    op = input("Введите операцию (+,-,*,/): ")
    b = float(input("Введите второе число: "))

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    else:
        result = None

    if result is not None:
        print("Результат:", result)
    else:
        print("Неизвестная операция")

if __name__ == "__main__":
    main()

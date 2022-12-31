expression = input("Expression: ").strip()

op1, operator, op2 = expression.split(" ")
op1 = float(op1)
op2 = float(op2)

match operator:
    case "+":
        print(f"{op1 + op2:.1f}")
    case "-":
        print(f"{op1 - op2:.1f}")
    case "*":
        print(f"{op1 * op2:.1f}")
    case "/":
        print(f"{op1 / op2:.1f}")

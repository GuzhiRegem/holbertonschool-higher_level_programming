#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    args = sys.argv
    if len(sys.argv) != 4:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            sys.exit(1)
    op = 0
    operations = ["+", "-", "*", "/"]
    if args[2] in operations:
        op = operations.index(args[2])
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    ar1 = int(args[1])
    ar2 = int(args[3])
    oper_f = [calc.add, calc.sub, calc.mul, calc.div]
    res = oper_f[op](ar1, ar2)
    print("{} {} {} = {}".format(ar1, operations[op], ar2, res))

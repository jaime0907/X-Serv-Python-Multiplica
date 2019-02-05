import sys

try:
    if sys.argv[1] == "suma":
        print(float(sys.argv[2]) + float(sys.argv[3]))
    elif sys.argv[1] == "resta":
        print(float(sys.argv[2]) - float(sys.argv[3]))
    elif sys.argv[1] == "multiplicacion":
        print(float(sys.argv[2]) * float(sys.argv[3]))
    elif sys.argv[1] == "division":
        print(float(sys.argv[2]) / float(sys.argv[3]))
    else:
        print("Operando no válido")

except ValueError:
    print("Operandos no válidos")
except ZeroDivisionError:
    print("No puedes dividir entre 0")
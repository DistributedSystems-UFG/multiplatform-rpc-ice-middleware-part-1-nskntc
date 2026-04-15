import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:tcp -h localhost -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

rep = printer.printString("Hello World!")
print("printString:", rep)

rep = printer.reverseString("Sistemas Distribuidos")
print("reverseString:", rep)

rep = printer.toUpperCase("hello ice middleware")
print("toUpperCase:", rep)

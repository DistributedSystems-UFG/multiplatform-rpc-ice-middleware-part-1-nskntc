import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
        return s + "*"

    def reverseString(self, s, current=None):
        result = s[::-1]
        print("reverse:", result)
        return result

    def toUpperCase(self, s, current=None):
        result = s.upper()
        print("upper:", result)
        return result

communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object = PrinterI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
adapter.activate()

communicator.waitForShutdown()

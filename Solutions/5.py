class Exercise5Handler():
    def __init__(self):
        self.strInput = ""

    @staticmethod
    def InputValidator(Input):
        if not isinstance(Input, str):
            raise ValueError('You did not input an string')
        return True

    def getString(self):
        #Can also use raw_input()
        self.strInput = input("Please enter a string: ")
        self.InputValidator(self.strInput)
    
    def printString(self):
        print(self.strInput.upper())

def main():
    handler = Exercise5Handler()
    handler.getString()
    handler.printString()

if __name__ == "__main__":
    main()

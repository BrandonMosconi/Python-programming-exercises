class Exercise1Handler():
    """Attempt for exercise 1"""
    def __init__(self, numInp):
        self.numInp = numInp

    @staticmethod
    def InputValidator(Input):
        if not isinstance(Input, int):
            raise ValueError('You did not input an integer')
        return True

    def MultAndDiv(self):
        self.InputValidator(self.numInp)
        self.arr = []

        for n in range(2000,3201):
            if n%7==0 and n%5!=0:
                #String so we can use .join later
                self.arr.append(str(n))
        
        #This is how you do the comma-print thingy
        print(','.join(self.arr))

"""What will run if the class is run without import"""
def main():
    handler = Exercise1Handler(0)
    handler.MultAndDiv()

    
if __name__ == "__main__":
    main()
        

    
 
    
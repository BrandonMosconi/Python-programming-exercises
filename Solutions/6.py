class Exercise2Handler():
    def __init__(self,inpStr):
        self.inpStr = inpStr
    
    def formulaOutput(self):
        import math 

        #Initialise variables
        self.inpArr = [self.inpStr.split(",")]
        """Define this as an array, not a string, so we can use
        the .join command to join them with commas."""
        self.outStr = []
        #Define these because ?
        self.C = 50
        self.H = 30

        for element in self.inpArr:
            outStr.append(str(int(round(math.sqrt(2*self.C*float(element)/self.H))))
            # outStr.append(str(int(round((2*C*float(element))/H)**1/2)))

        print("Hello")


def main():
    handler = Exercise2Handler("1,2,3,4")
    handler.formulaOutput()

if __name__ == "__main__":
    main()
        
    
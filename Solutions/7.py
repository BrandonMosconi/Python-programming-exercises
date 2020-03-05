class Exercise7Handler():
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y

    def arrGen(self):
        self.arr = []

        for i in range(0,self.X):
            self.arrCurr = []
            for j in range(0,self.Y):
                self.arrCurr.append(i*j)
            self.arr.append(self.arrCurr)
        
        print(self.arr)

def main():
    
    handler = Exercise7Handler(4,2)
    handler.arrGen()

if __name__ == "__main__":
    main()

"""This assumes that the input is two variables. If it were two variables
that were comma-separated, this is what it would be"""
def commaSeperator(strInt):
    #We need to first make them integers. We could also do it after.
    dimensions = [int(x) for x in strInt.split(",")]  

    x = dimensions[0]
    y = dimentions[1] 

     
    
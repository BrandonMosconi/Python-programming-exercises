class Exercise15Handler():
    def __init__(self,inpVal):
        self.inpVal = inpVal
    
    def seqSum(self):
        self.sum = 0

        for n in range(1,5):
            self.sum += int(str(self.inpVal)*n)
        
        print(self.sum)

def main():
    inpVal = input("> ")
    handler = Exercise15Handler(inpVal)
    handler.seqSum()

if __name__ == "__main__":
    main()
class Exercise2Handler():
    def __init__(self, factInp):
        self.factInp = factInp
        
    def factorial(self):
        self.factRes = 1

        for n in range(1, self.factInp + 1):
            self.factRes = self.factRes*n
    
        print(self.factRes)

def main():
    handler = Exercise2Handler(6)
    handler.factorial()


if __name__ == "__main__":
    main()


        



class Exercise2Handler():
    def __init__(self, valInp):
        self. valInp = valInp
    
    def squareDict(self):
        self.dictionary = {}

        for n in range(1,self.valInp+1):
            self.dictionary[n] = n*n

        print(self.dictionary)


def main():
    handler = Exercise2Handler(8)
    handler.squareDict()

if __name__ == "__main__":
    main()
        

class Exercise13Handler():
    def __init__(self,strInp):
        self.strInp = strInp

    def intstrCount(self):
        """We could import the set of lower-case letters, and define
        a set of numbers. Or, we could use the built-in functions
        .isdigit() and .isalpha()"""
        
        self.dictCount = {"Letters": 0, "Digits": 0}

        for letter in self.strInp:
            if letter.isdigit():
                self.dictCount["Digits"] += 1
            elif letter.isalpha():
                self.dictCount["Letters"] += 1
        
        print("Letters: " + str(self.dictCount["Letters"]))
        print("Digits: " + str(self.dictCount["Digits"]))

def main():
    inp = input("> ")
    handler = Exercise13Handler(inp)
    handler.intstrCount()

if __name__ == "__main__":
    main()
class Exercise12Handler():
    def __init__(self):
        pass

    def evenDigits(self):
        self.evenArr = []

        for n in range(2000,3001):
            self.s = str(n)
            for j in range(0,len(self.s)):
                if int(self.s[j])%2 != 0: #Make use of the fact we can select specific string letters
                    break
                elif j == len(self.s)-1: #This bit basically says "If all digits satisfy the conditions..."
                    self.evenArr.append(self.s)
        
        print(",".join(self.evenArr))

def main():
    handler = Exercise12Handler()
    handler.evenDigits()

if __name__ == "__main__":
    main()
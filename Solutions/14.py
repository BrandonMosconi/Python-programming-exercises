class Exercise14Handler():
    def __init__(self,inpStr):
        self.inpStr = inpStr
    
    def upperLower(self):
        self.countDict = {"Upper":0,"Lower":0}

        for letter in self.inpStr:
            if letter.lower() == letter:
                self.countDict["Lower"] += 1
            elif letter.upper() == letter:
                self.countDict["Upper"] += 1
        
        print("Lower",self.countDict["Lower"])
        print("Upper",self.countDict["Upper"])

def main():
    inp = input("> ")
    handler = Exercise14Handler(inp)
    handler.upperLower()

if __name__ == "__main__":
    main()
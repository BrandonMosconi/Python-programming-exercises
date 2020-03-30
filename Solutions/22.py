class Exercise22Handler():
    def __init__(self,inpStr):
        self.inpStr = inpStr
    
    def wordCount(self):
        self.lib = {}
        self.strList = sorted(set(self.inpStr.split(" ")))

        for word in self.strList:
            self.lib[word] = self.inpStr.split(" ").count(word)
        
        for w in self.strList:
            print(w,self.lib[w])

def main():
    inpstr = input("> ")
    Exercise22Handler(inpstr).wordCount()

if __name__ == "__main__":
    main()
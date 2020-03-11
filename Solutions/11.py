class Exercise11Handler():
    def __init__(self,inpStr):
        self.inpStr = inpStr

    def binDiv(self):
        self.binArr = self.inpStr.split(",")
        self.divArr = []

        for element in self.binArr:
            if int(element,2)%5 == 0:
                self.divArr.append(element)

        print(",".join(self.divArr))


def main():
    userInput = input("> ")
    handler = Exercise11Handler(userInput)
    handler.binDiv()

if __name__ == "__main__":
    main()
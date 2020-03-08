class Exercise9Handler():
    def __init__(self):
        pass

    def inpUpper(self):
        lines = []

        while True:
            s = input("> ")

            if s in ["stop",""]:
                break #Makes it false
            else:
                lines.append(s.upper())

        for element in lines:
            print(element)   

def main():
    handler = Exercise9Handler()
    handler.inpUpper()

if __name__ == "__main__":
    main()     
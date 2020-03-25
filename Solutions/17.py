class Exercise17Handler():
    def __init__(self):
        pass

    def bankBalance(self):
        self.balance = 0

        while True:
            self.statement = input("> ")
            
            if not self.statement:
                break
            else:
                if self.statement[0] == "D":
                    self.balance += int(self.statement[2:])
                elif self.statement[0] == "W":
                    self.balance -= int(self.statement[2:])
        
        print("Balance: ",self.balance)

def main():
    Exercise17Handler().bankBalance()

if __name__ == "__main__":
    main()


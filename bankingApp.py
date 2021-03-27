print("Welcome to Banking System \n")
global inputName
inputName= str(input("Enter your Name: "))


def menu():
    print("Select options from menu")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Money Transfer")
    print("5. Type of Account")
    print("6. Compare Account")
    print ("7. Exit")


class Account():
    custName = ["Ahmad", "Ali", "Usman", "Haider", "Karim"]
    custBal = [1000, 500, 500, 3000, 1500]
    accType = ["c", "s", "s", "c", "s"]
    index = custName.index(inputName)

    def __init__(self):
        pass

    def balanceEnq(self):
        balance = self.custBal[self.index]
        return balance

    def withdrawMoney(self, withdrawMoney):
        balance = self.balanceEnq()
        print(inputName, " you have ", balance, " rupees")
        if(withdrawMoney>balance):
            print(inputName, " you have insufficient balance for this transaction")
        else:
            self.custBal[self.index] = balance-withdrawMoney
            print("Money withdrawl successfull")
            print(inputName, " your current balance is: ", self.custBal[self.index])
        return self.custBal[self.index]

    def depositMoney(self, depositMoney):
        balance = self.balanceEnq()
        print(balance)
        self.custBal[self.index] = balance+depositMoney
        print("Money deposited successfully")
        print(inputName, " your current balance is: ", self.custBal[self.index])
        return self.custBal[self.index]

    def transMoney(self, recvrName, transAmnt):
        balance = self.balanceEnq()
        print(inputName, " you have ", balance, " rupees")
        recvrIndex = self.custName.index(recvrName)
        recvrBalnc = self.custBal[recvrIndex]
        if(self.custBal[self.index]<transAmnt):
            print(inputName, " you have insufficient balance for this money transfer")
        else:
            self.custBal[self.index] = balance-transAmnt
            self.custBal[recvrIndex] = recvrBalnc+transAmnt
            print("Money Transfer Successfull")
            print(inputName, " your current balance is: ", self.custBal[self.index])
            print("Receiver Balance: ", self.custBal[recvrIndex])
        return self.custBal[self.index]

    def typeOfAcc(self):
        if(self.accType[self.index] == "c"):
            print (inputName, " has a current account.")
        else:
            print(inputName, " has a saving account.")

    def compare(self, recvrName):
        recvrIndex = self.custName.index(recvrName)
        recvrBalnc = self.custBal[recvrIndex]
        if (self.custBal[self.index] > recvrBalnc):
            print(inputName, " has larger bank balance than ", recvrName)
        elif (self.custBal[self.index] < recvrBalnc):
            print(recvrName, " has larger bank balance than ", inputName)
        else:
            print (inputName, " and ", recvrName, " has equal bank balance ")


def main():
    accObj = Account()
    if (inputName not in accObj.custName):
        print(inputName, " has not an account")

    else:
        menu()
        inputOpt = int(input("Enter option from given menu: "))

        if inputOpt >= 7 or inputOpt < 1:
            print("Program Exit")

        else:
            if inputOpt == 1:
                print("Welcome to Balance Enquiry")
                res = accObj.balanceEnq()
                print(inputName, " your available balance is: ", res)


            elif inputOpt == 2:
                print("Withdraw Money")
                withdraw = int(input("Enter amount you want to withdraw: "))
                accObj.withdrawMoney(withdraw)

            elif inputOpt == 3:
                print("Deposit Money")
                deposit = int(input("Enter amount you want to deposit: "))
                accObj.depositMoney(deposit)

            elif inputOpt == 4:
                print("Money Transfer")
                recvrName = str(input("Enter name of the receiver: "))
                if (recvrName not in accObj.custName):
                    print(recvrName, " has not an account")
                else:
                    transAmnt = int(input("Enter amount you want to send: "))
                    accObj.transMoney(recvrName,transAmnt)

            elif inputOpt == 5:
                print ("Check your account type")
                accObj.typeOfAcc()

            elif inputOpt == 6:
                print("Compare your account")
                recvrName = str(input("Enter name of the person to compare your account with: "))
                if (recvrName not in accObj.custName):
                    print(recvrName, " has not an account")
                else:
                    accObj.compare(recvrName)

if __name__ == "__main__":
    main()
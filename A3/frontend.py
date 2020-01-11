import sys, os

#Agent Class
class Agent:

    ''' the init sets the variable that are needed for any account
        such as the account number that the user/actor is refering
        to and the balance that ever account will have, the variables
        are just being created right now and do not have any usable data '''
    def __init__(self, accountNum, balance):
        self.accountNum = accountNum
        self.balance = balance

    #Agent no argument constructor
    def __init__(self):
        self.accountNum = 0
        self.balance = 0

    #Function to create an Agent account
    def createacct(self, accountNum, accountName):
        if(checkAccountNum(accountNum)==True and checkAccountName(accountName)==True):
            #save account num and name to transaction summary file
            print("Created account!")
            print("Account Info:")
            print("Account Number: " + str(accountNum))
            print("Account Name: " + str(accountName))
        else:
            print("Invalid Account Number or Name!")


    #Function to delete an account
    def deleteacct(self, accountNum, accountName):
        if(checkAccountNum(accountNum)==True and checkAccountName(accountName)==True):
            #save account num and name to transaction summary file
            print("Deleted account!")
            print("Account Info:")
            print("Account Number: " + str(accountNum))
            print("Account Name: " + str(accountName))
        else:
            print("Invalid Account Number or Name!")

    #Function to deposit into an agents account
    def deposit(self,amount, accountName):
        if(self.checkAgentDepositAmount(amount)==True):
            self.balance += int(amount)
            print("Added " + str(amount) + " to your account!\n")
            print("Your new balance is: " + str(self.balance))
        else:
            print("Can't deposit over $999,999.99 try a smaller amount")

    #Function to check if the amount an agent is trying to deposit is acceptable
    def checkAgentDepositAmount(self,transactionAmount):
        # if (!(isinstance(transactionAmount, int))):
        #     return False
        if(int(transactionAmount)<=99999999 and int(amount)>0):
            return True
        else:
            return False


    #Function to withdraw from an agent account
    def withdraw(self,accountNum, amount):
        if(checkAccountNum(accountNum)==True and self.checkAgentWithdrawAmount(amount)==True):
            self.balance -= int(amount)
            print("Withdrew " + str(amount) + " from account " + str(accountNum))
        else:
            print("Invalid account number or amount to withdraw.")

    #Function to check amount an agent is withdrawing
    def checkAgentWithdrawAmount(self,amount):
        if(int(amount)<=99999999 and int(amount)>0):
            return True
        else:
            return False

    #Function to transfer money between accounts
    def transfer(self,fromAcctNum, toAcctNum, amount):
        fromAcct = Machine()
        toAcct = Machine()
        fromAcct.balance -= int(amount)
        toAcct.balance += int(amount)
        print("Transferred " + str(amount) + " from account " + str(fromAcctNum) + " to account " + str(toAcctNum))



    #Function to check if the amount an agent is trying to transfer is acceptable
    def checkAgentTransferAmount(self,transactionAmount):
        if(int(transactionAmount)<=99999999 and int(amount)>0):
            return True
        else:
            return False

#Machine Class
class Machine:


    ''' the init sets the variable that are needed for any account
        that is coming from the machine which means that there are
        no agent privledges such as the account number that the user/actor
        is refering to and the balance that ever account will have, the variables
        are just being created right now and do not have any usable data '''
    def __init__(self, accountNum, balance):
        self.accountNum = accountNum
        self.balance = balance

    #Machine no argument constructor
    def __init__(self):
        self.accountNum = 0
        self.balance = 0


    #Function to deposit into an agents account
    def deposit(self,amount, accountNum):
        self.balance += int(amount)
        print("Added " + str(amount) + " to your account!\n")
        print("Your new balance is: " + str(self.balance))

    #Function to check if the amount a machine is trying to deposit is acceptable
    def checkMachineDepositAmount(self,transactionAmount):
        # if (!(isinstance(transactionAmount, int))):
        #     return False
        if(int(transactionAmount)<=2000000 and int(amount)>0):
            return True
        else:
            return False


    #Function to withdraw from a machine account
    def withdraw(self,accountNum, amount):
        if(checkAccountNum(accountNum)==True and self.checkMachineWithdrawAmount(amount)==True):
            self.balance -= int(amount)
            print("Withdrew " + str(amount) + " from account " + str(accountNum))
        else:
            print("Invalid account number or amount to withdraw.")

    def checkDailyWithdraw(self,accountNum, amount):
        return 0

    #Function to check the amount a machine is withdrawing
    def checkMachineWithdrawAmount(self,amount):
        if(int(amount)<=100000 and int(amount)>0):
            return True
        else:
            return False


        '''This function handles a transfer from one account to another
        it takes the account number of both the sender and reciver
        as well as the amount to be transfered all three variables
        are checked to make sure that they are valid'''
    def transfer(self,fromAcctNum, toAcctNum, amount):
        if(checkAccountNum(fromAcctNum)==True and checkAccountNum(toAcctNum)==True and self.checkMachineTransferAmount(amount)==True):
            fromAcct = Machine()
            toAcct = Machine()
            fromAcct.balance -= int(amount)
            toAcct.balance += int(amount)
            print("Transferred " + str(amount) + " from account " + str(fromAcctNum) + " to account " + str(toAcctNum))
        else:
            print("Invalid from account, to account or amount.")

    #Function to check a machines transfer amount
    def checkMachineTransferAmount(self,amount):
        if(int(amount)<=1000000 and int(amount)>0):
            return True
        else:
            return False
        #function to check transfer amount for agent

    def checkDailyMachineTransfer(self,amount):
        #Reads transaction summary file
        #Checks if the amount their trying to transfer will exceed their daily Limit
        #If not return True
        #Otherwise False
        return True




#-------------------------------------SHARED METHODS-----------------------------------#
'''This login in method is used by both the machine and agent so it is shared and not in either class'''
def login():
    while True:
        begin = input("Please login with your login type (machine or agent):\n")
        if(begin == "exit"):
            sys.exit()
        elif(begin != "login machine" and begin != "login agent"):
            print("Incorrect format! Please try logging in again with the format \"login machine\"")
        else:
            transaction, loginType = begin.split(" ")
            break
    print("Logged in as: " + loginType)
    return loginType

#Function that logs user out by writing the transaction summary file and exiting the program
def logout():
    #write the transaction summary file
    print("Logged out!")
    sys.exit()

'''Again this is a shared method that calls a method based on the list of actions that can be preformed such as:
    creating an account
    deleating an account
    depositing money into an account
    wthdrawling money out of an account
    loging out of an account
    transfering money between two accounts'''
def getTransactionType():
    while True:
        transactionType = input("What transaction are you trying to perform?\n")
        userInput = transactionType.split(" ")
        if(userInput[0]=="createacct" or userInput[0]=="deleteacct" or userInput[0]=="deposit" or userInput[0]=="withdraw" or userInput[0]=="logout" or userInput[0]=="transfer"):
            return transactionType
        else:
            print("Invalid transaction type!")

def checkDailyDeposit():
    return 0


#-------------------------------------ACCOUNT-NUMBER-VERIFICATION-------------------------------------#

#Function that returns true if an account number already exists
def checkAccountExist(accountNum):
    #this function will read the accounts list file
    # if(accountNum in accounts list file):
    #     return True
    # else:
    #     return False
    return True

#Function to check if an account number has the correct format and doesn't already exist
def checkAccountNum(accountNum):
    if(len(accountNum)==7 and accountNum[0] != '0'):
        #if(checkAccountExist(accountNum)==False):
        return True
    else:
        return False


#-------------------------------------ACCOUNT-NAME-VERIFICATION-------------------------------------#

#Function to check the constraints on an account name
def checkAccountName(accountName):
    if(((len(accountName)<3) or len(accountName)>30) and (accountName[0] != ' ' or accountName[len(accountName)-1] != ' ')):
        return False
    else:
        return True



#------------------------------------------MAIN-DRIVER-PROGRAM---------------------------------------#

#main program that drives Quinterac
#Overall program intention is to allow the user to perform transactions in their selected MODE
#Input file will be accounts list file
#Output file will be transaction summary file
#Program does not write files as of right now, this will be implemented in future iterations as it is backend functionality not frontend
#program is run by typing "python3 frontend.py"

def main():
    #Get the login type and login
    loginType=login()
    #Create an object of the class based on what user is signing in as
    if(loginType=="machine"):
        userType = Machine()
    elif(loginType=="agent"):
        userType = Agent()
    #while(True):
    #Split the result to organize information of transaction
    transactionInfo = getTransactionType()
    transactionType = transactionInfo.split(" ")

    #If the transaction type is logout exit the program
    if(transactionType[0]=="logout"):
        logout()


#---------------------------------------CREATE ACCT CHECK----------------------------------------------

    #If a machine is trying to create an account dont allow it
    if(transactionType[0]=="createacct" and isinstance(userType, Machine)==True):
        print("Must be logged into agent mode to create an account!")

    #If its an agent create the account
    if(transactionType[0]=="createacct" and isinstance(userType, Agent)==True):

        accountNum = transactionType[1]
        accountName = transactionType[2]
        userType.createacct(accountNum, accountName)


#---------------------------------------DELETE ACCT CHECK----------------------------------------------

    #If machine is trying to delete an account dont allow it
    if(transactionType[0]=="deleteacct" and isinstance(userType, Machine)==True):
        print("Must be logged into agent mode to delete an account!")
    #If its an agent delete the account
    if(transactionType[0]=="deleteacct" and isinstance(userType, Agent)==True):
        accountNum = transactionType[1]
        accountName = transactionType[2]
        userType.deleteacct(accountNum, accountName)

# #---------------------------------------DEPOSIT-CHECK----------------------------------------------

# #---------------------------------------MACHINE MODE-----------------------------------------------
    #Check for deposit if machine mode perform its necessary specific checks
    if(transactionType[0]=="deposit" and isinstance(userType, Machine)==True):
        accountNum = transactionType[1]
        amount = transactionType[2]
        if(checkAccountNum(accountNum)==True and userType.checkMachineDepositAmount(amount)==True):
            print("Deposited " + str(amount) + " into account: " + str(accountNum))
            userType.deposit(amount, accountNum)
        elif(checkAccountNum(accountNum)==True and userType.checkMachineDepositAmount(amount)==False):
            print("Invalid Deposit Amount")
        elif(checkAccountNum(accountNum)==False and userType.checkMachineDepositAmount(amount)==True):
            print("Invalid Account Number")
        else:
            #checks the daily deposit sum for the account looking to deposit money
            dailyDepositLimit = checkDailyDeposit(accountNum)
            if(dailyDepositLimit>5000):
                print("Daily Deposit Limit reached! Please try again tomorrow!")
            else:
                print("Deposited " + str(amount) + " into account: " + str(accountNum))
                userType.deposit(accountNum, amount)


# #---------------------------------------AGENT MODE-----------------------------------------------

    #Check for deposit if agent mode perform its necessary specific checks
    if(transactionType[0]=="deposit" and isinstance(userType, Agent)==True):
        accountNum = transactionType[1]
        amount = transactionType[2]

        if(checkAccountNum(accountNum)==True):
            userType.deposit(accountNum, amount)
            print("Deposited " + str(amount) + " into account: " + str(accountNum))

        elif(checkAccountNum(accountNum)==True and userType.checkAgentTransferAmount(amount)==True):
            print("Invalid Deposit Amount")
        elif(checkAccountNum(accountNum)==False and userType.checkAgentTransferAmount(amount)==True):
            print("Invalid Account Number")


# #---------------------------------------WITHDRAW-CHECK----------------------------------------------

# #---------------------------------------MACHINE MODE-----------------------------------------------
    #Check for deposit if machine mode perform its necessary specific checks
    if(transactionType[0]=="withdraw" and isinstance(userType, Machine)==True):
        accountNum = transactionType[1]
        amount = transactionType[2]
        #200000 because input is in cents
        #check account returns true if its a valid account number otherwise false
        if(checkAccountNum(accountNum)==True and userType.checkMachineWithdrawAmount(amount)==True):
            #checks the daily deposit sum for the account looking to deposit money
            dailyWithdrawLimit = userType.checkDailyWithdraw(accountNum, amount)
            if(dailyWithdrawLimit>5000):
                print("Daily Withdraw Limit reached!")
            else:
                userType.withdraw(accountNum, amount)

        elif(checkAccountNum(accountNum)==True and userType.checkMachineWithdrawAmount(amount)==False):
            print("Invalid Withdraw Amount")

        elif(checkAccountNum(accountNum)==False and userType.checkMachineWithdrawAmount(amount)==True):
            print("Invalid Account Number")


# #---------------------------------------AGENT MODE-----------------------------------------------
    #Check for withdraw if agent mode perform its necessary specific checks
    if(transactionType[0]=="withdraw" and isinstance(userType, Agent)==True):
        accountNum = transactionType[1]
        amount = transactionType[2]

        if(checkAccountNum(accountNum)==True and userType.checkAgentWithdrawAmount(amount)==True):
            userType.withdraw(accountNum, amount)
            print("Withdrew " + str(amount) + " from account: " + str(accountNum))

        elif(checkAccountNum(accountNum)==True and userType.checkAgentWithdrawAmount(amount)==False):
            print("Invalid Withdraw Amount")

        elif(checkAccountNum(accountNum)==False and userType.checkAgentWithdrawAmount(amount)==True):
            print("Invalid Account Number")


# #---------------------------------------TRANSFER-CHECK----------------------------------------------

# #---------------------------------------MACHINE MODE-----------------------------------------------
    #Check for transfer if machine mode perform its necessary specific checks
    if(transactionType[0]=="transfer" and isinstance(userType, Machine)==True):
        fromAccountNum = transactionType[1]
        toAccountNum = transactionType[2]
        amount = transactionType[3]
        if(checkAccountNum(fromAccountNum)==True and checkAccountNum(toAccountNum)==True and userType.checkMachineTransferAmount(amount)==True):
            dailyFromDepositLimit = userType.checkDailyMachineTransfer(fromAccountNum)
            dailyToDepositLimit = userType.checkDailyMachineTransfer(toAccountNum)
            if(dailyFromDepositLimit>10000 and dailyToDepositLimit>10000):
                print("Daily Transfer Limit reached!")
            else:
                userType.transfer(fromAccountNum, toAccountNum, amount)


        elif(checkAccountNum(fromAccountNum)==True and checkAccountNum(toAccountNum)==False and userType.checkMachineTransferAmount(amount)==True):
            print("Invalid to Account Number")

        elif(checkAccountNum(fromAccountNum)==False and checkAccountNum(toAccountNum)==True and userType.checkMachineTransferAmount(amount)==True):
            print("Invalid from Account Number")

        elif(checkAccountNum(fromAccountNum)==True and checkAccountNum(toAccountNum)==True and userType.checkMachineTransferAmount(amount)==False):
            print("Invalid transfer amount")



# #---------------------------------------AGENT MODE-----------------------------------------------
#Check for deposit if agent mode perform its necessary specific checks
    if(transactionType[0]=="transfer" and isinstance(userType, Agent)==True):
        fromAccountNum = transactionType[1]
        toAccountNum = transactionType[2]
        amount = transactionType[3]


        if(checkAccountNum(fromAccountNum)==True and checkAccountNum(toAccountNum)==True and userType.checkAgentTransferAmount(amount)==True):
            userType.transfer(fromAccountNum, toAccountNum, amount)


        elif(checkAccountNum(fromAccountNum)==True and checkAccountNum(toAccountNum)==False and userType.checkAgentTransferAmount(amount)==True):
            print("Invalid to Account Number")

        elif(checkAccountNum(fromAccountNum)==False and checkAccountNum(toAccountNum)==True and userType.checkAgentTransferAmount(amount)==True):
            print("Invalid from Account Number")

        elif(checkAccountNum(fromAccountNum)==True and checkAccountNum(toAccountNum)==True and userType.checkAgentTransferAmount(amount)==False):
            print("Invalid transfer amount")

'''The intention of this program is to communicate with the user and find out their intent.
The program is intended to be run using communication through inputing text there are currently no input or output files
being used as this is the first prototype and there are comments where the input/output files will exist eventually'''
if __name__ == "__main__":
      main()

# Quinterac Backend - CISC 327

def transactionListFromFile(file):
    # This function imports that transaction list from the merged transaction file.
    # The transaction are stored in a 2D list.
    transactionList = []
    f = open(file,"r")
    while True:
        transaction = str.strip(f.readline())
        if transaction == "":
            break
        elif transaction[0:2] in "DEPWDRXFRNEWDEL":
            transactionInfo =transaction.split(" ")
            transactionList.append(transactionInfo)
        else:
            continue
    return transactionList

def masterAccountListFromFile(file):
    # This function imports the master account file and stores it in a list of lists.
    masterAccountList = []
    f = open(file,"r")
    while True:
        account = str.strip(f.readline())
        if account == "": # No accounts left
            break
        accountInfo = account.split(" ")
        masterAccountList.append(accountInfo)
    
    return masterAccountList # Returns the list of accounts.

def mergeTSF(file):
    # This function accesses the folder containing all the daily transaction files
    # and merges them into one "DailyTransactions" file.
    list_TSF = []
    list_all_transactions = []
    for subdir, dirs, files in os.walk("transactionSummaryFiles"):
        for file in files:
            list_TSF.append("transactionSummaryFiles/" + file)
        for file in list_TSF:
            list = open(file, "r")
            for line in list:
                list_all_transactions.append(line)
    f = open("DailyTransactions.txt", "w")
    for line in list_all_transactions:
        f.write(line)
        if line == "EOS":
            f.write("\n")
            
def cleanup(master):
    # This function takes in the master account list and writes the updated version of the
    # master account list to the file.
    validAccountsList = []
    masterFile = open("master.txt", "w")
    validAccountFile = open("validAccountsList.txt", "w")

    files = glob.glob('transactionSummaryFiles/*')
    for f in files:
        os.remove(f)

    for line in master:
        full_User = str(master[line][0]) + " " + str(master[line][1]) + " " +  str(master[line][2])
        masterFile.write(full_User)
        validAccountFile.write(master[line][0])
        validAccountFile.write("\n")

def createacct_action(master, transaction):
    # This function takes the master account list and the create transaction as the
    # parameters and returns the master account list with the account added.
    master.append([transaction[1],"0",transaction[2]])
    return master
        
def deleteacct_action(master, transaction):
    # This function takes the master account list and the delete transaction as the
    # parameters and returns the master account list with the account deleted
    # Deletion causes balance to become 0 and the account's removal from the valid accounts
    # list in the front end.
    for account in master:
        if account[0] == transaction[1]:
            account[1] == "0" # Account balance becomes zero.
    return master # Returns the master list

def deposit_action(master, transaction):
    # This function finds the appropriate account in the master account list, deposits the
    # amount that the transaction specifies and returns the master account list.
    for account in master:
        if account[0] == transaction[1]:
            account[1] = str(int(account[1]) + int(transaction[2]))
    return master

def withdraw_action(master, transaction):
    # This function finds the appropriate account in the master account list, withdraws the
    # amount and returns the master account list.
    for account in master:
        if account[0] == transaction[1]:
            account[1] = str(int(account[1]) - int(transaction[2]))
    return master

def transfer_action(master, transaction):
    # This function finds the two accounts in the master account list, withdraws
    # the amount from one account and then deposits it into the next account.
    for account in master: # Removes the balance from the "from account".
        if account[0] == transaction[1]:
            account[1] = str(int(account[1]) - int(transaction[2]))
    for account in master: # Adds the balance to the "to account".
        if account[0] == transaction[3]:
            account[1] = str(int(account[1]) + int(transaction[2]))
    return master  

def action(masterAccountList, transaction):
    # This function finds what action the certain transaction calls for and runs the
    # appropriate function. It then cleans up the master account list and returns it.
    if transaction[0] == "NEW":
        masterAccountList = createacct_action(masterAccountList, transaction)
    elif transaction[0] == "DEL":
        masterAccountList = deleteacct_action(masterAccountList, transaction)
    elif transaction[0] == "DEP":
        masterAccountList = deposit_action(masterAccountList, transaction)
    elif transaction[0] == "WDR":
        masterAccountList = withdraw_action(masterAccountList, transaction)
    elif transaction[0] == "XFR":
        masterAccountList = transfer_action(masterAccountList, transaction)
    #cleanup(masterAccountList)
    return masterAccountList

def processTransactions(masterAccountList, transactionList):
    # This function iterates through the list of transactions and calls
    # action to update the master account list after each transaction.
    newAccountsList = masterAccountList
    for line in transactionList:
        newAccountsList = action(newAccountsList,line)
    return newAccountsList

def writeMasterAccountList(masterAccountList):
    # This function writes the updated master account list to the "MasterAccount" file
    f = open("MasterAccounts.txt","w")
    for account in masterAccountList:
        f.write(str(account[0]+" "+str(account[1])+" "+str(account[2])+"\n"))
    f.close()
    
def first(element):
    # Returns the first element in a list (for sorting the new master account list.
    return element[0]

def main():
    #mergeTFS("DailyTransactions.txt")
    transactionList = transactionListFromFile("DailyTransactions.txt")
    masterAccountList = masterAccountListFromFile("MasterAccounts.txt")
    newMaster = processTransactions(masterAccountList, transactionList)
    newMaster.sort(key=first,reverse=True) # Sorts in descending order by the account number
    writeMasterAccountList(newMaster)
main()
    
    




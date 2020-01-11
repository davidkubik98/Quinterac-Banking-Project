import sys, os, frontend, glob


#This function takes the master file of all the users and makes a tuple of lists to have access to every data point in the list
#Takes the name of the master file as input and returns the tuple of lists as an output
def masterListFromFile(file):
        master = {}
        index_master = 0
        f = open(file, "r")
        for line in f:
            line.strip("\n")
            master_info = line.split(" ")
            master[index_master] = [master_info[0], master_info[1], master_info[2]]  # number, balance, name
            index_master+= 1
        return master

#This function makes a list of all the actions that need to be preformed from the aggregation of the daily transaction files
#Takes the name of the transaction text file as input and outputs a list of lists of the actions to take
def transactionListFromFile(file):
        master = {}
        index_master = 0
        f = open(file, "r")
        for line in f:
            if line[0:2] in "DEPWDRXFRNEWDEL":
                master_info = line.split(" ")
                master[index_master] = [master_info[0], master_info[1], master_info[2],master_info[3],master_info[4]]
                index_master+= 1
            else:
                master[index_master] = "EOS"
                index_master+= 1
        return master

#This function merges all the daily transaction files from each session into one big file of them all seperated by the "EOS" string
#Input nothing and it outputs a new transaction file with all actions taken over all the sessions
def mergeTSF():
    list_TSF = []
    list_all_transactions = []
    for subdir, dirs, files in os.walk("transactionSummaryFiles"):
        for file in files:
            list_TSF.append("transactionSummaryFiles/" + file)
        for file in list_TSF:
            list = open(file, "r")
            for line in list:
                list_all_transactions.append(line)
    f = open("transactions.txt", "w")
    for line in list_all_transactions:
        f.write(line)
        if line == "EOS":
            f.write("\n")

#This function takes the foder holding all the session files and deletes then when done
def cleanup():
    files = glob.glob('transactionSummaryFiles/*')
    # for f in files:
    #     os.remove(f)


#This function calls the respective functions for each transaction summary file line
#Input is the master list of all the users and the transactions that need to be processed
def actions(master, transactions):
    line_index = 0
    for line in transactions:
        action = transactions[line][0]
        line_index += 1
        if action == "NEW":
            createacct_action(master, transactions[line])
        if action == "DEL":
            delete_action(master, transactions[line])
        if action == "DEP":
            deposit_action(master, transactions[line])
        if action == "WDR":
            withdraw_action(master, transactions[line])
        if action == "XFR":
            transfer_action(master, transactions[line])
        master = masterListFromFile("master.txt")
    cleanup()


#This function makes a new user
#Input is the master list of all the users and the transaction that has happened in the list e.g. ["DEP", "1234567", "10000", "1234567", "Michael"]
def createacct_action(master, transaction):
    accountNum = transaction[1]
    amount = int(transaction[2])
    accountName = transaction[4]
    if(checkAccountNum(accountNum)==True and checkAccountExist(accountName)==True):
        valid = open("validAccountsList.txt", "r")
        for line in valid:
            if(accountNum==line):
                print("Account number already being used by another user try again.")
                return

        #save account num and name to transaction summary file
        print("Created account!")
        print("Account Info:")
        print("Account Number: " + str(accountNum))
        print("Account Name: " + str(accountName))
        fileMaster = open("master.txt", "a+")
        masterPerson = str(str(accountNum) + " " + str(amount) + " " + str(accountName))
        fileMaster.write("\n")
        fileMaster.write(masterPerson)
        fileMaster.close()
        file = open("validAccountsList.txt", "a+")
        file.write(accountNum)
        file.close()
    else:
        print("Invalid Account Number or Name!")

#This function deposits money into a user account by incrementing the users balance by the ammount specified
#Input is the master list of all the users and the transaction that has happened in the list e.g. ["DEP", "1234567", "10000", "1234567", "Michael"]
def deposit_action(master, transaction):
    person_id = transaction[1]
    amount = transaction[2]
    person_name = transaction[4]
    for account in master:
        if master[account][0] == person_id:
            master[account][1] = int(amount) + int(master[account][1])
    masterFile = open("master.txt", "w")
    for line in master:
        full_User = str(master[line][0]) + " " + str(master[line][1]) + " " +  str(master[line][2])
        masterFile.write(full_User)

#This function withdrawls money into a user account by decrementing the users balance by the ammount specified
#Input is the master list of all the users and the transaction that has happened in the list e.g. ["WDR", "1234567", "10000", "1234567", "Michael"]
def withdraw_action(master, transaction):
    if(not(transaction[0] == "WDR")):
        print("This is not the proper withdrawl code")
        return
    if(not (len(transaction[1]) == 7)):
        print("This is not the proper user ID number")
        return
    if(not (transaction[0] == 0)):
        print("This is not the proper user ID number")
        return
    if(not (transaction[2] == 0)):
        print("This is not enough money to withdrawal")
        return
    if(not (len(transaction[3]) == 7)):
        print("This is not the proper user ID number")
        return
    if(not (transaction[3]) == 0):
        print("This is not the proper user ID number")
        return
    person_id = transaction[1]
    amount = transaction[2]
    person_name = transaction[4]
    for account in master:
        accountNum = int(master[account][0].strip("\n"))
        accountName = str(master[account][2].strip("\n"))
        if accountNum == int(person_id) and accountName == str(person_name):
            master[account][1] = int(master[account][1]) - int(amount)
            print("Withdrew " + str(amount))
        masterFile = open("master.txt", "w")
        for line in master:
            full_User = str(master[line][0]) + " " + str(master[line][1]) + " " +  str(master[line][2])
            masterFile.write(full_User)
        else:
            print("Incorrect Name or Account Number")

#This function transfers money into a user account by decrementing the users balance by the ammount specified and incrementing the other users balance by the same amount
#Input is the master list of all the users and the transaction that has happened in the list e.g. ["XFR", "1234567", "10000", "1234565", "Michael"]
def transfer_action(master, transaction):
    fromAccount_id = transaction[1]
    toAccount_id = transaction[3]
    amount = transaction[2]
    person_name = transaction[4]
    for account in master:
        if master[account][0] == fromAccount_id and master[account][2] == person_name:
            master[account][1] = int(master[account][1]) - int(amount)
        if master[account][0] == toAccount_id:
            master[account][1] = int(amount) + int(master[account][1])
    masterFile = open("master.txt", "w")
    for line in master:
        full_User = str(master[line][0]) + " " + str(master[line][1]) + " " +  str(master[line][2])
        masterFile.write(full_User)

#This function deletes a user from the system which involves setting their balance to zero and taking them off the valid accounts list
#Input is the master list of all the users and the transaction that has happened in the list e.g. ["XFR", "1234567", "10000", "1234565", "Michael"]f
def delete_action(master, transaction):
    deleteUserNum = str(transaction[1])
    validAccounts = open("validAccountsList.txt", "r")
    validList = []
    for line in validAccounts:
        if (not(line == deleteUserNum)):
            validList.append(line)
    validAccounts.close()
    validAccounts = open("validAccountsList.txt", "w")
    for num in validList:
        validAccounts.write(num)
    for line in master:
        if (master[line][0] == deleteUserNum):
            master[line][1] = 0
    masterFile = open("master.txt", "w")
    for line in master:
        masterFile.write(master[line])


#Function that returns true if an account number already exists
def checkAccountExist(accountNum):
    file = open("validAccountsList.txt", "r")
    for line in file:
        if (accountNum==line):
            return False
    return True

#Function to check if an account number has the correct format and doesn't already exist
def checkAccountNum(accountNum):
    if(len(accountNum)==7 and accountNum[0] != '0'):
        return True
    else:
        return False

#This is the main function for the backend of the system. It preforms all the logic for a bank
# including making deposits, withdrawls, transfers, making a new user and deleting an existing user
# It works with a master file with all users, a valid accounts file with all the valid account numbers, and a transaction file
# that holds all the actions that need to be preformed from each session that happened that day
def main():
    mergeTSF()
    transaction = transactionListFromFile("transactions.txt")
    master = masterListFromFile("master.txt")
    actions(master, transaction)



if __name__ == "__main__":
    main()

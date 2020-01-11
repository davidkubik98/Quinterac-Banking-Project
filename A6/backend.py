import sys
import os
import frontend
import glob


# This function merges all the daily transaction files from each session into one big file of them all seperated by the "EOS" string
# Input nothing and it outputs a new transaction file with all actions taken over all the sessions
def mergeTSF():
    # This is a relative path so it needs to be changed to whichever user is running the program and have their correct path
    path = "/Users/michael/Desktop/SQA/A6/transactionSummaryFiles"
    files = []
    merged_transactions = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

    for file_path in files:
        transactionFile = open(file_path, "r")
        for line in transactionFile:
            # if(line=="EOS")
            merged_transactions.append(line)

    merged = open("mergedTransactionSummaryFile.txt", "w")
    for line in merged_transactions:
        if line == "EOS\n":
            merged.write("")
        else:
            merged.write(line)
    merged.write("EOS")

# Makes a list of lists of ever person that is in the master list file


def masterListFromFile():
    master = []
    f = open("master.txt", "r")
    for line in f:
        line.strip("\n")
        master_info = line.split(" ")
        person = [master_info[0], master_info[1], master_info[2]]  # number, balance, name
        master.append(person)
    return master

# Makes a list of lists of ever person that is in the valid accounts file


def validAccountsListFromFile():
    validAccountsList = []
    f = open("validAccountsList.txt", "r")
    for line in f:
        validAccountsList.append(line[0:7])
    return validAccountsList


# Makes a list of lists of every action that needs to be preformed
def transactionListFromFile():
    f = open("mergedTransactionSummaryFile.txt", "r")
    task = []
    for line in f:
        if line[0:2] in "DEPWDRXFRNEWDEL":
            line = line.strip("\n")
            line = line.split(" ")
            task.append([line[0], line[1], line[2], line[3], line[4]])
        else:
            task.append("EOS")
    return task

# This is the main function that is used to run every action with its corrosponding method


def actions():
    transactions = transactionListFromFile()
    master = masterListFromFile()
    valid = validAccountsListFromFile()
    for line in transactions:
        action = line[0]
        if action == "NEW":
            master, valid = create_action(master, line, valid)
        if action == "DEL":
            master, valid = delete_action(master, line, valid)
        if line[1] in valid:
            if action == "DEP":
                master = deposit_action(master, line)
            if action == "WDR":
                master = withdraw_action(master, line)
            if action == "XFR":
                master = transfer_action(master, line)
    masterFile = open("master.txt", "w")
    for line in master:
        masterFile.write(str(line[0]) + " " +
                         str(line[1]) + " " + str(line[2]).rstrip() + "\n")
    validAccountFile = open("validAccountsList.txt", "w")
    for line in valid:
        validAccountFile.write(line + "\n")
    masterFile.close()
    validAccountFile.close()
    cleanup()


# This function creates an account for a user if they have a unique id
# Input is the master list of all the users and the transaction that has happened in the list e.g. ["DEP", "1234567", "10000", "1234567", "Michael"] and the valid accounts list
def create_action(master, transaction, valid):
    if not(len(master) == 0):
        for line in master:
            if str(line[0]) == str(transaction[1]):
                print("This account number is already taken")
                return master, valid
    valid.append(transaction[1])
    master.append([transaction[1],  " 0 ", transaction[4] + "\n"])
    return master, valid


# This function deposits money into a user account by incrementing the users balance by the ammount specified
# Input is the master list of all the users and the transaction that has happened in the list e.g. ["DEP", "1234567", "10000", "1234567", "Michael"]
def deposit_action(master, transaction):
    person_id = transaction[1]
    amount = transaction[2]
    person_name = transaction[4]
    index = 0
    for account in master:
        if account[0] == person_id:
            master[index][1] = int(amount) + int(account[1])
        index = index + 1
    return master

# This function withdrawls money into a user account by decrementing the users balance by the ammount specified
# Input is the master list of all the users and the transaction that has happened in the list e.g. ["WDR", "1234567", "10000", "1234567", "Michael"]


def withdraw_action(master, transaction):
    if(not(transaction[0] == "WDR")):
        print("This is not the proper withdrawl code")
        return
    if(not (len(transaction[1]) == 7)):
        print("This is not the proper user ID number")
        return
    if((transaction[2] == 0)):
        print("This is not enough money to withdrawal")
        return
    if(not (len(transaction[3]) == 7)):
        print("This is not the proper user ID number")
        return
    if((transaction[3]) == 0):
        print("This is not the proper user ID number")
        return
    person_id = transaction[1]
    amount = transaction[2]
    person_name = transaction[4]
    for account in master:
        accountNum = account[0]
        accountName = str(account[2])
        if accountNum == int(person_id) and accountName == str(person_name):
            master[account][1] = int(master[account][1]) - int(amount)
    return master

# This function transfers money into a user account by decrementing the users balance by the ammount specified and incrementing the other users balance by the same amount
# Input is the master list of all the users and the transaction that has happened in the list e.g. ["XFR", "1234567", "10000", "1234565", "Michael"]


def transfer_action(master, transaction):
    fromAccount_id = transaction[1]
    toAccount_id = transaction[3]
    amount = transaction[2]
    person_name = transaction[4]
    for account in master:
        if account[0] == fromAccount_id and account[2] == person_name:
            account[1] = int(account[1]) - int(amount)
        if account[0] == toAccount_id:
            account[1] = int(amount) + int(account[1])
    return master

# This function deletes a user from the system which involves setting their balance to zero and taking them off the valid accounts list
# Input is the master list of all the users and the transaction that has happened in the list e.g. ["XFR", "1234567", "10000", "1234565", "Michael"] and the valid accounts list


def delete_action(master, transaction, valid):
    deleteUserNum = str(transaction[1])
    for num in valid:
        if (str(num) == deleteUserNum):
            valid.remove(transaction[1])
    index = 0
    for line in master:
        if (line[0] == deleteUserNum):
            master[index][1] = 0
        index = index + 1
    return master, valid

# Function that returns true if an account number already exists
def checkAccountExist(accountNum):
    file = open("validAccountsList.txt", "r")
    for line in file:
        if (accountNum == line):
            return False
    return True

# Function to check if an account number has the correct format and doesn't already exist


def checkAccountNum(accountNum):
    if(len(accountNum) == 7 and accountNum[0] != '0'):
        return True
    else:
        return False

# This function takes the foder holding all the session files and deletes then when done
def cleanup():
    files = glob.glob('transactionSummaryFiles/*')
    for f in files:
      os.remove(f)


if __name__ == "__main__":
    main()

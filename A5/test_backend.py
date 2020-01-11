import tempfile
import os
import io
import sys
import frontend as app
from backend import mergeTSF, transactionListFromFile, masterListFromFile, withdraw_action, createacct_action


#---------------------------------BACKEND CREATE_ACCOUNT TESTS--------------------------------


def test_createacct_test1(master):
    master_dict = master
    transaction = ['NEW', '14567', '100000', '1234567', 'Michael']
    createacct_action(master, transaction)

def test_createacct_test2(master):
    master_dict = master
    transaction = ['NEW', '1567', '100000', '1234567', 'Doug']
    createacct_action(master, transaction)

def test_createacct_test3(master):
    master_dict = master
    transaction = ['NEW', '1311111', '10000', '1311111', 'Micael']
    createacct_action(master, transaction)

def test_createacct_test4(master):
    master_dict = master
    transaction = ['NEW', '1111111', '10000', '1111111', 'Michael']
    createacct_action(master, transaction)

def test_createacct_test5(master):
    master_dict = master
    transaction = ['NEW', '1234567', '10000', '1234567', 'Michael']
    createacct_action(master, transaction)




#---------------------------------BACKEND WITHDRAW TESTS--------------------------------



def test_withdraw_test1(master):
    master_dict = master
    transaction = ['WDR', '234567', '100000', '1234567', 'Michael']
    withdraw_action(master_dict, transaction)

def test_withdraw_test2(master):
    master_dict = master
    transaction = ['WDR', '0234567', '100000', '1234567', 'Michael']
    withdraw_action(master_dict, transaction)

def test_withdraw_test3(master):
    master_dict = master
    transaction = ['WDR', '1234567', '0', '1234567', 'Michael']
    withdraw_action(master_dict, transaction)

def test_withdraw_test4(master):
    master_dict = master
    transaction = ['WDR', '1234567', '10000', '123456', 'Michael']
    withdraw_action(master_dict, transaction)

def test_withdraw_test5(master):
    master_dict = master
    transaction = ['WDR', '1234567', '10000', '0234567', 'Michael']
    withdraw_action(master_dict, transaction)

def test_withdraw_test6(master):
    master_dict = master
    transaction = ['WDR', '1111111', '10000', '1111111', 'Michael']
    withdraw_action(master_dict, transaction)






def main():
    mergeTSF()
    transaction = transactionListFromFile("transactions.txt")
    master = masterListFromFile("master.txt")
    test_withdraw_test1(master)
    test_withdraw_test2(master)
    test_withdraw_test3(master)
    test_withdraw_test4(master)
    test_withdraw_test5(master)
    test_withdraw_test6(master)

    # test_createacct_test1(master)
    # test_createacct_test2(master)
    # test_createacct_test3(master)
    # test_createacct_test4(master)
    # test_createacct_test5(master)
main()

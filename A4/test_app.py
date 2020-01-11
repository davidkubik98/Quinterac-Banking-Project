import tempfile
from importlib import reload
import os
import io
import sys
import frontend as app

path = os.path.dirname(os.path.abspath(__file__))

#-----------------------------------------AGENT TESTS----------------------------------------
#AGENT CREATE_ACCOUNT TESTS

#Successful account creation test
def test_agent_createacct_t1(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'createacct 1234567 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', 'Created account!', 'Account Info:', 'Account Number: 1234567', 'Account Name: Quentin'],
        expected_output_transactions=[
            'createacct'
        ]
    )

#6 digit account number test
def test_agent_createacct_t2(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'createacct 123456 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'createacct'
        ]
    )

#8 digit account number test
def test_agent_createacct_t3(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'createacct 12345678 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'createacct'
        ]
    )
#account number begins with 0 test
def test_agent_createacct_t4(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'createacct 0234567 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'createacct'
        ]
    )

#less than 3 character account name test
def test_agent_createacct_t5(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'createacct 1234567 ab'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'createacct'
        ]
    )

#above 30 character account name test
def test_agent_createacct_t6(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'createacct 1234567 QuentinQuentinQuentinQuentinQuentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'createacct'
        ]
    )

#account name begins with space test
def test_agent_createacct_t7(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'createacct 1234567  Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'createacct'
        ]
    )
#account name ends with space test
def test_agent_createacct_t8(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'createacct 1234567 Quentin '
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'createacct'
        ]
    )

#Invalid transaction test
def test_invalidTransaction_t1(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'createacccct 1234567 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid transaction type!"],
        expected_output_transactions=[
            'createacct'
        ]
    )


#AGENT DELETE_ACCOUNT TESTS


def test_agent_deleteacct_t1(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'deleteacct 1234567 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Deleted account!", "Account Info:", "Account Number:  1234567", 'Account Name: Quentin'],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

def test_agent_deleteacct_t2(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'deleteacct 123456 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

def test_agent_deleteacct_t3(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'deleteacct 12345678 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

def test_agent_deleteacct_t4(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'deleteacct 023456 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

def test_agent_deleteacct_t5(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'deleteacct 123456 Qu'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

def test_agent_deleteacct_t6(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'deleteacct 123456 QuentinQuentinQuentinQuentinQuentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

def test_agent_deleteacct_t7(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'deleteacct 123456  Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

def test_agent_deleteacct_t8(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent', 'deleteacct 123456 Quentin '
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number or Name!"],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

#AGENT DEPOSIT TESTS

def test_agent_deposit_t1(capsys):
    #Invalid Account Number
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'deposit 12312 1000.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number"],
    expected_output_transactions=[
        'deposit'
    ]
    )

def test_agent_deposit_t2(capsys):
    #Deposit amount invalid
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'deposit 1234567 -1000.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Deposit Amount"],
    expected_output_transactions=[
        'deposit'
    ]
    )

def test_agent_deposit_t3(capsys):
    #Deposit amount exceeded
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'deposit 1234567 10000000000.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Deposit Amount"],
    expected_output_transactions=[
        'deposit'
    ]
    )

def test_agent_deposit_t4(capsys):
    #Valid transaction
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'deposit 1234567 1000.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Deposited 1000.00 into account: 1234567"],
    expected_output_transactions=[
        'deposit'
    ]
    )

#AGENT WITHDRAW TESTS

def test_agent_withdraw_t1(capsys):
    #Invalid Account Number
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'withdraw 1234 1.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number"],
    expected_output_transactions=[
        'withdraw'
    ]
    )

def test_agent_withdraw_t2(capsys):
    #Withdraw from agent exceeded
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'withdraw 1234567 1000000.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Withdraw Amount"],
    expected_output_transactions=[
        'withdraw'
    ]
    )

def test_agent_withdraw_t3(capsys):
    #Deposit amount not valid
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'withdraw 1234567 -1000.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Withdraw Amount"],
    expected_output_transactions=[
        'withdraw'
    ]
    )
def test_agent_withdraw_t4(capsys):
    #Valid Transaction
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'withdraw 1234567 10.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Withdrew 10.00 from account: 1234567"],
    expected_output_transactions=[
        'withdraw'
    ]
    )

#AGENT TRANSFER TESTS

def test_agent_transfer_t1(capsys):
    #Account Number 1 Invalid
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'transfer 1234567 0123456 10.00'
    ],
    intput_valid_accounts=[
    '1234567','0123456'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid to Account Number"],
    expected_output_transactions=[
        'transfer'
    ]
    )

def test_agent_transfer_t2(capsys):
    #Account Number 2 Invalid
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'transfer 123456 1234567 10.00'
    ],
    intput_valid_accounts=[
    '1234567','0123456'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid from Account Number"],
    expected_output_transactions=[
        'transfer'
    ]
    )

def test_agent_transfer_t3(capsys):
    #Invalid transfer amount
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'transfer 1234567 1234568 -100000.00'
    ],
    intput_valid_accounts=[
    '1234567','0123456'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid transfer amount"],
    expected_output_transactions=[
        'transfer'
    ]
    )

def test_agent_transfer_t4(capsys):
    #Valid case
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'transfer 1234567 1234568 10.00'
    ],
    intput_valid_accounts=[
    '1234567','0123456'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Transferred 10.00 from 1234567 to 0123456"],
    expected_output_transactions=[
        'transfer'
    ]
    )

#-----------------------------------MACHINE TESTS------------------------------------


#MACHINE CREATE_ACCOUNT TESTS

#Successful account creation test
def test_machine_createacct_t1(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'createacct 1234567 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to create an account!'],
        expected_output_transactions=[
            'createacct'
        ]
    )

#6 digit account number test
def test_machine_createacct_t2(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'createacct 123456 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to create an account!'],
        expected_output_transactions=[
            'createacct'
        ]
    )

#8 digit account number test
def test_machine_createacct_t3(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'createacct 12345678 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to create an account!'],
        expected_output_transactions=[
            'createacct'
        ]
    )
#account number begins with 0 test
def test_machine_createacct_t4(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'createacct 0234567 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to create an account!'],
        expected_output_transactions=[
            'createacct'
        ]
    )

#less than 3 character account name test
def test_machine_createacct_t5(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'createacct 1234567 ab'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to create an account!'],
        expected_output_transactions=[
            'createacct'
        ]
    )

#above 30 character account name test
def test_machine_createacct_t6(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'createacct 1234567 QuentinQuentinQuentinQuentinQuentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to create an account!'],
        expected_output_transactions=[
            'createacct'
        ]
    )

#account name begins with space test
def test_machine_createacct_t7(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'createacct 1234567  Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to create an account!'],
        expected_output_transactions=[
            'createacct'
        ]
    )
#account name ends with space test
def test_machine_createacct_t8(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'createacct 1234567 Quentin '
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to create an account!'],
        expected_output_transactions=[
            'createacct'
        ]
    )


#MACHINE DELETE_ACCOUNT TESTS

def test_machine_deleteacct_t1(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'deleteacct 1234567 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to delete an account!'],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

#6 digit account number test
def test_machine_deleteacct_t2(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'deleteacct 123456 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to delete an account!'],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

#8 digit account number test
def test_machine_deleteacct_t3(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'deleteacct 12345678 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to delete an account!'],
        expected_output_transactions=[
            'deleteacct'
        ]
    )
#account number begins with 0 test
def test_machine_deleteacct_t4(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'deleteacct 0234567 Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to delete an account!'],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

#less than 3 character account name test
def test_machine_deleteacct_t5(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'deleteacct 1234567 ab'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to delete an account!'],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

#above 30 character account name test
def test_machine_deleteacct_t6(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'deleteacct 1234567 QuentinQuentinQuentinQuentinQuentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to delete an account!'],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

#account name begins with space test
def test_machine_deleteacct_t7(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'deleteacct 1234567  Quentin'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to delete an account!'],
        expected_output_transactions=[
            'deleteacct'
        ]
    )
#account name ends with space test
def test_machine_deleteacct_t8(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine', 'deleteacct 1234567 Quentin '
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: machine', 'What transaction are you trying to perform?', 'Must be logged into agent mode to delete an account!'],
        expected_output_transactions=[
            'deleteacct'
        ]
    )

#MACHINE DEPOSIT TESTS


def test_machine_deposit_t1(capsys):
    #Invalid Account Number
    helper(
    capsys=capsys,
    terminal_input = [
        'login machine', 'deposit 12312 1000.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number"],
    expected_output_transactions=[
        'deposit'
    ]
    )

def test_machine_deposit_t2(capsys):
    #Deposit amount invalid
    helper(
    capsys=capsys,
    terminal_input = [
        'login machine', 'deposit 1234567 -1000.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Deposit Amount"],
    expected_output_transactions=[
        'deposit'
    ]
    )

def test_machine_deposit_t3(capsys):
    #Deposit amount exceeded
    helper(
    capsys=capsys,
    terminal_input = [
        'login machine', 'deposit 1234567 10000000000.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Deposit Amount"],
    expected_output_transactions=[
        'deposit'
    ]
    )

def test_machine_deposit_t4(capsys):
    #Valid transaction
    helper(
    capsys=capsys,
    terminal_input = [
        'login machine', 'deposit 1234567 1000.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Deposited 1000.00 into account: 1234567"],
    expected_output_transactions=[
        'deposit'
    ]
    )


#MACHINE WITHDRAW TESTS

def test_machine_withdraw_t1(capsys):
    #Invalid Account Number
    helper(
    capsys=capsys,
    terminal_input = [
        'login machine', 'withdraw 1234 1.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Account Number"],
    expected_output_transactions=[
        'withdraw'
    ]
    )

def test_machine_withdraw_t2(capsys):
    #Withdraw from agent exceeded
    helper(
    capsys=capsys,
    terminal_input = [
        'login machine', 'withdraw 1234567 1000000.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Withdraw Amount"],
    expected_output_transactions=[
        'withdraw'
    ]
    )

def test_machine_withdraw_t3(capsys):
    #Deposit amount not valid
    helper(
    capsys=capsys,
    terminal_input = [
        'login machine', 'withdraw 1234567 -1000.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid Withdraw Amount"],
    expected_output_transactions=[
        'withdraw'
    ]
    )
def test_machine_withdraw_t4(capsys):
    #Valid Transaction
    helper(
    capsys=capsys,
    terminal_input = [
        'login machine', 'withdraw 1234567 10.00'
    ],
    intput_valid_accounts=[
    '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Withdrew 10.00 from account: 1234567"],
    expected_output_transactions=[
        'withdraw'
    ]
    )


#MACHINE TRANSFER TESTS


def test_machine_transfer_t1(capsys):
    #Account Number 1 Invalid
    helper(
    capsys=capsys,
    terminal_input = [
        'login machine', 'transfer 1234567 0123456 10.00'
    ],
    intput_valid_accounts=[
    '1234567','0123456'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid to Account Number"],
    expected_output_transactions=[
        'transfer'
    ]
    )

def test_machine_transfer_t2(capsys):
    #Account Number 2 Invalid
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'transfer 123457 1234567 10.00'
    ],
    intput_valid_accounts=[
    '1234567','0123456'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid from Account Number"],
    expected_output_transactions=[
        'transfer'
    ]
    )

def test_machine_transfer_t3(capsys):
    #Invalid transfer amount
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'transfer 1234567 1234568 100000000000000010.00'
    ],
    intput_valid_accounts=[
    '1234567','0123456'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Invalid transfer amount"],
    expected_output_transactions=[
        'transfer'
    ]
    )

def test_machine_transfer_t4(capsys):
    #Valid case
    helper(
    capsys=capsys,
    terminal_input = [
        'login agent', 'transfer 1234567 0123456 10.00'
    ],
    intput_valid_accounts=[
    '1234567','0123456'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent', 'What transaction are you trying to perform?', "Transferred 10.00 from 1234567 to 0123456"],
    expected_output_transactions=[
        'transfer'
    ]
    )




#--------------------------------------SHARED_METHODS_TESTS-----------------------------------

#LOGIN TESTS

def test_login_t1(capsys):
    #Incorrect format
    helper(
    capsys=capsys,
    terminal_input=[
        'login'
    ],
    intput_valid_accounts=[
        '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Incorrect format! Please try logging in again with the format "login machine"'],
    expected_output_transactions=[
        'error'
        ]
    )

def test_login_t2(capsys):
    #Correct format
    helper(
    capsys=capsys,
    terminal_input=[
        'login agent',
    ],
    intput_valid_accounts=[
        '1234567'
    ],
    expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged in as: agent What transaction are you trying to perform?'],
    expected_output_transactions=[
        'error'
        ]
    )


#LOGOUT TESTS

def test_logout_t1(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'logout'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Incorrect format! Please try logging in again with the format "login machine"'],
        expected_output_transactions=[
            'error'
        ]
    )

def test_logout_t2(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login agent','logout'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged out!'],
        expected_output_transactions=[
            'logout'
        ]
    )

def test_logout_t3(capsys):
        helper(
        capsys=capsys,
        terminal_input=[
            'login machine','logout'
        ],
        intput_valid_accounts=[
            '1234567'
        ],
        expected_tail_of_terminal_output=['Please login with your login type (machine or agent):', 'Logged out!'],
        expected_output_transactions=[
            'logout'
        ]
    )


def helper(
        capsys,
        terminal_input,
        expected_tail_of_terminal_output,
        intput_valid_accounts,
        expected_output_transactions
):
    """Helper function for testing
    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
        terminal_input -- list of string for terminal input
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        intput_valid_accounts -- list of valid accounts in the valid_account_list_file
        expected_output_transactions -- list of expected output transactions
    """

    # cleanup package
    reload(app)

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    transaction_summary_file = temp_file

    # create a temporary file in the system to store the valid accounts:
    temp_fd2, temp_file2 = tempfile.mkstemp()
    valid_account_list_file = temp_file2
    with open(valid_account_list_file, 'w') as wf:
        wf.write('\n'.join(intput_valid_accounts))

    # prepare program parameters
    sys.argv = [
        'frontend.py',
        valid_account_list_file,
        transaction_summary_file]

    # set terminal input
    sys.stdin = io.StringIO(
        '\n'.join(terminal_input))

    # run the program
    app.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # print out the testing information for debugging
    # the following print content will only display if a
    # test case failed:
    print('std.in:', terminal_input)
    print('valid accounts:', intput_valid_accounts)
    print('terminal output:', out_lines)
    print('terminal output (expected tail):', expected_tail_of_terminal_output)

    # compare terminal outputs at the end.`
    for i in range(1, len(expected_tail_of_terminal_output)+1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]

    # compare transactions:
    with open(transaction_summary_file, 'r') as of:
        content = of.read().splitlines()

        # print out the testing information for debugging
        # the following print content will only display if a
        # test case failed:
        print('output transactions:', content)
        print('output transactions (expected):', expected_output_transactions)

        for ind in range(len(content)):
            assert content[ind] == expected_output_transactions[ind]


    # clean up
    os.close(temp_fd)
    os.remove(temp_file)

#agent_createacct_t1()

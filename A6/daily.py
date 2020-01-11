import frontend
import backend
import time


def main(list):
    count = 0
    master_transaction_list = list
    for transaction_list in master_transaction_list:
        count = count + 1
        frontend.frontend(transaction_list, count)
        time.sleep(2)

    backend.mergeTSF()
    backend.actions()


main([["1", "createacct 1234567 Sam", "deposit 1234567 9500000", "withdraw 1234567 1000", "logout"],
      ["1", "createacct 2234567 Josh", "deposit 2234567 9500000",
          "withdraw 2234567 1000", "logout"],
      ["1", "createacct 3234567 James", "deposit 3234567 9050000",
          "withdraw 2234567 10000", "logout"],
      ["2", "deposit 1234567 127474", "transfer 1234567 2234567 300", "withdraw 2234567 10000", "logout"]])

import frontend
import backend
import daily
import time




# To run this file you much uncomment each grouping individually so that the
# program can shut down before you run the next batch otherwise the files are
# not updated correctly

# This program runs a fill week of sessions with each grouping representing a full day
def main():

    # listOfDay = [["1", "createacct 1234567 Sam", "deposit 1234567 9500000", "withdraw 1234567 1000", "logout"],
    #             ["1", "createacct 2234567 Josh", "deposit 2234567 9500000", "withdraw 2234567 1000", "logout"],
    #             ["1", "createacct 3234567 James", "deposit 3234567 9050000", "withdraw 2234567 1000" , "logout"]]
    # daily.main(listOfDay)


    # listOfDay = [["2", "deposit 1234567 15200", "withdraw 1234567 10000", "transfer 1234567 2234567 1000", "logout"],
    #             ["2", "deposit 3234567 100000", "withdraw 3234567 2000", "transfer 3234567 2234567 2000", "logout"]]
    # daily.main(listOfDay)


    # listOfDay = [["1", "createacct 7234567 Phillipss", "deposit 7234567 15200", "transfer 1234567 2234567 1000", "logout"],
    #             ["2", "deposit 2234567 100000", "withdraw 2234567 200", "transfer 2234567 1234567 2000", "logout"]]
    # daily.main(listOfDay)


    listOfDay = [["1", "deleteacct 3234567 James", "withdraw 1234567 10000", "transfer 1234567 2234567 1000", "logout"],
                ["2", "deposit 1234567 100000", "withdraw 1234567 200", "transfer 1234567 2234567 2000", "logout"]]
    daily.main(listOfDay)


    # listOfDay = [["2", "deposit 1234567 15200", "withdraw 1234567 10000", "transfer 1234567 2234567 1000", "logout"],
    #             ["2", "deposit 1234567 100000", "withdraw 1234567 200", "transfer 1234567 2234567 2000", "logout"]]
    # daily.main(listOfDay)


main()

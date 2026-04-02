import random
Sum = 0;
with open('TestingBankOverallBalance.txt', 'r') as file: #Reading a file that holds all Overall Balances
    lines = file.readlines()
    for line in lines: #200 accounts
        Sum += float(line)
file.close() #
print("Total Sum: " + str(Sum))

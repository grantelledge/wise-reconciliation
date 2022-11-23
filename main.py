import csv

# import transactions as a nested list
transactions = []
with open('wise-export.csv') as wiseexport:
    reader = csv.reader(wiseexport)
    for row in reader:
        transactions.append(row)

# remove the header row if it exists
if transactions[0][0] == 'Date':
    transactions.pop(0)

# grab the opening and closing balances
opening_wise_balance = float(transactions[-1][2]) - float(transactions[-1][1])
closing_wise_balance = float(transactions[0][2])
opening_qbo_balance = float(input('Opening QBO balance: '))
closing_qbo_balance = float(input('"Closing" QBO balance: '))

# sum the transactions and append the account type
wise_total = 0
for transaction in transactions:
    wise_total -= float(transaction[1])
    transaction.pop(2)
    if transaction[2] == 'Wise':
        transaction.append('Wise Fee')
    else:
        transaction.append('Contract Labor')

# compute the conversion factor and convert the transactions; sum for rounding error check
conversion_factor = (closing_wise_balance - opening_wise_balance + wise_total) / (closing_qbo_balance - opening_qbo_balance)
rounded_usd_total = 0
for transaction in transactions:
    usd_equivalent = round(float(transaction[1]) / conversion_factor, 2)
    rounded_usd_total -= usd_equivalent
    transaction[1] = str(usd_equivalent)

# compute the journal entry for the rounding error
discrepancy = round(closing_qbo_balance - opening_qbo_balance - (closing_wise_balance - opening_wise_balance)/conversion_factor - rounded_usd_total, 2)

error_tolerance = 0.001
if discrepancy > error_tolerance:
    print('Due to rounding, you need to add a journal entry to reconcile the accounts.')
    print('Credit reconciliation discrepancies $' + str(discrepancy) + ' and debit Wise PhP $' + str(discrepancy) + '.')
elif discrepancy < -error_tolerance:
    print('Due to rounding, you need to add a journal entry to reconcile the accounts.')
    print('Debit reconciliation discrepancies $' + str(-discrepancy) + ' and credit Wise PhP $' + str(-discrepancy) + '.')

# write the transactions to a new csv file
with open('qbo-import.csv', 'w', newline='') as qboimport:
    writer = csv.writer(qboimport)
    writer.writerow(['Date', 'Amount', 'Payee', 'Account'])
    writer.writerows(transactions)

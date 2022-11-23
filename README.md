# Wise PhP Reconciliation Tool
A simple tool to:
1. Import exported transactions in a foreign currency
2. Compute the average conversion rate
3. Prepare importable transactions for QBO in USD
4. Instructions to address rounding errors via journal entry

## Procedure for Use
1. Download the CSV of **fee-separated** transactions for the reconciliation period; add to the folder with name `wise-export.csv`
2. Remove line items for deposits (automatically generated in QBO because are a transfer from another account)
3. Remove all columns except:
- Date (may need to reformat, as Wise CSV uses day-month-year format)
- Amount
- Running Balance
- Payee Name (with step 2, all fields should be filled)
4. Run `main.py` and follow the prompts
5. Note any comments produced by the script
6. Upload the exported CSV to QBO; ensure the date format is correct and the proper columns are selected
7. Accept the transactions in QBO, cross-listing the payees from the exported CSV
8. Add a journal entry in the manner described, if applicable
9. Reconcile the account using the produced final balance (the starting balance should be already on the account; see [here](https://quickbooks.intuit.com/learn-support/en-us/help-article/bank-deposits/enter-opening-balance-account-quickbooks-online/L7NcxTbuu_US_en_US) for more on starting balances)
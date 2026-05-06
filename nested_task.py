transaction_amount = float(input("transaction amount"))
type= input("Enter Account type Standard/Premium")
type= type.lower()
# print(type)
if type=="standard":
    if transaction_amount > 500:
        print("Transaction exceeds the limit for standard accounts")
    else:
        print("Transaction Approved")
elif type == "premium":

    if transaction_amount < 1000:
        print("Transaction Approved")
    else:
        print("Transaction exceeds limit for premium")

else:
    print("wrong account type")

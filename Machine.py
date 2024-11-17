def machine():
    amount_due=50
    accepted_coins=[25,10,5]
    while amount_due>0:
        print("Amount_due is:",amount_due)
            
        coin=int(input("Enter the coin(25,10,5):"))
        if coin in accepted_coins:
           
            amount_due-=coin
        if amount_due<=0:
            break
    change=abs(amount_due)
    if change>0:
        print(f"Change owed is: {change} cents")
    else:
        print("No change is owed.")
machine()

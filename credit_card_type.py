def credit_card_type(income, history):
    ''' (number, str) -> str

    Returns the type of credit card based in the income and history of the
    client.
    '''
    if  (income < 20000):
        card_type = 'N/A'
    elif ((income >= 20000 and income < 30000) and (history == 'Fair' or history == 'fair')):
        card_type = 'Standard'
    elif ((income >= 20000 and income < 30000) and (history == 'Good' or history == 'good')):  
        card_type = 'Bronze'
    elif ((income >= 30000 and income < 40000) and (history == 'Fair' or history == 'fair')):
        card_type = 'Bronze'
    elif ((income >= 20000 and income < 30000) and (history == 'Excellent' or history == 'excellent')):
        card_type = 'Gold'
    elif ((income >= 30000 and income < 40000) and (history == 'Good' or hitory == 'good')):
        card_type = 'Gold'
    elif (income >= 40000 and (history == 'Fair' or history == 'fair')):
        card_type = 'Gold'
    elif ((income >= 30000 and income < 40000) and (history == 'Excellent' or history == 'excellent')):
        card_type = 'Platinum'
    elif (income >= 40000 and (history == 'Good' or history == 'good')):
        card_type = 'Platinum'
    elif (income >= 40000 and (history == 'Excellent' or history == 'excellent')):
        card_type = 'Diamond'
    else:
        card_type = 'N/A'
    return card_type

def credit_card_query():
    income = float(input("Client's income: "))
    credit_history = input("Client's credit history (Fair/Good/Excellent): ")

    card_type = credit_card_type(income, credit_history)
    
    if card_type == "N/A":
        print("That client can't have a credit card, sorry.")
    else:
        print("A client with income of £" + str(income), "and \"" +\
              credit_history + "\" credit history, gets a", card_type,\
              "credit card.")

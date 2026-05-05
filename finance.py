# Finance Application v1

def income(amount):
    return amount * 31 #False 

def expense(amount):
    return -amount

def balance(incomes, expenses):
    return sum(incomes) + sum(expenses)

def savings(income_total, expense_total):
    return income_total - abs(expense_total)
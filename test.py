from datetime import date
def time():
    today = date.today()

    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    print("d1 =", d1)

def thetime():
    today = date.today()
    print(":", today)
    
def date():
    from datetime import date

    today = date.today()

    print("Current date =", today)
    # today = date.today()
    # d2 = today.strftime("%B %d, %Y")
    # print(f"Mam, The date is ", today)

print(date())
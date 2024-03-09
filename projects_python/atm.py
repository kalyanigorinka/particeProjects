username="kalyani"
password="ammu123"
c_name=input("enter your name plz:")
c_password=str(input("enter your password:"))

if c_name==username and c_password==password:
    print('''
    1.deposite
    2.withdraw
    3.ministatement
    4.exit 
     ''')
    amount=4000
    option=int(input("select your option:"))
    if option==1:
        dep=int(input("enter the amount:"))
        amount+=dep
        print("total amount:",amount)
    elif option==2:
        withd=int(input("enter the amount:"))
        amount-=withd
        print("total amount:",amount)
    elif option==3:
        print("**********ATM**************")
        print("username:",username)
        print("total amount:",amount)
        print("thanks for visiting")  
        print("***************************")
    elif option==4:
      exit()
else:
    print("plz enter valid information")



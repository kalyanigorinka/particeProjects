from datetime import datetime 
date = datetime.now()
date1 = date.strftime("%d-%m-%y %H:%M:%S")

name = ">........kalyani super market........<"
print(name.title())
name=input("Enter the customer name:")

#list of items
lists='''
Oil             Rs 100/l
Rice            Rs 45/kg
Salt            Rs 50/kg
Rin             Rs 80/kg
Sugar           Rs 50/kg
Sope            Rs 10/each
Chocolate       Rs 150/each
Ice cream       Rs 200/kg
Drink           Rs 100/l
Colgate         Rs 45/each
Boost           Rs 250/kg
'''

#declaration
price=0
pricelist=[]
totalprice=0
finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items = { 
'oil':100,
'rice':45,
'salt':50,
'rin':80,
'sugar':50,
'sope':10,
'chocolate':150,
'ice cream':200,
'drink':100,
'colgate':45,
'boost':250
}

inp=int(input('list of items press 1:'))
if inp==1:
   print(lists)
for i in range(len(items)):
    inp1=int(input('if you want to buy press 1 or 2 for exit:'))
    if inp1==2:
        break
    if inp1==1:
        item=input('enter your items:')
        quantity=int(input('enter quantity:'))
        if item in items.keys():
           price=quantity*(items[item])
           pricelist.append((item,quantity,items,price))
           totalprice+=price
           ilist.append(item)
           qlist.append(quantity)
           plist.append(price)
           gst=(totalprice*5)/100
           finalamount=gst+totalprice
        else:
            print('sorry you entered item is not available')
    else:
        print('you anter wrong number')

    inp3=input('can i bill the items yes or no:')
    if inp3=="yes":
        pass
        if finalamount!=0:
            print(25*"=","kalyanisupermarket",25*"=")
            print(30*" ","wanaparthy")
            print("name:",name,37*" ","Date:",date1)
            print(75*'-')
            print("sno",8*" ",'items',8*" ","quantity",3*" ",'price')

        for i in range(len(pricelist)):
            print(i,8*" ",5*" ",ilist[i],3*" ",qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ","TotalAmount:",'Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-")
            print(50*' ','finalamount:','Rs',finalamount)
            print(75*"-")
            print(20*' ',"thanks for visiting")    
            print(75*"-")



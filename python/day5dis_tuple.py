
#Python Dictionary Methods
a = {}
print(type(a))

#clear
a = {1:1,2:3,4:3,6:4,9:5}
a.clear()
print(a)

#copy
a = {1:"ammu",2:"deepu"}
a.copy()
print(a)

#get
a = {1:"ammu",2:"deepu"}
print(a.get(2))

#keys
a = {1:"ammu",2:"deepu","ganga":12343}
print(a.keys())

#values
a = {1:"ammu",2:"deepu","ganga":12343}
print(a.values())

#items
a = {1:"ammu",2:"deepu","ganga":12343}
print(a.items())

#pop
a = {1:"ammu",2:"deepu","ganga":12343}
a.pop(2)
print(a)


#update
a = {1:"ammu",2:"deepu","ganga":12343}
a.update({33:"priya"})
print(a)

#nested - dic within  a dic
















#tuple methods

ammu =()
print(type(ammu))
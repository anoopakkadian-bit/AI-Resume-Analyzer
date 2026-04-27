name = input("enter your name:")
print(f"welcome {name}")
password = input ("enter password")
if   password == "1234":
     print("welcome to the app")
else:
     print("wrong password")
 #list ane 
centers =["ulliyeri","balussery","koyilandy","perambra"]
print("welcome to akshaya centeres")
place = input("enter your place to search:").lower().strip()
if place in centers:
     print(f"yes we have an akshaya centre in {place}")
else:
     print(f"sorry no  centre found {place}")
     print ("please check the spelling and try again ")
print ("\n our available locations are:")
for x in centers:
     print(f"- {x}")

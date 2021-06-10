class Items:
    itemname:str
    itemcode:str

    def createItems(self):
        #we will do this portion later
        print("itemcode : " + self.itemcode)
        print("itemname : " + self.itemname)
        print("Item created")

    def checkItemsWithZeroSale(self):
        #will do later todo
        pass

objItems=Items()
objItems.itemname="Sugar"
objItems.itemcode="67890"

#del keyword deletes class object
# del objItems
#del keyword deletes class object property
# del objItems.itemname
# print(objItems.itemname)

objItems.createItems()

#python we have four type of collections (data grouping)
#1. different datatype data grouping
#2. same datatype
#3. different datatype, no duplicate
#four collection types:
#1. Tuple 2. List 3. Set 4. Dictionary

#this is tuple
tupleExample=("Shivani","Neeraj","Deepak","Prabhat")
print(tupleExample)
print(tupleExample[0])
print(tupleExample[1])
shivaniTuple=("Shivani",True,25,True)
neerajTuple=("Neeraj",True,25,False)

print(shivaniTuple[1])
print(neerajTuple[2])

columns=("itemname","itemcode")
print(shivaniTuple[-2])
#len : to get tuple length
print(len(shivaniTuple))


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#looping a tuple
for tupleValue in shivaniTuple:
    print(tupleValue)

#if shivanituple has true in 2 position, print "shivani is attending the class"
if(shivaniTuple[1]==True):
    print("shivani is attending the class")
elif(shivaniTuple[1]==False):
    print("shivani is not attending the class")
else:
    print("I don't know")

if(shivaniTuple[1]==True):
    print("shivani is attending the class")
else:
    print("shivani is not attending the class")
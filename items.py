import mysql.connector as mysql

class Items:
    itemname:str
    itemcode:str
    price:float
    gstrate:float

    dbConn = mysql.connect(
        host="localhost",
        user="root",
        password="mysqltest",
        database="cowin"
    )

    dbCursor = dbConn.cursor()

    def createItems(self):
        #we will do this portion later
        print("itemcode : " + self.itemcode)
        print("itemname : " + self.itemname)
        self.dbCursor.execute("insert into items(itemcode,itemname) values"
                              "('"+self.itemcode+"','"+self.itemname+"')")
        self.dbConn.commit()
        print("Item created")

    def createItemsWithParams(self):
        #we will do this portion later
        print("itemcode : " + self.itemcode)
        print("itemname : " + self.itemname)
        self.dbCursor.execute("insert into items(itemcode,itemname,"
                              "price,gstrate) values(%s,%s,%s,%s)",
                              (self.itemcode,self.itemname,self.price,self.gstrate))
        self.dbConn.commit()
        self.dbConn.close()
        print("Item created")

    def checkItemsWithZeroSale(self):
        #will do later todo
        pass


objItems=Items()
# objItems.itemname="Snickers"
# objItems.itemcode="67878"
#
# objItems.createItems()

objItems.itemname="Cadbury Dairy Milk"
objItems.itemcode="67678"
objItems.price=56
objItems.gstrate=12
objItems.createItemsWithParams()
class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price=price
        self.item_name=item_name
        self.weight=weight
        self.brand=brand
        self.cost=cost
        self.status="for sale"

    def sell(self):
        self.status="sold"
        return self

    def add_tax(self,tax):
        return self.price*(1+tax)  

    def return_item(self, status):
        if status == "defective":
            self.status="defective" 
            self.price=0
        elif status == "like new":
            self.status="for sale"
            self.price*=0.8
        return self
    
    def displayInfo(self):
        print "Price:", self.price
        print "Item Name:", self.item_name
        print "Weight:", str(self.weight) + "lbs"
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        return self
        

item1 = Product(10,"cat toy",5,"Fisher", 5)
item1.displayInfo() 
sale_price = item1.add_tax(0.2)
print "the original price is: $",item1.price,"with sales tax, it's $",sale_price

item1.sell().displayInfo().return_item("like new").displayInfo()
item1.sell().return_item("defective").displayInfo()
class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner=owner

    # adds a product to our list of product objects
    def add_product(self,product):
        self.products.append(product)
        return self

    # remove a product according to a product's name
    def remove_product(self, product_name):
        index = -1
        for i in range(len(self.products)):    
            if (self.products[i]["name"]==product_name):
                index=i    
        if (index>-1):
            del self.products[index]       
        else:
            print "invalid entry"
        return self

    # inventory
    def inventory(self):
        print "INVENTORY"
        for item in self.products:
            print "Name:", item.name
            print "Brand:", item.brand
            print "Price: $", item.price
        return self

"""
products = [ {"name":"Leaf","type":"car","price":2000},{"name":"Accord","type":"bike","price":500} ]

piercey = Store(products,"Sunnyvale, CA","Mr. T")
piercey.inventory()
piercey.add_product({"name":"Tesla","type":"Sedan","price":10000}).inventory()
piercey.remove_product("Accord").inventory()
"""
import store
import product


if __name__ == "__main__":
    item1 = product.Product(10,"cat toy",5,"Fisher", 5)
    item2 = product.Product(20,"leash",2,"doge", 2)
    item2.return_item("like new")
    item2.displayInfo()
    print item1.add_tax(0.18)

    target = store.Store([item1, item2],"Mountain View", "Mr. T")
    target.inventory()

    # adding a product here
    item3 = product.Product(240000,"Car",2500,"Tesla", 100000)
    target.add_product(item3)
    target.inventory()

    # exercise for tomorrow -- if we sell an item from the store, we should have the product "sold" and remove from the store's inventory
    
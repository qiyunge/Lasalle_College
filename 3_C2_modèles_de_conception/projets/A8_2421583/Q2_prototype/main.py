from products import Product, ProductCatalog

def main():
    # Load the product catalog
    ProductCatalog.load_catalog()

    # Retrieve a product from the catalog
    try:
        p1 = ProductCatalog.get_product("p1")
        p2 = ProductCatalog.get_product("p1")
        print(p1)  
        print(p2) 

        print (p1 is p2)

        p1.price = 777.77
        print(p1)
        print(p2)

        print (p1 is p2)

        p3 = ProductCatalog.get_product("p1")
        print(p3)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
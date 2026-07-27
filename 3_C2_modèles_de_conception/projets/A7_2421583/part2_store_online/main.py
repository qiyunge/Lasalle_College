from application.builders import BasicStoreBuilder, AdvancedStoreBuilder
from application import StoreDirector
from domain import StoreOnline

def print_store(store: StoreOnline) -> None:
    print("Layout:", store.layout)
    print("Product Catalog:", store.product_catalog)
    print("Shopping Cart:", store.shopping_cart)
    print("Payment System:", store.payment_system)
    print("*" * 40)

def main() -> None:
    # Create a Basic Store
    basic_store_builder = BasicStoreBuilder()
    store_director = StoreDirector(basic_store_builder)
    basic_store = store_director.construct_store_online()
   
    print("Basic Store:")
    print_store(basic_store)

    # Create an Advanced Store
    advanced_store_builder = AdvancedStoreBuilder()
    store_director.set_builder(advanced_store_builder)
    advanced_store = store_director.construct_store_online()
    print("Advanced Store:")
    print_store(advanced_store)


if __name__ == "__main__":
    main()
from concrete_factories import ConcreteCreatorA, ConcreteCreatorB, ConcreteCreatorC

def main():
    print("___ Factory Method Pattern Demo ___\n")
    creators = [ConcreteCreatorA(), ConcreteCreatorB(), ConcreteCreatorC()]
    # various product sets to test
    product_sets = ["basic", "premium", "standard", "deluxe", "modern", "classic"] 
    
    # Iterate through each creator and product set
    for creator in creators:
        for product_set in product_sets:
            try:
                result = creator.sample_operation(product_set)
                print(result)
                print("-" * 40)
            except ValueError as e:
                # Handle unknown product sets
                print(e)
                print("-" * 40)

if __name__ == "__main__":
    main()
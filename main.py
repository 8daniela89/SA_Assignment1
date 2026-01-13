from document_editor import DocumentFactory
from car_configurator import CarBuilder
from car_management import CarManagementSystem

def demonstrate_solutions():
    print("\n" + "="*50)
    print("DEMONSTRATION OF SOLUTIONS")
    print("="*50)

    # Exercise 1 demo
    print("\n--- 1. Document Editor (Factory Pattern) ---")
    my_doc = DocumentFactory.create_document("pdf")
    print(f"User selected PDF -> {my_doc.display()}")
    print(f"Action -> {my_doc.save('My assignment')}")

    # Exercise 2 demo
    print("\n--- 2. Car Configuration (Builder Pattern) ---")
    print("Building a Sports Car...")
    sports_car = (CarBuilder()
                  .set_engine("V8 Turbo")
                  .set_transmission("Manual")
                  .add_exterior_option("Red Paint")
                  .build())
    print(sports_car)

    # Combined exercises demo
    print("\n--- 3. Combined System (Manager App) ---")
    cms = CarManagementSystem()
    builder = CarBuilder().set_engine("Electric").set_transmission("Auto")
    
    print("Generating an order for an Electric Car in Word format...")
    result = cms.generate_order_document(builder, "word")
    print(f"System Output: {result}")

if __name__ == "__main__":
    demonstrate_solutions()
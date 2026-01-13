class Car:
    """The complex final product."""
    def __init__(self):
        self.engine = None
        self.transmission = None
        self.interior = []
        self.exterior = []
        self.safety = []

    def __str__(self):
        return (f"  [Car Configuration]\n"
                f"    - Engine: {self.engine}\n"
                f"    - Transmission: {self.transmission}\n"
                f"    - Interior: {', '.join(self.interior)}\n"
                f"    - Exterior: {', '.join(self.exterior)}\n"
                f"    - Safety: {', '.join(self.safety)}")

class CarBuilder:
    """The builder that constructs the car step-by-step."""
    def __init__(self):
        self.car = Car()

    def set_engine(self, engine_type):
        self.car.engine = engine_type
        return self

    def set_transmission(self, transmission):
        self.car.transmission = transmission
        return self

    def add_interior_feature(self, feature):
        self.car.interior.append(feature)
        return self

    def add_exterior_option(self, option):
        self.car.exterior.append(option)
        return self

    def add_safety_feature(self, feature):
        self.car.safety.append(feature)
        return self

    def build(self):
        if not self.car.engine or not self.car.transmission:
            raise ValueError("Error: Engine and transmission are mandatory!")
        return self.car
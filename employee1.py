class employee:
    def __init__(self,name,age,designation):
        self.name=name
        self.age=age
        self.designation=designation

    def display_info(self):
        print(f"name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Designaton: {self.designation}")
from abc import ABC, abstractmethod

class Recipe(ABC):
    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    @abstractmethod
    def get_type(self):
        pass

    def display(self):
        print(f"\n📌 Nama Resep: {self.name}")
        print("🍽️ Tipe:", self.get_type())
        print("\n🧂 Bahan:")
        for item in self.ingredients:
            print(f"- {item.strip()}")
        print("\n👨‍🍳 Langkah-langkah:")
        for i, step in enumerate(self.steps, 1):
            print(f"{i}. {step.strip()}")
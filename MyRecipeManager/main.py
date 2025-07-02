import json
from models.dessert import Dessert
from models.savory import Savory

def save_recipes(recipes, filename='data/recipes.json'):
    data = []
    for r in recipes:
        data.append({
            "type": r.get_type(),
            "name": r.name,
            "ingredients": r.ingredients,
            "steps": r.steps
        })
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_recipes(filename='data/recipes.json'):
    recipes = []
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            for r in data:
                if r['type'] == 'Dessert':
                    recipes.append(Dessert(r['name'], r['ingredients'], r['steps']))
                else:
                    recipes.append(Savory(r['name'], r['ingredients'], r['steps']))
    except FileNotFoundError:
        pass
    return recipes

def main():
    recipes = load_recipes()
    while True:
        print("\n== MyRecipeManager ==")
        print("1. Tambah Resep")
        print("2. Lihat Semua Resep")
        print("3. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            name = input("Nama resep: ")
            tipe = input("Tipe (dessert/savory): ").lower()
            ingredients = input("Bahan (pisahkan dengan koma): ").split(',')
            steps = input("Langkah-langkah (pisahkan dengan | ): ").split('|')

            if tipe == 'dessert':
                recipe = Dessert(name, ingredients, steps)
            else:
                recipe = Savory(name, ingredients, steps)

            recipes.append(recipe)
            save_recipes(recipes)
            print("✅ Resep berhasil ditambahkan!")

        elif choice == '2':
            for r in recipes:
                r.display()

        elif choice == '3':
            print("👋 Sampai jumpa!")
            break
        else:
            print("⚠️ Pilihan tidak valid.")

if __name__ == "__main__":
    main()

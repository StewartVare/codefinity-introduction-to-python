vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
if "carrots" not in vegetables:
    vegetables.append("carrots")
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
vegetables.sort()
print("Updated Vegetable Inventory:"), vegetables


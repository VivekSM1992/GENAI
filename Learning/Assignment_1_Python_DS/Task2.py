"""
From your products list, create a set of categories called categories_set. (If product names do not contain categories, create a short parallel list categories = [...] with matching length and use that.)
Demonstrate adding a new category to the set and show that duplicates are ignored.
Show how to check whether a category exists in the set (print a boolean result).
Extra (optional): Show how to get the total number of unique categories using a set.
"""

products=["Chips","Pen","Pencil","Milk","Wheat Floor","Tshirt","Socks"]
categories=set(["Food","Education","Education","Food","Food","Clothing","Footware"])
print(categories)
print("Food" in categories)
print(len(categories))
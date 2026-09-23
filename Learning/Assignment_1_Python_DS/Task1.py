"""
Create a list named products containing at least 6 product names (strings).
Create a tuple named sample_product that stores (product_name, price, category) for one product.
Print the 2nd and last product from the products list.
Append two new product names to products and then print the updated list.
Extra (optional): Convert sample_product into a list, change its price, and convert it back to a tuple.

"""
products=["Chips","Pen","Pencil","Milk","Wheat Floor","Tshirt","Socks"]
sample_product=("Chips",10.00,"Food")
print(products[1],"\n",products[len(products)-1])
products.append("Tie")
products.append("Shoes")
print(products)
sample_product=list(sample_product)
sample_product[1]=12.00
sample_product=tuple(sample_product)
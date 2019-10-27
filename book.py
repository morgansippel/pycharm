book_price = 24.95
print(book_price, " retail price per book")
discount = book_price * 40 / 100
new_price = book_price - discount
shipping = 3 + (.75 * 59)
total_cost = (new_price * 60) + shipping
print("%.2f"%new_price, " book store price.")
print("%.2f"%total_cost, " total amount per 60 copies and shipping")


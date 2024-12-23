# Determine amount of paint available in litres
paint = int(input())

# Determine amount of bottlecaps available
bottlecaps = int(input())

# Determine price point of each badge
dollars = int(input())

# Calculate total revenue
# (P // B) -> calculate amount of badges made from the paint 
# (P // B) * D -> calculate amount of money made from badges
# + P % B -> Calculate total amount of money made from badges plus the sale of leftover paint (remainder of the modulo operator)
total = (paint // bottlecaps) * dollars + paint % bottlecaps

print(total)

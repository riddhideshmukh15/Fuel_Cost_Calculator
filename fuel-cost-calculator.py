
print("==== FUEL COST CALCULATOR ====")

distance = float(input("Enter distance (km): "))
mileage = float(input("Enter vehicle mileage (km/litre): "))
fuel_price = float(input("Enter the fuel price per litre: ₹"))

fuel_needed = distance / mileage
total_cost = fuel_needed * fuel_price

print("\n===== FUEL SUMMARY =====")
print("Distance:", distance, "km")
print("Mileage:", mileage, "km/litre")
print("Fuel needed:", round(fuel_needed, 2), "litres")
print("Fuel price per litre: ₹", fuel_price)
print("Total Fuel Cost: ₹", round(total_cost, 2))
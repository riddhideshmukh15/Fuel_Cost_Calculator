print("====FUEL COST CALCULATOR====")
distance=float(input("Enter distance(km):"))
mileage=float(input("Enter vehicle mileage(km/1):"))
fuel_price=float(input("Enter the fuel price per litre:"))
fuel_needed=distance/mileage
total_cost=fuel_needed*fuel_price
print("\nFuel needed:",round(fuel_needed,2),"liters")
print("Total Fuel Cost:",round(total_cost,2))
# Birthday Celebration Budget PLanner

budget = 10000.0

print("Birthday Celebration Budget PLanner")

total_cost = 0.0

def get_cost_input(prompt):
    while True:
        try:
            value = float(input(prompt + ": ₱"))
            if value < 0:
                print("Please enter a non-negative amount: ")
            else:
                return value 
        except ValueError:
            print("Invalid input. PLease enter a valid number.")

venue_cost = get_cost_input("Enter estimated cost for Venue: ")
total_cost += venue_cost

catering_cost = get_cost_input("Enter estimated cost Catering: ")
total_cost += catering_cost

decorations_cost = get_cost_input("Enter estimated cost Decorations: ")
total_cost += decorations_cost

entertainment_cost = get_cost_input("Enter estimated cost Entertainment: ")
total_cost += entertainment_cost

miscellaneous_cost = get_cost_input("Enter estimated cost Miscellaneous items: ")
total_cost += miscellaneous_cost

print("\n=== Summary ===")
print(f"Total Estimated Cost: ₱{total_cost:,.2f}")
print(f"Predefined Budget: ₱{budget:,.2f}")

if total_cost <= budget:
    print("Status: The estimated cost is **within** the budget.")
else:
    print("Status: The estimated cost is **exceeds** the budget.")
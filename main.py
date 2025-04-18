# Travel Time Calculator

start_location = input("Enter the starting location: ")
destination = input("Enter the destination: ")
mode_of_transport = input("Enter mode of transport (e.g., car, bus, train): ")

distance_km = float(input("Enter the distance in kilometers: "))
speed_kph = float(input("Enter the speed in km/h: "))

travel_time = distance_km / speed_kph

needs_rest = travel_time > 5

print("\n--- Travel Summary ---")
print(f"From: {start_location}")
print(f"To: {destination}")
print(f"Mode of Transport: {mode_of_transport}")
print(f"Distance: {distance_km} km")
print(f"Speed: {speed_kph} km/h")
print(f"Estimated Travel Time: {travel_time:.2f} hours")

if needs_rest:
    print("⚠️  Warning: Travel time exceeds 5 hours. A rest stop is recommended.")
else:
    print("✅ Travel time is within safe limits. No rest stop necessary.")

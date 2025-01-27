# Define weight variable
weight = 41.5

# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print("The cost of Ground Shipping is $", cost_ground)

# Ground Shipping Premium
cost_ground_premium = 125.00

print("The cost of Ground Shipping Premium is $", cost_ground_premium)

# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print("The cost of Drone Shipping is $", cost_drone)
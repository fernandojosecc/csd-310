"""
Title: tables.py
Author: Green Team - Fernando Contreras, Maddison Montijo, Oscar Avina, Jordyn Rylander, Desarai Lofton
Date: May 10, 2026
"""


# -- Customer Table --
print("\n--- Customer Table ---")
customers = [
    (1, "John", "Smith", "john@email.com", "1234567890"),
    (2, "Maria", "Lopez", "maria@email.com", "1234567891"),
    (3, "David", "Johnson", "david@email.com", "1234567892"),
    (4, "Sarah", "Williams", "sarah@email.com", "1234567893"),
    (5, "James", "Brown", "james@email.com", "1234567894"),
    (6, "Linda", "Davis", "linda@email.com", "1234567895")
]

# print header
print("{:<15} {:<12} {:<12} {:<25} {:<15}".format(
    "customer_id", "first_name", "last_name", "email", "phone"))
print("-" * 75)

# iterate over each customer and display their details
for c in customers:
    print("{:<15} {:<12} {:<12} {:<25} {:<15}".format(c[0], c[1], c[2], c[3], c[4]))


# -- Employee Table --
print("\n--- Employee Table ---")
employees = [
    (1, "Jake", "Willson", "jake@email.com", 1),
    (2, "Ned", "Willson", "ned@email.com", 1),
    (3, "Phoenix", "TwoStar", "phoenix@email.com", 3),
    (4, "June", "Santos", "june@email.com", 4),
    (5, "Mads", "Mackenzie", "mads@email.com", 2),
    (6, "Juan", "Snow", "juan@email.com", 5)
]

# print header
print("{:<15} {:<12} {:<12} {:<25} {:<10}".format(
    "employee_id", "first_name", "last_name", "email", "role_id"))
print("-" * 75)

# iterate over each employee and display their details
for e in employees:
    print("{:<15} {:<12} {:<12} {:<25} {:<10}".format(e[0], e[1], e[2], e[3], e[4]))


# -- Employee Role Table --
print("\n--- Employee Role Table ---")
employee_roles = [
    (1, "Guide"),
    (2, "Marketing"),
    (3, "Inventory"),
    (4, "Admin"),
    (5, "Software Developer")
]

# print header
print("{:<10} {:<20}".format("role_id", "role_name"))
print("-" * 30)

# iterate over each role and display details
for r in employee_roles:
    print("{:<10} {:<20}".format(r[0], r[1]))


# -- Trip Table --
print("\n--- Trip Table ---")
trips = [
    (1, "Safari Adventure", "2026-06-01", "Africa", "Africa", 1),
    (2, "Mountain Trek", "2026-07-10", "Asia", "Asia", 2),
    (3, "Beach Escape", "2026-08-15", "Southern Europe", "Southern Europe", 1),
    (4, "Desert Tour", "2026-09-01", "Africa", "Africa", 2),
    (5, "Forest Hike", "2026-10-05", "Asia", "Asia", 1),
    (6, "Island Trip", "2026-11-20", "Southern Europe", "Southern Europe", 2)
]

# print header
print("{:<10} {:<20} {:<14} {:<18} {:<18} {:<10}".format(
    "trip_id", "trip_name", "trip_date", "location", "region", "guide_id"))
print("-" * 90)

# iterate over each trip and display details
for t in trips:
    print("{:<10} {:<20} {:<14} {:<18} {:<18} {:<10}".format(
        t[0], t[1], t[2], t[3], t[4], t[5]))


# -- Booking Table --
print("\n--- Booking Table ---")
bookings = [
    (1, 1, 1, "2026-05-01", "Confirmed"),
    (2, 2, 2, "2026-05-02", "Confirmed"),
    (3, 3, 3, "2026-05-03", "Pending"),
    (4, 4, 4, "2026-05-04", "Confirmed"),
    (5, 5, 5, "2026-05-05", "Cancelled"),
    (6, 6, 6, "2026-05-06", "Confirmed")
]

# print header
print("{:<12} {:<14} {:<10} {:<14} {:<12}".format(
    "booking_id", "customer_id", "trip_id", "booking_date", "status"))
print("-" * 65)

# iterate over each booking and display details
for b in bookings:
    print("{:<12} {:<14} {:<10} {:<14} {:<12}".format(
        b[0], b[1], b[2], b[3], b[4]))


# -- Equipment Table --
print("\n--- Equipment Table ---")
equipment = [
    (1, "Tent", "2020-01-01", "Good", "Available", True),
    (2, "Backpack", "2021-03-15", "Good", "Available", False),
    (3, "Sleeping Bag", "2019-07-10", "Fair", "In Use", True),
    (4, "Boots", "2022-05-20", "Excellent", "Available", False),
    (5, "Jacket", "2018-11-30", "Poor", "Repair", True),
    (6, "Helmet", "2023-02-10", "Excellent", "Available", False)
]

# print header
print("{:<14} {:<16} {:<14} {:<12} {:<12} {:<18}".format(
    "equipment_id", "equipment_name", "purchase_date", "condition", "status", "needs_inspection"))
print("-" * 90)

# iterate over each equipment item and display details
for e in equipment:
    print("{:<14} {:<16} {:<14} {:<12} {:<12} {:<18}".format(
        e[0], e[1], e[2], e[3], e[4], str(e[5])))


# -- Equipment Purchase Table --
print("\n--- Equipment Purchase Table ---")
purchases = [
    (1, 1, 1, "Buy", "2026-04-01"),
    (2, 2, 2, "Rent", "2026-04-02"),
    (3, 3, 3, "Buy", "2026-04-03"),
    (4, 4, 4, "Rent", "2026-04-04"),
    (5, 5, 5, "Buy", "2026-04-05"),
    (6, 6, 6, "Rent", "2026-04-06")
]

# print header
print("{:<12} {:<14} {:<14} {:<18} {:<16}".format(
    "purchase_id", "customer_id", "equipment_id", "transaction_type", "transaction_date"))
print("-" * 75)

# iterate over each purchase and display details
for p in purchases:
    print("{:<12} {:<14} {:<14} {:<18} {:<16}".format(
        p[0], p[1], p[2], p[3], p[4]))

print("\n")
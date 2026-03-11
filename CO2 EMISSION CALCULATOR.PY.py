git add .from tkinter import *
from tkinter import ttk

# --- Emission Factors (grams CO₂ per km) ---

LAND_VEHICLES = {
    "Small Car": 192,
    "Medium Car": 210,
    "SUV / Large Car": 255,
    "Electric Car": 50,
    "Motorcycle": 103,
    "Bus": 27,  # per passenger
    "Truck": 300,
    "Van": 220,
    "Bicycle": 0
}

AIR_VEHICLES = {
    "Airplane (Short Haul)": 255,  # per passenger
    "Airplane (Long Haul)": 195,
    "Helicopter": 350
}

WATER_VEHICLES = {
    "Ferry": 120,  # per passenger
    "Cargo Ship": 10,  # per ton of goods
    "Speed Boat": 250
}

RAIL_VEHICLES = {
    "Passenger Train": 41,  # per passenger
    "Freight Train": 22  # per ton of goods
}

# --- Functionality ---

def update_vehicle_options(event=None):
    """Update vehicle dropdown based on selected category"""
    category = category_box.get()

    if category == "Land":
        vehicle_box["values"] = list(LAND_VEHICLES.keys())
    elif category == "Air":
        vehicle_box["values"] = list(AIR_VEHICLES.keys())
    elif category == "Water":
        vehicle_box["values"] = list(WATER_VEHICLES.keys())
    elif category == "Rail":
        vehicle_box["values"] = list(RAIL_VEHICLES.keys())

    vehicle_box.set("")


def calculate():
    category = category_box.get()
    vehicle = vehicle_box.get()
    distance = distance_entry.get()
    passengers = passengers_entry.get()

    try:
        distance = float(distance)
        passengers = int(passengers) if passengers else 1

        if category == "" or vehicle == "":
            result_label.config(text="Please select category and vehicle.")
            return

        # Pick correct emission factor dictionary
        if category == "Land":
            factor = LAND_VEHICLES[vehicle]
        elif category == "Air":
            factor = AIR_VEHICLES[vehicle]
        elif category == "Water":
            factor = WATER_VEHICLES[vehicle]
        else:
            factor = RAIL_VEHICLES[vehicle]

        # Calculate total CO₂
        if vehicle in [
            "Bus",
            "Airplane (Short Haul)",
            "Airplane (Long Haul)",
            "Ferry",
            "Passenger Train",
        ]:
            total = factor * distance * passengers
        else:
            total = factor * distance

        # Display result
        if factor == 0:
            result_label.config(text="Zero CO₂ — Great choice!")
        else:
            result_label.config(text=f"Estimated CO₂ Emission:\n{total:.2f} grams")

    except ValueError:
        result_label.config(text="Enter valid numeric values.")


# --- GUI Setup ---

root = Tk()
root.title("CO₂ Emission Calculator (Land, Air, Water, Rail)")
root.geometry("420x420")

Label(root, text="CO₂ Emission Calculator", font=("Arial", 15, "bold")).pack(pady=10)

Label(root, text="Select Transport Category:").pack()
category_box = ttk.Combobox(root, values=["Land", "Air", "Water", "Rail"])
category_box.pack(pady=5)
category_box.bind("<<ComboboxSelected>>", update_vehicle_options)

Label(root, text="Select Vehicle Type:").pack()
vehicle_box = ttk.Combobox(root)
vehicle_box.pack(pady=5)

Label(root, text="Enter Distance (in km):").pack()
distance_entry = Entry(root)
distance_entry.pack(pady=5)

Label(root, text="Passengers / Units (optional):").pack()
passengers_entry = Entry(root)
passengers_entry.pack(pady=5)

Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
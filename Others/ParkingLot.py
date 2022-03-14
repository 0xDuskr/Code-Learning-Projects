def user_input():
    possible_vehicles = ['motorcycle', 'car', 'truck']

    vehicle = input("\n> Vehicle type (motorcycle | car | truck): ").lower()
    if vehicle not in possible_vehicles:
        print("\n [!] Vehicle not identified!")
        quit()

    covered_parking = input("\n> Covered parking lot (y/n)? ").lower()
    if "y" != covered_parking != "n":
        print("\n [!] Answer not identified!")
        quit()
    elif covered_parking == "y":
        covered_parking = 1.5
    else:
        covered_parking = 1

    time = input("\n> Calculate by hours or days? ").lower()
    if "hours" != time != "days":
        print("\n [!] Answer not identified!")
        quit()

    amount = int(input(f"\n> How many {time}? "))

    profiles(vehicle,covered_parking,time,amount)

def profiles(vehicle,covered_parking,time,amount):
    if vehicle == "motorcycle":
        if time == "hours":
            profile = 1.8
        else:
            profile = 15
    elif vehicle == "car":
        if time == "hours":
            profile = 5
        else:
            profile = 25
    else:
        if time == "hours":
            profile = 8
        else:
            profile = 40
    output(profile,covered_parking,amount)

def output(profile,amount,covered_parking):
    total_costs = (profile * amount) * covered_parking

    print("\n[$] Total cost: $%.2f" % total_costs)

user_input()
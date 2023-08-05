MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
# TODO: 1 print report
def available_resources(used_water, used_milk, used_coffee):
    water = resources["water"] - used_water
    milk = resources["milk"] - used_milk
    coffee = resources["coffee"] - used_coffee
    return [water, milk, coffee]
def cost_drink(drink):
    if drink == "espresso":
        bill = MENU["espresso"]["cost"]
    elif drink == "latte":
        bill = MENU["latte"]["cost"]
    elif drink == "cappuccino":
        bill = MENU["cappuccino"]["cost"]
    return bill
def money_payed(npenny, ndime, nnickel, nquarter):
    penny = 0.01 * npenny
    dime = 0.10 * ndime
    nickel = 0.05 * nnickel
    quarter = 0.25 * nquarter
    return penny + dime + nickel + quarter

def make_brevrage(drink):
    if drink == "espresso":
        water = MENU["espresso"]["ingredients"]["water"]
        milk = 0
        coffee = MENU["espresso"]["ingredients"]["coffee"]
    elif drink ==  "latte":
        water = MENU["latte"]["ingredients"]["water"]
        milk = MENU["latte"]["ingredients"]["milk"]
        coffee = MENU["latte"]["ingredients"]["coffee"]
    elif drink == "cappuccino":
        water = MENU["cappuccino"]["ingredients"]["water"]
        milk = MENU["cappuccino"]["ingredients"]["milk"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    return [water, milk, coffee]



x = True
while x:
    used_water = 0
    used_milk = 0
    used_coffee = 0
    while True:
        resource = available_resources(used_water, used_milk, used_coffee)
        drink = input("what would you like to drink? (espresso, latte, cappuccino) ")
        to_pay = cost_drink(drink)
        print(f"you are to pay {to_pay} in coins")
        n_penny = int(input("how many penny? "))
        n_dime = int(input("how many dime? "))
        n_nickel = int(input("how many nickel? "))
        n_quarter = int(input("how many quarter? "))
        payed =  money_payed(n_penny, n_dime, n_nickel, n_quarter)
        make_drink = make_brevrage(drink)
        if resource[0] >= make_drink[0] and resource[1] >= make_drink[1] and resource[2] >= make_drink[2]:
            if payed >= to_pay:
                used_water += make_drink[0]
                used_milk += make_drink[1]
                used_coffee += make_drink[2]
                made_drink = make_drink[0] + make_drink[1] + make_drink[2]
                change = payed - to_pay
                print(f"your {drink} is ready, you have ${change} as change")
            else:
                print("insufficient funds")
        else:
            print("unavailable resources")

# TODO: 2 check resource sufficiency
# TODO: 3 process coin
# TODO: 4 check transaction succesfull
# TODO: 5 make coffee
travel_log = [
    {
        "country" : "France",
        "visits" : 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "visits" : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgard"]
    }
]



def add_new_country(country_new,visits_new,cities_new):
    new_countries = {}

    new_countries["country"] = country_new
    new_countries["visits"] = visits_new
    new_countries["cities"] = cities_new
    travel_log.append(new_countries)



add_new_country("Russia", 2, ["Moscow","Saint=Petersburg"])



print(travel_log)



if choice == "yes":
    clear()
    add_bids = {}
    name = input("What is your name? ")
    bid = int(input("What is your bid?: $"))
    choice = input("Are there any other bidders? Type 'yes' or 'no'.")
    add_bids["name"] = name
    add_bids["bids"] = bid
    bids_dic.append(add_bids)

elif choice == 'no':
    clear()
  
    bids_dic["bids"] = bid
  
    print("The Winner is James with a bid of $131")

print(bids_dic)

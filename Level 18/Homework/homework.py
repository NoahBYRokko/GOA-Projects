# Task1.
print("__________________Task1__________________")


person = {
    "name": "Bachi",
    "surname": "Nuskhelidze",
    "city": "Gori",
    "age": "14"
}

x = f"{person["name"]} is {person["age"]} yours old and lives in {person["city"]}."
print(x)

# Task2.
print("__________________Task2__________________")


school_subjects = {
    "english": 10,
    "Mathematics": 10,
    "History": 8,
    "Geography": 7
}

x = sum(school_subjects.values()) / len(school_subjects)
print("average:", x)

# Task3.
print("__________________Task3__________________")


fav_anime = {
    "name": "Jojo's Biazarre Adventure",
    "anime release date": 2013,
    "manga release date": 1986,
    "creator": "Hirohiko Araki"
}

x = f"My favourite anime {fav_anime["name"]} was written in {fav_anime["manga release date"]} by {fav_anime["creator"]} and later anime was published in {fav_anime["anime release date"]}."
print(x)

# Task4.
print("__________________Task4__________________")


products = {
    "Can of Coke": "2$",
    "Bag of Doritos": "8$",
    "Ice Cream": "1.5$",
    "Red Bull Energy Drink": "3$",
    "Oreo Cookies": "4.5$" 
}
print(products)
keys = (input("Would you like to purchess any item from this list? "))
new_products = {

}

x = new_products[keys]
print("Items in your Bucket:", x)






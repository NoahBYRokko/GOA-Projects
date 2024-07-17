# Task1.
print("__________________Task1__________________")

car = {
    "mark": "Honda",
    "name": "Civic",
    "year": "2015",
    "engine": "1.8L i-VTEC 4-cylinder",
}
print(car)


# Task2.
print("__________________Task2__________________")

person = {
    "name": "Bachi",
    "age": 14,

}
person["surname"] = "Nuskhelidze"

person.update({"Email": "a1f98a0a1f@gmail.com"})
print(person)


# Task3.
print("__________________Task3__________________")

for i in person:
    print(person[i])


# Task4.
print("__________________Task4__________________")

dict = {}
values = 0

for i in range(1000):
    keys = f"item_{i+1}"
    values += 1
    dict[keys] = values

print(dict)
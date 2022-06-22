customers = [
    {
        "name": "William Wills",
        "Account_number": "003",
        "age": 24,
        "Balance": 10_000,
        "type": "savings",
        "gender": "female",
        "is_married": True

    },
    {
        "name": "William Wine",
        "Account_number": "005",
        "age": 24,
        "Balance": 19_000,
        "type": "savings",
        "gender": "Male",
        "is_married": False

    },
    {

        "name": "Idiot Olamide",
        "Account_number": "065",
        "age": 58,
        "Balance": 25_000,
        "type": "Currents",
        "gender": "Male",
        "is_married": False

    },
    {

        "name": "Asake Boyo",
        "Account_number": "009",
        "age": 48,
        "Balance": 200_000,
        "type": "Currents",
        "gender": "Male",
        "is_married": True

    },
    {

        "name": "Charles Odogwu",
        "Account_number": "070",
        "age": 68,
        "Balance": 200_000_000,
        "type": "savings",
        "gender": "Male",
        "is_married": True

    }

]

names = [d["name"] for d in customers]
age = [d["age"] for d in customers]
print(names)
print(age)

married = [d["is_married"] for d in customers]
print(married)

gender = [d["gender"] for d in customers]
print(gender)

average = sum(customer["age"] for customer in customers) / len(customers)
savings_account = [dict(name=customers["name"], balance=customers["Balance"]) for customers in customers if
                   customers["type"] == "savings"]

# print(average)
print(savings_account)


def get_balance(dict_: dict) -> int:
    return dict_["Balance"]


customers.sort(key=get_balance, reverse=True)

print(sorted(customers, key=get_balance, reverse=True))

print(max(customers, key=get_balance))

print(customers)

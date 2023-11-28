my_user_data_dict = {
    'user1': {
        'name': 'Kevin Losem',
        'alter': 28,
        'info': 'Ich habe Angst vor Spinnen!',
    },
    'user2': {
        'name': 'Alexandra Seidel',
        'alter': 53,
        'info': 'Putzfimmel!',
    },
    'user3': {
        'name': 'Marc Losem',
        'alter': 31,
        'info': 'Gebe Geld aus ohne meine Frau zu informieren!',
    },
}

# Ausgabe Dictionary
print("Hier ist das Dict:")
for user, data in my_user_data_dict.items():
    print(f"{user}:\n Name - {data['name']}\n Alter - {data['alter']}\n Info - {data['info']}\n")


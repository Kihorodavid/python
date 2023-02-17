# car = {
#     "model" : "ford",
#     "year" :1998,
#     "color" : "red",
#     "country":"Kenya"
# }

# # Accessing dictionary items
# print(car["color"])

# person = {
#     "name" : "Cathy",
#     "pets" : ["dog", "cats" , "salamander" , "bats"]
# }
# print(person["pets"][1])
# profile = {}
# profile ["username"] = "user123"
# profile["age"]=20
# profile["email"]="user123@gmail.com"
# print(profile)

profile = {}
def register():
    # ask for username
    username =input("Enter username :")
    # ask for email
    email= input("Enter email :")
    # ask for password
    password =input("Emter password :")
    # store in dictionary
    profile["username"] = username 
    profile["email"] = email
    profile["password"] = password


def get_profile():
    print(profile)

def change_username():
    new_name = input("Enter new username :")
    profile["username"] = new_name

register()
get_profile()

change_username()
get_profile()
def generate_profile (age):
    if (age > 0 and age <=12):
        return "Child"
    elif (age >= 13 and age <= 19):
        return "Teenager"
    elif (age >= 20):
        return "Adult"
    else:
        return "Please, enter correct age"

user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = []

while True :
    hobby = input("Enter a favorite hobby hobby or type 'stop' to finish: ")
    if hobby == 'stop':
        break
    hobbies.append(hobby)

life_stage = generate_profile(current_age)
user_profile = {"Name": user_name, "Age": current_age, "Life Stage" : life_stage, "Favorite Hobbies" : hobbies}


print("\n --- ")
print("Profile Summary: ")

for key, value in user_profile.items():
    if key != "Favorite Hobbies":
     print(f"{key}: {value}")

if hobbies == []:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(hobbies)}): ")
    for hobby in hobbies:
        print(f"- {hobby}")

print(" --- ")





import random

subject = ["SRK", "Salman Khan", "Aamir Khan", "Kareena Kapoor", "Deepika Padukone"]
actions = ["spotted", "seen", "caught", "filmed", "photographed"]
places = ["in Mumbai", "at the airport", "in a restaurant", "at a party", "on the streets"]

def generate_fake_news():
    sub_choice = random.choice(subject)
    act_choice = random.choice(actions)
    place_choice = random.choice(places)
    return f"BREAKING NEWS : {sub_choice} was {act_choice} {place_choice}."

while True:
    print("\n" + generate_fake_news())

    user_choice = input("Wanna generate fake news ? (yes/no)").lower()

    if user_choice == "no":
        break

print("Thank you for using the Fake News Generator!")
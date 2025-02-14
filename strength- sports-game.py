import random

class Hero:
    def __init__(self, name, strength, agility, endurance):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.endurance = endurance
        self.health = 100

    def perform_challenge(self, challenge):
        result = 0
        if challenge == "weightlifting":
            result = self.strength * random.uniform(0.8, 1.2)
        elif challenge == "climbing":
            result = self.agility * random.uniform(0.8, 1.2)
        elif challenge == "tug_of_war":
            result = self.endurance * random.uniform(0.8, 1.2)
        return result

    def lose_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

def choose_hero():
    heroes = [
        Hero("Titan", 10, 5, 7),
        Hero("Nimble", 5, 10, 7),
        Hero("Stalwart", 7, 5, 10)
    ]
    print("Choose your hero:")
    for i, hero in enumerate(heroes):
        print(f"{i + 1}. {hero.name} (Str: {hero.strength}, Agi: {hero.agility}, End: {hero.endurance})")
    choice = int(input("Enter the number of your choice: ")) - 1
    return heroes[choice]

def main():
    player_hero = choose_hero()
    computer_hero = random.choice([
        Hero("Titan", 10, 5, 7),
        Hero("Nimble", 5, 10, 7),
        Hero("Stalwart", 7, 5, 10)
    ])

    challenges = ["weightlifting", "climbing", "tug_of_war"]

    while player_hero.health > 0 and computer_hero.health > 0:
        challenge = random.choice(challenges)
        print(f"Challenge: {challenge}")
        player_result = player_hero.perform_challenge(challenge)
        computer_result = computer_hero.perform_challenge(challenge)

        print(f"You scored {player_result:.2f}, Computer scored {computer_result:.2f}")

        if player_result > computer_result:
            computer_hero.lose_health(10)
            print(f"Computer loses health! Remaining health: {computer_hero.health}")
        else:
            player_hero.lose_health(10)
            print(f"You lose health! Remaining health: {player_hero.health}")

    if player_hero.health > 0:
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    main()
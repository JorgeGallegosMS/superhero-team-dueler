import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        random_value = random.randint(0, self.max_block)
        return random_value

class Weapon(Ability):
    def attack(self):
        half_max_damage= self.max_damage // 2
        random_value = random.randint(half_max_damage, self.max_damage)
        return random_value

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

        self.abilities = list()
        self.armors = list()

        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def attack(self):

        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage

    def defend(self):

        total_block = 0

        for armor in self.armors:
            total_block += armor.block()

        return total_block

    def take_damage(self, damage):
        defense = self.defend()
        self.current_health -= damage - defense

    def is_alive(self):
        
        if self.current_health <= 0:
            return False
        
        return True

    def fight(self, opponent):

        if self.abilities == [] and opponent.abilities == []:
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                my_dmg = self.attack()
                opponent.take_damage(my_dmg)
                
                if opponent.is_alive():
                    opponent_dmg = opponent.attack()
                    self.take_damage(opponent_dmg)

                    if self.is_alive():
                        continue
                    else:
                        opponent.kills += 1
                        self.deaths += 1
                        print(f"{opponent.name} wins!")
                else:
                    self.kills += 1
                    opponent.deaths += 1
                    print(f"{self.name} wins!")

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        
        foundHero = False

        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)

                foundHero = True

        if not foundHero:
            return 0

    def view_all_heroes(self):
        
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} K/D: {kd}")

    def revive_heroes(self):

        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            my_hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            my_hero.fight(opponent)

            if my_hero.is_alive():
                living_opponents.remove(opponent)
            else:
                living_heroes.remove(my_hero)

class Arena:
    def __init__(self):
        team_one = None
        team_two = None

    def create_ability(self):
        name = input("Ability Name: ")
        max_damage = input("Max Damage: ")

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("Weapon Name: ")
        max_damage = input("Max Damage: ")

        return Weapon(name, max_damage)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
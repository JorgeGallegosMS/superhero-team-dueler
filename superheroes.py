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
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("Ability Name: ")
        max_damage = int(input("Max Damage: "))

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("Weapon Name: ")
        max_damage = int(input("Max Damage: "))

        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("Armor Name: ")
        max_block = int(input("Max Block: "))

        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("1. Add an ability\n2. Add Weapon\n3. Add Armor\n4. Done adding items\n\nWhat would you like to do?\n")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)

        return hero

    def build_team_one(self):
        team_name = input("Team 1 Name: ")
        num_heroes = int(input("How many heroes would you like on this team?\n"))
        team = Team(team_name)

        for _ in range(num_heroes):
            hero = self.create_hero()
            team.add_hero(hero)

        self.team_one = team

    def build_team_two(self):
        team_name = input("Team 2 Name: ")
        num_heroes = int(input("How many heroes would you like on this team?\n"))
        team = Team(team_name)

        for _ in range(num_heroes):
            hero = self.create_hero()
            team.add_hero(hero)

        self.team_two = team

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        alive_heroes = [hero.name for hero in self.team_one.heroes if hero.is_alive()]
        alive_enemies = [hero.name for hero in self.team_two.heroes if hero.is_alive()]
        hero_kills = 0
        hero_deaths = 0
        enemy_kills = 0
        enemy_deaths = 0

        if len(alive_heroes) > len(alive_enemies):
            print(f"{self.team_one.name} Wins!")
        elif len(alive_heroes) < len(alive_enemies):
            print(f"{self.team_two.name} Wins!")
        else:
            print("It's a draw")

        for hero in self.team_one.heroes:
            hero_kills += hero.kills
            hero_deaths += hero.deaths

        for enemy in self.team_two.heroes:
            enemy_kills += enemy.kills
            enemy_deaths += enemy.deaths

        print(f"K/D for {self.team_one.name}: {hero_kills/hero_deaths}")
        print(f"K/D for {self.team_two.name}: {enemy_kills/enemy_deaths}")

if __name__ == "__main__":
    game_is_running = True

    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
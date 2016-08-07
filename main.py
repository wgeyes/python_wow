# TODO: Add command that shows all available commands
# TODO: Handle Character death and health resets
# TODO: Leave/Enter combat methods in classes
# TODO: Add list with last twenty prints, clear the console and rewrite again whenever a command has been added
# TODO: A million other things
"""
current commands:
attack - attacks the creature and ends the turn
print stats - prints your health and the monster's. does not end the turn
engage - start the fight
"""
GAME_VERSION = '0.0.1 ALPHA'
def main():
    welcome_print()
    main_character = Character(name="Netherblood",
                               health=10,
                               mana=10,
                               strength=3)
    print("Character {0} created!".format(main_character.name))
    test_creature = Monster(name="Zimbab",
                            health=5,
                            mana=0,
                            min_damage=1,
                            max_damage=3)
    alive_monsters = [test_creature]
    while True:
        print_live_monsters(alive_monsters)

        command = input()
        if command == 'engage':
            main_character.in_combat = True

        while main_character.in_combat:
            creature_swing = test_creature.deal_damage()
            main_character.take_attack(creature_swing)
            print("{0} attacks {1} for {2} damage!".format(test_creature.name, main_character.name, creature_swing))

            command = input()
            while True:
                if command == 'print stats':
                    print("Character {0} is at {1}/{2} health.".format(main_character.name, main_character.health, main_character.max_health))
                    print("Monster {0} is at {1}/{2} health".format(test_creature.name, test_creature.health, test_creature.max_health))
                    command = input()
                else:
                    break
            if command == 'attack':
                character_dmg = main_character.deal_damage()
                test_creature.take_attack(character_dmg)
                print("{0} attacks {1} for {2} damage!".format(main_character.name, test_creature.name, character_dmg))

            if not test_creature.alive:
                main_character.in_combat = False
                print("{0} has slain {1}".format(main_character.name, test_creature.name))


def print_live_monsters(alive_monsters: list):
    print("Alive monsters: ")
    for i in range(len(alive_monsters)):
        print(alive_monsters[i])

class LivingThing:
    """
    This is the base class for all things alive - characters, monsters and etc.
    """
    def __init__(self, name: str, health: int=1, mana: int=1):
        self.name = name
        self.health = health
        self.max_health = health
        self.mana = mana


class Monster(LivingThing):
    def __init__(self, name: str, health: int=1, mana: int=1, min_damage: int=0, max_damage: int=1):
        super().__init__(name, health, mana)
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.alive = True

    def __str__(self):
        return "Creature {0} - {1}/{2} HP | {3}/{4} Mana".format(self.name, self.health, self.max_health, self.mana, self.mana)

    def deal_damage(self):
        import random
        damage_to_deal = random.randint(self.min_damage, self.max_damage + 1)
        return damage_to_deal

    def take_attack(self, damage: int):
        self.health -= damage
        self.check_if_dead()

    def check_if_dead(self):
        if self.health <= 0:
            self.alive = False
            self.die()
        else:
            pass

    def die(self):
        print("Creature {} has been slain!".format(self.name))


class Weapon:
    def __init__(self, min_damage: int=0, max_damage: int=1):
        self.min_damage = min_damage
        self.max_damage = max_damage


class Character(LivingThing):
    def __init__(self, name: str, health: int=1, mana: int=1, strength: int=1):
        super().__init__(name, health, mana)
        self.strength = strength
        self.min_damage = 0
        self.max_damage = 1
        self.equipped_weapon = Weapon()
        self.alive = True
        self.in_combat = False

    def equip_weapon(self, weapon: Weapon):
        self.equipped_weapon = weapon
        self._calculate_damage(self.equipped_weapon)

    def _calculate_damage(self, weapon: Weapon):
        # current formula for damage is: wep_dmg * 0.1 * strength
        self.min_damage = weapon.min_damage * 0.1 * self.strength
        self.max_damage = weapon.max_damage * 0.1 * self.strength

    def deal_damage(self):
        import random
        damage_to_deal = random.randint(self.min_damage, self.max_damage + 1)
        return damage_to_deal

    def take_attack(self, damage: int):
        self.health -= damage
        self.check_if_dead()

    def check_if_dead(self):
        if self.health <= 0:
            self.alive = False
            self.die()
        else:
            pass

    def die(self):
        print("Character {} has been slain!".format(self.name))

def welcome_print():
    print("WELCOME TO PYTHON WOW VERSION: {0}".format(GAME_VERSION))
    print("A simple console RPG game inspired by the Warcraft universe!")
    print()
if __name__ == '__main__':
    main()
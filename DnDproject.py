import sys
import time
import random
import json
from pathlib import Path


# Class stat presets
CLASS_PRESETS = {
    "knight":{
        "vig": 10,
        "mind": 3,
        "end": 3,
        "str": 10,
        "dex": 5,
        "int": 2,
        "arc": 2
    },

    "samurai":{
        "vig": 8,
        "mind": 2,
        "end": 7,
        "str": 3,
        "dex": 10,
        "int": 3,
        "arc": 2
    },

    "mage":{
        "vig": 3,
        "mind": 10,
        "end": 5,
        "str": 1,
        "dex": 2,
        "int": 11,
        "arc": 3
    },

    "necromancer": {
        "vig": 6,
        "mind": 7,
        "end": 3,
        "str": 2,
        "dex": 1,
        "int": 6,
        "arc": 10
    },
    "beserker": {
        "vig": 5,
        "mind": 3,
        "end": 5,
        "str": 11,
        "dex": 7,
        "int": 1,
        "arc": 3
    }
} 


class PLAYER:
    def __init__(self, player_name, player_species, player_class, vig, mind, end, str, dex, int, arc):
        self.name = player_name
        self.species = player_species
        self.player_class = player_class
        self.vig = vig
        self.mind = mind
        self.end = end
        self.str = str
        self.dex = dex
        self.int = int
        self.arc = arc

    def display_created_character(self):

        print("--------------------------")
        print("CREATED CHARACTER: ")
        print("--------------------------")
        print()
        print(f"Name: {self.name}")
        print(f"Class: {self.player_class}")
        print(f"Species: {self.species}")
        print()

    def display_current_stats(self):
        print("--------------------------")
        print(f"CURRENT STATS")
        print("--------------------------")
        print()
        print(f"Vigour --> {self.vig}")
        print(f"Mind --> {self.mind}")
        print(f"Endurance --> {self.end}")
        print(f"Strength --> {self.str}")
        print(f"Dexterity --> {self.dex}")
        print(f"Intelligence --> {self.int}")
        print(f"Arcane -->  {self.arc}")

# Make text appear one letter at a time(use display_text instead of print)
def display_text(text_to_display):
    text = text_to_display
    for letter in text:
        print(letter, end='')  
        sys.stdout.flush()  
        time.sleep(0.0)  
    print("")

# -------------------------------------------------------
# Main menus
# -------------------------------------------------------
def first_main_menu():
    print("--------------------------")
    print("MAIN MENU")
    print("--------------------------")
    time.sleep(1)
    print("[1] New Game")
    print("[2] Load Game")

    valid_choice = False
    while valid_choice == False:
        menu_choice = input()
        if menu_choice == "1":
            display_text("Staring new game...")
            loading_screen()
            player_character = character_creator()
            valid_choice = True
            return player_character
        elif menu_choice == "2":
            display_text("Loading game...")
            return load_game()
        else:
            print("Please pick a valid option (1, 2)")
    valid_choice = False



def main_menu(player_character):
    print()
    print("--------------------------")
    print("MAIN MENU")
    print("--------------------------")
    print()
    time.sleep(1)
    print("[1] View character")
    print("[2] View stats")
    print("[3] View inventory")
    print("[4] Explore world")
    print("[5] Save game")
    print("[6] Quit game")
    print("[7] New game")

    valid_choice = False
    while valid_choice == False:
        menu_choice = input()
        if menu_choice == "1":
            display_text("Viewing character")
            valid_choice = True
            player_character.display_created_character()

            input("Press ENTER to continue")
            main_menu(player_character)
        elif menu_choice == "2":
            display_text("Viewing stats")
            valid_choice = True
            player_character.display_current_stats()

            input("Press ENTER to continue")
            main_menu(player_character)
        elif menu_choice == "3":
            display_text("Viewing inventory")
            valid_choice = True
            print("INVENTORY HERE ONCE MADE")

            input("Press ENTER to continue")
            main_menu(player_character)
        elif menu_choice == "4":
            display_text("Exploring world")
            valid_choice = True
            explore_world(player_character)

            input("Press ENTER to continue")
            main_menu(player_character)
        elif menu_choice == "5":
            display_text("Saving game")
            valid_choice = True
            save_game(player_character)

            input("Press ENTER to continue")
            main_menu(player_character)
        elif menu_choice == "6":
            display_text("Quitting game")
            valid_choice = True
            # NO FUNCTION HERE, PROGRAM ENDS
        elif menu_choice == "7":
            display_text("New game")
            valid_choice = True
            player_character = first_main_menu()
            main_menu(player_character)

        else:
            display_text("Please pick a valid option (1, 2, 3, 4...)")
            valid_choice = False
    valid_choice = False


def character_creator():
    # Welcome messages
    display_text("Welcome traveler, you are about to embark on a perilous journey")
    display_text("Your goal is to escape these wretched lands and cut down any foe in your way")

    # Initialise variables
    valid_choice = False

    # -------------------------------------------------------
    # Pick name
    # -------------------------------------------------------
    display_text("Pick your name: ")
    player_name = input()


    # -------------------------------------------------------
    # Pick Species
    # -------------------------------------------------------
    display_text("Pick a species (1, 2, 3, 4):")
    display_text("[1] Human, a superior species that is in the midst of a war with the Orcs")
    display_text("[2] Orc, a simple beast that forgoes intelligence for raw violence")
    display_text("[3] Elf, a fierce warrior that pairs honour with frightening skill with a sword")
    display_text("[4] Dwarf, what thay lack in height they make up for in firepower")

    while valid_choice == False:
        species_choice = str(input())
        if species_choice == "1":
            display_text("You have chosen human")
            player_species = "human"
            valid_choice = True
        elif species_choice == "2":
            display_text("You have chosen orc")
            player_species = "orc"
            valid_choice = True
        elif species_choice == "3":
            display_text("You have chosen elf")
            player_species = "elf"
            valid_choice = True
        elif species_choice == "4":
            display_text("You have chosen dwarf")
            player_species = "dwarf"
            valid_choice = True
        else:
            display_text("Please pick a valid option (1, 2, 3, 4)")
            valid_choice = False

    # Set valid_choice to false again for future use
    valid_choice = False

    # -------------------------------------------------------
    # Pick Class
    # -------------------------------------------------------

    display_text("Pick your class (1, 2, 3, 4, 5):")
    display_text("[1] Knight: A heavy soilder clad in thick iron armour, can negate some incoming damage")
    display_text("[2] Samurai: A skilled swordsman that favour honour and courage, has a chance do deal double damage in a critical strike")
    display_text("[3] Mage: An intelligent spellcaster that prefers to attack from a distance, both own and enemies' attacks have a chance to miss")
    display_text("[4] Necromancer: A cursed soul that can summon dark magic, can skip turns to queue up multiple actions")
    display_text("[5] Beserker: A maddened and bloodthirsty warrior, attack damage increases as HP lowers")

    while valid_choice == False:
            class_choice = str(input())
            if class_choice == "1":
                display_text("You have chosen knight")
                player_class = "knight"
                valid_choice = True
            elif class_choice == "2":
                display_text("You have chosen samurai")
                player_class= "samurai"
                valid_choice = True
            elif class_choice == "3":
                display_text("You have chosen mage")
                player_class = "mage"
                valid_choice = True
            elif class_choice == "4":
                display_text("You have chosen necromancer")
                player_class = "necromancer"
                valid_choice = True
            elif class_choice == "5":
                display_text("You have chosen beserker")
                player_class = "beserker"
                valid_choice = True
            else:
                display_text("Please pick a valid option (1, 2, 3, 4, 5)")
                valid_choice = False

    # Set valid_choice to false again for future use
    valid_choice = False

    # Get the stats based on what class the player picks
    stats = CLASS_PRESETS[player_class]
    player = PLAYER(player_name= player_name, player_species= player_species, player_class=player_class, **stats)

    # Let the player level up a few times immediately
    time.sleep(2)
    print()
    print()
    print()
    print()

    display_text("Here is your chosen class stats:")

    print()
    skill_points = 5
    level_up(player, skill_points)


    # Loading Screen effect
    loading_screen()
    
    player.display_created_character()
    player.display_current_stats()


    return player

# -------------------------------------------------------
# Level Up
# -------------------------------------------------------

def level_up(player, skill_points):
    print("")
    print("--------------------------")
    print("LEVEL UP")
    print("--------------------------")

    stat_inputs = {
        "1": "vig",
        "2": "mind",
        "3": "end",
        "4": "str",
        "5": "dex",
        "6": "int",
        "7": "arc"
    }
    player.display_current_stats()
    print()
    while skill_points > 0:
        print()
        print("Current skill points = ", skill_points)
        time.sleep(1)
        display_text("Which stat do you want to level up?")
        time.sleep(0.5)
        print()
        print("[1] Vigour")
        print("[2] Mind")
        print("[3] Endurance")
        print("[4] Strength")
        print("[5] Dexterity")
        print("[6] Intelligence")
        print("[7] Arcane")

        stat_choice = str(input())

        if stat_choice in stat_inputs:
            stat_to_increase = stat_inputs[stat_choice]

            current_stat_value = getattr(player, stat_to_increase)
            setattr(player, stat_to_increase, current_stat_value + 1)
            skill_points = skill_points - 1

            print("[+] Increased", stat_to_increase, "by 1")
            print(stat_to_increase, "[", current_stat_value-1, "] --> [", current_stat_value, "]")
        else:
            print("Please pick a valid option (1, 2, 3, 4, 5, 6, 7)")
    player.display_current_stats()



def loading_screen():
    for i in range (random.randint(3,5)):
        time.sleep(random.randint(1,3))
        print("LOADING...")
        print()
        print()
        print()

# -------------------------------------------------------
# Save game
# -------------------------------------------------------
def save_game(player_character):
    save_data = {
        "name": player_character.name,
        "species": player_character.species,
        "class": player_character.player_class,
        "vig": player_character.vig,
        "mind": player_character.mind,
        "end": player_character.end,
        "str": player_character.str,
        "dex": player_character.dex,
        "int": player_character.int,
        "arc": player_character.arc
    }
    with Path(__file__).with_name("saveSlot1.json").open("w", encoding="utf-8") as save_file:
        json.dump(save_data, save_file)


def load_game():
    with Path(__file__).with_name("saveSlot1.json").open(encoding="utf-8") as save_file:
        loaded_data = json.load(save_file)
    return PLAYER(
        player_name=loaded_data["name"],
        player_species=loaded_data["species"],
        player_class=loaded_data["class"],
        vig=loaded_data["vig"],
        mind=loaded_data["mind"],
        end=loaded_data["end"],
        str=loaded_data["str"],
        dex=loaded_data["dex"],
        int=loaded_data["int"],
        arc=loaded_data["arc"],
    )

# -------------------------------------------------------
# World Exploration
# -------------------------------------------------------

def explore_world(player_character):
    print("--------------------------")
    display_text("TRAVELLING TO : Inkwell Tavern")
    print("--------------------------")
    print()
    display_text("You enter an old, warm structure, the comforting smell of wood greets you as the heavy oak door slams behind you")
    display_text("The harsh, icy wind is instantly blocked out and you are overcome with a warmth you haven't felt in a long time")
    display_text("")
    input("Press ENTER to continue")
    print()
    display_text("Where do you want to go?")
    time.sleep(0.5)
    print("[1] Map room")
    print("Where you can select areas to go on an expedition to")
    print("ADD MORE LOCATIONS HERE ONCE MADE")

    valid_choice = False
    while valid_choice == False:
        location = input()
        if location == "1":
            explore_dungeon(player_character)
            valid_choice = True
        elif location == "2":
            # call location function here
            valid_choice = True
        else:
            display_text("Please pick a valid option (1, 2)")
            valid_choice = False
    valid_choice = False


def explore_dungeon(player_character):
    # Initialise player stats when they enter the area
    derived_stats_list = derived_stats(player_character)
    current_hp = derived_stats_list[0]
    
    print("--------------------------")
    display_text("TRAVELLING TO : The Sunken Ossuary")
    print("--------------------------")
    # Enterance
    display_text("A heavy stone door groans open to release a gust of stagnant, freezing air")
    display_text("Before you lies a dark, stone corridor. Moisture leaks from the cracked ceiling, feeding patches of dark green moss")
    display_text("It is deathly quiet save for rhythmic drip of water echoing in the dark")

    time.sleep(1)

    # First room
    print()
    display_text("You traverse the corridor, which opens into a large room, a sole figure stands in the center")
    display_text("A heavy metalic clang reverberates from the stone floor behind you as a large rusted gate slams shut")
    time.sleep(1)
    print()
    display_text("The figure steps into the light to reveal a skeleton, its bones stained a moss green")
    display_text("It tilts its skull, a dull, dead weight shifting in its empty sockets")
    display_text("It draws a rusted, serated broadsword, standing between you and the only exit...")
    
    
    # Initilalise enemy variables the player will go into combat with
    # Strucutre is [enemy name, enemy type, enemy level]
    enemy_structure = ["moss skeleton", "sword", 40]

    combat_loop(player_character, derived_stats_list, current_hp, enemy_structure)


# -------------------------------------------------------
# Combat
# -------------------------------------------------------
def combat_loop(player_character, derived_stats_list, current_hp, enemy_structure):
    # Initialise enemy based on enemy_structure
    enemy_derived_stats_list = define_enemy(enemy_structure)

    enemy_turn(enemy_derived_stats_list)

    player_turn(player_character, derived_stats_list, current_hp, enemy_derived_stats_list)
    

def derived_stats(player_character):
    hp_max = player_character.vig * 10
    if player_character.player_class == "mage" or player_character.player_class == "necromancer":
        mana = player_character.mind * 10
    else:
        mana = 0
    if player_character.player_class == "knight":
        damage = player_character.str * 10 + player_character.dex * 2
    elif player_character.player_class == "samurai":
        damage = player_character.dex * 10 + player_character.str * 2
    elif player_character.player_class == "mage":
        damage = player_character.int * 11
    elif player_character.player_class == "necromancer":
        damage = player_character.arc * 10 + player_character.int * 2
    elif player_character.player_class == "beserker":
        damage = player_character.str * 6 + player_character.dex * 5

    hp_fp_dmg = [hp_max, mana, damage]
    return hp_fp_dmg

def player_turn(player_character, derived_stats_list, current_hp, enemy_derived_stats_list):
    display_text("ACTIONS:")
    print()
    if player_character.player_class == "knight":
        display_text("[1] GREATSWORD SWING: Slash the enemy with a heavy downward swing of your greatsword (deals moderate damage)")
        display_text("[2] PALISADE FORM: Raise your shield forming an unbreakable guard (blocks all next attack's damage recieved)")
        display_text("[3] HEAL: Drink up a brew from the tavern (restores some HP)")
        print("ADD MORE ACTIONS LIKE RUN AWAY ONCE MADE")
        print()
        valid_choice = False
        while valid_choice == False:
            action = input()
            if action == "1":
                display_text("You drive your greatsword into the enemy at frightening speed")
                time.sleep(0.5)
                print("They take", derived_stats_list[2], "damage")
                # DEAL DAMAGE FUNCTION HERE
                damage_to_deal = derived_stats_list[2]
                player_deal_damage(damage_to_deal, enemy_derived_stats_list)
                valid_choice = True
            elif action == "2":
                display_text("You raise your shield and assume a defensive stance")
                time.sleep(0.5)
                print("Enemy's next attack will be blocked")
                # DEAL DAMAGE FUNCTION HAS NO EFFECT HERE
                # PRINT ATTACK BLOCKED MESSAGE INSTEAD
                valid_choice = True
            elif action == "3":
                display_text("You pull the potion from your satchel and take a good swig")
                time.sleep(0.5)
                current_hp = heal(derived_stats_list, current_hp)
                valid_choice = True
            else:
                display_text("Please pick a valid option (1, 2, 3)")
                valid_choice = False
        valid_choice = False
    elif player_character.player_class == "samurai":
        display_text("[1] KATANA SLASH: Draw your blade at lightning speed and use the momentum to swing at the enemy (deals moderate damage with a chance to deal a critical strike)")
        display_text("[2] SHARPEN KATANA: Sharpen your sword mid combat (greatly incresases chance of a critical strike next turn)")
        display_text("[3] HEAL: Drink up a brew from the tavern (restores some HP)")
        print("ADD MORE ACTIONS LIKE RUN AWAY ONCE MADE")
        print()
        valid_choice = False
        while valid_choice == False:
            action = input()
            if action == "1":
                display_text("You unsheath your pristinely sharpened blade, slashing the enemy")
                time.sleep(0.5)
                print("They take", derived_stats_list[2], "damage")
                # DEAL DAMAGE FUNCTION HERE
                valid_choice = True
            elif action == "2":
                display_text("You pull a whetstone from your satchel and run it up and down the smooth edge of your katana")
                time.sleep(0.5)
                print("Increased chance of a critical strike next turn")
                # DEAL DAMAGE FUNCTION HERE WITH CRIT MULTIPLIER
                valid_choice = True
            elif action == "3":
                display_text("You pull the potion from your satchel and take a good swig")
                time.sleep(0.5)
                current_hp = heal(derived_stats_list, current_hp)
                valid_choice = True
            else:
                display_text("Please pick a valid option (1, 2, 3)")
                valid_choice = False
        valid_choice = False
    elif player_character.player_class == "mage":
        display_text("[1] CAST SORCERY: Channel power into your staff and release it towards the enemy (deals moderate damage with a chance to miss)")
        display_text("[2] HONE MAGIC: Focus all of your power into the next strike (Greatly decreases next attack's chance to miss)")
        display_text("[3] HEAL: Drink up a brew from the tavern (restores some HP)")
        print("ADD MORE ACTIONS LIKE RUN AWAY ONCE MADE")
        print()
        valid_choice = False
        while valid_choice == False:
            action = input()
            if action == "1":
                display_text("You point your staff forwards the enemy and a glowing projectile is produced which fires towards them")
                time.sleep(0.5)
                print("They take", derived_stats_list[2], "damage")
                # DEAL DAMAGE FUNCTION HERE
                valid_choice = True
            elif action == "2":
                display_text("You hold your staff up to the sky, channeling its")
                time.sleep(0.5)
                print("Decreased next attack's chance to miss")
                # DEAL DAMAGE FUNCTION HERE WITH CHANCE TO MISS MULTIPLIER
                valid_choice = True
            elif action == "3":
                display_text("You pull the potion from your satchel and take a good swig")
                time.sleep(0.5)
                current_hp = heal(derived_stats_list, current_hp)
                valid_choice = True
            else:
                display_text("Please pick a valid option (1, 2, 3)")
                valid_choice = False
        valid_choice = False
    elif player_character.player_class == "necromancer":
        display_text("[1] SUMMON DARK MAGIC: Channel the power of the dead to cast dark magic (deals moderate damage)")
        display_text("[2] DARK TIME DIALATION: Allow the dead to warp the very time around you and the enemy, the sheer force of this action weakens you (Forgoe an action this turn but queue it for use next turn, damage taken is multiplied by amount of queued actions)")
        display_text("[3] DESOLATION OF TIME: Instantly release the energy stored due to dark time dialation (Release a massive burst of damage, multiplied by turns currently queued, can only be cast with over 3 turns queued)")
        display_text("[4] HEAL: Drink up a brew from the tavern (restores some HP)")
        print("ADD MORE ACTIONS LIKE RUN AWAY ONCE MADE")
        print()
        valid_choice = False
        while valid_choice == False:
            action = input()
            if action == "1":
                display_text("You summon a ghoulish blue scythe and swing it towards the enemy")
                time.sleep(0.5)
                print("They take", derived_stats_list[2], "damage")
                # DEAL DAMAGE FUNCTION HERE
                valid_choice = True
            elif action == "2":
                display_text("You summon spirits which unravel the threads of time around you, as their power grows, yours diminishes")
                time.sleep(0.5)
                print("Queued -TURNS QUEUED VARIABLE HERE- actions")
                # NO DEAL DAMAGE FUNCTION HERE, INCREMENT TURNS QUEUED VARIABLE
                valid_choice = True
            elif action == "3":
                display_text("The spirits vigourously snap the threads of time, the sheer magnitude of power explodes and as quickly as it appeared, the dialation dies down to mere echoes in the wind")
                time.sleep(0.5)
                print("-TURNS QUEUED VARIABLE HERE- queued turns consumed")
                # QUEUED TURNS RESET TO ZERO
                valid_choice = True
            elif action == "4":
                display_text("You pull the potion from your satchel and take a good swig")
                time.sleep(0.5)
                current_hp = heal(derived_stats_list, current_hp)
                valid_choice = True
            else:
                display_text("Please pick a valid option (1, 2, 3)")
                valid_choice = False
        valid_choice = False
    elif player_character.player_class == "beserker":
        display_text("[1] AXE SWIPES: Wildly swing your axe, chanelling the blood of your injuries into the blade (deals moderate damage scaling with hp lost)")
        display_text("[2] BLOOD HEX: Cast blood magic that reduces own hp (increases attack multiplier due to lower health)")
        display_text("[3] HEAL: Drink up a brew from the tavern (restores some HP)")
        print("ADD MORE ACTIONS LIKE RUN AWAY ONCE MADE")
        print()
        valid_choice = False
        while valid_choice == False:
            action = input()
            if action == "1":
                display_text("You slash the enemy rapidly, the blade glows a deep red, empowered by your injuries")
                time.sleep(0.5)
                print("They take", derived_stats_list[2], "damage")
                # DEAL DAMAGE FUNCTION HERE
            elif action == "2":
                display_text("You summon a blood red sigil and shatter it, its shards cutting deep into your skin")
                time.sleep(0.5)
                hp_to_remove = derived_stats_list[0] // 3
                current_hp = current_hp - hp_to_remove
                if current_hp <= 0:
                    current_hp = 1
                print("HP decreased by ", hp_to_remove)
                print(current_hp)
                valid_choice = True
            elif action == "3":
                display_text("You pull the potion from your satchel and take a good swig")
                time.sleep(0.5)
                current_hp = heal(derived_stats_list, current_hp)
                valid_choice = True
            else:
                display_text("Please pick a valid option (1, 2, 3)")
                valid_choice = False
        valid_choice = False


def player_deal_damage(damage_to_deal, enemy_derived_stats_list):
    enemy_derived_stats_list[2] = enemy_derived_stats_list[2] - damage_to_deal
    print("The", enemy_derived_stats_list[0], "has", enemy_derived_stats_list[2], "HP left")
    

# Healing
def heal(derived_stats_list, current_hp):
    health_to_heal = derived_stats_list[0] // 4
    if derived_stats_list[0] >= current_hp + health_to_heal:
        current_hp = current_hp + health_to_heal
        return current_hp
    else:
        current_hp = derived_stats_list[0] 
        return current_hp

# -------------------------------------------------------
# Enemy
# -------------------------------------------------------
def define_enemy(enemy_structure):
    enemy_name = enemy_structure[0]
    enemy_type = enemy_structure[1]
    enemy_hp = enemy_structure[2] * 11
    enemy_damage = enemy_structure[2] * 2
    enemy_derived_stats_list = [enemy_name, enemy_type, enemy_hp, enemy_damage]
    return enemy_derived_stats_list

def enemy_turn(enemy_derived_stats_list):
    attack_choice = random.randint(1,10)
    print("Attck choich is", attack_choice)
    if attack_choice <= 3:
        if enemy_derived_stats_list[1] == "sword":
            print("The ", enemy_derived_stats_list[0], "raises its sword high and slams it down onto you")
            time.sleep(0.5)
            print("You take", enemy_derived_stats_list[3] * 2 , "damage")
    elif attack_choice > 3:
        if enemy_derived_stats_list[1] == "sword":
            print("The ", enemy_derived_stats_list[0], "performs a swift strike with its sword")
            time.sleep(0.5)
            print("You take", enemy_derived_stats_list[3], "damage")

# -------------------------------------------------------
# Main program
# -------------------------------------------------------
player_character = first_main_menu()
main_menu(player_character)
#explore_world(player_character)
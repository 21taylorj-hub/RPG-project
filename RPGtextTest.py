import sys
import time

# Make text appear one letter at a time(use display_text instead of print)
def display_text(text_to_display):
    text = text_to_display
    for letter in text:
        print(letter, end='')  
        sys.stdout.flush()  
        time.sleep(0.06)  

display_text("Welcome traveler, ")
time.sleep(0.5)
display_text("you are about to embark on a perilous journey")
print()
display_text("Pick your class:")
print("\n")
display_text("[1] Knight: A heavy soilder clad in thick iron armour, can negate some incoming damage")
print("\n")
display_text("[2] Samurai: A skilled swordsman that favour honour and courage, has a chance do deal double damage in a critical strike")
print("\n")
display_text("[3] Mage: An intelligent spellcaster that prefers to attack from a distance, both own and enemies' attacks have a chance to miss")
print("\n")
display_text("[4] Necromancer: A cursed soul that can summon dark magic, can skip turns to queue up multiple actions")
print("\n")
display_text("[5] Beserker: A maddened and bloodthirsty warrior, attack damage increases as HP lowers")
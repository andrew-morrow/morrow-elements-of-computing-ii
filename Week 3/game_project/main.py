# main.py
from characters.character import Character
from characters.warrior import Warrior
from characters.healer import Healer
from characters.mage import Mage
from characters.rogue import Rogue
from characters.archer import Archer

# Simulating Dynamic Behavior
def battle_round(character, target):
    """
    Simulates a single round of battle between two characters.

    Args:
        character (Character): The character performing the action.
        target (Character): The target of the action.
    """
    # Display the character's information
    print("\nBefore round info:")
    print(character.display_info())
    print(target.display_info())

    print("\nAction taken:")
    # Check the character's type and perform the corresponding action
    if isinstance(character, Rogue):  # If the character is a Rogue
        print(character.sneak_attack(target))  # Perform a sneak attack
    elif isinstance(character, Archer):  # If the character is an Archer
        print(character.fire_arrow(target))  # Fire an arrow
    elif isinstance(character, Mage):  # If the character is a Mage
        print(character.cast_spell(2))  # Cast a spell
    elif isinstance(character, Healer):  # If the character is a Healer
        print(character.heal(target))  # Heal the target
    elif isinstance(character, Warrior):  # If the character is a Warrior
        print(character.strength)  # Display the warrior's strength

    print("\nAfter round info:")
    print(character.display_info())
    print(target.display_info())

# Main game execution
if __name__ == "__main__":
    # create characters
    robin = Rogue("Robin", 4, 100, 20, 3)
    leo = Mage("Leo", 100, 100, 10)
    doc = Healer("Doc", 100, 10, 10)
    link = Archer("Link", 30, 100, 20, 4)
    
    # create condition for while loop
    has_arrows = True

    # allow link to fire arrows until they run out
    while has_arrows:

        # check arrow count, set loop to end after this round if at 0
        if link.arrows == 0: has_arrows = False
        
        # commence battle round
        battle_round(link,leo)

    


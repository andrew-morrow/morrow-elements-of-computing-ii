# archer.py
from .warrior import Warrior

# create new archer class that inherits from warrior
class Archer(Warrior):
    """
    Represents an Archer character, inheriting from Warrior.

    Attributes:
        name (str): The archer's name.
        level (int): The archer's level.
        health (int): The archer's current health.
        strength (int): The archer's strength attribute.
        arrows (int): The archer's arrow count.
    """
    def __init__(self, name, level, health, strength, arrows):
        """Initializes a new Archer object."""

        # Call the parent class's __init__ method to initialize inherited attributes
        super().__init__(name, level, health, strength)

        # Initialize the archer's specific attribute: arrows
        self.arrows = arrows

    def fire_arrow(self, target):
        """
        Shoots an arrow at the target, reducing their health.

        Args:
            target (Character): The target of the arrow shot.

        Returns:
            str: A message describing the shot and its damage dealt.
        """

        # check to see if the archer has any arrows
        if self.arrows > 0:
            # shoot arrow
            self.arrows -= 1
            
            # deal damage to target
            target.health -= self.strength

            # return the interaction as a string
            return f"{self.name} fires an arrow at {target.name}, dealing {self.strength} damage!"
        else:
            # return message about having no arrows
            return f"{self.name} tries to draw an arrow, but their quiver is empty!"








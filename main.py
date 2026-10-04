# DAY 16 {OBJECT ORIENTED PROGRAM(OOP)}!!!!

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")  #shape.
timmy.color("coral")  #color.
timmy.forward(100)   # move.

#OBJECT ATTRIBUTES AND METHODS!!
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick() # THIS 

#MODIFYING OBJECT ATTRIDUTES AND CALLING METHOD!!
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", [
    "Pikachu",
    "Squirtle",
    "Charmander",
    "Haxorus",
    "Salamence",
    "Garchomp",
    "Goodra",
    "Krookodile",
    "Staraptor",
    "Gengar"
])

table.add_column("Type", [
    "Electric",
    "Water",
    "Fire",
    "Dragon",
    "Dragon",
    "Dragon",
    "Dragon",
    "Ground/Dark",
    "Normal/Flying",
    "Ghost/Poison"
])

table.align = "l"

print(table)
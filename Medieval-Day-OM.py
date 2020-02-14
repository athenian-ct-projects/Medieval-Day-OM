print("""
My code is for medieval day, and it is intended to be a fun way to learn about medieval warfare; crossbows, swords, and armor. 
The user types either A, B, C , y, or n depending on the prompt. Each path has a different ending, so the game is replayable.

by OM '23
""")

import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
sword = 0
crossbow = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print ("After successfully infiltrating the castle and stealing the King's golden amulet, you are on the run from the Royal Guard. You have been running for days, so you seek shelter in some forest brush and fall into a restless sleep. ")
  time.sleep(1)
  print ("You awaken "
  "in a thick, dark forest. You stand and marvel at your new, "
  "unfamiliar setting. The peace quickly fades when you hear a "
  "heavy footsteps emitting from behind you. One of the King's Knights is "
  "running towards you. You will:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the knight
  B. Lie down and surrender
  C. Run""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nYou plead for you life, but the knight takes no pity on you, and delivers you a swift death. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_rock(): 
  print ("\nThe knight is temporarily stunned, but regains control. he begins "
  "running towards you again. Will you:")
  time.sleep(1)
  print ("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decide to throw another rock, as if the first " 
    "rock thrown did much damage. The rock fles well over the "
    "knight's head. You miss. \n\nYou died!")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("\nYou are hesitant, since the cave i dark and "
  "ominous. Before you fully enter, you notice a shiny sword on "
  "the ground. Do you pick up a sword. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 #adds a sword
  else:
    sword = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nReally? You hide in the dark, but the knight hears your breathing and finds you.\n\nYou died!")
  elif choice in answer_B:
   if sword > 0:
    print ("\nYou lie in wait. The shimmering sword attracts "
    "the knight, which thinks you are no match. As he walks "
    "closer and closer, your heart beats rapidly. As the knight "
    "reaches out to grab the sword, you pierce the blade between the links in his armor into his stomach. \n\nYou survived!")
   else: #If the user didn't grab the sword
     print ("\nYou should have picked up that sword. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the knight enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the knight turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the knight's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for a well armed and well trained knight. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print ("\nWhile frantically running, you notice a rusted "
  "sword lying in the mud. You quickly reach down and try to grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the knight to come "
  "charging around the corner. You notice an old, loaded crossbow sitting amongst some rubble "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    crossbow = 1 #adds a crossbow
  else:
    crossbow = 0
  print ("You hear his heavy footsteps and ready yourself for "
  "the impending knight.")
  time.sleep(1)
  if crossbow > 0:
    print ("\nYou ready your crossbow and aim at the visor in his helmet. The knight is almost on top of you as you let the bolt fly, "
    "hoping it will stop the knight. It does! The bolt soars through the air and strikes the knight between the eyes, killing him."
    "\n\nYou survived!")
  else: #If the user didn't grab the sword
     print ("\nMaybe you should have picked up the crossbow. "
     "\n\nYou died!")

intro()

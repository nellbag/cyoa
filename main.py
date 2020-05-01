
##
## Author: Neil MacPhail  ## Started: 28/04/2020
##
## Description:
## Choose your own adventure game, welll at least 
## an attempt at it as I am a NOOB. 
##
## See references.txt for ideas/resources used
##

import time
import sys
import random
global hp


locations = {
    'jungle': {
        'name': 'doon the Jungle', 
        'north': 'main_st', 
        'south': 'glasgow_rd',
        'items': ['iphone', 'wallet'],
        'npc_name': '',
        'npc_text': '',
        'desc': "Everything seems creepily quiet.\nThe trees don't seem to be moving at all.\nThis is spooky as fuck.",
        'text': 'You see a path to the north leading to the\nMain St and a path to the south leading to\nAuld Glasgow Rd.'},
    'main_st': {
        'name': 'up the Main St', 
        'east': 'top_glass', 
        'south': 'jungle',
        'items': [],
        'npc_name': 'that burd',
        'npc_text': "In the distance you see a wumin shuffling towards you...\nShit! It's that burd!",
        'desc': "All the street lights are out, probably just a power cut\nor the young team have smashed them all. Wee bams.",
        'text': 'To the east you can head towards Top Glass.\nTo the south you can go back doon the Jungle.'},
    'glasgow_rd': {
        'name': 'auld Glasgow Rd', 
        'east': 'spur_tunnel', 
        'west': 'hoose',
        'north': 'jungle',
        'items': [],
        'npc_name': "",
        'npc_text': "",
        'desc': "",
        'text': ""}
    }

enemies = {'that burd': 
          {'description': 'That psycho you winched up paps.',
        'contents': None,
        'hp': 18,
        'attack': [3, 7, 4, 5, 1, 9, 3]}
          }
        #random.choice(items['that burd']['attack'])


#set player details and stats to begin game
player = ''
bird = ''
hp = 100
inventory = []
current_location = locations['jungle']
directions = ['north', 'south', 'east', 'west']
keep_going = True
loc_count = -1

def delay_print_slow(string):
  for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15) #0.15

def delay_print(string):
  for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.10) #0.10

def delay_print_fast(string):
  for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0005) #0.0005

def whitey():
  spew = random.randrange(100)
  if loc_count > 4 and spew >= 85:
    global hp
    hp = hp -3
    return 'You begin to get hot and sweaty.\nYou start to feel dizzy.\nSuddenly you spew. It is an absolute honkin mess.\nHP now: ' + str(hp) + '\n'
  else:
    return ''

#intro and name getting

delay_print_fast("|----------------------------------------------------------------|\n")
delay_print_fast("|8888888888888888888888888888888888888888888888888888888888888888|\n")
delay_print_fast("|88|--------------------------------------------------------- |88|\n")
delay_print_fast("|88|             .___________. __    __   _______ 			  |88|\n")
delay_print_fast("|88|             |           ||  |  |  | |   ____|			  |88|\n")
delay_print_fast("|88|             `---|  |----`|  |__|  | |  |__   			  |88|\n")
delay_print_fast("|88|                 |  |     |   __   | |   __|  			  |88|\n")
delay_print_fast("|88|                 |  |     |  |  |  | |  |____ 			  |88|\n")
delay_print_fast("|88|                 |__|     |__|  |__| |_______|			  |88|\n")
delay_print_fast("|88|                                              			  |88|\n")
delay_print_fast("|88|          ____    ____ ____    ____ .___________.         |88|\n")
delay_print_fast("|88|          \   \  /   / \   \  /   / |           |         |88|\n")
delay_print_fast("|88|           \   \/   /   \   \/   /  `---|  |----`         |88|\n")
delay_print_fast("|88|            \      /     \_    _/       |  |              |88|\n")
delay_print_fast("|88|             \    /        |  |         |  |              |88|\n")
delay_print_fast("|88|              \__/         |__|         |__|              |88|\n") 
delay_print_fast("|88|                                                          |88|\n")
delay_print_fast("|88|          _______.     ___       _______      ___         |88|\n")
delay_print_fast("|88|         /       |    /   \     /  _____|    /   \        |88|\n")
delay_print_fast("|88|        |   (----`   /  ^  \   |  |  __     /  ^  \       |88|\n")
delay_print_fast("|88|         \   \      /  /_\  \  |  | |_ |   /  /_\  \      |88|\n")
delay_print_fast("|88|     .----)   |    /  _____  \ |  |__| |  /  _____  \     |88|\n")
delay_print_fast("|88|     |_______/    /__/     \__\ \______| /__/     \__\    |88|\n")
delay_print_fast("|88| 														  |88|\n")
delay_print_fast("|88|														  |88|\n")
delay_print_fast("|88|--------------------------------------------------------- |88|\n")
delay_print_fast("|8888888888888888888888888888888888888888888888888888888888888888|\n")
delay_print_fast("|----------------------------------------------------------------|\n")
delay_print_fast("By repl.it/@nellbag\n")

print('')
print('')

delay_print_slow("It’s cold as fuck....\n")
print('')
time.sleep(2) #2
delay_print_slow("It’s dark....\n") 
print('')
time.sleep(2) #2
delay_print("You appear to be lying on the ground.\n")
delay_print("WTF, what even happened last night?!\n")
print('')
time.sleep(2) #2
delay_print("The last thing you remember is tanning a bottle\nof wine and 4 cans a Dragon Soop......\n")
print('')
time.sleep(3) #3

print('Can you even remember your own name?')
#player = 'Testy McDebug'
player = input('Name: ').strip()       
player = player.lower()
print('')

print("Suddenly you get a flashback from last night, you\nremember winching that psycho burd fae the scheme up Paps :/")
time.sleep(3) #3
print("Fuck sake " + str(player) + ", she's fuckin' mental.")

print('')
print("Anyway.... you slowly open your eyes and come to.") 
time.sleep(2) #2
print("Your heid is absolutely banging and you feel a whitey coming on.") 
time.sleep(4) #4
print('')
print("Fuck this shit, you need to find the troops\nand work out what happened last night.")
time.sleep(4) #4
delay_print_slow(".......\n")
delay_print_slow(".......\n")
delay_print_slow(".......\n")
delay_print_slow(".......\n")
print('')

while keep_going == True:

  print('  ||  ') #change these
  print('  ||  ')
  print('  ||  ')
  print(' \  / ')
  print('  \/  ')  
  print('')

###
### Movement
###

  loc_count += 1
  print('You are {}.'.format(current_location['name']))
  print(current_location['desc'])
  if current_location['npc_text']:
    print(current_location['npc_text'])
  print('')
  print(current_location['text'])
  print('')
  print(whitey()) 

  if current_location['items']:
    print('Through your fuzzy hungover eyes you\nsee these items: {}'.format(', '.join(current_location['items'])))

  
  command = input("What do you do?\n").strip()
  command = command.lower().split()[1]

  # movement
  if command in directions: 
    if command in current_location:
      current_location = locations[current_location[command]]
    else:
    # bad movement
      print('')
      print('           xxxxxxxxxxxxxxxxxxxxxxxx')
      print("           Cannae go that way mate.")
      print('           xxxxxxxxxxxxxxxxxxxxxxxx')
      print('')

      # quit game
  elif command.lower() in ('q', 'quit'):
      print('')
      print('           xxxxxxxxxxxxxxxxxxxxxxxx')
      print("           xxx SHAT IT, GOODBYE xxx")
      print('           xxxxxxxxxxxxxxxxxxxxxxxx')
      print('')
      break

    # gather objects
  elif command.lower().split()[0] == 'get':
    item = command.lower().split()[1]
    if item in current_location['items']:
            current_location['items'].remove(item)
            inventory.append(item)
            print('')
            print('           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            print("           xxx You've lifted '" + str(item) + "' xxx")
            print('           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            print('')
    else:
      print('')
      print('           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
      print("           xxxx That's no here dafty xxxx")
      print('           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
      print('')

    # get rid of objects
  elif command.lower().split()[0] == 'drop':
    item = command.lower().split()[1]
    if item in inventory:
            current_location['items'].append(item)
            inventory.remove(item)
            print('')
            print('           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            print("           xxx You've drapped " + str(item) + " xxx")
            print('           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            print('')
            #print("You've drapped " + str(item) + ".")
    else:
      print('')
      print('           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
      print("           xx You've no goat that hing xx")
      print('           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
      print('')

  
   # check HP
  elif command.lower().split()[1] == 'hp':
      print('')
      print('           xxxxxxxxxxxxxxxxxxxxxxxx')
      print("           xxx Current HP: " + str(hp) + " xxxx")
      print('           xxxxxxxxxxxxxxxxxxxxxxxx')
      print('')

   # check Inventory
  elif command.lower().split()[1] == 'inventory':
      print('')
      print('           xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
      print('           Items currently in inventory:')
      print('           \n           '.join(inventory))
      print('           xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
      print('           xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
      print('')

    # bad command
  else:
    print('')
    print('           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print("           xx Nae idea what you're oan about mate xx")
    print('           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print('')




 # keep_going = False






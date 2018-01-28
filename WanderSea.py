# Myers-Briggs Framework 
import time
introCount = 0
extraCount = 0
senseCount = 0
intuitCount = 0
thinkCount = 0
feelCount = 0
judgeCount = 0
perceptCount = 0

(IE) = "IE"
(SN) = "SN"
(TF) = "TF"
(JP) = "JP"

#Story Framework
research = 0
tools = 0

# Menu 

print("Welcome to the WanderSea Interactive Adventure")
time.sleep(0.35)
print("Over time, your decisions will help it analyze your Myer-Briggs personality type")

menuCommand = "notbegin"

while menuCommand != "begin":
  print("Type begin to start the game")
  menuCommand = input("Navigation Selection")
  if (menuCommand == "begin"):
      time.stop(.5)
      print()
      print()
      print("Preparing Simulation")
      break
     


  
# Awakening
print()
print("Chapter 0 - Awakening")
print()


print ("Sensations of sand, cool crashing of waves, wind whooshing through the trees")
name = input("Who am I?")
print ("Yes, I am that I am, I am ... " + name)
print()
print ("[Type in wake]")
time.sleep(0.5)
input("What do you do?")
print("The sun strikes your eyes, making you wince and blinding you until your eyes finally adjust. In front of you are azure waves that twinkle in the light. To your left and right is a line of sand that curves around behind you into the distance, behind you lies a verdant jungle that simmers with both vitality, and underneath, a sense of malevolence. The shrieks of birds echo outwards, assaulting your ears.")
time.sleep(0.35)
print()
d1 = input("What would you like to do? 1 - explore the coast 2 - look for food and water")
  
if (d1 == "1"):
  print("The island takes you about five minutes to walk around, and you see some small crabs skittering around, but no humans, and certainly no sight of another island. On your way back, you notice some coconuts on a nearby tree.")
  
elif (d1 == "2"):
  print ("There are some coconuts on a tree near the edge of the forest, but certainly no water.")
  
print()

d2 = input("What would you like to do? 1 - pick and eat the coconuts 2 - look for better stuff inland, they'll surely be more")

if (d2 == "1"):
  senseCount += 1
  print ("You manage to grab a coconut off a particularly short tree, ")
  d2a = input("Do you want to head inland in search of water? y/n")
  if d2a == "y":
    print()
    print("You head inland, crashing through the thick undergrowth, suffering many smalls cuts and scrapes. It eventually pays off. The jungle disappears to reveal an idyllic clearing, which contained trees with delicious-looking fruit line it, a clear pool fed by a small stream, and the ruins of a ramshackle lean-to. You gorge yourself on the fruit and water.")
  elif d2a == "n":
    print()
    print("While your hunger and thirst are sated by the coconuts, you feel yourself gradually become more and more disheartened as one by one, the coconuts are eventually consumed. Delirious from dehydration, you head inland, crashing through the thick undergrowth, you suffer many smalls cuts and scrapes, but it pays off. The jungle clears to reveal an idyllic clearing, with several trees with delicious-looking fruit, a clear pool with a river flowing into it, and the ruins of a small lean-to. You gorge yourself on the water and fruit.")
elif (d2 == "2"):
  intuitCount += 1
  print()
  print ("you head inland, crashing through the thick undergrowth, you suffer many smalls cuts and scrapes, but it pays off. The jungle clears to reveal an idyllic clearing, with several trees with delicious-looking fruit, a clear pool with a river flowing into it, and the ruins of a small shelter. You gorge yourself on the water and fruit.") 

print()

d3 = input("What would you like to do with the shelter? 1 - Repair the shelter 2 - Build a newer, better one from the materials.")
if d3 == "1":
  senseCount += 1
  print()
  print("You repair the shelter in a matter of a week, and enjoy your new home.")
elif d3 == "2":
  intuitCount += 1
  print()
  print ("Over the next four weeks, you build your new home. While it may not be the prettiest shelter, your new shelter is certainly different from the ruins of the old one. Whether that is positive remains to be seen.")
  
print("After finishing your shelter, you have a lot of free time. How do you spend it?")
print()
freetime = int(input("1 - building new tools 2 - researching the properties of the local plants"))
if freetime == 1:
  senseCount += 1 
  tools += 1
  print("Work becomes easier with your new tools, and you have much more free time as a result.")
elif freetime == 2:
  intuitCount += 1
  research += 1
  print("With your new research, you discover how to cultivate several tubers and legumes and start your own farm. Food is common.")
  


# Chapter One
time.sleep(5)
print()
print("Chapter One - The One Who Walks Towards Omelas")
print()


# Human Interlude

print("One night, as you lie on the sand resting, in the distance you think see a dark shape as you drift to bed. The next morning, you wake to see another island, miraculously right next to yours. On the beach across from you, separated by a mere twenty feet of water, stands a ragtag bunch of people, waving vigorously")
t1 = input("What do you think of people? 1 - Oh no! 2 - I love people")
if t1 == "1":
  introCount += 1 
elif t1 == "2":
  extraCount += 1 

# The One Who Walks Towards Omelas

print("Their leader moves forward, a heavy-set man in ragged yellow robes. 'Hello!,' he cries")
time.sleep(.35)
print("I am Omelas! It is nice to meet you fellow wanderer.")
time.sleep(.35)
print("Would you care to join us on my island? We've been hoping to meet you.")
print()
d4 = input("How do you respond to this? 1 - (warily) What do you mean? 2 - (openly) Hello Omelas, I'd love to join you!")

print()

if d4 == "1":
  judgeCount += 1 
  introCount += 1 
  print("Worry not stranger! We mean you no harm. We only have need of an outsider as yourself to stand as a Judge.")
elif d4 == "2": 
  print("You wade over to the other island and Omelas greets you with a warm embrace. 'Welcome Judge,' what may we call you? " + "'" + name + ".' " + "You reply.")
  print("It is an honor to meet you Judge " + name + ".")
  time.sleep(.35)
  print("'What do you mean by Judge, Omelas?' you ask.")
  time.sleep(.35)
  print("'You're a Judge. Only an Outsider can lay judgement when such a crime has been committed, and the universe has sent you to us")
  time.sleep(.35)
print()
d5 = int(input("How do you respond? 1 - Very well. I am prepared. 2 - It will be a pleasure to serve, I will hear the facts and decide. 3 - No. I decline. It is not my place."))
while d5 <= 3:
  if d5 == 1:
   judgeCount += 1
   print("'Thank you, Judge " + name + ", it is an honor to have you here.'")
   print()
   time.sleep(.35)
   print("He leads you onto a well-concealed path in the jungle")
  elif d5 == 2:
    perceptCount += 1 
    extraCount += 1
    print("Thank you Judge " + name + ", but it is unusual that a Judge be so exuberant in their desire to judge, but who am I to do so. Follow me.")
    print()
    print("He leads you onto a well-concealed path in the jungle")
    print()
  elif d5 == 3:
    introCount += 1 
    break
  print()
  print("After ten minutes of walking, you come upon a cleared space housing a bustling village. Houses made of thatch and clay stand as people are working with joy. You walk by some children who, instead of working, are seemingly caught up in some game.")
  print()
  print("'What do you think of the children's game, Judge' Omelas asks?")
  t2 = int(input("What do you think? 1 - They should make themselves more useful. 2 - It's good that they have time to indulge their childhood fantasies."))
  print()
  if t2 == 1:
    senseCount += 1
  elif t2 == 2:
    intuitCount += 1 
  print("'A fair point Judge, a fair point.'")
  print()
  print("He guides you to a large round building at the center of the village, where a large hole in the ceiling lets a thin line of fire-smoke out.")
  print()
  print("He turns 'This is the Hall of Judgement, inside you will find your trial. I am forbidden from entering the sanctum. Only you, the accused, and the Forbidden One may set foot there.'")
  print()
  print("'I wish you common sense in your dealings.'")
  print()
  t3 = int(input("How do you respond? 1 - It never leads us astray 2 - I find common sense should be questioned."))
  print()
  if t3 == 1:
    senseCount += 1 
  elif t3 == 2:
    intuitCount += 1
  time.sleep(.35)
  print("'Wisely said, my Judge.'")
  time.sleep(.35)
  print("'Tell me Judge, would you rather be known as a logical or sentimental person in our annals?'")
  ls1 = int(input("1 - logical 2 - sentimental"))
  if ls1 == 1:
    thinkCount += 1
  elif ls1 == 2:
    feelCount += 1
  print("'I shall mark it so in our annals. But enough of these serious questions, tell me, are you a cat or dog person?")
  fave = input("cat/dog")
  print("'A wise choice indeed. I wish you such good Judgement inside the Hall.'")
  time.sleep(.35)
  print()
  print("You walk up the ancient steps to the hulking building. A large flame burns on the inside, and you see figures. As you approach, they become clear. A large man, fearfully sobbing with bloodied hands, a small man with a wry smile on his face, and a single chained child, stunted and deformed.")
  print()
  t4 = int(input("Any judgements already? 1 - It must be the big man 2 - It must be the little man 3 - I cannot judge at this moment."))
  time.sleep(.35)
  if t4 == 1:
    perceptCount += 3
    feelCount += 1
    print()
    print("The big man breaks down as the child begins to laugh, a clap of tombstones cracking open on a cold night. The chains fall off the child and clasp themselves around the big man. The small man started laughing and turns to you. 'The Judgement is cast, Judge.' The child stands on legs thin as bone. 'So it goes' it intones, and motions for you to leave. ")
    print()
  elif t4 == 2:
    perceptCount += 3
    feelCount += 1
    print()
    print("The small man's smirk flies as the child begins to laugh, a clap of tombstones cracking open on a cold night. The chains fall off the child and clasp themselves around the small man. The big man stops sobbing and turns to you, throwing himself at your feet 'Thank you Judge!' The child stands on legs thin as bone. 'So it goes' it intones, and motions for you to leave.")
    print()
  elif t4 == 3:
    time.sleep(.35)
    judgeCount += 1
    thinkCount += 1
    print()
    print("The child intones in a voice of granite,deep and old, 'One of these men have sinned. You may pardon them or doom them. The guilty one will take my place in chains.' ")
    print()
    time.sleep(.35)
    t5 = int(input("1 - Why are you chained? This is all wrong. 2 - The small man did it. 3 - The big man did it. 4 - You are unholy, child. Remain where you are."))
    print()
    if t5 == 1:
      thinkCount += 1
      time.sleep(.35)
      print("The child grimaces 'I am here that the others shall not be. That their joy shall be in opposition to my misery. The basis of their prosperity is my misery. Answer now, or be trapped in my place, Judge.'")
      print()
      time.sleep(.35)
      judgement = int(input("I understand my choice. 1 - The Big Man 2 - The Small Man 3 - You Shall Remain 4 - All Shall be Free"))
      print()
      time.sleep(.35)
      if judgement == 1:
        print("The big man breaks down as the child begins to laugh, a clap of tombstones cracking open on a cold night. The chains fall off the child and clasp themselves around the big man. The small man started laughing and turns to you. 'The Judgement is cast, Judge.' The child stands on legs thin as bone. 'So it goes' it intones, and motions for you to leave. ")
      elif judgement == 2:
        print("The small man's smirk flies as the child begins to laugh, a clap of tombstones cracking open on a cold night. The chains fall off the child and clasp themselves around the small man. The big man stops sobbing and turns to you, throwing himself at your feet 'Thank you Judge!' The child stands on legs thin as bone. 'So it goes' it intones, and motions for you to leave.")
      elif judgement == 3:
        print("The child shrieks as the chains rattle around it, wracking its weak body with spasms of agony. The big man and small man, stunned, stand and leave the room, leaving you alone with the tortured child.perceptCount += 1")
      elif judgement == 4:
        feelCount += 1
        time.sleep(.35)
        print("The chains shatter in front of you, and thunder rolls in the distance.")
        time.sleep(.35)
        print("Omelas runs in,'You fool, you have doomed us all! Begone from this place accursed Judge! I name you our doom, I name you " + name + ".'") 
        time.sleep(.35)
        print("'Leave here and never return!' ")
        time.sleep(.35)
    elif t5 == 2:
      perceptCount += 1
      print("The small man's smirk flies as the child begins to laugh, a clap of tombstones cracking open on a cold night. The chains fall off the child and clasp themselves around the small man. The big man stops sobbing and turns to you, throwing himself at your feet 'Thank you Judge!' The child stands on legs thin as bone. 'So it goes' it intones, and motions for you to leave.")
      print()
    elif t5 == 3:
      perceptCount += 1
      print("The big man breaks down as the child begins to laugh, a clap of tombstones cracking open on a cold night. The chains fall off the child and clasp themselves around the big man. The small man started laughing and turns to you. 'The Judgement is cast, Judge.' The child stands on legs thin as bone. 'So it goes' it intones, and motions for you to leave. ")
      print()
    elif t5 == 4:
      perceptCount += 1
      time.sleep(.35)
      print("The child shrieks as the chains rattle around it, wracking its weak body with spasms of agony. The big man and small man, stunned, stand and leave the room, leaving you alone with the tortured child. Finally, you walk out, the child's screams behind you")
      perceptCount += 1
      print()
  time.sleep(.35)
  print("Omelas waits. 'I pray this is the last time we meet, at least in your lifetime.'") 
  break


time.sleep(.35)
print("You walk away from Omelas. By the next morning, the island of Omelas is but a smudge on the horizon, if that.")
time.sleep(.75)

  
# Epilogue

print()
print("Chapter Two: Epilogue")
print()
time.sleep(.35)

advantage = "shelter"
if tools == 1:
  advantage = "equipment"
elif research == 1:
  advantage = "farm"
print("Life is uneventful on your island, as your " + advantage + " makes your life easy.")

print("You come across an ancient turtle, stranded on the beach.")
turtle = int(input("What do you do with the turtle? 1 - kill it for food 2 - place it back in the water"))
time.sleep(.35)
if turtle == 1:
  thinkCount += 1 
  print("You enjoy the warm meat for dinner that night.")
elif turtle == 2:
  feelCount += 1 
  print("The turtle floats off into the reefs.")
  
print("Years go by, hair greys, lines mar your skin, and your legs don't work like they used to before.")
print()
time.sleep(1)

print("One day, when you go on your morning walk. Something has changed.")
time.sleep(1)
print()
print("There is something on the beach")
time.sleep(1)
print()
print("A ship")
print()
time.sleep(1)
print()
print("With people on it, preparing to leave.")
print()
time.sleep(1)
print("Do you join them?")
final = input("y/n")
if final == "y":
  print("You run up to the boat, shouting at them, just as they are about to leave.")
  time.sleep(1)
  print("They do not understand your language.")
  time.sleep(1)
  print("But they stop and let you board.")
  time.sleep(1)
  extraCount += 1 
  if turtle == 1:
    print("Mere days after joining the ship, you have yet to learn the language when a terrible storm takes the ship. The mast splits in two, trapping you beneath it as the ship sinks.")
    time.sleep(1)
    print("As you sink beneath the waves, you see an empty sea turtle shell, floating on the water above you as everything...")
    print()
    print()
    print()
    print()
    print()
    time.sleep(1)
    print("blackness")
  if turtle == 2:
    print("You rejoin humanity. They take you on their boat to their homeland. Along the way, you learn their language and forget the island. You live there, get married, and are much beloved. Decades after your arrival, you lie in your bed, sick, coughing. You finally sleep. In your dreams, you remember your island, Omelas, and the stranded sea turtle you saved. ")
    time.sleep(1)
    print()
    print()
    print()
    print()
    print("You pass peacefully.")
if final == "n":
  introCount += 1 
  if turtle == 1:
    print("Mere days after the ship leaves, a terrible storm strikes your island. Lightning strikes all around as you cower in your shelter. A tree is knocked over, falling onto your small shelter, and falling down onto you, smashing you, breaking bones until...")
    time.sleep(1)
    print()
    print()
    print()
    print()
    print("blackness")
    
  if turtle == 2:
    print("After watching the boat sail away, you spend your days on that island, enjoying the fruits of your labors. Soon, a " + fave + " washes up on the shores. You name it")
    pet = input("What do you name it?")
    print("You and " + pet + " spend many happy years together.")
    time.sleep(1)
    print()
    print("One night you go to sleep, and dream of swimming in the shimmering sea, far past the reefs, until you swim next to the stranded sea turtle you saved.")
    time.sleep(1)
    print()
    print("You pass peacefully that night.")
    print()
    print()
    print()
    print()
    print()


  
#Final Calculations
if introCount > extraCount:
  (IE) = "I"
elif extraCount > introCount:
  (IE) = "E"

if senseCount > intuitCount:
  (SN) = "S"
elif intuitCount > senseCount:
  (SN) = "N"
  
if thinkCount > feelCount:
  (TF) = "T"
elif feelCount > thinkCount:
  (TF) = "F"
  
if judgeCount > perceptCount:
  (JP) = "J"
elif perceptCount > judgeCount:
  (JP) = "P"
  
print("Your Myers-Briggs personality type, out of introverted/extraverted, sensing/intuitive, thinking/feeling, and judging/perceiving, is ")
print("Calculating...")
time.sleep(1.5)
print((IE) + (SN) + (TF) + (JP))

print("Go to bit.ly/WanderSeaTest to find a description of your Myers-Briggs type, and to take a more in-depth, if less interesting version of the test. If you have more than four letters, one trait was not more dominant than the other in this playthrough.")

input("Enter Continue to Finish")

# Final Credits
time.sleep(.5)
print()
print()
print()
print("Writer: Gus Kmetz")
print()
print()
time.sleep(1.5)
print("Editor: Camillo Saueressig")
print()
print()
time.sleep(1.5)
print("Heartfelt thanks to my CS Mentor, Andrew Duca")
print()
print()
time.sleep(1.5)
print("Special thanks to Hack@Brown for making this possible")
print()
print()
time.sleep(1.5)
print("Thanks to Hack@Brown's sponsors: Google, pMD, Bracket, Lightstep, Facebook, Stripe, TaptoBook, and Upserve")
print()
print()
time.sleep(1.5)
print("and most importantly, thank you " + name)
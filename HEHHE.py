print("You are stranded on a island")
print("Press a to jump off a cliff")
print("Press b to drink sea water")
print("Press c to search for coconuts")
user_choice = input()
if user_choice == "a" :
    print("You found a cliff")
    print("Do you wish to jump off the cliff? (a/b)")
    user_choice = input()
    if user_choice == "a" :
        print ("You decided not to jump off the cliff and survived")
    elif user_choice == "b" :
        print("You jumped off the cliff and DIED!")
elif user_choice == "b" :
    print("You found a beach")
    print("Do you wish to drink the seawater (y/n)")
    user_choice = input()
    if user_choice == "y" :
        print ("You drank from the sea and you survived!")
    elif user_choice == "n" :
        print("You DIED of dehydration")
elif user_choice == "c" :    
    print("You found a coconut tree")
    print("Do you wish to climb it? (a/b)")
    user_choice = input()
    if user_choice == "a" :
        print ("You climbed up the tree, and you fell, so you DIED!")
    elif user_choice == "b" :
        print("You decided not climb the tree, but then...!")
    print("A coconut fell on your head and you DIED!")
print("Press a if you died")
print("Press b if you survived and want to look for food")
print("Press c to quit")
user_choice = input()
if user_choice == "a" :
    print("You DIED")
    print("Do you wish to Revive?(a/b)")
    user_choice = input()
    if user_choice == "a" :
        print ("You revived... Then you died of hunger and thirst")
    elif user_choice == "b" :
        print("You DIED!")
elif user_choice == "b" :
    print("You found a dead lizard")
    print("Do you wish to eat the lizard (y/n)")
    user_choice = input()
    if user_choice == "y" :
        print ("You roast the lizard over a blazing fire and ate it...")
        print ("You ate the lizard and barley survived.")
    elif user_choice == "n" :
        print("You DIED of hunger")
elif user_choice == "c" :    
    print("You Quit!")
print("Press a if you died")
print("Press b if you want to search the island")
print("Press c to quit")
user_choice = input()
if user_choice == "a" :
    print("You DIED")
    print("Do you wish to Revive?(a/b)")
    user_choice = input()
    if user_choice == "a" :
        print ("You revived... Then you DIED")
    elif user_choice == "b" :
        print("You DIED!")
elif user_choice == "b" :
    print("You found a helicopter")
    print("Do you wish to get in? (y/n)")
    user_choice = input()
    if user_choice == "y" :
        print ("You went in the helicopter... ")
        print ("You then flew home with the help of other people! YOU SURVIVED!")
    elif user_choice == "n" :
        print("You DIED because the helicopter blew up!")
elif user_choice == "c" :    
    print("You Quit!")

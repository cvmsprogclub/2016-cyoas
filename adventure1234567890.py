print("You are stranded on a island")
print("press a to climb a tree")
print("press b to start swimming")
print("press c to scope the island")
print("press d to drink coconut water")
user_choice = input()
if user_choice == "c" :
    print("you scope the island")
    print("you find flint")
    print("Do you want to pick up the flint and use it? (y/n)")
    user_choice = input()
    if user_choice == "n":
        print("you die of hypothermia")
    elif user_choice == "y":
     print("You survive the night")
     print("you wake up and see smoke you think it is the airplane but then you hear some one yell help")
     print("do you go and help this person? (y/n)")
    user_choice = input()
    if user_choice == "n":
        print("You here a person die of the heat")
        print("you feel guilty and kill yourself by jumping into the fire you had from the previous night")
    elif user_choice == "y":
        print("You go and find your childhood friend Jim Bob Cooter")
        print("he starts acting like a savage")
        print("You try and help him")
        print("HE KILLS YOU!!!!!")
elif user_choice == "b" :
    print("you start swimming")
    print("You are surrounded by sharks")
    print("Do you want to ride a shark? (y/n)")
    user_choice = input()
    if  user_choice == "y":
        print("You get bucked of and die")
    elif user_choice == "n":
        print("You die while trying to escape")
elif user_choice == "a" :
    print("you climb a tree")
    print("you see pinapples at the top")
    print("Do you wish to drop the pinapples on the ground? (y/n)")
    user_choice = input()
    if user_choice == "y":
        print("You lose your balance and fall off the tree and die")
    elif user_choice == "n":
        print("you slide down the tree and think about what to do")
        print("You see a pinapple on the ground")
        print("Do you wish to eat it? (y/n)")
        user_choice = input()
        if user_choice == "y":
            print("Oh no it was a rotten pinapple")
            print("You die of food poisoning")
        elif user_choice == "n":
            print("You use the pinapple as a trap")
            print("You capture a turtle")
            print("Do you want to eat the turtle? (y/n)")
            user_choice = input()
            if user_choice == "y":
                print("You die of food posioning initially from the pinapple")
            elif user_choice == "n":
                print("you put the turtle in the ocean doget on it? (y/n)?")
            user_choice = input()
            if user_choice == "y":
                print("you are two heavy and drown you die")
            elif user_choice == "n":
                print("You kill yourself because you did not get on the turtle")
elif user_choice == "d" :
    print("you drink coconut water")
    print("Do you want to run now? (y/n)", end=' ')
    user_choice = input()
    if user_choice == "n":
        print("you die of nothing to do")
    elif user_choice == "y":
        print("you find a crashed burning airplane")
        print("Do you run into the airplane? (y/n)", end=' ')
        user_choice = input()
        if user_choice == "y":
            print("You die of the heat")
        elif user_choice == "n":
            print("You survive Yay!!!!")
            print("you see a parachute")
            print("do you try to fly with the parachute? (y/n)")
            user_choice = input()
            if user_choice == "y":
                print("You get in the air but lose your grip on the parachute then fall into the burning plane")
            elif user_choice == "n":
                print("You use the parachute as a fishing net")
                print("You catch five fish")
                print("You go back to the burning airplane to cook them")
                print("you see a flare gun do you pick it up? (y/n)")
            user_choice = input()
            if user_choice == "n":
                print("you see a helicopter pass by and you kill yourself because you didn't pick up")
            elif user_choice == "y":
                print("you take the flare gun back to your campsite")
                print("do you shoot the flare gun? (y/n)")
            user_choice = input()
            if user_choice == "y":
                print("You kill yourself because you relize you only had one shot")
            elif user_choice == "n":
                print("you save your shot")
                print("you figure out you only have one shot")
                print("when you wake up you hear and see a helicopter")
                print("You shoot your flare gun and the helicopter comes down")
                print("Do you get on? (y/n)")
            user_choice = input()
            if user_choice == "n":
                print("you kill your self because you didn't get on the helicopter")
            elif user_choice == "y":
                print("you get on the helicopter and leave the island")
                print("YOU WIN")
                

                
            
            
    





      

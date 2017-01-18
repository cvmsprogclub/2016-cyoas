score = 0
print("THIS IS A FIVE QUESTION MULTIPULE CHOICE QUIZ. YOUR GRADE WILL BE PRINTED AT THE END OF THE QUIZ, AS WELL AS A COMMENT. TEST VERSION 1.1.1")
print()
user = input("START THE TEST?")
if user == "Yes":
    print("QUESTION 1: WHICH OF THE AIRCRAFT ARE MADE OUT OF COMPOSITE MATERIALS?")
    print("A: Boeing 777")
    print("B: Boeing 737 MAX")
    print("C: Boeing 747-8")
    print("D: None of the above.")
    user = input()
    prompt = True
    while prompt is True:
        if user == "A" :
                print("YOU ARE SOOOOOOOO DUMB!")
                print("The answer is D.")
                score = score + 0
        elif user == "B" :
                print("YOU ARE SOOOOOOOO DUMB!")
                print("The answer is D.")
                score = score + 0
        elif user == "C" :
                print("YOU ARE SOOOOOOOO DUMB!")
                print("The answer is D.")
                score = score + 0
        elif user == "D" :
                print("GOOD JOB!")
                score = score + 1
        else:
                print("NOOOOO, WHAT ARE YOU DOING!")
                score = score - 1
        print()
        print("QUESTION 2: WHICH OF THESE FLAPS ARE ABLE TO TILT UPWARDS?")
        print("A: FOWLER FLAPS")
        print("B: ZAP FLAPS")
        print("C: FAIREY-YOUNGMAN FLAPS")
        print("D: GURNEY FLAPS")
        user = input()
        if user == "A" :
                print("YOU ARE SOOOOOOOO DUMB!")
                print("The answer is C.")
                score = score + 0
        elif user == "B" :
                print("YOU ARE SOOOOOOOO DUMB!")
                print("The answer is C")
                score = score + 0
        elif user == "C" :
                print("GOOD JOB!")
                score = score + 1
        elif user == "D" :
                print("YOU ARE SOOOOOOOO DUMB!")
                print("The answer is C")
                score = score + 0
        else : 
                print("NOOOOO, WHAT ARE YOU DOING!")
                score = score - 1
        print()
        print("QUESTION 3: WHICH FLIGHT SUCCESSFULLY DITCHED IN THE HUDSON RIVER?")
        print("A: US AIRWAYS FLIGHT 1559")
        print("B: US AIRWAYS FLIGHT 1549")
        print("C: SCANDIVADIAN FLIGHT 751")
        print("D: NONE OF THE ABOVE")
        user = input()
        if user == "A" :
                print("YOU ARE SOOOOOOOO DUMB!")
                print("The answer is B.")
                score = score + 0
        elif user == "B" :
                print("GOOD JOB!")
                score = score + 1
        elif user == "C" :
                print("YOU ARE SOOOOOOOO DUMB!")
                print("The answer is B")
                score = score + 0
        elif user == "D" :
                print("YOU ARE SOOOOOOOO DUMB!")
                print("The answer is B")
                score = score + 0
        else : 
                print("NOOOOO, WHAT ARE YOU DOING!")
                score = score - 1
        print()
        print("QUESTION 4: WHICH THRUST REVERSER TYPE IS USED ON THE BOMBARDIER CRJ SERIES?")
        user = input()
        if user == "Target" :
                print("GOOD JOB!")
                score = score + 1
        else :
                print("YOU ARE SOOOOOOOO DUMB!")
                print("THE ANSWER IS: Target")
                score = score + 0
        print()
        print("QUESTION 5: THE AIRBUS A320 SERIES HAVE A _______ WINGLET")
        user = input()
        if user == "blended" :
                print("GOOD JOB!")
                score = score + 1
        else :
                print("YOU ARE SOOOOOOOO DUMB!")
                print("THE ANSWER IS: blended")
                score = score + 0
        score = score * 20
        strScore = str(score)
        print("YOU GRADE IS " + strScore + " %")
        if score == 100 :
                print("GOOD JOB!")
        elif score <= 60 and score > 0:
                print("TRY AGAIN, DUMMY")
        elif score <= 0 :
                print("YOU'RE SCUM TIER!")
        else :
                print("AT LEAST YOU TRIED")
        print("RETAKE?")
        user_now = input()
        if user_now == "Yes":
            prompt = True
        else:
            print("VISIT www.xkcd.com NOW!!!!!")
            quit()
else:
    print("VISIT www.xkcd.com NOW!!!!!")
    quit()

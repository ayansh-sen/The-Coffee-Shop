#init
import time
import random
wait_time = 0
customername = 0
coffee = 0
base = 0
water = 0
milk = 0
sweetener = 0
valuation = 0
name = 0
npcnames = [
    "Shrek", "Robert", "Mary", "Michael", "Patrik", "John", "Unc", "David", "Abel", "Mr.Testfire", "William", "Richard", "Fiona", "Joseph", "Jessica", "Hari", "Stephanie", "Brotato", "Sir Bartholomew the Third, Guardian of the Left Shoe", "Gabriel the Great Ruler of Stolen Dior Sunglasses" 
]

cofenames = [
    "Espresso", "Americano", "Latte", "Cappuccino", "Mocha", "Cortado", "Affogato", "Filter Coffee", "Cold brew", 
]
#intro
print ("    ")
print ("    ")
                                                                 
                                                                 
print (" _____ _          _____     ___ ___            _____ _           ")
print ("|_   _| |_ ___   |     |___|  _|  _|___ ___   |   __| |_ ___ ___ ")
print ("  | | |   | -_|  |   --| . |  _|  _| -_| -_|  |__   |   | . | . |")
print ("  |_| |_|_|___|  |_____|___|_| |_| |___|___|  |_____|_|_|___|  _|")
print ("                                                            |_|  ")
                                                                 
#brief
time.sleep(2)
print ("    ")
print ("    ")
print ("    ")
print ("    ")
print ("    ")

print ("𝐎𝐛𝐣𝐞𝐜𝐭𝐢𝐯𝐞- To expand your small coffee shop and make $100! Keep your customers happy and satisfied- they shouldn't get a chance to complain!")
time.sleep(3.5)
print ("    ")
print ("Customers will come to your shop often, make sure to make their coffee properly, and you'll do great!")
time.sleep(3)
print ("    ")
print ("    ")
print ("Good luck!")
name = input("Enter your name: ")
time.sleep(2)

#game start
while valuation < 100:
    print ("    ")
    print ("    ")
    print ("    ")
    print ("    ")
    print ("    ")
    print ("𝘞𝘢𝘪𝘵𝘪𝘯𝘨 𝘧𝘰𝘳 𝘊𝘶𝘴𝘵𝘰𝘮𝘦𝘳")
    customername = random.choice(npcnames)
    wait_time = random.randint(1,10)
    coffee = random.choice(cofenames)
    time.sleep(wait_time)
    print ("    ")
    print ("Customer is here!")
    print ("    ")
    print (f"{customername}:   Hello there! My name is {customername}.")
    time.sleep (0.5)
    print (f"You:   Hi {customername}! What kind of coffee would you like?")
    time.sleep(0.5)
    print (f"{customername}:   I would like a {coffee}.")
    time.sleep(1)
    print ("    ")
    print ("    ")
    print ("    ")
    guide = input ("Do you want a guide on how to make coffee? (y/n)")
    if guide == "y":
        print ("There are four main ingredients of coffee-")
        time.sleep(1)
        print ("i) Base")
        time.sleep(1)
        print ("ii) Water")
        time.sleep(1)
        print ("iii) Milk")
        time.sleep(1)
        print ("iv) Sweetener")
        time.sleep(1)
        print ("   ")
        print ("These can be put in various quanities to make different kinds of coffee! (remember these quantites!)")
        time.sleep(1)
        print (f"For instance, the coffee you got an order for ({coffee}) can be made like this!-")

    #details of coffee
        time.sleep(1)
        if coffee == "Espresso":
            print ("Base - 10")
            print ("Water - 0")
            print ("Milk - 0")
            print ("Sweetener - 0")

        if coffee == "Americano":
            print ("Base - 3")
            print ("Water - 7")
            print ("Milk - 0")
            print ("Sweetener - 0")

        if coffee == "Latte":
            print ("Base - 2")
            print ("Water - 0")
            print ("Milk - 8")
            print ("Sweetener - 1")

        if coffee == "Cappuccino":
            print ("Base - 4")
            print ("Water - 0")
            print ("Milk - 6")
            print ("Sweetener - 0")

        if coffee == "Mocha":
            print ("Base - 3")
            print ("Water - 0")
            print ("Milk - 5")
            print ("Sweetener - 2")

        if coffee == "Cortado":
            print ("Base - 5")
            print ("Water - 0")
            print ("Milk - 5")
            print ("Sweetener - 0")

        if coffee == "Affogato":
            print ("Base - 6")
            print ("Water - 0")
            print ("Milk - 0")
            print ("Sweetener - 4")

        if coffee == "Filter Coffee":
            print ("Base - 5")
            print ("Water - 5")
            print ("Milk - 0")
            print ("Sweetener - 0")

        if coffee == "Cold brew":
            print ("Base - 8")
            print ("Water - 2")
            print ("Milk - 0")
            print ("Sweetener - 0")
    else:
        print ("Okay! No tutorial for you.")

    print ("Now, you make the coffee!")
    time.sleep(1)
    base = int(input("How much base? "))
    water = int(input("How much water? "))
    milk = int(input("How much milk? "))
    sweetener = int(input("How much sweetener? "))
    time.sleep(1)
    print ("You:   Coffee done!")
    time.sleep(0.5)
    print (f"{customername}:   *𝘨𝘳𝘢𝘣𝘴 𝘤𝘰𝘧𝘧𝘦𝘦*")
    time.sleep(1)

    #coffee check!
    if coffee == "Espresso" and base == 10 and water == 0 and milk == 0 and sweetener == 0:
        print(f"{customername}: This Espresso is perfect!")
        print(f"{customername}: Here is your payment. *𝘩𝘢𝘯𝘥𝘴 𝘰𝘷𝘦𝘳 𝘤𝘢𝘴𝘩*")
        valuation +=5
        print (f"𝐁𝐚𝐧𝐤 𝐁𝐚𝐥𝐚𝐧𝐜𝐞- ${valuation}")

    elif coffee == "Americano" and base == 3 and water == 7 and milk == 0 and sweetener == 0:
        print(f"{customername}: Great Americano!")
        print(f"{customername}: Here is your payment. *𝘩𝘢𝘯𝘥𝘴 𝘰𝘷𝘦𝘳 𝘤𝘢𝘴𝘩*")
        valuation +=6
        print (f"𝐁𝐚𝐧𝐤 𝐁𝐚𝐥𝐚𝐧𝐜𝐞- ${valuation}")

    elif coffee == "Latte" and base == 2 and water == 0 and milk == 8 and sweetener == 1:
        print(f"{customername}: This Latte is so creamy!")
        print(f"{customername}: Here is your payment. *𝘩𝘢𝘯𝘥𝘴 𝘰𝘷𝘦𝘳 𝘤𝘢𝘴𝘩*")
        valuation +=7
        print (f"𝐁𝐚𝐧𝐤 𝐁𝐚𝐥𝐚𝐧𝐜𝐞- ${valuation}")

    elif coffee == "Cappuccino" and base == 4 and water == 0 and milk == 6 and sweetener == 0:
        print(f"{customername}: Love this Cappuccino!")
        print(f"{customername}: Here is your payment. *𝘩𝘢𝘯𝘥𝘴 𝘰𝘷𝘦𝘳 𝘤𝘢𝘴𝘩*")
        valuation +=6.75
        print (f"𝐁𝐚𝐧𝐤 𝐁𝐚𝐥𝐚𝐧𝐜𝐞- ${valuation}")

    elif coffee == "Mocha" and base == 3 and water == 0 and milk == 5 and sweetener == 2:
        print(f"{customername}: Mmm, chocolatey Mocha!")
        print(f"{customername}: Here is your payment. *𝘩𝘢𝘯𝘥𝘴 𝘰𝘷𝘦𝘳 𝘤𝘢𝘴𝘩*")
        valuation +=8
        print (f"𝐁𝐚𝐧𝐤 𝐁𝐚𝐥𝐚𝐧𝐜𝐞- ${valuation}")

    elif coffee == "Cortado" and base == 5 and water == 0 and milk == 5 and sweetener == 0:
        print(f"{customername}: A perfect Cortado split!")
        print(f"{customername}: Here is your payment. *𝘩𝘢𝘯𝘥𝘴 𝘰𝘷𝘦𝘳 𝘤𝘢𝘴𝘩*")
        valuation +=6.5
        print (f"𝐁𝐚𝐧𝐤 𝐁𝐚𝐥𝐚𝐧𝐜𝐞- ${valuation}")

    elif coffee == "Affogato" and base == 6 and water == 0 and milk == 0 and sweetener == 4:
        print(f"{customername}: This Affogato is a delicious dessert!")
        print(f"{customername}: Here is your payment. *𝘩𝘢𝘯𝘥𝘴 𝘰𝘷𝘦𝘳 𝘤𝘢𝘴𝘩*")
        valuation +=9
        print (f"𝐁𝐚𝐧𝐤 𝐁𝐚𝐥𝐚𝐧𝐜𝐞- ${valuation}")

    elif coffee == "Filter Coffee" and base == 5 and water == 5 and milk == 0 and sweetener == 0:
        print(f"{customername}: A very reliable Filter Coffee!")
        print(f"{customername}: Here is your payment. *𝘩𝘢𝘯𝘥𝘴 𝘰𝘷𝘦𝘳 𝘤𝘢𝘴𝘩*")
        valuation +=5.5
        print (f"𝐁𝐚𝐧𝐤 𝐁𝐚𝐥𝐚𝐧𝐜𝐞- ${valuation}")

    elif coffee == "Cold brew" and base == 8 and water == 2 and milk == 0 and sweetener == 0:
        print(f"{customername}: So refreshing! Great Cold brew.")
        print(f"{customername}: Here is your payment. *𝘩𝘢𝘯𝘥𝘴 𝘰𝘷𝘦𝘳 𝘤𝘢𝘴𝘩*")
        valuation +=7.5
        print (f"𝐁𝐚𝐧𝐤 𝐁𝐚𝐥𝐚𝐧𝐜𝐞- ${valuation}")

    #Ur coffee tastes worse than shrek
    else:
        print(f"{customername}: Yuck! This isn't how you make a {coffee}!")
        print(f"{customername}: Im not paying for this!")
        valuation -=3
        print (f"𝐁𝐚𝐧𝐤 𝐁𝐚𝐥𝐚𝐧𝐜𝐞- ${valuation}")

time.sleep(2)
print ("Congratulations! You made $100 and expanded your coffee shop!") 

#Dramatic ending
print("     ")
print("     ")
print("     ")
print("     ")
print("     ")
print("     ")
print("     ")
print("     ")
print("     ")
print("     ")

time.sleep(4)
print("╔══════════════════════════════════════════════════════════════════════════╗")
print("║                                                                          ║")
print("║           The sound of a car echoes through your quiet shop...           ║")
print("║                                                                          ║")
print("╚══════════════════════════════════════════════════════════════════════════╝")
time.sleep(2)
print ("    ")
print ("    ")
print ("    ")
print ("A sleek black limousine pulls up outside your coffee shop.")
time.sleep(2)
print ("    ")
print ("    ")
print("The door opens, and out steps a figure in a tailored suit, radiating power.")
ceo_name = random.choice(["Mr. Nyx", "Blair Cross", "Victor Thorne"])
print (f"{ceo_name}:  (Smiling warmly) Congratulations, {name}. I've heard of your dedication and skill towards your craft.")
time.sleep(2)
print ("You:  Uh... Who are you? And how do you know my name?")
time.sleep(1)
print (f"{ceo_name}: (Extending a hand) I'm {ceo_name}, CEO of-")
print ("   ____ _       _           _   ____                      _   _       _     _ _                 ")
print ("  / ___| | ___ | |__   __ _| | | __ ) _ __ _____      __ | | | | ___ | | __| (_)_ __   __ _ ___ ")
print (" | |  _| |/ _ \| '_ \ / _` | | |  _ \| '__/ _ \ \ /\ / / | |_| |/ _ \| |/ _` | | '_ \ / _` / __|")
print (" | |_| | | (_) | |_| | (_| | | | |_) | | |  __/\ V  V /  |  _  | (_) | | (_| | | | | | |_| \__ |")
print ("  \____|_|\___/|_.__/ \__,_|_| |____/|_|  \___| \_/\_/   |_| |_|\___/|_|\__,_|_|_| |_|\__, |___/")
print ("                                                                                      |___/     ")
time.sleep(3)
print ("    ")
print ("    ")
print(f"{ceo_name}: 'For years, my company has dominated the coffee world. We thought we were untouchable.'")
time.sleep(3)
print ("    ")
print ("    ")
print(f"{ceo_name}: 'But then... you came along. Your passion, your precision... it's revolutionized the industry.'")
time.sleep(3.5)
print ("    ")
print ("    ")
print(f"{ceo_name}: 'I've seen your potential. Your coffee has a magic ours can only dream of.'")
time.sleep(3)
print ("    ")
print ("    ") 
print("He reaches into his inner jacket pocket and pulls out a single, golden key.")
time.sleep(3)
print ("    ")
print ("    ") 
print(f"{ceo_name}: 'So, I've made a decision. I'm retiring. And I'm handing over the reins.'")
time.sleep(3.5)
print ("    ")
print ("    ") 
print("He places the key onto your counter. It gleams under the shop lights.")
time.sleep(2.5)
print ("    ")
print ("    ") 
print(f"{ceo_name}: 'This key opens every door. Every vault. Every office of Global Brew Holdings.'")
time.sleep(3.5)
print ("    ")
print ("    ") 
print(f"{ceo_name}: 'The company... it's yours now. Rule it well.'")
time.sleep(3)
print ("    ")
print ("    ") 
print("He turns, steps back into his limousine, and it silently glides away, disappearing into the sea of other cars.")
time.sleep(4)
print ("    ")
print ("    ") 
print ("    ")
print ("    ") 
print ("    ")
print ("    ") 
print("╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
print("║                                                                                                                 ║")
print("║                                                      The End                                                    ║")
print("║                                                                                                                 ║")
print("╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
time.sleep (6)
print ("    ")
print ("    ") 
print ("    ")
print ("    ") 
print ("    ")
print ("    ") 
print ("    ")
print ("    ") 
print ("    ")
print ("    ") 
print ("    ")
print ("    ") 
print ("    ")
print ("    ") 
print ("    ")
print ("    ") 
print ("    ")
print ("    ") 
print (" _____ _          _____     ___ ___            _____ _           ")
print ("|_   _| |_ ___   |     |___|  _|  _|___ ___   |   __| |_ ___ ___ ")
print ("  | | |   | -_|  |   --| . |  _|  _| -_| -_|  |__   |   | . | . |")
print ("  |_| |_|_|___|  |_____|___|_| |_| |___|___|  |_____|_|_|___|  _|")
print ("                                                            |_|  ")
print ("                                                    by Ayansh Sen")
time.sleep(3)
print ("    ") 
print ("    ")
print ("    ") 
print ("A project initiated out of boredom, quickly turning into one of my favourite games to develop.")
time.sleep(1)
print ("Special thanks to-")
time.sleep(1)
print ("Some of my dearest friends, who I unfortunately cannot name here, for testing and giving feedback on the game.")
time.sleep(1)
print ("My teachers for always standing by me in my never-ending quest to learn and create.")
time.sleep(1)
print ("And most importantly, thank YOU, the player, for taking the time to play my game. It really means a lot to me.")



#Its been a long run 
#wow i need to really take a nap


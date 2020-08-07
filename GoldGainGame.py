from sys import exit
print("-"*60,"THIS IS A STRING GAME..HOPE YOU WILL DO WELL","-"*60)
def gold_room(): 
    print ("This room is full of gold.  How much do you take?") 
    next = input("> ") 
    try:
        how_much = int(next)  
    except TypeError:
        dead("Man, learn to type a number.")
    if how_much < 50:
        dead("Nice, you're not greedy, you win!")
    else: 
        dead("You greedy bastard!")
        
def bear_room():
    print ("There is a bear here.")
    print ("The bear has a bunch of honey." )       
    print ("The fat bear is in front of another door.")        
    print ("How are you going to move the bear?")
    bear_moved = False
       
    while True:
        next = input("*take honey\n*taunt bear\n*open door\n> ")
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.") 
        elif next == "taunt bear" and not bear_moved:
            print ("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        elif next == "open door" and not bear_moved:
            dead("The bear cought you.")
        else:          
            print ("I got no idea what that means.")
        
def cthulhu_room():
    print ("Here you see the great evil Cthulhu.") 
    print ("He, it, whatever stares at you and you go insane.") 
    print ("Do you flee for your life or eat your head?")
    next = input("flee or head\n> ")
    if "flee" in next:           
        start()
    elif "head" in next:
        dead("Well that was tasty!") 
    else:
        cthulhu_room()

def dead(why):
    print (why, "Good job!")      
    a = input("Wanna Start Again?\n*y or *n\n>")
    if a == 'y':
        start()
    else:
        input("Good Bye")
        exit(0)
    
def start():
    print ("You are in a dark room.")
    print ("There is a door to your right and left.")  
    print ("Which one do you take?")
    next = input("left or right\n>")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.") 
start()
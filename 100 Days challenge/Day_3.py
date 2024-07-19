print( """
    Welcome to Treasure Island.
    Your mission is to find the treasure.
    """)
First = input("left or right\n").lower()

if First == "left":
    Second = input("swim or wait\n").lower()
    if Second == "wait":
        Third = input("Red, Blue or Yellow\n").lower()
        if Third == "yellow":
                 print("You Win!!!")  
        else:
                 print("Game Over")   
    else:
        print("Game over")
else:
    print("Game Over")

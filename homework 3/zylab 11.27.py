pdict={}
for i in range(1,6):
    print("Enter player "+str(i)+"'s jersey number:")
    key=int(input())
    print("Enter player "+str(i)+"'s rating:\n")
    value=int(input())
    pdict[key]=value

print("ROSTER")

for i in sorted(pdict):#printing the values in dictionary
    print("Jersey number: "+str(i)+", Rating: "+str(pdict[i]))

print('MENU')

while(1):#menu
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print("\nChoose an option:")
    n=input()#loop control variable

    if(n=="o"):#output the roster
        print("Roster")
        for i in sorted(pdict):
            print("Jersey number: "+str(i)+", Rating: "+str(pdict[i]))

    elif(n=="a"):#adds a new player
        print("Enter a new player's jersey number:")
        key=int(input())
        print("Enter the player's rating:")
        value=int(input())
        pdict[key]=value

    elif(n=="d"):#delete a player
        print("Enter a jersey number:")
        key=int(input())
        pdict.pop(key)

    elif(n=="u"):#updates a player's rating
        print("Enter a jersey number:")
        key=int(input())
        print("Enter a new rating for player:")
        value=int(input())
        pdict[key]=value

    elif(n=="r"):#prints ratings above a particular value
        print("Enter a rating:")
        rating=int(input())
        print("Above "+str(rating))

        for i in sorted(pdict.items(),key=lambda x:x[1],reverse=True):
            if(i[1]>rating):
                print("Jersey number: "+str(i[0])+", Rating: "+str(i[1]))
    else:#exits the program

        exit(0)
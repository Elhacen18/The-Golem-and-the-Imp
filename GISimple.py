
import time
import random 

def GISimple(impSpd=(1,9), golemSpd=(3,5), headStart=5, exitPosition=50):
    #print(impSpd,golemSpd,headStart,exitPosition)
    Tunnel_Distance = exitPosition
    I_current_position = 0
    G_current_position = 0
    second_passed = 0
    i_distance = headStart
    G_distance = 0
    while True:
        G_current_position +=G_distance
        I_current_position += i_distance
        #print(f"G's :{G_current_position}"+f" I's : {I_current_position}")
        if(I_current_position>=Tunnel_Distance) :
            return True
        if(G_current_position>=I_current_position):#if the golem’s position overtakes (>=) the imp’s position beforehand, the imp is captured and its fun ends.
            return False
    
        i_distance = random.randint(impSpd[0],impSpd[-1]) ; 
        G_distance = random.randint(golemSpd[0], golemSpd[-1]) 
        time.sleep(1)
        second_passed= second_passed + 1


while True:
    try:
        impSpd_input = input("Imp min and max speed. ex: 1,9\n")
        impSpd = tuple(map(int, impSpd_input.split(","))) if impSpd_input  else (1,9)
        if impSpd[0] <1 or impSpd[1] > 9:
            print("Please enter valid inputs.")
            continue

        golemSpd_input =  input("Golem min and max speed. ex: 3,5\n")
        golemSpd = tuple(map(int, golemSpd_input.split(","))) if  golemSpd_input else (3,5)
        if golemSpd[0] <3 or golemSpd[1] >5:
            print("Please enter valid inputs.")
            continue

        headStart_input = input("Imp start position. ex: 5\n")
        headStart = int(headStart_input) if headStart_input else 5
        if headStart <0:
            print("Please enter invalid inputs.")
            continue

        exitPosition_input = input("Imp exit position. ex: 50\n")
        exitPosition = int(exitPosition_input) if exitPosition_input else 50
        if exitPosition <0 or exitPosition>50 :
            print("Please enter invalid inputs.")
            continue

        GISimple(impSpd,golemSpd,headStart,exitPosition)
        break
    except ValueError:
        print("Please enter intigers only")
        continue
           


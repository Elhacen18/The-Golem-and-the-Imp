import time
import random 
Tunnel_Distance = 50
I_current_position = 0
G_current_position = 0
second_passed = 0
i_distance = 5
G_distance = 0
x=' '
dash = '-'
tunnel=[dash]*Tunnel_Distance
while True:
    G_current_position +=G_distance
    I_current_position += i_distance
    
    if(I_current_position>=Tunnel_Distance) :
        print(f"\nTHE IMP HAS ESCAPED TO FREEDOM AFTER {second_passed} SECONDS. MISCHIEF AND TRICKERY AWAIT!")
        break
    if(G_current_position>=I_current_position):#if the golem’s position overtakes (>=) the imp’s position beforehand, the imp is captured and its fun ends.
        print(f"\nSADLY, IT’S BACK TO THE TOWER FOR THE IMP AFTER A {second_passed} SECOND-CHASE.")
        break
   
    #print(f"G's :{G_current_position}"+x*2+f"I's : {I_current_position}")
    
    tunnel[I_current_position]='I'
    tunnel[G_current_position]='G'
    
    formatted_output = ''.join(tunnel)# Remove the single quotes and commas when printing the array. Ex: ['-','-'] --> - - 
    print(f"{formatted_output}"+"X"+x*2+f"{second_passed}S")
    
    i_distance = random.randint(1, 9) ; 
    G_distance = random.randint(3, 5) 
    time.sleep(1)
    second_passed= second_passed + 1
    tunnel[I_current_position]='-' 
    tunnel[G_current_position]='-'


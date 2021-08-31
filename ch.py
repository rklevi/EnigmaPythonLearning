p1=[1,1]
p2=[1,1]


#Attack


def attack(f,s,p1,p2):
    if f=='L':
        if s=='L':
            p2[0]+=p1[0]
        else:
            p2[1]+=p1[0]
    if f=='R':
        if s=='L':
            p2[0]+=p1[1]
        else:
            p2[1]+=p1[1]
    



 
# Splitting the fingers


def splitfingers(f,b,n,p):
    if f=='L':
        p[0]=b
        p[1]=n
    if f=='R':
        p[1]=b
        p[0]=n



# Display


def display():
    
    
    print("Current status:\n")
    print("Player1 info =", p1)
    print("Player2 info =", p2)
p1turn=True
p2turn=False
game = True


#Main game
print ("\t\t\t\t\t\t\tCHOPSTICKS")
print("\t\t\t1.In the game L means Left hand and R means Right hand")
print("\t\t\t2.Game has 2 move options\n \t\t\t Enter A To Attack and S to Split ")
print("\t\t\t3.After entering the move specify move combination")
print("\t\t\t4.If chosen A: enter combination in form: <Hand that will attack> <Hand to be attacked> separated by space\n \t\t\tExample:L R")
print("\t\t\t5.If chosen S: enter combination in form: <Hand to be splitted> <Left hand after split> <Right hand after split>\n \t\t\tExample: L 1 2 ")
print("\t\t\t\t\t\t\tENJOY THE GAME \n \t\t\t\t\t\t\tMAY THE BEST ONE WINS")
while game:
    display()   #Calling function display to show the data in the beginning 
   
   #Player 1 turn
   
    while p1turn:    
        m=input("Enter move for player 1 -")
        m=m.lower()
        if m=='a':
            f,s=input("Enter move combination - ").split()  
            attack(f,s,p1,p2)   #attack function 
        if m=='s':
            f,b,n=input("Enter move combination - ").split()
            b=int(b)
            n=int(n)
            splitfingers(f,b,n,p1)
        if p1[0]>=5:  #rules condition 
            p1[0]=0
        if p1[1]>=5:
            p1[1]=0
        if p2[0]>=5:
            p2[0]=0
        if p2[1]>=5:
            p2[1]=0
        if p1[0]==0 and p1[1]==0:
            print ("Player 2 wins")
            game = False
            break 
        if p2[0]==0 and p2[1]==0:
            print ("Player 1 wins")
            game= False
            break 

        p1turn=False   #Changing values for player 2 loop to continue
        p2turn=True
  
    #Player 2 turn
    
    while p2turn:
        display()      #display status after player 1 turn 
        m=input("Enter move for player 2 -")
        m=m.lower()
        if m=='a':
            f,s=input("Enter move combination - ").split()
            attack(f,s,p2,p1)  
        if m=='s':
            f,b,n=input("Enter move combination - ").split()
            b=int(b)
            n=int(n)
            splitfingers(f,b,n,p2)
        if p1[0]>=5:     #rules condition
            p1[0]=0
        if p1[1]>=5:
            p1[1]=0
        if p2[0]>=5:
            p2[0]=0
        if p2[1]>=5:
            p2[1]=0
        if p1[0]==0 and p1[1]==0:
            print ("Player 2 wins")
            game = False
            break 
        if p2[0]==0 and p2[1]==0:
            print ("Player 1 wins")
            game= False
            break 
           
        p1turn=True        #Changing values for player 1 loop to continue
        p2turn=False

    

        

m=input("MR. 1 enter your choice for play\n") 
n=input("MR. 2 enter your choice for play\n") 
l=[['_','|','_','|','_'],['_','|','_','|','_'],['_','|','_','|','_']]
mm=['',0,1,2,0,1,2,0,1,2]
kk=['',0,0,0,2,2,2,4,4,4]
def pad():
     for i in l:
           print("".join(map(str,i))) #printing pad of game

def change(x):                  #entry the turns of players on the board  
    if x==1 or x==2 or x==3:
        z=mm[x]
        x=0
        return[x,z]
    elif x==4 or x==5 or x==6:
        z=mm[x]
        x=2
        return[x,z]
    elif x==7 or x==8 or x==9:
        z=mm[x]
        x=4
        return[x,z]
        
pad()        
def wl():   #checking the win
   if (l[0][0]==m)and (l[0][2]==m)and (l[0][4]==m)or(l[0][0]==n)and (l[0][2]==n)and (l[0][4]==n):
       return True
   elif (l[1][0]==m)and (l[1][2]==m)and (l[1][4]==m)or(l[1][0]==n)and (l[1][2]==n)and (l[1][4]==n):
         return True
   elif (l[2][0]==m)and (l[2][1]==m)and (l[2][4]==m)or(l[2][0]==n)and (l[2][2]==n)and (l[2][4]==n):
         return True
   elif (l[0][0]==m)and (l[1][0]==m)and (l[2][0]==m)or(l[0][0]==n)and (l[1][0]==n)and (l[2][0]==n):
         return True    
   elif (l[0][2]==m)and (l[1][2]==m)and (l[2][2]==m)or(l[0][2]==n)and (l[1][2]==n)and (l[2][2]==n):
         return True
   elif (l[0][4]==m)and (l[1][4]==m)and (l[2][4]==m)or(l[0][4]==n)and (l[1][4]==n)and (l[2][4]==n):
         return True  
   elif (l[0][0]==m)and (l[1][2]==m)and (l[2][4]==m)or(l[0][0]==n)and (l[1][2]==n)and (l[2][4]==n):
         return True  
   elif (l[0][4]==m)and (l[1][2]==m)and (l[2][0]==m)or(l[0][4]==n)and (l[1][2]==n)and (l[2][0]==n):
         return True
def usr1():
   tr=True
   while tr:
                                            #taking input from 1st user
         x=int(input("MR. 1 enter where you want to insert"))
         if x in (1,4,7):
             d=0
         elif x in (2,5,8):
             d=1
         elif x in (3,6,9):
             d=2
         else:
             print("wrong input")
         mr=kk[x]
         if l[d][mr]=='_':
             a=change(x)   
             l[a[1]].pop(a[0])           
             l[a[1]].insert(a[0],m)
             tr=False
         else:
             print("u are inserting used place")     
def usr2(): 
   tr=True
   while tr:                                          #taking input from 2nd user
         x=int(input("MR. 2 enter where you want to insert"))
         if x in (1,4,7):
             d=0
         elif x in (2,5,8):
             d=1
         elif x in (3,6,9):
             d=2
         else:
             print("wrong input")
         mr=kk[x]
         if l[d][mr]=='_':    
           a=change(x)   
           l[a[1]].pop(a[0])           
           l[a[1]].insert(a[0],n)
           tr=False
         else:
           print("wrong place mr2")  
try:                                             
     board=True       
     v=0
     while v<10 and board:
            if v in (0,2,4,6,8):
                 usr1()
                 pad()
                 if wl():
                     board=False
                     print("MR 1 YOU WON THE GAME")
                 else:
                     print()
            elif v in (1,3,5,7):
                 usr2()
                 pad()
                 if wl():
                     board=False
                     print("MR 2 YOU WON THE GAME")
                 else:
                     print()
            else:
                print("MATCH IS TIE")
                board=False
            v+=1            
except Exception as e:
     print("ERROR=>\n",e.args[0])
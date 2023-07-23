import random
l=["rock","scissor","paper"]

while True:
    Ccount=0
    Ucount=0
    uc=int(input('''
Game Start....
1 Yes
2 No | Exit                                  
    
                 '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1.Rock
2.Scissor
3.Paper                                                                
'''))
            if userInput==1:
                      uchoice="rock"  #uchoice= userchoice
            elif userInput==2:
                      uchoice="scissor"
            elif userInput==3:
                      uchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                   print("Computer value",Cchoice)
                   print("User Value",uchoice)
                   print("Game Tie")
                   Ucount=Ucount+1  #ucount= user count
                   Ccount=Ccount+1   #ccount = computer count
            elif (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                      print("Computer value:",Cchoice)
                      print("User Value:",uchoice)
                      print("You win")
                      Ucount=Ucount+1
                            

            else:
                   print("Computer value:",Cchoice)
                   print("User Value:",uchoice) 
                   print("computer win")
                   Ccount=Ccount+1



        if Ucount==Ccount:
             
                      print("final game draw...")
                      print("user score",Ucount)
                      print("computer score",Ccount)
        elif Ucount>Ccount:
                      print("final user win")
                      print("user score",Ucount)
                      print("computer score",Ccount)     
        else:
                     print("final computer win")
                     print("user score",Ucount)
                     print("computer score",Ccount)
             
    else:
        break

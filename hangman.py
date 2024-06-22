import random

wordset=["arnold","maserati","car","club"]


def hangman(wordset):

    list_word=[]
    list_display=[]
    word=wordset[random.randint(0,len(wordset)-1)]

    for i in range(len(word)):
        list_word.append(word[i])
    
    for j in range (len(list_word)):
        list_display.append(" - ")

    chance=6
    wrong_list=[]

    while chance>0:
        index=0
        print(''.join(list_display))
        
        letter=input("Enter a letter >>")
        
        if letter in wrong_list:
            print("You've already guessed this one!")

        elif letter not in list_word:
            wrong_list.append(letter)
            chance-=1
            hangman_pic_(chance)
            print ("Missed, you have",chance,"more chance")
        
        
        
        else:
            for k in list_word:
                if k==letter:
                    list_display[index]=" "+k+" "
                index+=1

        if " - " not in list_display:
            print(''.join(list_display))
            print ("You win!!")
            break
        elif chance==0:
            print ("You lose!!")
            break
        

def hangman_pic_(chance):
    if chance==5:
        print("___________\n"" |     |\n"" |     O\n"" |\n"" |\n"" |\n"" |\n""--------")
    elif chance==4:
        print("___________\n"" |     |\n"" |     O\n"" |     |\n"" |\n"" |\n"" |\n""--------")

    elif chance==3:
        print("___________\n"" |     |\n"" |     O\n"" |    /|\n"" |\n"" |\n"" |\n""--------")

    elif chance==2:
        print("___________\n"" |     |\n"" |     O\n"" |    /|\ \n"" |\n"" |\n"" |\n""--------")

    elif chance==1:
        print("___________\n"" |     |\n"" |     O\n"" |    /|\ \n"" |    /\n"" |\n"" |\n""--------")

    elif chance==0:
        print("___________\n"" |     |\n"" |     O\n"" |    /|\ \n"" |    / \ \n"" |\n"" |\n""--------")
    
    


hangman(wordset)

                
                


    

        
        

    



        

                

            




   




    
        


    


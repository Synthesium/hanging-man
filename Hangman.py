import pyfiglet
import os
import random 
from time import sleep

def inits():
    randomVar=random.randint(0,58110)
    tf=open('wordlist.txt','r')
    lines=tf.readlines()
    tf.close()
    global char
    char=(lines[randomVar].strip())
    #print(char)
    global num
    num=len(char)

def startVisual():
    os.system('clear')
    result = pyfiglet.figlet_format("HANGMAN!!!",font= "slant")
    print("Synthesium Presents")
    sleep(3)
    os.system('clear')
    print(result)

def wait():
    os.system('clear')
    sleep(1)
    
def rules():
    print("WELCOME TO HANGMAN")
    input("Press enter to continue")
    os.system('clear')
    print("you are about to be hanged to atone for your crimes")
    sleep(2)
    print("To save yourself,guess the word")
    sleep(2)
    print("You have 10 guesses")
    sleep(1)


def generator():
    count=0
    while count<num:
        print(" _ ",end ="")
        count+=1
    
def main():
    startVisual()
    inits()
    rules()
    generator()    
    int 
    
main()


#the initialization [1]
global hitemp
hitemp=0
lose =0
word = char
length= len(word)
list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list2=["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj","kk","ll","mm","nn","oo","pp","qq","rr","ss","tt","uu","vv","ww","xx","yy","zz"]
##list3=["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj","kkk","lll","mmm","nnn","ooo","ppp","qqq","rrr","sss","ttt","uuu","vvv","www","xxx","yyy","zzz"]
##theword="@"
counter=0
global letr




#initializing list2 to dashes  [2]
count = 0
while count<length:
    list2[count]="_"
    count+=1

#just prints the initalized list2 to show the dashes once . [3]
#count =0
#while count<length:
 #   print(list2[count]," ",end="")
  #  count+=1

#initializes the list1 with the letters. [4]
count=0
while count<length:
    list1[count]=word[count]
    count+=1

#print the list1 once for conformation [trial] [works so far]
#count =0
#while count<length:
#    print(list1[count]," ",end="")
#    count+=1"


def state():          # prints the state of word being guessed
    c2=0
    while c2<length:
        print(list2[c2]," ",end="")
        c2+=1

def check():

    if letter == list1[count]:
        #print(letter,end="")
        list2[count]=list1[count]
        return 1

    elif letter!= list1[count]:
        return 0

def lettre():
    global theword
    global letter
    global lose
    letr=input("\n\n\tType a letter and then press enter:\n\t\t")
    temp = len(letr)
    if temp!=1:
        print("\tYou have entered more than 1 letter")
        lettre()
    elif letr in theword:
        print("\tyou have already used that letter")
        lettre()
    elif letr not in theword and temp==1:
        letter = letr
        theword=theword + letter
        lose+=1

#the main program
hitemp=1
theword="@"
win=0
lose =0
hello= True
while hello:
    lettre()            # the input letter is taken [5]
    os.system('clear')
    print("\n\n\t")
    hitemp+=1
    count = 0
    while count<length:                          #checking is initiated [6]
        temps=check()
        win+=temps
        count+=1
    state()
    if win==length:   #the winning statement
        print("\n\tCONGRATULATIONS ,you have won.The word was ",word)
        hello=False
    if lose==(10+ win) and win!= length:     #the losing statement
        print("\n\nyou have used up all your chances. now you must be hanged.")
        print("\nthe word was ",word)
        hello=False

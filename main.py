import random
from words import word_list
wordChosen = random.choice(word_list)
numOfLetter = len(wordChosen)
# print(wordChosen)
Lives = numOfLetter
# print(numOfLetter)
seperate_Word= list(wordChosen)
# print(seperate_Word)
print(f'You are now playing Hangman. You have {Lives} lives.')
guessed=list()
for x in str(numOfLetter):
  print("_"*numOfLetter)
  
# print(wordChosen)


while Lives != 0:
  letterGuessed = input("guess a letter: ")
  letterGuessed
  if letterGuessed in seperate_Word:
    
    seperate_Word.remove(letterGuessed)
    guessed.append(letterGuessed)
    print(guessed)
    if seperate_Word == []:
      print("You win")
      break
  else:
    Lives += -1
    print(f'Number of lives left: {Lives}')




if Lives == 0:
  print("YOU LOSE")
  print(f"The word was {wordChosen}.")
# if lives ==numOfLetterm:
#   print(YOU WON)
#   break

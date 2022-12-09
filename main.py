import random
from words import word_list
from lives import Lives
# print(wordChosen)
def game():
  wordChosen = random.choice(word_list)
  numOfLetter = len(wordChosen)
  print(wordChosen)
  Lives = numOfLetter
# print(numOfLetter)
  seperate_Word = list(wordChosen)
# print(seperate_Word)


  print(f'You are now playing Hangman. You have {Lives} lives.')
  guessed = list()
  for x in str(numOfLetter):
   print("_" * numOfLetter)



  while Lives != 0:
    letterGuessed = input("guess a letter: ")
    letterLowercased = letterGuessed.lower()
    if letterGuessed in seperate_Word:

      seperate_Word.remove(letterGuessed)
      guessed.append(letterGuessed)
      print(guessed)
      if seperate_Word == []:
        print(f'You win the word was {wordChosen}')
  
        break
    else:
      Lives += -1
    print(f'Number of lives left: {Lives}')
def num_lives():
      if Lives == 0:
        print("YOU LOSE")
        print(f"The word was {wordChosen}.")
# if lives ==numOfLetterm:
#   print(YOU WON)
#   break


num_lives()
game()

# import depencies
import random
import pandas as pd
game_id = 0

class WordGame():
  game_id+=1
  words = pd.read_csv('https://raw.githubusercontent.com/oanokyen/Tutorials/main/Word-Game/dictionary_words.csv')
  

  def __init__(self, num_of_letters=5):
    self.num_of_letters = num_of_letters
    self.words_pool = []  # load words with num of letters indicated
    for word in self.words['words']:
      if len(str(word))== self.num_of_letters:
        self.words_pool.append(word)
    self.word_to_guess = random.choice(self.words_pool)
    
  

  def find_indexes(self, word_attempt):
    if word_attempt not in list(WordGame.words['words']):
      return 'Not in word list'
    elif len(word_attempt) != self.num_of_letters:
      return 'Word has more letters than {}'.format(self.num_of_letters)
    else:
      self.word_attempt = word_attempt
      for i,char in enumerate(word_attempt):
        if char == [*self.word_to_guess][i]:
          print(char)
        elif char in self.word_to_guess:
          print('*{}'.format(char))
        else:
          print('_') 

  


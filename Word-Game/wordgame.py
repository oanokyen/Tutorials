# import depencies
import random
import pandas as pd
game_id = 0

class WordGame():
  game_id+=1
  

  def __init__(self, num_of_letters=5):
    self.num_of_letters = num_of_letters
    self.words = pd.read_csv('https://raw.githubusercontent.com/oanokyen/Tutorials/main/Word-Game/dictionary_words.csv')
    self.words_pool = []  # load words with num of letters indicated
    for word in self.words['words']:
      if len(str(word))== self.num_of_letters:
        self.words_pool.append(word)
    self.word_to_guess = random.choice(self.words_pool)


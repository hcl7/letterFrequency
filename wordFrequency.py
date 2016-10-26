import sys

def countWord(word, sentence):
  count = 0
  for i in range(len(sentence)):
    if sentence[i] == word:
      count += 1
  return count

def countedWords(word, sentence, n):
  found = False
  for i in range(n):
    if sentence[i] == word:
      found = True
  return found
  
def wordFrequency(sentence):
  sentence = sentence.split();
  for i in range(len(sentence)):
    if (countedWords(sentence[i], sentence, i) == True):
      continue
    else:
      print sentence[i], '=', countWord(sentence[i], sentence)
      
wordFrequency('this mesage is the good message for the word frequecy test')

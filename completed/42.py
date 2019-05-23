#Read in words and clear off quotes
words = open("p042_words.txt", "r")
swords = words.read()
dirty_list = swords.split(",")
word_list = []
for w in dirty_list:
  word_list.append(w.strip('"'))

# Find the longest word, to approximate the limit of
# possible triangle numbers (not needed in final 
# program). The longest word is 14 characters.

"""
def find_max_len():
  m = 0
  for w in word_list:
    if (len(w) > m):
      m = len(w)
  return m
"""

# Since the longest word is only 14 characters, 
# the maximum word value must be less than 14*26 = 364
# So, all the triangle numbers up to 364 can be 
# and stored to be checked

def calc_triangle_numbers():
  tri_nums = set()
  number = 0
  counter = 1
  while number < 364:
    number = counter+number
    tri_nums.add(number)
    counter += 1

  return tri_nums

tri_set = calc_triangle_numbers()

# Now we have to create a function for converting words
# to their coded values. We'll use a dictionary that
# maps letters to ints

alph = {'A':1,'B':2,'C':3,'D':4,'E':5,
'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,
'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,
'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,
'Y':25,'Z':26}

def calc_word_val(word):
  val = 0
  for c in word:
    val += alph[c]
  return val

# Now, we can iterate the word list and
# count the number of triangle words

num_tri_words = 0
for w in word_list:
  if calc_word_val(w) in tri_set:
    num_tri_words += 1

print(num_tri_words)

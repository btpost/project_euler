# This can check to see if a sequence of squares is equal to 1/2
# Still have to figure out how to search for sequences

def check_half():
  hsum = 0
  tot = 0
  denom = 1
  for x in sq_list:
    denom *= x
  
  hsum = denom/2

  for x in sq_list:
    tot += denom/x
  
  print 'hsum:' + str(hsum)
  print 'tot: ' + str(tot)

  if tot == hsum:
    return 0
  elif tot < hsum:
    return 1
  elif tot > hsum:
    return 2

counter = 0
cstr = str(bin(counter))
while len(cstr) < 80:
  counter += 1
  cstr = str(bin(counter))
  print counter

"""
done = False
num_list = [2]
sq_list = [4]
i = 2
while(not done):
  raw_input()
  i += 1
  print i
  print num_list
  c = check_half()
  if(c == 0):
    print num_list
    print "done"
  elif(c == 1):
    num_list.append(i)
    sq_list.append(i**2)
  elif c == 2:
    num_list.pop(-2)
    sq_list.pop(-2)
  
"""

  



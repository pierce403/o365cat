import re
import io
import sys

f = io.open('10-million-password-list-top-100000.txt', mode="r", encoding="utf-8")

minchars=7
maxchars=16

for line in f:
#while True:
#  line = "potato"
#  try: 
#    line = f.readline()
#  except:
#    continue

  word = line.strip()
  if len(word)<minchars:
    continue

  if len(word)>maxchars:
    continue

  oScore = 0
  if re.search('[a-z]',word):
    oScore+=1

  if re.search('[A-Z]',word):
    oScore+=1

  if re.search(r'\d',word):
    oScore+=1

  if re.search('[@_!#$%^&*()<>?/\|}{~:\ ]',word):
    oScore+=1

  #print(oScore)
  if oScore>=3:
    print(word)
    sys.stdout.flush()

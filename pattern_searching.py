s = "geeks for geeks"
pattern = "geeks"


pos = s.find(pattern)
while pos>=0:
   print(pos)
   pos = s.find(pattern,pos+1) 


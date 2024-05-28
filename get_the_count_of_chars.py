def char_counts(s):
   dict = {} 

   for n in s:
      keys = dict.keys()
      print(keys)     
 
      if n in keys:
         dict[n] += 1
      else:  
         dict[n] = 1
   
   return dict 

print(char_counts("unforseen"))

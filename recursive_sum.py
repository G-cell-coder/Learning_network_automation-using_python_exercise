def list_sum(lst):
   if len(lst) == 1:
      return lst[0]
   else:
      sum_list =int( lst[0]) + int(list_sum(lst[1:]))
      return sum_list


lst = ['100','200','300','400','500','600','700','800']
print("Sum of elements in List:",list_sum(lst))

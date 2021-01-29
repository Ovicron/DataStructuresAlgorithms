
def reverse_list(lst):
  if len(lst) <= 1:
    return lst
  return [lst[-1] + reverse_list(lst[:-1])
  
 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reverse_list(x))

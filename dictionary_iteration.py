def find_uniq(arr):
  dic = {}
  for i in arr:
    if i not in dic:
      dic[i] = 1
    else:
      dic[i] += 1
  
  for k, v in dic.items():
    if v == 1:
      return k


find_uniq([ 1, 1, 1, 2, 1, 1 ])

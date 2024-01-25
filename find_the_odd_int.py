def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i


#A way to do it with a dictionary
def find_it(seq):
    dic = {}
    for number in seq:
        if number not in dic:
            dic[number] = 1
        else:
            dic[number] = 1 + dic[number]
    for k,v in dic.items():
        if v%2 != 0:
            return k

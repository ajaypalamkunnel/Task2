import random

randomlist = []
def ran(minimum,maximum):
    for i in range(0,3):
      n= random.randint(minimum,maximum)
      randomlist.append(n)
    print(randomlist)
    return randomlist








import pprint 
import numpy as np
from random import randrange


rows = 10
cols = 10
Array =[[0 for j in range(cols)] for i in range(rows)]
# print(len(Array))

for arr in Array:
  # print(arr)
  for j in range(len(arr)):
    arr[j] = randrange(0,2)
    # print(arr[j])

pprint.pprint(Array)
# test0 = np.array(Array[0][0])
# test1 = np.array(Array[1][0])
# arr_new = test0 + test1 
# pprint.pprint(arr_new)


# for x in range(10):
#   test = np.array(Array[x][0])
#   print(test)
  



































# # pprint.pprint(Array)
# count = 0

# print 
# for i in range(len(Array)):
#   print(Array[i])
  # if(Array[i][1] = 1):
  #   print(i)
  # for j in i:
  #   pprint.pprint(Array)

# for i in range(10):
#   for j in range(10):
#     if(Array[i][j] )
  
    # while count == 10:
    #   print(count)
#       if count == 10:
#         break
#       # print(Array)
#     while count <= 10:
#     if count == 10:
#       print(count)
#       print(Array)
#       break
#       print(i)
# #     print(i)


# for i in range(0,9):
#   if (Array[i][0]==1) and (Array[i+1][0]==1):
#     pprint.pprint(Array)

# import numpy as np

# # arr = np.array([[1,2,3,4,5,6,7,8],[0,9,8,7,6,5,4,3]]) #this is one array
# # print (arr.shape)

# # arr2 = np.array ([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
# # print (arr2.size,arr2)

# # arr3 = np.array ([[[1,2], [1,2],[1,2], [1,2]]]) # if we want to create a new column then we will do use comma,
# # print (arr3.shape)

# # arr = np.zeros((3,4))
# # print (arr)

# # arr1 = np.ones ((2,3))
# # print (arr1)

# # arr2 = np.full ((2,2),7)
# # print (arr2)

# # arr3 = np.full ((10,12),8)
# # print (arr3)

# # arr = np.arange (1,10,2)
# # print (arr)

# arr = np.array (([1,2,3], [1,2,3])) #shape always retruns in rows and columens
# print (arr.shape)

# # arr = np.array (([1,2,3], [1,2,3]))
# # print (arr.size)


# a = np.array ([[1,2,3,4], [1,2,3,4], [1,2,3,4],[1,2,3,4]])
# print (a.shape) #it will give us the shape row and column

# # a = np.array ([[1,2,3,4], [1,2,3,4], [1,2,3,4]])
# # print (a.size) # it will give us the elements and say how many elements are therer in a array

# # a = np.array ([[1,2,3,4,5],[1,2,3,5,6]])
# # print (a.shape)  

# # b = np.array([[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4],  # Layer 1
# #                [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
# #               [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4],  # Layer 2
# #                [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4],
# #                [1, 2, 3, 4], [1, 2, 3, 4]]]) 

# # print (b.shape)



# # b = np.array ([[1,2,3,4], [1,2,3,4],[1,2,3,4],[1,2,3,4],
# #               [1,2,3,4], [1,2,3,4],[1,2,3,4],[1,2,3,4]])

# # print (b.shape)

# # b = np.array ([[1,2,3,4], [1,2,3,4],[1,2,3,4],[1,2,3,4],
# #               [1,2,3,4], [1,2,3,4], [1,2,3,4],[1,2,3,4]])

# # print (b.shape)

# # b  = np.array ([1,2,3])
# # c = np.array ([[1,2,3,4], [1,2,3,4]])
# # d = np.array([[1,2] ,[1,2],[1,2],[1,2],[1,2],[1,2]])

# # print (b.ndim)
# # print (c.ndim)
# # print (d.ndim)


# # b = np.array ([["anil", "saini", "Inida"], ["china", "India", "Russia"],["US", "trump", "Idiot"]])
# # print (b.dtype)
# # print (b.shape)
# # print (b.ndim)
# # print (b.size)

# # a = np.array([[1,2,3,4,4], [1,2,3,4,4]])
# # b = a/10
# # print  (b)

# # a = np.sum ([1,2,3,4,5,6]) 
# # print (a)
# # a = np.mean ([1,2,3,4,5,6]) 
# # print (a)
# # a = np.min ([1,2,3,4,5,6]) 
# # print (a)
# # a = np.max ([1,2,3,4,5,6]) 
# # print (a)

# # a = np.max ([1,2,3,4,5,6]) 
# # print (a)

# # a = np.std ([1,2,3,4,5,6]) 
# # print (a)


# # a = np.array ([10,20,30,40,50,60])
# # print (a[2:4]) # remeber it does not count the last one 

# # a = np.array([10,20,30,40,50,60])
# # print (a[[2,3,4]]) # in fancyindexing we use double brackets 


# # a = np.array ([100, 200,300,400])
# # discount = 10
# # newdicsoun = a - (a*discount)/100
# # print (newdicsoun)


# # a = np.array ([[1,2,3],[1,2,3]])
# # b = np.array 
# # print (b)


# l1 = []
# for i in range (4):
#     a = int(input("enter your number"))
#     l1.append(a)
# print (l1)


# dic = {}
# for i in range (4):
#     name = input("enter your name")
#     lang = input("enter your language")
#     dic.update({name:lang})

# print (dic)

# l1  = []
# for i in range (6):
#     a = int (input("enter your number"))
#     l1.append(a)
# l1.sort() #whenever i need to sort i will sort it directly
# print (l1)

# dic = {"name":"anil",
#        "b":"c",
#        "c":"d"}

# b = input("enter your word")

# print (dic[b])

# s = set()
# for i in range (6):
#     a = int(input("enter your number"))
#     s.add (a)

# print (s)

# username = input("enter your username")
# if len(username)<10:
#     print ("again")

# while True: # if we are not able to provide any condition then we use true and false
#     username = input("enter your username")
#     if len(username)>10:
#         print ("good")
#         break

#     else:
#         print ("try again")

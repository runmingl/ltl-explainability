import matplotlib.pyplot as plt

x = [42, 42, 34, 40, 54, 50, 61, 25, 33, 61, 25, 33, 156, 26, 109, 55, 47, 59, 39, 75, 18, 18, 17, 23, 23, 18, 18, 18, 17, 17, 17, 23, 23, 23, 24, 24, 10, 17, 17, 17, 24, 24, 24, 10, 17, 17, 17, 17, 17, 17, 121, 5, 30, 20, 20, 32, 32, 42, 42, 18, 20, 12, 14, 14, 14, 14, 14, 14, 49, 49, 49, 49, 14, 14, 14, 14, 14, 14, 24, 20, 10, 27, 68, 20, 23, 20, 63]
y1 = [5, 9, 1, 5, 5, 5, 41, 9, 21, 113, 9, 21, 86042, 9, 170, 6, 5, 5, 6, 21, 5, 5, 1, 5, 5, 5, 5, 5, 1, 1, 1, 5, 5, 5, 9, 9, 5, 1, 1, 1, 9, 9, 9, 5, 1, 1, 1, 1, 1, 1, 303958, 2, 9, 5, 9, 9, 9, 9, 9, 1, 5, 5, 1, 1, 1, 1, 1, 1, 113, 113, 113, 113, 1, 1, 1, 1, 1, 1, 2, 1, 5, 9, 69, 5, 5, 9, 7]
y2 =  [1, 1, 0, 1, 1, 1, 2, 1, 2, 3, 1, 2, 8, 1, 3, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 8, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 1, 1, 1, 1]

fig1 = plt.figure()
plt.xlabel('Length of LTL Formula')
plt.ylabel('Star height')
#x.remove(156)
y1.remove(86042)
#x.remove(121)
y1.remove(303958) # use log or other scaling
plt.scatter(x, y2)

plt.show()

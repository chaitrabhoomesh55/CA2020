
# 13. Create a list of given structure and run 
# 	x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# ●	Access list [1, 2, 3, 4]   # ●	Access list [600,  700]#     ●	Access list [100, 300, 500, 600, 800]
# ●	Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# ●	Access list [10]
# ●	Access list [ ]
###test_list[pos:pos] = insert_list 
list1 = [x for x in range(100, 900, 100)]
print (list1)
list2 = [x for x in range(1, 10)]
print(list2)
list3 = [x for x in range(10, 60, 10)]
print(list3)
list2[5:5] =list3
print (list2)
list1[5:5] = list2
print(list1)

list1[5][0]
l[6][7]
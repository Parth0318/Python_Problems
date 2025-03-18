# # # n = 42
# # # print(n)

# # # 42 = n
# # # print(n)

# # x = y = 1

# # x = 2
# # y = 4
# # print(xy)

# # exercise 2.2 
# #The volume of a sphere with radius r is 4
# # 3 r3. What is the volume of a sphere with radius 5?

# # r = 5
# # pi = 3.1415926535897931
# # v = 4/3*pi*r*r*r
# # print(v)

# # r = 5
# # pi = 3.1415926535897931
# # v = 4/3*pi*r**3
# # print(v)

# # r = int(input("Enter the radius of the sphere: "))
# # pi = 3.1415926535897931
# # v = 4/3*pi*r*r*r
# # print(v)

# '''Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
#  $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
#  60 copies?'''

# cover_price = 24.95
# discout = 0.4
# shipping_cost = 3
# additional_cost = 0.75
# total_copies = 60

# total_cost =  (cover_price - (cover_price * discout)) 
# print(total_cost)

# total_shipping_cost = shipping_cost + (additional_cost * (total_copies - 1))
# print(total_shipping_cost)

# total_wholesale_cost = (total_cost * total_copies) 
# print(total_wholesale_cost)

# total_c = total_wholesale_cost + total_shipping_cost
# print(total_c)



'''If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
 tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast? '''

s_h = 6
s_m = 52
s_s = 0

a_m = 23
a_s = 42

n_s = (s_s + a_s) % 60
e_m = (s_s + a_s) // 60

n_m = (s_m + a_m + e_m) % 60
e_h = (s_m + a_m + e_m) // 60

n_h = (s_h + e_h) % 12
print(f"Final Time: {n_h}:{n_m:02}:{n_s:02} AM")


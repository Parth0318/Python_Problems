# import turtle

# parth = turtle.Turtle()

# import turtle
# p = turtle.Turtle()

# for i in range(4):
#     p.fd(100)
#     p.lt(90)
# turtle.mainloop()

'''1. Write a function called square that takes a parameter named t, which is a turtle. It
 should use the turtle to draw a square.
 Write a function call that passes bob as an argument to square, and then run the
 program again.'''

# import turtle

# p = turtle.Turtle()

# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)
#     print(t)
# square(p)    
# turtle.mainloop()    


'''2. Addanother parameter, named length, to square. Modify the body so length of the
 sides is length, and then modify the function call to provide a second argument. Run'''

# import turtle

# p = turtle.Turtle()

# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)
#     print(t)
# square(p, 300)
# turtle.mainloop()


# import turtle

# p = turtle.Turtle()

# def square(t,length):
#     for i in range(4):
#         t.fd(length)
#         t.rt(90)
#     print(t)
# square(p,100)
# turtle.mainloop()       

''' 3. Make a copy of square and change the name to polygon. Add another parameter
 named n and modify the body so it draws an n-sided regular polygon. Hint: The
 exterior angles of an n-sided regular polygon are 360/n degrees.'''

# import turtle

# p = turtle.Turtle() 

# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)
#     print(t)
# polygon(p, 100, 6)
# turtle.mainloop()


# import turtle

# p = turtle.Turtle()

# def polygen(t,length,n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)
#     print(t)
# polygen(p,100,6)
# # polygen(p,100,3)
# # polygen(p,100,4)
# # polygen(p,100,5)
# turtle.mainloop()    

'''Write a function called circle that takes a turtle, t, and radius, r, as parameters and
 that draws an approximate circle by calling polygon with an appropriate length and
 number of sides. Test your function with a range of values of r.
 Hint: figure out the circumference of the circle and make sure that length * n =
 circumference.'''

# import turtle

# p = turtle.Turtle() 

# def polygen(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.rt(360 / n)

# def circle(t,r):
#     circumference = 2 * 3.14 * r
#     n = 50
#     length = circumference / n
#     polygen(t, length, n)
#     print(t)
# circle(p, 100)
# turtle.mainloop()    


'''Makeamoregeneralversion of circle called arc that takes an additional parameter
 angle, whichdetermineswhatfractionofacircletodraw. angleisinunitsofdegrees,
 so when angle=360, arc should draw a complete circle.'''

# import turtle

# p = turtle.Turtle() 

# def polygen(t, length, n):
#     for i in range(n):
#         t.fd(length)    
#         t.rt(360 / n)
#     print(t)

# def arc(t, r, angle):
#     arc_length = 2 * 3.14 * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n
#     polygen(t, step_length, n)
#     print(t)
# arc(p, 100, 180)

# turtle.mainloop()



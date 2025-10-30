import cmath
def quad (a,b,c):
    if (a == 0):
        if (b == 0):
            if (c != 0):
                print("Non-zero constant cannot be equal to 0")
                x = ()
            else:
                print("0 = 0, hence infinite solutions")
                x =("Infinite",)
            return x
        else:
           x = (-c/b)
           return x    
    else:
        disc = (b**2) - (4*a*c)
        disc = cmath.sqrt(disc)
        x1 = (-b + disc)/(2*a)
        x2 = (-b - disc)/(2*a)
    return x1,x2

def cubic(a,b,c,d):
    if (a == 0):
        return quad(b,c,d)
    #Depressed cubic co-effs
    p = ((3*a*c)- (b**2))/(3*(a**2))
    q = ((2*b**3)-(9*a*b*c)+(27*(a**2)*d))/(27*(a**3)) 
    #onto y = u + v part and solving the helper quadratic
    #helper quad: t^2 + qt - (p^3)/27 = 0, roots are U,V
    t = quad(1, q, -(p**3)/27) 
    #defining the cube root of unity to get 3 solutions of u,v
    w = complex(-0.5, (3**0.5)/2)
    u = t[0] ** (1/3)
    if (u == 0):
        v = t[1] ** (1/3)
    else:
        v = -p/(3*u)
    y1 = u + v
    y2 = (u*w) + (v*(w**2))
    y3 = (v*w) + (u*(w**2))

    #getting the x's back
    x1 = y1 -(b/(3*a))
    x2 = y2 -(b/(3*a))
    x3 = y3 -(b/(3*a))

    return x1,x2,x3

def quartic (a,b,c,d,e):
    if (a == 0):
        return cubic(b, c, d, e)
# Depressing the equation        

    A, B, C, D = b/a, c/a, d/a, e/a #initializing A,B,C,D for ease of defining p,q,r
    p = B - ((3 * (A**2))/8)
    q = C + ((A**3)/8) - ((A*B)/2)
    r = D - ((3*(A**4))/256) + (((A**2)*B)/16) - ((A*C)/4)

    if (q == 0):    #handling the q = 0 case, leading to a bi-quad eq.
        m = quad(1, p, r)
        y1,y2,y3,y4 = cmath.sqrt(m[0]), -cmath.sqrt(m[0]), cmath.sqrt(m[1]), -cmath.sqrt(m[1])
        x1,x2,x3,x4 = (y1-(b/(4*a))), (y2-(b/(4*a))), (y3-(b/(4*a))), (y4-(b/(4*a)))
        return x1, x2, x3, x4

    else:       #Back to Ferrari's method
        z = cubic(8, 8*p, (2 * p**2) - (8 * r), -(q**2))
        z = z[0]
        T1 = quad(1, cmath.sqrt(2*z), ((p/2) + z - (q/(2*(cmath.sqrt(2*z))))))
        T2 = quad(1, -cmath.sqrt(2*z), ((p/2) + z + (q/(2*(cmath.sqrt(2*z))))))
        y1,y2,y3,y4 = T1[0],T1[1], T2[0], T2[1]
        x1,x2,x3,x4 = (y1 - (b/(4*a))), (y2 - (b/(4*a))), (y3 - (b/(4*a))), (y4 - (b/(4*a)))
        return x1,x2,x3,x4

#Onto out main code!
print("ax^4 + bx^3 + cx^2 +dx +e = 0")
print("Please enter the co-efficients for the given general eqution: ")
co_effs = ("a","b", "c", "d", "e")
x = []
for i in range(5):
    t = float(input(f"{co_effs[i]} = "))
    x.append(t)
a,b,c,d,e = x
if (a == 0):
    if (a==0) and (b == 0):
        t = quad(c,d,e)
        if (len(t) == 0):
            print("Non-zero constant cannot be equal to 0")
        elif (len(t) == 1) and (type(t[0] == str)):
            print("0 = 0, hence infinite solutions occur")
        elif (len(t) == 1) and (type(t[0] == float)):
            print("Linear Eqution entered. The roots are:")
            print(f"x1 = {t[0]:.2f}")
        else:
            print ("Quadratic equation entered. The roots are:")
            print(f'''x1 = {t[0]:.2f} \nx2 = {t[1]:.2f}''')
    elif (a == 0) and (b != 0):
        t = cubic(b,c,d,e)
        print("Cubic Equation entered. The roots are:")
        print(f'''x1 = {t[0]:.2f} \nx2 ={t[1]:.2f}\nx3 = {t[2]:.2f}''')

else:
    t = quartic(a,b,c,d,e)
    print(f'''x1 = {t[0]:.2f} \nx2 = {t[1]:.2f}\nx3 = {t[2]:.2f}\nx4 = {t[3]:.2f}''')

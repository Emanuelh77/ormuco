def questionA(x1,x2,x3,x4):

    if x1==x2 or x3==x4 or x1>x2 or x3>x4:
        return False

    if x2>x3:
        if x4 >= x2:
            return True
        elif x4 < x2 and x4 > x1:
            return True
    
    return False

a = questionA(2,8,3,10)
b = questionA(1,5,6,8)
c = questionA(3,10,2,8)
d = questionA(-1,8,3,5)
e = questionA(1,1,3,10)
f = questionA(-3,0,1,10)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

def questionB(stringOne, stringTwo):
    
    v1 = round(float(stringOne),18)
    v2 = round(float(stringTwo),18)

    if v1>v2:
        print("first value is greater than second value")
    elif v2>v1:
        print("second value is greater than first value")
    else:
        print("both values are the same")

questionB("2","26")
questionB("3.1","2.2")
questionB("7","6")
questionB("5.9","6.000001")
questionB("-1","1")
questionB("-3.4","-2.2")
questionB("-43.444444443","-43.444444443")
questionB("2","0")

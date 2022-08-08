from fractions import *
print('>>>>>                                THE LINE REFLECTOR!                                                <<<<<')
print('>>>>>                               Coded by Fahad Arefin.                                              <<<<<')
print('>>>>>  This calculator will find the reflection of a straight line in respect of the other line.        <<<<<')
print(">>>>>                         Input the lines in ax+by+c=0 formate.                                     <<<<<")
print('>>>>>                            a1x+b1y+c1=0 is the main line.                                         <<<<<')
print('>>>>>                          a2x+b2y+c2=0 is the reference line.                                      <<<<<')
print('>>>>>                        The ans will be in y-y1=m(x-x1) format.                                    <<<<<')
print('''
         ''')
a1 = Fraction(input('a1= '))
b1 = Fraction(input('b1= '))
c1 = Fraction(input('c1= '))
a2 = Fraction(input('a2= '))
b2 = Fraction(input('b2= '))
c2 = Fraction(input('c2= '))
if a1==a2 and b1==b2 and c1==c2:
    print('INVALID INPUT')
    exit()
m1 = -Fraction(a1/b1)
m2 = -Fraction(a2/b2)


angles_tangent = (m1 - m2)/(1+m1*m2)

slope_1 = (m2 + angles_tangent)/(1-m2*angles_tangent)
slope_2 = (m2 - angles_tangent)/(1+m2*angles_tangent)

x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
y = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)

x_str = str(x)
y_str = str(y)


if float(slope_1) == float(m1):
    m = slope_2
if float(slope_2) == float(m1):
    m = slope_1
str_m = str(m)

print('y-' + '('+ y_str +')' + '=' + str_m + '(x-' +'(' + x_str+')' +')')
exit()
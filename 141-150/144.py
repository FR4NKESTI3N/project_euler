def round(a):
    # print 'rounding',a
    a = int((a * 100) + 0.5) / 100.0
    # print 'rounded',a
    return a
class eclipse:
    "Format of ecliple: a(x)**2 + b(y)**2 = c. Make sure input is float"
    a=0
    b=0
    c=0
    def __init__(self,a,b,c=0):
        self.a=a
        self.b=b
        self.c=c

    def check(self,x,y):
        "Checks if point lies on elcipse"
        # return ((self.a*(x**2))+(self.b*(y**2)))==self.c
        return True

    def slope(self,x,y):
        "Returns slope (in float) of eclipse at point x,y"
        if not self.check(x,y):
            raise "ERROR: Point not on Eclipse"
        return ((-self.a)*x)/(self.b*y)

def get_reflection(m1,m2):
    m=(m1-m2)/(1-m1*m2)
    m3=(m-m2)/(m*m2-1)
    return m3

def solve_quadratic(a,b,c):
    d=b**2-4*a*c
    # if d<0:
    #     raise 'ERROR: Equation has imaginary solutions'
    d=d**0.5
    a,b= round((-b+d)/(2*a)),round((-b-d)/(2*a))
    # print a,b
    return a,b

def get_inersection(x,y,m):
    c=y-x*m
    #Now we need to solve quadratic equation: x**2(a+b*m*m)+x(2*b*m*c)+(b*c*c-k)=0
    a=ecl.a
    b=ecl.b
    k=ecl.c
    sol=solve_quadratic((a+b*m*m),(2*b*m*c),(b*c*c-k))
    print 'solutions =',sol
    x1,y1=None,None
    for i in sol:
        if i!=x:
            print '--------------------',i
            x1=i
    y1=round(c+m*x1)
    return x1,y1

def check_point(x,y):
    return target_range[0][0]<=x<=target_range[0][1] and target_range[1][0]<=y<=target_range[1][1]
target_range=((-0.01,0.01),(-9.99998,9.99998))
ecl=eclipse(4,1,100)
def recusive(x0,y0,x1,y1):
    m=(y1-y0)/(x1-x0)
    print 'lineslope = ',m
    m1=ecl.slope(x1,y1)
    print 'ellipse slope = ',m1
    m2=get_reflection(m,m1)
    x2,y2=get_inersection(x1,y1,m2)
    print x2,y2
    if check_point(x2,y2):
        return 1
    else:
        return 1+recusive(x1,y1,x2,y2)
print recusive(0.0,10,1.4,-9.6)
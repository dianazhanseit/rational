
from numbers import Number
from vector import *
#1st task 
def gcd(self, other):
	if self == 0 & other == 0:
		raise ArithmeticError( "gcd(0,0) does not exist" )
    sn = self.n*other.d
    on = other.n * self.d
    d  = self.d  * other.d
    return (sn, on, d)
#2nd task
class Rational( Number ) :
	def __init__( self, num, denum = 1 ) :
		self. num = num
		self. denum = denum
		self. normalize( )

	def normalize():
		if denum == 0:
			print("Can't divide by zero!")
		else if num == 0:
			num = 0
			denum = 1
		else if num < 0 & denum > 0:
			num = num//gcd(num,denum)
			denum = denum//gcd(num,denum)
		else
			num = abs(num)//gcd(num,denum)
			denum = abs(denum)//gcd(num,denum)
		print(num + "/" + denum)
	#3rd task
	def __repr__(self):
    	return '%s(%d, %d)' % (self.__class__.__name__, self.n, self.d)
    #4th task
	def __neg__( self ) :
		r = self.__class__(-self.n, self.d)
    	return r
	def __add__(self, other):
    	s, o, d = self.gcd(other)
    	r = self.__class__(s + o, d)
    	return r
	def __sub__( self, other ) :
		s, o, d = self.gcd(other)
		r = self.__class__(s - 0, d)
		return r
	def __radd_( self, other ) :
		s, o, d = self.gcd(other)
		r = self.__class__(s + o, d)
		return r
	def __rsub_( self, other ) :
		s, o, d = self.gcd(other)
		r = self.__class__(o - s, d)
		return r
	#task #5
	def __mul__( self, other ) :
		r = self.__class__(self.n*other.n, self.d*other.n)
		return r
	def __truediv__( self, other ) :
		r = self.__class__(self.n*other.d, self.d*other.n)
		return r
	def __rmul__( self, other ) :
		r = self.__class__(self.n*other.n, self.d*other.n)
		return r
	def __rtruediv__( self, other ) :
		r = self.__class__(other.n*self.d, other.d*self.n)
		return r
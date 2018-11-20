from numbers import *
from vector import *
#task #1
def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)
#print(gcd(-4,12))
#task #2
class Rational(Number):
	def __init__(self, num, denum = 1):
		self.num = num
		self.denum = denum
		self.normalize()
	def normalize():
		if denum == 0:
			raise ArithmeticError( "Can not divide by 0!" )
		if num == 0:
			denum = 1
		if denum < 0:
			__neg__(self)
			num = num//gcd(num, denum)
			denum = denum//gcd(num, denum)
		else:
			num = num//gcd(num, denum)
			denum = denum//gcd(num, denum)
		print(num + "/" + denum)
	#task #3
	def __repr__(self):
		return '%s( %d, %d)' % (self.__class__.__name__, self.n, self.d)
	#task #4
	def __neg__(self):
		r = self.__class__(-self.n, self.denum)
		return r
	def __add__(self, other):
		s, o, d = self.gcd(other)
		r = self.__class__(s + o, d)
		return r
	def __sub__( self, other ) :
		s, o, d = self.gcd(other)
		r = self.__class__(s - o, d)
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
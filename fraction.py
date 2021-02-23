from math import floor, sqrt

class Fraction:
	def __init__(self, numerator, denominator = 1):
		self.numerator = numerator
		self.denominator = denominator
		
		self.reduce()
		
	def __str__(self):
		if self.denominator == 1:
			return str(self.numerator)
		else:
			return str(self.numerator) + "/" + str(self.denominator)
		
	def __add__(self, other):
		d1 = self.denominator
		d2 = other.denominator
		
		result = Fraction(0,0)
		result.numerator = self.numerator * d2 + other.numerator * d1
		result.denominator = self.denominator * d2
		
		result.reduce()
		return result
		
	def __sub__(self, other):
		d1 = self.denominator
		d2 = other.denominator
		
		result = Fraction(0,0)
		result.numerator = self.numerator * d2 - other.numerator * d1
		result.denominator = self.denominator * d2
		
		result.reduce()
		return result
		
	def __mul__(self, other):
		result = Fraction(0,0)
		result.numerator = self.numerator * other.numerator
		result.denominator = self.denominator * other.denominator
		
		result.reduce()
		return result
		
	def __div__(self, other):
		result = Fraction(0,0)
		result.numerator = self.numerator * other.denominator
		result.denominator = self.denominator * other.numerator
		
		result.reduce()
		return result
		
	def reduce(self):
		maximum = floor(min(self.numerator, self.denominator))
		for k in range(maximum, 1, -1):
			if (self.numerator % k == 0) and (self.denominator % k == 0):
				self.numerator //= k
				self.denominator //= k
		

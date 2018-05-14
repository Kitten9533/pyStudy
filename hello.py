# encoding: utf-8
# import sys
import functools
import time
from types import FunctionType
from enum import Enum, unique
from functools import reduce
from urllib import request
import json
# reload(sys)
# sys.setdefaultencoding('utf8')
# print sys.getdefaultencoding() + "  - sys.getdefaultencoding()"

def normalize(name):
	arr = list(name)
	return arr[0].upper() + ('').join(arr[1:])
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
	def multi(x, y):
		'''第一次循环： x=3, y=5   '''
		return x * y
	return reduce(multi, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
	print(u'测试成功')
	# print('测试成功!'.decode('utf-8').encode(sys.getfilesystemencoding()))
else:
	# print('测试失败!'.decode('utf-8').encode(sys.getfilesystemencoding()))
	print(u'测试失败')

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
	L1 = list(str(n))
	t = len(L1)//2
	i = 0
	Flag = True
	while i <= t:
		if L1[i] != L1[0-i-1]:
			Flag = False
			break
		i = i+1
	return Flag
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
	print(u'测试成功!')
else:
	print(u'测试失败!')

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	# 按照姓名排序 返回t[0]
	# 年轻 t[1]
	return t[0]
	# return t[1]
L2 = sorted(L, key=by_name)
print(L2)

def count():
	fs = []
	for i in range(1,4):
		fs.append((lambda i: i * i)(i))
	return fs
f1, f2, f3 = count()
print(f1, f2, f3)

# 装饰器 兼容@log  和 @log('hah')
def log(text):
	text2 = 'default' if type(text) == FunctionType else text
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print ('%s %s %s' % (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), text2, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator(text) if callable(text) else decorator

@log('hah')
def fa():
	print('************')

fa()

@log
def fa2():
	print('-------------')

fa2()

class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.score, lisa.get_grade())
print(bart.name, lisa.score, bart.get_grade())
lisa.score = 100
print(lisa.score)

class Student(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender

	def get_gender(self):
		return self.gender

	def set_gender(self, gender):
		self.gender = gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
	print(u'测试失败!')
else:
	bart.set_gender('female')
	if bart.get_gender() != 'female':
		print(u'测试失败!')
	else:
		print(u'测试成功!')

# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
	count = 0

	def __init__(self, name):
		self.name = name
		Student.count = Student.count + 1

# 测试:
if Student.count != 0:
	print(u'测试失败!')
else:
	bart = Student('Bart')
	if Student.count != 1:
		print(u'测试失败!')
	else:
		lisa = Student('Bart')
		if Student.count != 2:
			print(u'测试失败!')
		else:
			print('Students:', Student.count)
			print(u'测试通过!')

class Screen(object):
	@property
	def resolution(self):
		return self.width * self.height	

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
	print(u'测试通过!')
else:
	print(u'测试失败!')

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

try:
	print('try...')
	r = 10 / 0
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
finally:
	print('finally...')
print('END')

try:
	print('try...')
	r = 10 / 2
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
else: 
	print('no error')
finally:
	print('finally...')
print('END')

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7')
    print('99 + 88 + 7.6 =', r)

print('*******************')
try:
	main()
except TypeError as e:
	print('except:TypeError  ', e)
except ValueError as e:
	print('except:ValueError  ', e)
else:
	print('main(): no Error...')
finally:
	print('main(): finally...')
print('main(): END')

def foo(s):
	n = int(s)
	print('>>> n = %d' % n)
	return 10 / n

def main():
	foo('1')

try:
	main()
except ZeroDivisionError as e:
	print('error in main: ', e)
else:
	print('no error')
finally:
	print('11')
print('end')


def fetch_data(url):
    with request.urlopen(url) as f:
    	data = json.loads(f.read().decode('utf-8'))
    	return data

# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
# print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
# Dont be afraid to use previous answers' functions in later answers :)
# (Thats why I included a couple functions you've already written at the beginning)
# (Reimplement them for practice)
# (or else)

#prelimA remove duplicates
def uniq(l):
	"""Return new version of l without any duplicates
	(you already did this)"""
	pass


#prelimB list has
def has(l, value):
	"""Return True if 'l' contains 'value', else false
	(you already did this)"""
	pass



#0 count element
def count_el(l, value):
	"""Returns number of times 'value' occurs in 'l'"""
	# example count_el([1,1,2,2,3,3,3,4,3,2,1], 2)  ->  3
	pass


#1 absolute value
def absolute(value):
	"""Return absolute value of 'value'"""
	# example absolute(-51)  ->  51
	# example absolute(51)  ->  51
	pass


#2 sum of list 
def sum_list(l):
	"""Return sum of all elements of 'l'"""
	# example: sum_list([1,2,3])  ->  6
	# example: sum_list([])  ->  0
	# example: sum_list([1,-1,1,-1])  ->  0
	pass


#3 abs of list
def absolute_list(l):
	"""return new list that is absolute value of every element in 'l'"""
	# example: absolute_list([-1,2,-3])  ->  [1,2,3]
	pass


#4 take greedily
def greedy_take(l, max_sum):
	"""Given some list of numbers 'l', and a value 'max_sum', make a new list, and add
	elements from 'l' to it until adding another element would make the sum of that new
	list exceed 'max_sum'"""
	# example greedy_take([1,3,5,7,9], 5)  ->  [1,3]    # taking 5 would make sum=9 which is > 5
	# example greedy_take([1,1,1,1,1,1,1], 3)  ->  [1,1,1]
	# example greedy_take([3,3,-5,3,3,-5,3,3,-5,7], 6)  ->  [3,3,-5,3]
	pass


#5 make all elements even
def evenify(l):
	"""Return new list that is the elements of 'l', except having added 1 to any odd-valued
	elements to make them even"""
	# example: evenify([1,2,3,4,5])  ->  [2,2,4,4,6]
	pass


#6 find index
def find_index(l, value):
	"""Return the index of the first instance of 'value' in 'l' if it exists, else return None"""
	# example: find_index([1,2,3], 2)  ->  1
	# example: find_index([1,2,3,2,2,2], 2)  ->  1
	# example: find_index([1,2,3], 4)  ->  None
	pass


#7 insert into sorted array
def insert_sorted(l, value):
	"""Takes 'l', a sorted list (smallest to largest), and some 'value', and inserts
	'value' into the correct place in 'l', then returns the the new 'l'.
	"""
	# example: insert_sorted([1,2,3,5,7,99], 6)  ->   [1,2,3,5,6,7,99]
	# example: insert_sorted([2,2,2], 2)  ->   [2,2,2,2]
	pass


#8 rotate right
def rotate_right(l, n):
	"""returns 'l' rotated right n times
	BONUS: make sure you never rotate more than 'len(l) - 1' times but still get the right answer
	"""
	# example: rotate_right([1,2,3,4], 1)  ->  [4,1,2,3]
	# example: rotate_right([1,2,3,4], 3)  ->  [2,3,4,1]
	# example: rotate_right([1,2,3,4], 4)  ->  [1,2,3,4]
	# example: rotate_right([1,2,3,4], 0)  ->  [1,2,3,4]
	pass


#9 interleave
def interleave(l, value):
	"""Puts 'value' between every two items in 'l'"""
	# example: interleave([1,2,3], 5)  ->  [1,5,2,5,3]
	# example: interleave([1,2], 5)  ->  [1,5,2]
	# example: interleave([1], 5)  ->  [1]
	# example: interleave([], 5)  ->  []
	pass


#10 list union
def union(l1, l2):
	"""This should take two lists, 'l1' & 'l2', and return a new list with ALL the 
	elements that occur in either (at least one) lists, excluding duplicates"""
	"""HINT: if you already wrote the code to remove duplicates from an array,
	make that code into a function and reuse it here."""
	# example: union([1,2,3], [2,2,3,4])  ->   [1,2,3,4]
	pass

	
#11 list intersection
def intersection(l1, l2):
	"""This should take two lists, 'l1' & 'l2', and return a new list with ONLY the 
	elements that occur in both lists, excluding duplicates"""
	# example: intersection([1,2,3], [2,2,3,4])  ->   [2,3]
	pass


#12 cartesian product
def cartesian_product(l1, l2):
	"""This should take two lists, 'l1' & 'l2', and return a new list-of-lists that
	is the cartesian product of the two lists 'l1' & 'l2'. A cartesian product of two
	lists is a list of all the pairs of items where the first item is from the one 
	list and the second item is from the second list.
	"""
	# example: intersection([1,2,3], [3,4])  ->   [ [1,3], [1,4], [2,3], [2,4], [3,3], [3,4] ]
	# example: intersection([3], [4])  ->   [ [3,4] ]
	# example: intersection([], [4])  ->   [ ]
	pass


#13 check if prefix
def is_prefix(s1, s2):
	"""Return True if 's2' is a prefix of 's1', otherwise False"""
	# example: is_prefix("abcd", "ab")  ->  True
	# example: is_prefix("abcd", "abc")  ->  True
	# example: is_prefix("abcd", "abcd")  ->  True
	# example: is_prefix("abcd", "bc")  ->  False
	# example: is_prefix("abcd", "xxx")  ->  False
	# example: is_prefix("abcd", "")  ->  True
	pass


#14 check if palindrome
def is_palindrome(s):
	"""return true if 's' is a palindrome, else false"""
	# example: is_palindrome("acbca")  ->  true
	# example: is_palindrome("")  ->  true
	# example: is_palindrome("abba")  ->  true
	# example: is_palindrome("abcd")  ->  false
	pass


#15 longest repeating character
def lrc(s):
	"""lrc takes 's', a string, and should return a single character, where that character is whichever occurs
	in the longest repeating sequence of a single character in 's' (example is clearer).
	If there is a tie return either.
	"""
	# example: lrc("acbacbaabbaaaaabbcccdefdef")  -> "a"
	# (because the longest repeating sequence of a single character is a)
	pass


#16 n'th fibonacci number
def fib(n):
	"""Return the n'th fibonnaci number
	Fibonnaci number n is defined as the sum of the previous two fibonnaci numbers (n-1 and n-2)
	fib(0) is defined as 0,
	fib(1) is defines as 1
	"""
	pass


#17 apply-to-all
def my_map(l, f):
	"""my_map will take two arguments, 'l' - a list, and 'f' - a function that takes and returns the
	same type as the elements of the list*.
	my_map should return a new list that is all the elements of 'l' with the function 'f' applied to them.

	*that is to say, if 'l' is a list of numbers, 'f' should take a single number as an argument, and return
	a single number.
	"""
	"""Example:
	def add_one(some_number):
		return some_number + 1

	my_map([1,2,3], add_one)  -> [2,3,4]
	"""
	pass


#18 use map
def absolute_list_2(l):
	"""Reimplement absolute_list (#3) using 'my_map' (#17) and 'absolute' (#1)"""
	pass

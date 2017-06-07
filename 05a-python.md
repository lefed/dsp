# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>>Answer Below:

**Q1 Breakdown -**

**How are Python lists and tuples similar and different?**
 
Lists and tuples in Python are similar in that they both are containers able to store values as a sequence of objects. Both can hold objects of any type.
 
Lists are mutable, however tuples are immutable meaning that you cannot change the elements or values in a tuple however you can index and revise the values in a list. This results in a difference in the methods able to be used on a list vs. a tuple. 
 
Tuples are created using parenthesis () and lists are created using square brackets [].
 
Example: 
 
_Create a tuple named t1 with values 4, 2:_
 
t1 = (4,2)
 
_Create a list named t1 with values 4,2:_
 
t1 = [4,2]
 
**Which will work as keys in dictionaries? Why?**
 
Only tuples will work as keys in dictionaries. This is because they are immutable (cannot be changed) vs. a list which is mutable and would allow for reassignment of keys in your dictionary. The fact that keys are immutable makes them efficient data structures for storing information and using it in a program because the keys are hashable - i.e. stored at a particular location that does not change and can therefore be accessed at this non changing location without searching. 



---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Answer below:

**Q2 Breakdown -**

**How are Python lists and sets similar and different?**
 
Lists and sets in Python are similar in that they both are containers able to store values as objects in a collection and are both mutable (unless a frozen set). 
 
They are different in that sets are unordered collections of mutable objects (frozen sets are unordered collections of immutable and hashable objects) and cannot contain duplicates vs. lists are ordered collections of mutable objects that can contain duplications. Because sets are an unordered collection, they do not record element position or information about order of insertion. They therefore do not support any sequence-like behaviour such as slicing or indexing.
 
Lists are created using square brackets [] and sets are created using curly brackets {}.
 
_sets_ allows you to do operations such as _intersection, union, difference,_ and _symmetric difference_, i.e operations of math's set theory. Sets doesn't allow indexing and are implemented on hash tables.

**Give examples of using both:**
 
_Sets Example:_ 
 
_Create an empty set:_
 
set()
 
_Creating a set of values 1,3,5,7,11,13,17_
 
primes1 = {1,3,5,7,11,13,17, 17}
print(primes1)
 
_Could give output_ 
 
{1,5,7,17,13,3,11}
 
_Lists Example:_ 
 
_Create an empty list:_
 
primes2 = []
 
_Creating a list of values 1,3,5,7,11,13,17,17_
 
primes2 = [1,3,5,7,11,13,17,17]
print(primes2)
 
_Gives output_ 
 
[1,3,5,7,11,13,17,17]
 
 
**How does performance compare between lists and sets for finding an element. Why?**
 
Sets are significantly faster for finding an element (i.e. determining if an element is present) however sets are slower than lists when it comes to iterating over their contents because they are not hashable and unordered. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Answer below:

The lambda operator or lambda function is used to create small anonymous functions, i.e. functions without a name. These functions are throw-away functions, i.e. they are just needed where they have been created. The expression “lambda arguments: expression” yields a function object. The unnamed object behaves like a function object defined with:
 
def<lambda>(arguments):
	Return expression
 
The general syntax of a lambda function is:
lambda argument_list: expression 
 
The argument list consists of a comma separated list of arguments and the expression is an arithmetic expression using these arguments. You can assign the function to a variable to give it a name. 
 
_Example: The following example of a lambda function returns the product of its two arguments:_
 
f_xy = lambda x, y : x*y
 
_Therefore_
f_xy(2,3)

_gives_

6
 
_More Examples: The following use of a lambda function within the key of sorted returns a sorted list with a customized key order based on the lambda functions:_
 
new_list = [0,2,333,4,-9, 67,89, -55]

new_list

_gives_

[0, 2, 333, 4, -9, 67, 89, -55]

sorted(new_list, key = lambda x: x>=0)

_gives_

[-9, -55, 0, 2, 333, 4, 67, 89]
 
new_words = ['THIS', 'IS', 'MY', 'list', 'of', 'words']

new_words

_gives_

['THIS', 'IS', 'MY', 'list', 'of', 'words']

sorted(new_words, key = lambda x: x.isupper()==1)

_gives_

['list', 'of', 'words', 'THIS', 'IS', 'MY']

sorted(new_words, key = lambda x: x.isupper()==0)

_gives_

['THIS', 'IS', 'MY', 'list', 'of', 'words']
 

_The result of the above sorting using lambda as a key is a bit confusing, however it is important to note two things:_

_1 - that what the lambda key is doing is giving a 0 or 1 value back for each of the list sets such that in new list when checking if >=0 on new_list you would get 1, 1, 1, 1, 0, 1, 1, 0 so really you are only looking to call sort on the values that are at the beginning of the transformed list - those that are 0s ie the negative values._

_2 - sorted is only called once so only the first two values are sorted and interestingly it seems to only sort via absollute values instead of actual distance from zero as would be understood by the mathematical notation._

---
### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>>>Answer below:

List comprehensions provide a concise way to create lists based on evaluations of an expression. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. List comprehensions always returns a result list.
 
_Examples of list comprehensions vs. filtering:_

_If you used to do it like this with a filter:_

old_list = [0,1,2,3,4,5,6]

just_evens = list(filter(lambda x: x%2 ==0, old_list))

just_evens

_gives_

[0,2,4,6]

less_than_five = list(filter(lambda x: x<5, old_list))

less_than_five

_gives_

[0,1,2,3,4]

_You can obtain the same thing using list comprehension:_

old_list1 = [0,1,2,3,4,5,6]

just_evens1 = [x for x in old_list1 if x%2 ==0]

just_evens1

_gives_

[0,2,4,6]

less_than_four = [x for x in old_list1 if x<4]

less_than_four

_gives_

[0,1,2,3]
 
_Examples of list comprehensions vs. mapping:_

If you used to do it like this with a map:

list_of_numbers = [1,1,1,1,1,2,2]

list2 = list(map(lambda x: x*2, list_of_numbers))

list2

_gives_

[2,2,2,2,2,4,4]

_You can do the same thing using list comprehension:_

second_list_of_numbers = [1,1,1,3,3]

list3 = [x*3 for x in second_list_of_numbers]

list3

_gives_

[3,3,3,9,9]
 
map() function

map() applies a function func to all the elements of a sequence seq. It returns a new list with the elements changed by func. The first argument func is the name of a function and the second a sequence (e.g. a list) seq. It is used as a way to map a change onto a set of elements and create a new set of elements with the new values.
 
**Python documentation:**
 
map(object):

map(func, *iterables) → map object

Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.
 
filter() function

The filter function takes an set of elements and keeps elements based on the evaluation of a function and filters out all other elements that do not meet the condition.
 
**Python documentation:**
 
filter(object):
 
filter(function or None, iterable) → filter object

Return an iterator yielding those items of iterable for which function (item) is true. If function is None, return the items that are true.

---
### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)






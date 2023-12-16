print("Hello World")
x = 5
y = "John"
print(x)
print(y)
def camelcase(list_words):  
    converted = "".join(word[0].upper() + word[1:].lower() for word in list_words)  
    return converted[0].lower() + converted[1:]  
  
words = ["Hello", "Welcome", "To", "Python", "Programming", "In", "Javatpoint"]  
print(camelcase(words))
x = 5
print(type(x))
print( 'This is not a comment' )
def add(x, y):  
    """This function adds the values of x and y"""  
    return x + y  
   
# Displaying the docstring of the add function   
print("Hyd")
print('scts')
# list of animals 
Animals= ["cat", "dog", "tiger"] 
# searching positiion of cat 
print(Animals.index("cat"))
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])
# Python code to demonstrate string length 
# using len
 
str = "reddy"
print(len(str))


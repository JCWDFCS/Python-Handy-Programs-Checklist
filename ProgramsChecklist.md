

#### Fibonacci:

> ### Yield
>
> Here's a simple `yield` based approach, to compute the fibonacci series, explained:
>
> ```python
> def fib(limit=50):
>     a, b = 0, 1
>     for i in range(limit):
>        yield b
>        a, b = b, a+b
> ```
>
> When you enter this into your REPL and then try and call it, you'll get a mystifying result:
>
> ```python
> >>> fib()
> <generator object fib at 0x7fa38394e3b8>
> ```
>
> This is because the presence of `yield` signaled to Python that you want to create a *generator*, that is, an object that generates values on demand.
>
> So, how do you generate these values? This can either be done directly by using the built-in function `next`, or, indirectly by feeding it to a construct that consumes values.
>
> Using the built-in `next()` function, you directly invoke `.next`/`__next__`, forcing the generator to produce a value:

> ### Memo:
>
> Onew solution is to keep track of values that have already been computed by storing them in a dictionary. A previously computed value that is stored for later use is called a memo. Here is a “memoized” version of fibonacci:
>
> ```python
> known = {0:0, 1:1}
>
> def fibonacci(n): 
>   if n in known: 
>     return known[n]
>   res = fibonacci(n-1) + fibonacci(n-2) 
>   known[n] = res 
>   return res
>
>
> ```
>



#### Dictionary Substraction

> Finding the words from the book that are not in the word list from words.txt is a problem you might recognize as set subtraction; that is, we want to find all the words from one set (the words in the book) that are not in the other (the words in the list).
>
> subtract takes dictionaries d1 and d2 and returns a new dictionary that contains all the keys from d1 that are not in d2. Since we don’t really care about the values, we set them all to None.
>
> ```python
> def subtract(d1, d2):
>     res = dict()
>     for key in d1:
>         if key not in d2:
>             res[key] = None
>     return res
> ```
>
> To find the words in the book that are not in words.txt, we can use `process_file` to build a histogram for words.txt, and then subtract:
>
> ```python
> words = process_file('words.txt')
> diff = subtract(hist, words)
>
> print("Words in the book that aren't in the word list:")
> for word in diff:
>     print(word, end=' ')
> ```
>
> 






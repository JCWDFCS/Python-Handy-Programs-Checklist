

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



#### Combine files:

[Python concatenate text files - Stack Overflow](https://stackoverflow.com/questions/13613336/python-concatenate-text-files/13613375#13613375)



> This should do it
>
> **For large files:**
>
> ```python
> filenames = ['file1.txt', 'file2.txt', ...]
> with open('path/to/output/file', 'w') as outfile:
>     for fname in filenames:
>         with open(fname) as infile:
>             for line in infile:
>                 outfile.write(line)
> ```
>
> **For small files:**
>
> ```python
> filenames = ['file1.txt', 'file2.txt', ...]
> with open('path/to/output/file', 'w') as outfile:
>     for fname in filenames:
>         with open(fname) as infile:
>             outfile.write(infile.read())
> ```
>
> **… and another interesting one that I thought of**:
>
> ```python
> filenames = ['file1.txt', 'file2.txt', ...]
> with open('path/to/output/file', 'w') as outfile:
>     for line in itertools.chain.from_iterable(itertools.imap(open, filnames)):
>         outfile.write(line)
> ```
>
> Sadly, this last method leaves a few open file descriptors, which the GC should take care of anyway. I just thought it was interesting

---

> Use `shutil.copyfileobj`. It should be more efficient.

> ```python
> with open('output_file.txt','wb') as wfd:
>     for f in ['seg1.txt','seg2.txt','seg3.txt']:
>         with open(f,'rb') as fd:
>             shutil.copyfileobj(fd, wfd, 1024*1024*10)
>             #10MB per writing chunk to avoid reading big file into memory.
> ```

> 
>
> ---
>
> would be a bit shorter:
>
> ```python
> import glob
> import fileinput
> import os
>
> pat = os.path.expanduser('~/Documents/*.md')
> with open('single-file.md', 'w') as fout:
>     for line in sorted(fileinput.input(glob.glob(pat))):
>         fout.write(line)
> ```


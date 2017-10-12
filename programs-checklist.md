

#### Km Per Liter

> Output:

> ```python
> The Kilometers Per Liter Program
> =============================================
> Please enter liters of gas used:	8
> Please enter kilometers driven: 	100
> Please enter cost per liter: 		6.3
> =============================================
> Kilometers Per Liter: 			12.5
> Cost Per 100Kms: 			50.4
>
> ```

> | 地 区                                      | 90号汽油      | 93号汽油      | 97号汽油      | 0号柴油 | 报价时间               |
> | ---------------------------------------- | ---------- | ---------- | ---------- | ---- | ------------------ |
> | [北京](http://ny.gold600.com/beijing.html) | 5.88(京89号) | 6.28(京92号) | 6.68(京95号) | 5.92 | 2017-10-4 10:50:10 |

> 中国车用汽油有无铅和含铅的两类。无铅的辛烷值有90、93和95RON(研究法)车用汽油三种。含铅的辛烷值有90、93和97RON三种。其中90号的铅含量不超过0.35g/L，93和97的铅含量不超过0.45g/L。
>
> ```
> 根据《北京市出租汽车价格标准》
> 3公里以内13元，基本单价每公里2.3元。燃油附加费每运次1元。23点（含）至次日5点（不含）运营时，基本单价加收20%的费用。
> 所以不论白天晚上3公里以内加上燃油附加费一共是14元。
> ```

> 1.6L排量的捷达,新车8个油,50元百公里.市区9个油.

#### Move files:

> 2017-10-02
>
> Move multiple files to
>
> 1. Change to the working directory
> 2. Filter(or select) files
> 3. Using pipes(command) to move single files
> 4. Using iterating to move multiple  

> Diagram Checklist 2017-10-01
>
> <img src='../images/python-handy-programs/move-files.JPG' width='500'>

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
>---
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



#### future value

> seperate the interest amount and the principle
>
> ```python
> def calculate_future_value(monthly_investment, yearly_interest_rate, years=20):
>     #convert the yearly values to monthly values.
>     print('Entering calculate_future_value():')
>     monthly_interest_rate = yearly_interest_rate / 12 / 100
>     months = years * 12
>     #calculate future value,initialize the future value.
>     future_value = 0.0
>     for i in range(0, months):
>         monthly_interest_amount = future_value * monthly_interest_rate
>         future_value += monthly_investment
>         future_value += monthly_interest_amount
>         print('month = ', i,'future value = ',round(future_value,2))
>         if i % 12 == 0:
>             print('year =', i/12, 'future value = ', round(future_value,2))
>     return future_value
> ```
>
> 

#### temperature

> The **Fahrenheit scale** is a [temperature scale](https://en.wikipedia.org/wiki/Scale_of_temperature) based on one proposed in 1724 by Amsterdam-based physicist [Daniel Gabriel Fahrenheit](https://en.wikipedia.org/wiki/Daniel_Gabriel_Fahrenheit) (1686–1736), after whom the scale is named.[[1\]](https://en.wikipedia.org/wiki/Fahrenheit#cite_note-1) It uses the **degree Fahrenheit** (symbol: °F) as the unit. Several accounts of how he originally defined his scale exist. The lower defining point, 0 °F, was established as the [temperature](https://en.wikipedia.org/wiki/Temperature) of a solution of [brine](https://en.wikipedia.org/wiki/Brine) made from equal parts of ice and salt. Further limits were established as the melting point of ice (32 °F) and his best estimate of the average [human body temperature](https://en.wikipedia.org/wiki/Human_body_temperature) (96 °F, about 2.6 °F less than the modern value due to a later redefinition of the scale).[[2\]](https://en.wikipedia.org/wiki/Fahrenheit#cite_note-2) The scale is now usually defined by two fixed points: the temperature at which [water](https://en.wikipedia.org/wiki/Water) freezes into [ice](https://en.wikipedia.org/wiki/Ice) is defined as 32 °F, and the boiling point of water is defined to be 212 °F, a 180 °F separation, as defined at sea level and standard atmospheric pressure.



### Problems:

循环结构的设置.

> ```python
> option = 'y'
>     while option.lower() == 'y':
>
> def main():
>     display_menu()
>     liters_used, kms_driven, cost_per_liter = get_entries()
>     km_per_liter, cost_per_km = calculate_results(liters_used, kms_driven, cost_per_liter)
>     cost_per_100kms = cost_per_km * 100
>     # display the result
>     print("=============================================")
>     print("Kilometers Per Liter: \t\t\t" + str(km_per_liter))
>     print("Cost Per 100Kms: \t\t\t" + str(cost_per_100kms))
>     print()
>     print('Bye')
>     option = input('Do you continue?:(Y/N) ')
>     if option == 'y':
>         continue
> ```
>
> 
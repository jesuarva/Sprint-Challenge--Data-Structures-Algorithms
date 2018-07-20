# Exercise I:

a. O(n^3)
b. O(logn)
c. O(n^(1/2)) -> O(√n)

d. O( nlogn )
d.1 for (i = 1; i < n; i `*=` 2) -> i = 2^m for 'm' in range(0,logn) -> n >= 2^m -> logn >= m -> O(logn)
d.2 for (j = 0; j < n; j++) -> O(n)

e. O( n^4 )
e.1 for (i = 0; i < n; i++) -> O(n)
e.2 for (j = i + 1; j < n; j++) -> O(n(n+1)/2)
e.3 for (k = j + 1; k < n; k++) -> O( 1/4 n (n^3 + 2 n^2 - n - 2) )
e.4 for (l = k + 1; l < 10 + k; l++) -> O( 13 n (n^3 + 2 n^2 - n - 2) )
e.3.1 https://www.wolframalpha.com/input/?i=13+n+(-2+-+n+%2B+2+n%5E2+%2B+n%5E3)&lk=1&assumption=%22ClashPrefs%22+-%3E+%7B%22Math%22%7D

f. O(n)
g. O(n)

# Exercise II

- Please go to `Answers.py` file.

# Exercise III

a. O( n(n+1)/2 ) -> O(n^2)
a.1 At every iteration we are passing to `quicksort()` the `greater` list with n-1 elements,
thus the number of iteration/runtime is a summatory like: sum\_(x=1)->n ( x ) = 1/2 n (n + 1)

b. O( logn ) , I guess.
b.1 Each iteration we are decresing the number of iterations by 2^m for `m` in range(0,logn)

# just-use-a-stack-bro
the stupidest way to evaluate prefix expressions ever.


the problem statement:
```
# Operations include: 
# 1. add x y -> returns x + y
# 2. mul x y -> returns x * y
# 3. sub x y -> returns x - y
# 4. neg x -> returns -x
# 5. inc x -> returns x + 1

# Example1: mul add 1 2 sub 5 1
# Ans1: (1 + 2) * (5 - 1) = 12

# Example2: add mul sub 3 2 inc 5 3
# Ans2: (3 - 2) * (5 + 1) + 3 = 9
```


### Running the code
All the parser files are here, just run
```
$ python parser.py
```

and then evaluate expressions as necessary 
```
REPL> add 3 4
7
```

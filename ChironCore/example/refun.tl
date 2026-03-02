// Recursion

to fact(:n) [	
	if :n == 0 [
		return 1
	] else [
		return :n * fact(:n - 1)
	]
]

assert(fact(5) == 120)

to fib(:n) [
	if :n == 0 [
		return 0
	] else [
		if :n == 1 [
			return 1
		] else [
			return fib(:n - 1) + fib(:n - 2)
		]
	]
]

assert(fib(5) == 5)
assert(fib(6) == 8)
assert(fact(fib(5)) == 120)

// Simple Function Declaration and Calls

to fun(:x, :y) [
	repeat 5 [
		goto(:x, :y)
		pendown
		forward 50
		penup
		:x = :x * 2
		:y = :y + :x
	]
	return void
]

to add(:a, :b) [
	:a = :a + :b
	return :a
]

:a = 3
:b = 4

fun(:a, :b)

goto(100, 100)
:b = add(:a, :b)

:a = add(67, 42)
assert(:a == 109)

fun(:a, :b)

// RHS evaluation in assignment

:a = add(5, 6) * add(7, 8)
assert(:a == 11 * 15)

goto(:a, :b)

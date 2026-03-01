to fun(:x, :y) [
	goto(:x, :y)
	pendown
	forward 50
	penup
	:x = :x * 2
	:y = :y + :x
	return
]

to add(:a, :b) [
	:a = :a + :b
	return :a
]

:a = 30
:b = 40

fun(:a, :b)

goto(100, 100)
:b = add(:a, :b)

print :a
:a = add(67, 42)
print :a

fun(:a, :b)

// TODO: add support for this
// :a = add(5, 6) * add(7, 8)

goto(:a, :b)
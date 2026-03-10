// Function redefintion not allowed

to add(:a, :b) [
	return :a + :b
]

:x = add(42, 42)

assert(:x == 84)

to add(:a, :b) [
	return :a * :b
]

// Control won't reach here
:x = add(6, 7)

assert(:x == 42)


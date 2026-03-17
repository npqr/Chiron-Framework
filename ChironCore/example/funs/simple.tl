to fun(:a, :b) [
    return :a + :b
]

:x = 5
:y = 6
:z = fun(:x, :y)
assert (:z == 11)
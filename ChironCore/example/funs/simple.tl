to fun(:a, :b) [
    return :a + :b
]

//to main() [

:x = 5
:y = 6

:z = 5 * fun(:x, :y) * fun(1, 2)
print(:z)
assert (:z == 165)

:z = fun(:x, :y)
print(:z)
assert(:z == 11)

:z = fun(fun(1, 2), 3)
print(:z)
assert(:z == 6)

//return void
//]

//main()
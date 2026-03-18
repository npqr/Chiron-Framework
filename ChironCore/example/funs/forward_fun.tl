to fun(:a, :b) [
    :x = add(:a, :b)
    :y = mul(:a, :b)
    return add(:x, 5)
]

to add(:p, :q) [
    return :p + :q
]

to mul(:a, :b) [
    return :a * :b
]

fun(6, 7)
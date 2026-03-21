to fun(:a, :b) [
    :x = add(:a, :b)
    :y = mul(:a, :b)

    print(:x)
    // not supported
    to foo(:p, :q) [
        return :p + :q
    ]

    :x = foo(:x, :a)
    print(:x)
    return :x
]

to add(:p, :q) [
    return :p + :q
]

to mul(:a, :b) [
    return :a * :b
]

:xx = fun(6, 7)
print(:xx)
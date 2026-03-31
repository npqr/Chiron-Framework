:x = 10

to funy() [
    global :x
    return :x + 10
]

assert(funy() == 20)

to funx() [
    global :x
    :x = 10
    return void
]

funx()
assert(:x == 10)
// Using function calls inside control structures

:arr0 = 3
:arr1 = 7
:arr2 = 12
:arr3 = 18
:arr4 = 29
:arr5 = 31
:arr6 = 47

:n = 7

to valueAt(:i) [
    if :i == 0 [ return :arr0 ]
    if :i == 1 [ return :arr1 ]
    if :i == 2 [ return :arr2 ]
    if :i == 3 [ return :arr3 ]
    if :i == 4 [ return :arr4 ]
    if :i == 5 [ return :arr5 ]
    if :i == 6 [ return :arr6 ]
    return -1
]

to isGreater(:a, :b) [
    if :a > :b [ return 1 ]
    return 0
]

print(isGreater(5, 3)) // 1
print(isGreater(2, 4)) // 0

print(valueAt(3)) // 18

to bs(:low, :high, :key) [
    if :low > :high [ return -1 ]

    :mid = (:low + :high) / 2
    
    print(:low)
    print(:high)
    print(:mid)
    print(:key)

    if (valueAt(:mid) == :key) [ return :mid ]
    
    if (isGreater(:key, valueAt(:mid))) [
        return bs(:mid + 1, :high, :key)
    ] else [
        return bs(:low, :mid - 1, :key)
    ]
]

:idx = bs(0, :n - 1, 18)
print(:idx) // 3
assert(:idx == 3)

:idx = bs(0, :n - 1, 47)
assert(:idx == 6)

/* not supported yet
:x = (:idx == 6)
print(:x)
*/

/*
:idx = bs(0, :n - 1, 19)
assert(:idx == -1)
*/
# testing python's dis module to see the IR for a simple code snippet

import dis

code = """
prefix = "Hello"
def greet(name):
    return prefix + " " + name
a = 10
x = greet("World")
y = a * 2

def fun(x, y):
    return x + y

fun(5, 6)
a = fun(x, 3) * fun(a, x)
"""

# Show the IR for the top-level (Normal code)
print("--- Module Level IR ---")
dis.dis(code, show_caches=True)

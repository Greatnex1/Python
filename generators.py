# generators are iterators
# in place of return yield is used
def generate_up_to_down(num):
    start = 1
    while start <= num:
        yield start
        start += 1
        # yield "spoop"


gen = generate_up_to_down(10)
gen_exp = (num for num in range(1, 11))
print("Gen exp", gen_exp)
print(next(gen))

print(next(gen))
print(next(gen))

print(list(gen))

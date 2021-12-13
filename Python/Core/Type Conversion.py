
# %% Example
x = input("x: ")
print(type(x))
y = int(x) + 1
print(f"x: {x} ,y: {y}")

print(int(x))
print(float(x))
print(bool(x))
print(str(x))


# Falsy
# ""
# 0
# None

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(""))
print(bool("False"))

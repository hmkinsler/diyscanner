def hash_square(x):
    y = x
    while y > 0:
        print("#" * x)
        y -= 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)
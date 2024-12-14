def print_sequence(n):
    if n < 0:
        return


    print(n, end="")

    print_sequence(n - 1)
    if n > 0:
        print(n,  end="")


print_sequence(5)
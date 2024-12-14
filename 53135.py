def print_sequence(n):
    if n <= 0:
        return
    print(n, ends="")
    if n!= 1:
        print_sequence

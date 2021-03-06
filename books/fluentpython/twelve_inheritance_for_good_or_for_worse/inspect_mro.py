def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))

def main():
    print_mro(bool)
    print_mro(int)
    import numbers
    print_mro(numbers.Integral)
    import io
    print_mro(io.BytesIO)

if __name__=="__main__":
    main()


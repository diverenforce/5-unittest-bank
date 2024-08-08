def main():
    greeting = input("Greeting: ")
    print(f'${value(greeting)}')

def value(greeting):
    if greeting.strip().casefold().startswith('hello'):
        return 0
    elif greeting.strip().casefold().startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
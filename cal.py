def calculate_area(radius):
    area = 3.14 * radius ** 2
    unused_variable = 42  # Unused variable
    return area

def main():
    RADIUS = 5  # Constants should be in uppercase
    area = calculate_area(RADIUS)
    print("Area:", area)

    # Poor error handling: catching a broad exception
    try:
        result = 10 / 0  # This will cause a ZeroDivisionError
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()


def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """

    max_value = max(numbers)
    print("time to create some conflict")
    return max_value


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = []

    for item in a:
        if item < 0:
            result.append(abs(item))  # |item|
        # if abs(item) in cache:
        #     cache[abs(item)] += 1
        #     if item[abs(item)] > 1:
        #         result.append(abs(item))
        # else:
        #     cache[item] = 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

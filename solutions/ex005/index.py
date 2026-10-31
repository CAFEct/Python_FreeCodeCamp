def square_root_bisection(number, tolerance=0.0001, max_iterations=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0:
        print(f"The square root of 0 is 0")
        return 0
    elif number == 1:
        print(f"The square root of 1 is 1")
        return 1

    # Set up the bisection search bounds
    if number >= 1:
        low, high = 0, number
    else:
        low, high = number, 1

    for i in range(max_iterations):
        mid = (low + high) / 2
        square = mid * mid

        # Check if we've converged (difference between bounds is within tolerance)
        if (high - low) <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid

        # Adjust bounds based on whether mid^2 is too high or too low
        if square < number:
            low = mid
        else:
            high = mid

    print(f"Failed to converge within {max_iterations} iterations")
    return None

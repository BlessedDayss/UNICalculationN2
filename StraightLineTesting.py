import numpy as np
def test_point_slope(a, c, num_points=100, x_min=0, x_max=10):
    def f(x):
        return 4 * x + 1
    f_c = f(c)
    x_points = np.random.uniform(x_min, x_max, num_points)

    all_passed = True
    tolerance = 1e-10

    print(f"Testing {num_points} random points in interval [{x_min}, {x_max}]")
    print(f"Fixed point: c = {c}, f(c) = {f_c}")
    print(f"Expected slope: a = {a}\n")

    failed_count = 0

    for i, x_i in enumerate(x_points):
        if abs(x_i - c) < tolerance:
            continue
        calculated_slope = (f(x_i) - f_c) / (x_i - c)

        if abs(calculated_slope - a) > tolerance:
            if failed_count < 5:
                print(f"FAILED at point {i + 1}: x = {x_i:.4f}, "
                      f"calculated slope = {calculated_slope:.6f}")
            failed_count += 1
            all_passed = False

    if all_passed:
        print(f"Tests: {num_points}")
        print(f"The condition (f(x_i) - f(c))/(x_i - c) = {a} holds for all points.\n")
    else:
        print(f"✗ {failed_count} Tests FAILED out of {num_points}\n")

    return all_passed

result = test_point_slope(a=4, c=2, num_points=100, x_min=0, x_max=10)
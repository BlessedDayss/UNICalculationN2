import numpy as np

def interpolate(y_measurements, delta_t, t):
    i = int(t / delta_t)


    if i < 0:
        return y_measurements[0]
    if i >= len(y_measurements) - 1:
        return y_measurements[-1]
    t_i = i * delta_t
    t_i_plus_1 = (i + 1) * delta_t
    y_interpolated = y_measurements[i] + \
                     (y_measurements[i + 1] - y_measurements[i]) * \
                     (t - t_i) / (t_i_plus_1 - t_i)

    return y_interpolated


def find_y(y_measurements, delta_t):
    n = len(y_measurements) - 1
    max_time = n * delta_t

    print(f"Enter time in range [0, {max_time}] (negative to exit):")

    while True:
        try:
            t = float(input("Time t (min): "))

            if t < 0:
                break

            if t > max_time:
                print(f"Warning: t exceeds maximum time {max_time}")

            y_value = interpolate(y_measurements, delta_t, t)
            print(f"Interpolated value at t = {t} min: y = {y_value:.4f}\n")

        except ValueError:
            print("Invalid input. Please enter a number.\n")


measurements = np.array([4.4, 2.0, 11.0, 21.5, 7.5])
delta_t = 1.0
t1 = 2.5
t2 = 3.1

y1 = interpolate(measurements, delta_t, t1)
y2 = interpolate(measurements, delta_t, t2)

print("\nCALCULATION:")
print(f"\nMeasurements: {measurements}")
print(f"Times: 0, 1, 2, 3, 4 (min)\n")
print(f"At t = {t1} min: y = {y1:.4f}")
print(f"At t = {t2} min: y = {y2:.4f}\n")

print("\nInteractive mode:")
find_y(measurements, delta_t)
import adafruit_bno055
import board
import time


def round_tuple_values(tuple, amount):
    """
    Round values within tuples, add them to a list, and return.

    :param tuple: tuple being rounded
    :param amount: number of decimals to round to
    :return: list with all values of tuple rounded to amount
    """
    tuple_list = []
    for value in tuple:
        if value is None:
            tuple_list.append("None.")
        else:
            tuple_list.append(round(value, amount))

    return tuple_list


def print_imu(sensor, interval):
    """
    Print out the values of a passed adafruit_bno055 sensor every interval (in seconds).

    :param sensor: adafruit_bno055 sensor
    :param interval: frequency in seconds to print information
    :return: nothing
    """
    while True:
        print(f"Temperature: {sensor.temperature} "
              f"\tEuler: {round_tuple_values(sensor.euler, 2)} "
              f"\tGravity: {round_tuple_values(sensor.gravity, 2)}")
        time.sleep(interval)


if __name__ == '__main__':
    i2c = board.I2C()
    sensor = adafruit_bno055.BNO055_I2C(i2c)
    print_imu(sensor, 0)


import requests
import math


def turbine_status(wind_speed):
    if wind_speed < 3:
        return "Off"
    if wind_speed >= 3:
        return "On"


# Need to add cutin / cutout speed
def power_output(wind_speed, sweep=15, coefficient_of_performance=0.4):
    # P = 0.5Apv^3(COP)
    return (0.5 * sweep * 1.2 * wind_speed ** 3) * coefficient_of_performance

"""
Company: Juniper Networks


Calculate the angle between hour hand and minute hand

This problem is know as Clock angle problem where we need to find angle between hands of an analog clock at a given time.

Input:  h = 12:00, m = 30.00
Output: 165 degree

Input:  h = 3.00, m = 30.00
Output: 75 degree


https://www.geeksforgeeks.org/calculate-angle-hour-hand-minute-hand/
https://en.wikipedia.org/wiki/Clock_angle_problem


Clock angle problems relate two different measurements: angles and time.
The angle is typically measured in degrees from the mark of number 12 clockwise.
The time is usually based on 12-hour clock.

A method to solve such problems is to consider the rate of change of the angle in degrees per minute.
 *** The hour hand of a normal 12-hour analogue clock turns 360° in 12 hours (720 minutes) or 0.5° per minute. ***
*** The minute hand rotates through 360° in 60 minutes or 6° per minute. ****

Hours hand
-----------
12 hrs = 360°
1 hr = 360°/12 = 30°
1 min = 30°/60 = 0.5°

Minutes hand
------------
60 mins = 360°
1 min = 360°/60 = 6°

The idea is to take 12:00 (h = 12, m = 0) as a reference. Following are detailed steps.

1) Calculate the angle made by hour hand with respect to 12:00 in h hours and m minutes.
2) Calculate the angle made by minute hand with respect to 12:00 in h hours and m minutes.
3) The difference between two angles is the angle between two hands.

"""

def calc_angle(hours, mins):
    if hours > 12 or hours < 0 or mins > 60 or mins < 0:
        print("Invalid input")
        return

    if hours == 12:
        hours = 0
    if mins == 60:
        mins = 0

    hour_angle = 0.5 * (hours * 60 + mins)
    mins_angle = 6 * mins

    angle = abs(hour_angle - mins_angle)

    # Return smaller angle of possible angles - right angle or left angle
    # (Imagine 11:40)
    angle = min(360 - angle, angle)

    return angle

if __name__ == '__main__':
    print(calc_angle(9, 10))
    print(calc_angle(9, 40))
    print(calc_angle(12, 40))
    print(calc_angle(1, 10))

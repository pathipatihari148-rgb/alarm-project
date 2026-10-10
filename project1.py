import winsound
from datetime import datetime
import time

alarm_time = input("Enter alarm time (HH:MM:SS): ")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time == alarm_time:
        print("Wake up!")
        winsound.Beep(10000, 20000)
        break

    time.sleep(1)
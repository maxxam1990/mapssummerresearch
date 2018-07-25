import csv
import time
from selenium import webdriver

url = 'https://www.google.com/maps/dir/Elizabeth,+NJ/40.775968,-73.9612638/@40.7580619,-74.3537463,10z/data=!3m1!4b1!4m9!4m8!1m5!1m1!1s0x89c24d5fee42051d:0x3285591b526b03ad!2m2!1d-74.2107006!2d40.6639916!1m0!3e0'
browser = webdriver.Chrome()


def grabAndSave():
    browser.get(url)
    nav = browser.find_elements_by_class_name("section-directions-trip-description")

    for i in range(0, 3):
        data = (nav[i].text).splitlines()  # Splits str at every new line
        print(data)
        print(readable)
        writer.writerow({'Route Number': (i+1), 'ETA': data[0], 'Distance': data[1], 'Route': data[2], 'Time': readable})


with open('googleMapsData.csv', 'w', newline='') as csvfile:
    fieldnames = ['Route Number', 'ETA', 'Distance', 'Route', 'Time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    try:
        while True:
            ts = time.time()
            readable = time.ctime(ts)
            grabAndSave()
            time.sleep(10)  # 298 second day, gives 2 seconds for the program to run
    except KeyboardInterrupt:
        print("\n\nStopped by KEYBOARD INTERRUPTION\n\n")
        pass

browser.close()

import csv
import time
from selenium import webdriver

url = 'https://www.waze.com/livemap?zoom=17&lat=40.78306&lon=-73.97125&from_lat=40.66901&from_lon=-74.21812&to_lat=40.78306&to_lon=-73.97125&at_req=0&at_text=Now'
browser = webdriver.Chrome()


def grabAndSave():
    browser.get(url)
    time.sleep(20)
    nav = browser.find_element_by_class_name("route-info")
    data = (nav.text).splitlines()  # Splits str at every new line
    length = browser.find_element_by_class_name("route-length")
    length_data = (length.text).splitlines()
    eta = browser.find_element_by_class_name("route-time")
    eta_data = (eta.text).splitlines()
    ts = time.time()
    readable = time.ctime(ts)
    print(data)
    print("Miles: " + length_data[0] + " | Duration: " + eta_data[0] + " | Route: " + data[0])
    print(readable)
    writer.writerow({'ETA': eta_data[0], 'Distance': length_data[0], 'Route': data[0], 'Time': readable})


with open('wazeMapsData.csv', 'w', newline='') as csvfile:
    fieldnames = ['ETA', 'Distance', 'Route', 'Time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    try:
        while True:
            grabAndSave()
            time.sleep(10)  # 298 second day, gives 2 seconds for the program to run
    except KeyboardInterrupt:
        print("\nStopped by KEYBOARD INTERRUMPTION\n\n")
        pass

browser.close()

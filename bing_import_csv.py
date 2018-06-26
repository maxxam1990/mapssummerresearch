import csv
import time
from selenium import webdriver

url = 'https://www.bing.com/maps?osid=4ee7d2ae-d2fc-4f1d-b61e-043c9ff64314&cp=40.776661~-74.262416&lvl=10&v=2&sV=2&form=S00027'
browser = webdriver.Chrome()

def grabAndSave():
    browser.get(url)
    time.sleep(15)
    nav = browser.find_element_by_class_name("drTitle")
    data = (nav.text).splitlines()  # Splits str at every new line
    ts = time.time()
    readable = time.ctime(ts)
    print(data)
    print("Duration: " + data[0] + data[2] + data[3] + " | Route: " + data[7] + " | Miles: " + data[8])
    print(readable)
    writer.writerow({'ETA': data[0] + data[2] + data[3], 'Distance': data[8], 'Route': data[7], 'Time': readable})

with open('bingMapsData.csv', 'w', newline='') as csvfile:
    fieldnames = ['ETA', 'Distance', 'Route', 'Time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    try:
        while True:
            grabAndSave()
            time.sleep(10) # 298 second day, gives 2 seconds for the program to run
    except KeyboardInterrupt:
        print("\n\nStopped by KEYBOARD INTERRUMPTION\n\n")
        pass

browser.close()
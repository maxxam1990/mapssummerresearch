import csv
import time
from selenium import webdriver

url = 'https://www.waze.com/livemap?zoom=17&lat=40.78306&lon=-73.97125&from_lat=40.66901&from_lon=-74.21812&to_lat=40.78306&to_lon=-73.97125&at_req=0&at_text=Now'
browser = webdriver.Chrome()


def grabAndSave():
    browser.get(url)
    time.sleep(25)
    nav = browser.find_elements_by_class_name("wm-route-list__routes")


    # Route 1 data
    # Route info
    route1 = browser.find_element_by_xpath("//*[@id='map']/div[2]/div/div/div[3]/div[2]/div/div/a[1]/div[2]")
    route1data = (route1.text).splitlines()
    # Distance info
    distance1 = browser.find_element_by_xpath("//*[@id='map']/div[2]/div/div/div[3]/div[2]/div/div/a[1]/div[1]/div[2]")
    distance1data = (distance1.text).splitlines()
    # Time info
    time1 = browser.find_element_by_xpath("//*[@id='map']/div[2]/div/div/div[3]/div[2]/div/div/a[1]/div[1]/div[1]")
    time1data = (time1.text).splitlines()

    # Route 2 data
    # Route info
    route2 = browser.find_element_by_xpath("//*[@id='map']/div[2]/div/div/div[3]/div[2]/div/div/a[2]/div[2]")
    route2data = (route2.text).splitlines()
    # Distance info
    distance2 = browser.find_element_by_xpath("//*[@id='map']/div[2]/div/div/div[3]/div[2]/div/div/a[2]/div[1]/div[2]")
    distance2data = (distance2.text).splitlines()
    # Time info
    time2 = browser.find_element_by_xpath("//*[@id='map']/div[2]/div/div/div[3]/div[2]/div/div/a[2]/div[1]/div[1]")
    time2data = (time2.text).splitlines()

    # Route 3 data
    # Route info
    route3 = browser.find_element_by_xpath("//*[@id='map']/div[2]/div/div/div[3]/div[2]/div/div/a[3]/div[2]")
    route3data = (route3.text).splitlines()
    # Distance info
    distance3 = browser.find_element_by_xpath("//*[@id='map']/div[2]/div/div/div[3]/div[2]/div/div/a[3]/div[1]/div[2]")
    distance3data = (distance3.text).splitlines()
    # Time info
    time3 = browser.find_element_by_xpath("//*[@id='map']/div[2]/div/div/div[3]/div[2]/div/div/a[3]/div[1]/div[1]")
    time3data = (time3.text).splitlines()

    # Print all 3 routes to confirm info
    print("ETA: " + time1data[0] + " | Distance: " + distance1data[0] + " | Route: " + route1data[0])
    print("ETA: " + time2data[0] + " | Distance: " + distance2data[0] + " | Route: " + route2data[0])
    print("ETA: " + time3data[0] + " | Distance: " + distance3data[0] + " | Route: " + route3data[0])
    print(readable)
    
    # Write to csv file
    writer.writerow({'Route Number': 1, 'ETA': time1data[0], 'Distance': distance1data[0], 'Route': route1data[0], 'Time': readable})
    writer.writerow({'Route Number': 2, 'ETA': time2data[0], 'Distance': distance2data[0], 'Route': route2data[0], 'Time': readable})
    writer.writerow({'Route Number': 3, 'ETA': time3data[0], 'Distance': distance3data[0], 'Route': route3data[0], 'Time': readable})


with open('wazeMapsData.csv', 'w', newline='') as csvfile:
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
        print("\nStopped by KEYBOARD INTERRUPTION\n\n")
        pass

browser.close()

import csv
import time
from selenium import webdriver

url = 'https://wego.here.com/directions/drive/I-95,-Fredericksburg,-VA-22405,-United-States:38.34009,-77.49205/I-95,-Springfield,-VA-22150,-USA:loc-dmVyc2lvbj0xO3RpdGxlPUktOTU7bGF0PTM4Ljc0MDMyMjtsb249LTc3LjE4OTYwODtzdHJlZXQ9SS05NTtjaXR5PVNwcmluZ2ZpZWxkO3Bvc3RhbENvZGU9MjIxNTA7Y291bnRyeT1VU0E7ZGlzdHJpY3Q9U3ByaW5nZmllbGQ7c3RhdGVDb2RlPVZBO2NvdW50eT1GYWlyZmF4O2NhdGVnb3J5SWQ9c3RyZWV0LXNxdWFyZTtzb3VyY2VTeXN0ZW09aW50ZXJuYWw?map=38.54051,-77.34086,11,normal&avoid=carHOV'
browser = webdriver.Chrome()

def grabAndSave():
    browser.get(url)
    time.sleep(5)
    
    # Selects route 1 (unique) and retrieves route info        
    nav = browser.find_element_by_xpath("//*[@id='routes_list']/div[2]/ul/li[1]/div/div[2]/div[3]/span[3]")
    data = (nav.text).splitlines()

    #Retrieves time data from Route 1
    time1 = browser.find_element_by_xpath("//*[@id='routes_list']/div[2]/ul/li[1]/div/div[2]/div[1]/span/span[1]")
    timedata1 = (time1.text).splitlines()

    #Retrieves distance data from Route 1
    distance1 = browser.find_element_by_xpath("//*[@id='routes_list']/div[2]/ul/li[1]/div/div[2]/div[3]/span[1]")
    distancedata1 = (distance1.text).splitlines()
    
    #Prints out Route 1 results
    print("Route: " + data[0] +" | Time: " + timedata1[0] + " | Distance: " + distancedata1[0])
    
    # Prepare clicker for route 2
    check1 = False;
    try:
        check1 = browser.find_element_by_xpath("//*[@id='routes_list']/div[2]/ul/li[2]/div/div[2]/div[3]/span[3]")
    except:
        print("There is no route 2 this time!")

    if (check1):
        # Gets route info from route 2
        nav1 = browser.find_element_by_xpath("//*[@id='routes_list']/div[2]/ul/li[2]/div/div[2]/div[3]/span[3]")
        data1 = (nav1.text).splitlines()

        #Retrieves time data from Route 2
        time2 = browser.find_element_by_xpath("//*[@id='routes_list']/div[2]/ul/li[2]/div/div[2]/div[1]/span/span[1]")
        timedata2 = (time2.text).splitlines()

        #Retrieves distance data from Route 2
        distance2 = browser.find_element_by_xpath("//*[@id='routes_list']/div[2]/ul/li[2]/div/div[2]/div[3]/span[1]")
        distancedata2 = (distance2.text).splitlines()

        #Prints out Route 2 results
        print("Route: " + data1[0] +" | Time: " + timedata2[0] + " | Distance: " + distancedata2[0])

    # Prepare Clicker for Route 3
    check2 = False;
    try:
        check2 = browser.find_element_by_xpath("//*[@id='routes_list']/div[2]/ul/li[3]/div/div[2]/div[3]/span[3]")
    except:
        print("There is no route 3 this time!")
    # Check if there is a route 3 available
    if (check2):
        # Get route info from Route 3
        nav2 = browser.find_element_by_xpath("//*[@id='routes_list']/div[2]/ul/li[3]/div/div[2]/div[3]/span[3]")
        data2 = (nav1.text).splitlines()
        #Retrieves time data from Route 1
        time3 = browser.find_element_by_xpath("//*[@id='routes_list']/div[2]/ul/li[3]/div/div[2]/div[1]/span")
        timedata3 = (time3.text).splitlines()
        #Retrieves distance data from Route 1
        distance3 = browser.find_element_by_xpath("//*[@id='routes_list']/div[2]/ul/li[3]/div/div[2]/div[3]/span[1]")
        distancedata3 = (distance3.text).splitlines()
        #Prints out Route 1 results
        print("Route: " + data2[0] +" | Time: " + timedata3[0] + " | Distance: " + distancedata3[0])

    print(readable)
    writer.writerow({'Route Number': 1, 'ETA': timedata1[0] + " min", 'Distance': distancedata1[0], 'Route': data[0], 'Time': readable})
    if (check1):
        writer.writerow({'Route Number': 2,'ETA': timedata2[0] + " min", 'Distance': distancedata2[0], 'Route': data1[0], 'Time': readable})
    if (check2):
        writer.writerow({'Route Number': 3,'ETA': timedata3[0] + " min", 'Distance': distancedata3[0], 'Route': data2[0], 'Time': readable})
    print ("Cycle completed\n\n")

with open('hereMapsDataDC.csv', 'w', newline='') as csvfile:
    fieldnames = ['Route Number', 'ETA', 'Distance', 'Route', 'Time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    try:
        while True:
            ts = time.time()
            readable = time.ctime(ts)
            grabAndSave()
            time.sleep(1) # 298 second day, gives 2 seconds for the program to run
    except KeyboardInterrupt:
        print("\n\nStopped by KEYBOARD INTERRUMPTION\n\n")
        pass

browser.close()
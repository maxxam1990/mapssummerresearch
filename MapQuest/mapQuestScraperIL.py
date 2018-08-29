import csv
import time
from selenium import webdriver

url = 'https://www.mapquest.com/directions/from/near-41.813766,-87.629745/to/near-41.982496,-87.801521'
browser = webdriver.Chrome()

def grabAndSave():
    browser.get(url)
    time.sleep(3)

    # Click on route 2
    click = False;
    try:
        click = browser.find_element_by_xpath("//*[@id='primaryPanel']/div[8]/div[1]/div/div[2]/div[1]/form/div[2]/div/div/ol/li[1]")
    except:
        # Selects route 1 (unique) and retrieves route info        
        nav = browser.find_element_by_xpath("//*[@id='primaryPanel']/div[8]/div[1]/div/div[2]/div[1]/form/div[2]/div/div/div/route-info/div/div[2]/div[1]")
        data = (nav.text).splitlines()

        #Retrieves time data from Route 1
        time1 = browser.find_element_by_xpath("//*[@id='primaryPanel']/div[8]/div[1]/div/div[2]/div[1]/form/div[2]/div/div/div/route-info/div/div[2]/div[2]/span[1]")
        timedata1 = (time1.text).splitlines()

        #Retrieves distance data from Route 1
        distance1 = browser.find_element_by_xpath("//*[@id='primaryPanel']/div[8]/div[1]/div/div[2]/div[1]/form/div[2]/div/div/div/route-info/div/div[2]/div[2]/div")
        distancedata1 = (distance1.text).splitlines()
    
    if (click):
        # Selects route 1 and retrieves route info
        nav = browser.find_element_by_class_name("container-fluid")
        data = (nav.text).splitlines()

        #Retrieves time data from Route 1
        time1 = browser.find_element_by_xpath("//*[@id='primaryPanel']/div[8]/div[1]/div/div[2]/div[1]/form/div[2]/div/div/div/route-info/div/div[2]/div[2]/span[1]")
        timedata1 = (time1.text).splitlines()
        
        #Retrieves distance data from Route 1
        distance1 = browser.find_element_by_xpath("//*[@id='primaryPanel']/div[8]/div[1]/div/div[2]/div[1]/form/div[2]/div/div/div/route-info/div/div[2]/div[2]/div")
        distancedata1 = (distance1.text).splitlines()
    
    #Prints out Route 1 results
    print("Route: " + data[0] +" | Time: " + timedata1[0] + " | Distance: " + distancedata1[0])
    
    # Prepare clicker for route 2   

    # Click on route 2
    click1 = False;
    try:
	    click1 = browser.find_element_by_xpath("//*[@id='primaryPanel']/div[8]/div[1]/div/div[2]/div[1]/form/div[2]/div/div/ol/li[2]")
    except:
    	print("There is no route 2 this time!")

    if (click1):
	    # Click on route 2
	    click1.click()

	    # Gets route info from route 2
	    nav1 = browser.find_element_by_class_name("container-fluid")
	    data1 = (nav1.text).splitlines()

	    #Retrieves time data from Route 2
	    time2 = browser.find_element_by_xpath("//*[@id='primaryPanel']/div[8]/div[1]/div/div[2]/div[1]/form/div[2]/div/div/div/route-info/div/div[2]/div[2]/span[1]")
	    timedata2 = (time2.text).splitlines()

	    #Retrieves distance data from Route 2
	    distance2 = browser.find_element_by_xpath("//*[@id='primaryPanel']/div[8]/div[1]/div/div[2]/div[1]/form/div[2]/div/div/div/route-info/div/div[2]/div[2]/div")
	    distancedata2 = (distance2.text).splitlines()

	    #Prints out Route 2 results
	    print("Route: " + data1[0] +" | Time: " + timedata2[0] + " | Distance: " + distancedata2[0])

    # Prepare Clicker for Route 3
    click2 = False;
    try:
        click2 = browser.find_element_by_xpath("//*[@id='primaryPanel']/div[8]/div[1]/div/div[2]/div[1]/form/div[2]/div/div/ol/li[3]")
    except:
        print("There is no route 3 this time!")
    # Check if there is a route 3 available
    if (click2):
        # Click on Route 3
        click2.click()
        # Get route info from Route 3
        nav2 = browser.find_element_by_class_name("container-fluid")
        data2 = (nav2.text).splitlines()
        #Retrieves time data from Route 1
        time3 = browser.find_element_by_xpath("//*[@id='primaryPanel']/div[8]/div[1]/div/div[2]/div[1]/form/div[2]/div/div/div/route-info/div/div[2]/div[2]/span[1]")
        timedata3 = (time3.text).splitlines()
        #Retrieves distance data from Route 1
        distance3 = browser.find_element_by_xpath("//*[@id='primaryPanel']/div[8]/div[1]/div/div[2]/div[1]/form/div[2]/div/div/div/route-info/div/div[2]/div[2]/div")
        distancedata3 = (distance3.text).splitlines()
        #Prints out Route 1 results
        print("Route: " + data2[0] +" | Time: " + timedata3[0] + " | Distance: " + distancedata3[0])

    print(readable)
    writer.writerow({'Route Number': 1, 'ETA': timedata1[0], 'Distance': distancedata1[0], 'Route': data[0], 'Time': readable})
    if (click1):
	    writer.writerow({'Route Number': 2,'ETA': timedata2[0], 'Distance': distancedata2[0], 'Route': data1[0], 'Time': readable})
    if (click2):
        writer.writerow({'Route Number': 3,'ETA': timedata3[0], 'Distance': distancedata3[0], 'Route': data2[0], 'Time': readable})
    print ("Cycle completed\n\n")

with open('mapQuestDataIL.csv', 'w', newline='') as csvfile:
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
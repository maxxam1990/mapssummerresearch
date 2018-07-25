import csv
import time
from selenium import webdriver

url = 'https://wego.here.com/directions/drive/310-Morris-Ave,-Elizabeth,-NJ-07208,-USA:loc-dmVyc2lvbj0xO3RpdGxlPTMxMCtNb3JyaXMrQXZlO2xhbmc9ZW47bGF0PTQwLjY2ODg5OTUzNjEzMjgxO2xvbj0tNzQuMjE4NTEzNDg4NzY5NTM7c3RyZWV0PU1vcnJpcytBdmU7aG91c2U9MzEwO2NpdHk9RWxpemFiZXRoO3Bvc3RhbENvZGU9MDcyMDg7Y291bnRyeT1VU0E7c3RhdGU9TmV3K0plcnNleTtzdGF0ZUNvZGU9Tko7Y291bnR5PVVuaW9uO2NhdGVnb3J5SWQ9YnVpbGRpbmc7c291cmNlU3lzdGVtPWludGVybmFsO25sYXQ9NDAuNjY5MjM5MDQ0MTg5NDU7bmxvbj0tNzQuMjE4MDc4NjEzMjgxMjU7cGRzQ2F0ZWdvcnlJZD05MDAtOTMwMC0wMDAw/Manhattan:loc-dmVyc2lvbj0xO3RpdGxlPU1hbmhhdHRhbjtsYW5nPWVuO2xhdD00MC43MTQ1MTtsb249LTc0LjAwNjAyO2NpdHk9TWFuaGF0dGFuO2NvdW50cnk9VVNBO3N0YXRlPU5ldytZb3JrO3N0YXRlQ29kZT1OWTtjb3VudHk9TmV3K1lvcms7Y2F0ZWdvcnlJZD1jaXR5LXRvd24tdmlsbGFnZTtzb3VyY2VTeXN0ZW09aW50ZXJuYWw7cGRzQ2F0ZWdvcnlJZD05MDAtOTEwMC0wMDAw?map=40.72011,-74.10485,13,normal&avoid=carHOV'
browser = webdriver.Chrome()


def grabAndSave():
    browser.get(url)
    time.sleep(5)
    nav = browser.find_elements_by_class_name("route_list_result")

    for i in range(0, 3):
        data = (nav[i].text).splitlines()  # Splits str at every new line
        print(data)
        print(readable)
        writer.writerow({'Route Number': (i+1), 'ETA': data[0], 'Distance': data[2], 'Route': data[3], 'Time': readable})


with open('hereWeGoData.csv', 'w', newline='') as csvfile:
    fieldnames = ['Route Number', 'ETA', 'Distance', 'Route', 'Time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    try:
        while True:
            ts = time.time()
            readable = time.ctime(ts)
            grabAndSave()
            time.sleep(5)  # 298 second day, gives 2 seconds for the program to run
    except KeyboardInterrupt:
        print("\n\nStopped by KEYBOARD INTERRUPTION\n\n")
        pass

browser.close()

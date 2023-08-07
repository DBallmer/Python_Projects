import sys
import matplotlib.pyplot as plt
import numpy as np


#read the RSSI number and return it
def rssi(entry):
    for z in range(len(entry)):
        if entry[z] == "R" and entry[z + 1] == "S" and entry[z + 2] == "S" and entry[z + 3] == "I":
            rssi = entry[z+6:z+10]
            return rssi
        else:
            continue

#read the channel number and return it
def channel(entry):
    for z in range(len(entry)):
        if entry[z] == "C" and entry[z + 1] == "h" and entry[z + 2] == ":":
            chan = entry[z+4:z+6]
            return chan
        else:
            continue

#read the ESSID name and return it
def essid(entry):
    for z in range(len(entry)):
        if len(entry[z:]) > 5:
            if entry[z] == "E" and entry[z + 1] == "S" and entry[z + 2] == "S" and entry[z + 3] == "I" and \
                    entry[z + 4] == "D":
                ssid = entry[z + 5: -2]
                return ssid
            else:
                continue
        else:
            return None

def take_dist(elem):
    return elem[0]

def getDist(thelist):
    # print clean results sorted by RSSI
    x1 = []
    y1 = []
    thelist.sort()
    print("\033[1;34;40m Wifi broadcasts from nearest to furthest:")
    title()
    for ents in range(len(thelist)):
        num = str(ents + 1)
        if ents < (len(thelist) // 3):
            print("\033[1;32;40m", end="")
        elif ents >= (len(thelist) // 3) and ents <= ((len(thelist) // 3) * 2):
            print("\033[1;33;40m", end="")
        else:
            print("\033[1;31;40m", end="")
        print(thelist[ents])
    # print chart
    print("Do you want a chart <this requires the matplotlib and numpy modules to work>, Y/N?")
    answer = input()
    if answer == 'y' or answer == 'Y':
        # Copy channel numbers into the x-axis list and wifi names into the y-axis list
        for j in range(len(thelist)):
            disty = take_dist(thelist[j])
            x1.append(disty)
            namey = take_name(thelist[j])
            y1.append(namey)
            x = np.array(x1)
            y = np.array(y1)
        plt.xlabel("Wifi strength (hover over dot for SSID name)")
        plt.scatter(x, y)
        plt.show()
    else:
        return

#Used as a sorted() key for channel
def take_chan(elem):
    return elem[1]

#sort by channel
def getChan(theList):
    sorted_list = sorted(theList, key=take_chan)
    title()
    x1 = []
    y1 = []
    # print list
    for i in range(len(sorted_list)):
        print(sorted_list[i])
    print("Do you want a chart <this requires the matplotlib and numpy modules to work>, Y/N?")
    answer = input()
    if answer == 'y' or answer == 'Y':
        #Copy channel numbers into the x-axis list and wifi names into the y-axis list
        for j in range(len(sorted_list)):
            channy = take_chan(theList[j])
            x1.append(channy)
            namey = take_name(theList[j])
            y1.append(namey)
            x = np.array(x1)
            y = np.array(y1)
        plt.xlabel("Wifi Channel (hover over dot for SSID name)")
        plt.scatter(x, y)
        plt.show()
    else:
        return

#Used to provide sorted() key for name
def take_name(elem):
    return elem[2]

#print wifi sorted by name
def getName(theList):
    sorted_list = sorted(theList, key=take_name)
    title()
    x1 = []
    y1 = []
# print list
    for i in range(len(sorted_list)):
        print("\033[1;33;40m",sorted_list[i])
#print chart
    print("Do you want a chart <this requires the matplotlib and numpy modules to work>, Y/N?")
    answer = input()
    if answer == 'y' or answer == 'Y':
            # Copy channel numbers into the x-axis list and wifi names into the y-axis list
        for j in range(len(sorted_list)):
            channy = take_chan(theList[j])
            x1.append(channy)
            namey = take_name(theList[j])
            y1.append(namey)
            x = np.array(x1)
            y = np.array(y1)
        plt.xlabel("Wifi Channel (hover over dot for SSID name)")
        plt.scatter(x, y)
        plt.show()
    else:
        return

def title():
    print("\033[1;34;40m RSSI | Channel | SSID")

def txt_reset():
    print("\033[1;37;40m")

#create lists needed to convert log file data into usable data for this program
entry = []
dataset = []
dataentry = []
result = []
onenet = []

#attempt to open scanap file
filename = input("Enter the path and filename of the scanap log file (.eg /home/<user>/Documents/<filename>.log: ")
try:
    file = open(filename, "r")
except:
    print("Unable to find or open file. Check the path, filename, and permissions.")
    sys.exit()

#read the scanap file and copy into the dataset list, then read each line from dataset into dataentry
dataset = file.readlines()
for x in range(len(dataset)):
    entry = dataset[x]
    dataentry.append(entry)
file.close()

#create individual list for each wifi entry and store it in result
for i in range(len(dataentry)):
    onenet = [rssi(dataentry[i]), channel(dataentry[i]), essid(dataentry[i])]
    result.append(onenet)

#clean entries containing None values from dataentry list
newlist = []
for j in range(len(result)):
    if None not in (result[j]):
        newlist.insert(0, result[j])
        continue
    else:
        continue
result = newlist

#print options
print("Choose how to sort the access point list:")
keystroke = "a"
while keystroke != "q" and keystroke != "Q":
    keystroke = input("(D)istance, (N)ame, (C)hannel, (Q)uit ")
    if keystroke == "d" or keystroke =="D":
        getDist(result)
        txt_reset()
    elif keystroke == "c" or keystroke =="C":
        getChan(result)
        txt_reset()
    elif keystroke == "n" or keystroke =="N":
        getName(result)
        txt_reset()
    elif keystroke == "q" or keystroke =="Q":
        break
    else:
        print("That's not one of the four options. Try D, N, C, or Q.")



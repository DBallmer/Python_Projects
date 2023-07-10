import sys

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
def getDist(thelist):
    # print clean results sorted by RSSI
    thelist.sort()
    print("\033[1;34;40m Wifi broadcasts sorted by signal strength:")
    title()
    for ents in range(len(thelist)):
        #Turn RSSI into positive int
        rssi = thelist[ents]
        numtemp = (rssi[0])
        num = int(numtemp[1: ])
        if num < 51:
            print("\033[1;32;40m", thelist[ents])
        elif num > 50 and num <= 75:
            print("\033[1;33;40m", thelist[ents])
        elif num > 75:
            print("\033[1;31;40m", thelist[ents])

#Used as a sorted() key for channel
def take_chan(elem):
    return elem[1]

#sort by channel
def getChan(theList):
    sorted_list = sorted(theList, key=take_chan)
    title()
    # print list
    for i in range(len(sorted_list)):
        print(sorted_list[i])

#Used to provide sorted() key for name
def take_name(elem):
    return elem[2]

#print wifi sorted by name
def getName(theList):
    sorted_list = sorted(theList, key=take_name)
    title()
# print list
    for i in range(len(sorted_list)):
        print("\033[1;33;40m",sorted_list[i])

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
    keystroke = input("(S)trength, (N)ame, (C)hannel, (Q)uit ")
    if keystroke == "s" or keystroke =="S":
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



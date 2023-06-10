# Need the sys module to gracefully exit
import sys

# Lists for parsing and rearranging Flipper beacon sniff log file
entry = []
dataset = []
dataentry = []
ssid_list = []

# open file
filename = input("Enter path and filename of the beacon sniff log file (.eg /home/<user>/Documents/<filename>.log: ")
try:
    file = open(filename, "r")
except:
    print("Unable to find or open file. Check the path, filename, and permissions.")
    sys.exit()

# read file
dataset = file.readlines()

# break each line of the log file into a list, and reassemble these lines in dataentry[]
for x in range(len(dataset)):
    entry = dataset[x]
    dataentry.append(entry)

# close file
file.close()

# scan our list of entries for "ESSID", grab the name that comes after, store in ssid_list
for y in range(len(dataentry)):
    getssid = dataentry[y]
    for z in range(len(getssid)):
        if len(getssid[z:]) > 5:
            if getssid[z] == "E" and getssid[z+1] == "S" and getssid[z+2] == "S" and getssid[z+3] == "I" \
                    and getssid[z+4] == "D":
                ssid = getssid[z+6:]
                if ssid not in ssid_list:
                    ssid_list.append(ssid)
            else:
                continue
        else:
            continue

# sort the ssid_list
ssid_list.sort()

# print a numbered list of the SSIDs
for ents in range(len(ssid_list)):
    num = str(ents + 1)
    print(num + ".", ssid_list[ents], end="")

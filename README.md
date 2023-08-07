# Python_Projects
ezscanap.py: A utility for sorting Flipper/Maurauder scanap.log files. You will be prompted to enter the filepath and file name 
of the log (eg. /home/<user>/Documents/<logfile.log>). The utility will allow you to sort the log according to name (SSID), channel,
or signal strength (RSSI). It can also print scatterplot diagrams for all three outputs if the user installs the matplotlib and numpy modules.

ezbeak.py: A utility for pulling individual wifi network names (ESSID) out of a beacon sniffing log. Capture the log using 
Flipper/Marauder -> Applications -> GPIO -> Maurader -> Sniff: Beacon. Download the captured file. Then run python3 eazybeak.py.
You will be prompted to enter the filepath and file name of the log (eg. /home/<user>/Documents/<logfile.log>). The utility will
iterate through the log file and list each individually broadcast ESSID (mostly local wifi networks). Don't be suprised if you 
see one or two blank entries. Some devices don't broadcast their names, others are obfuscated by using special characters.

Monster_fight: A short and simple text-based game. I created it after completing my PCEP certification to reinforce my understanding of 
data structures and functions. The code contains lists, tuples, a dictionary, and multiple functions. If you have python installed, simply 
download the game and run it by typing: python3 Monster_Fight.py
Good hunting!

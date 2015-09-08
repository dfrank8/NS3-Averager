#  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  
# /  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \
# Code Written by Douglas Franklin for NS-3 Users
# Northeastern University Undergraduate Student, August 2015
# The purpose of this program is to take NS-3's provided Uplink 
# or Downlink Rlc Stats
#
#       UlRlcStats.txt or DlRlcStats.txt
#
# and to export an average for throughput, minimum data rate, 
# and maximum data rate for all users.
#
# Example Exported .txt File:
# NumNodes AvgTP AvgMinDR AvgMaxDR
# 10 16898.2 105 209
#
# Default In-File procedure:
#
# Check for file name in command line arguments
#
# If none is found:
# 	Check for DlRlcStats.txt.
# If that is not found:
# 	Check for UlRlcStats.txt.
# If that is not found:
#	Raise error.
#
# Default Out-File procedure:
#
# Check for file name as second command-line argument
#
# If none is found:
#	Use inFile name + Averages.txt
import string
import sys
import os.path


def getN(str, subStr, occr):
    # Function that gets the Nth index of a character or sequence in a string
    z = 0
    count = 0
    while count < occr:
        x = string.find(str,subStr,z)
        if x == -1:
            break
        else:
            count = count + 1
            z = x + 1
    return x

defaultInFiles = ["DlRlcStats.txt", "UlRlcStats.txt"] 

# Organize InFiles and OutFiles
if(len(sys.argv) == 1):
	print('No commandLine arguments found.')
	for(int i = 0; i < len(defaultInFiles); i ++)
		if(os.path.isfile(defaultInFiles[i])):
			inFile = defaultInFiles[i]
			outFile = inFile[i:inFile.find('.')] + 'Averages.txt'
			print('Using the file "' + defaultInFiles[i] + '" as the input.')
	# elif(os.path.isfile(defaultInFiles[1])):
	# 	inFile = defaultInFiles[1]
	# 	outFile = inFile[0:inFile.find('.')] + 'Averages.txt'
	# 	print('Using the file "' + defaultInFiles[1] + '" as the input.')
elif(len(sys.argv) == 2):
	inFile = sys.argv[1]
	outfile = inFile[0:inFile.find('.')] + 'Averages.txt'
	print('Using "' + outFile + '" as outFile')
elif(len(sys.argv) == 3):
	inFile = sys.argv[1]
	outFile = sys.arv[2]

outFile = open(outFile, 'w')
outFile.write('NumNodes' + ' ' + 'AvgTP' + ' ' + 'AvgMinDR' + ' ' + 'AvgMaxDR' + '\n')

def exportAverages(IDs, throughputs, mins, maxs):
	#Have reached the end of a file, so print the averages
	global outFile
	avgThroughput = sum(throughputs)/len(throughputs)
	avgMin = sum(mins)/len(mins)
	avgMax = sum(maxs)/len(maxs)
	outFile.write(str((max(IDs))) + ' ' + str(avgThroughput) + ' ' + str(avgMin) + ' ' + str(avgMax) + '\n')

with open(inFile, 'r') as infile:
	infile.next()
	IDs = []
	throughputs = []
	maxs = []
	mins = []
	for raw_line in infile:
		line = 'x'.join(raw_line.split())
		ID_value = line[getN(line,'x',3)+1:getN(line,'x',4)]
		throughput_value = line[getN(line,'x',9)+1:getN(line,'x',10)]
		min_value = line[getN(line,'x',12)+1:getN(line,'x',13)]
		max_value = line[getN(line,'x',13)+1:getN(line,'x',14)]
		IDs.append(float(ID_value))
		throughputs.append(float(throughput_value))
		mins.append(float(min_value))
		maxs.append(float(max_value))
	exportAverages(IDs, throughputs, mins, maxs)



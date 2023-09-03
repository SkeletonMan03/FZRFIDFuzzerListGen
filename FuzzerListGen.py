print("Basic as fuck Flipper Zero RFID Fuzzer list generator by SkeletonMan")
print("I'm obviously not responsible if you get caught tampering with a reader (Yes, fuzzing is tampering)")
knownvalue=input("Please enter known card value excluding the last octet and colons: ")
outputfile=input("Please enter a name for an output file: ")
askforrange=input("Would you like to use a range of values for the last octet? (Y/N): ")
if askforrange=='Y' or askforrange=='y':
	valueone='0x'+input("Please enter the starting value: ")
	valuetwo='0x'+input("Please enter the ending value: ")
	valuestart=int(valueone, 16)
	valueend=int(valuetwo, 16)
	print("Range of", hex(valuestart)[2:].upper().zfill(2), "to", hex(valueend)[2:].upper().zfill(2), "will be generated for the last octet for fuzzing list")
elif askforrange=='N' or askforrange=='n':
	print("All possible values will be generated for the last octet for fuzzing list")
	valuestart=0
	valueend=255
else:
	print("Seriously? That's not a valid option!")
	exit()
with open(outputfile, 'a+') as f:
	f.write("#Generated with SkeletonMan's Flipper Zero RFID FuzzerListGen"+"\n")
	for i in range(int(valuestart), int(valueend+1)):
		lastoctet=hex(i)[2:].upper().zfill(2)
		fuzzvalue=knownvalue+lastoctet
		f.write(fuzzvalue+"\n")
	f.write("\n")
print("RFID Fuzzer list has been generated and saved to", outputfile)

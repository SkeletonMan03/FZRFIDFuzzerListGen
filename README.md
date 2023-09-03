# FZRFIDFuzzerListGen
Simple RFID Fuzzer List Generator for Flipper Zero

## How to use
1) Simply run `python FuzzerListGen.py`.  
2) You enter all but the last octet of a known RFID card then either pick a range of values to use or just all possible values for the last octet.  
3) Throw the generated list into your Flipper Zero's RFID Fuzzer Folder.  

## Why?
I keep seeing skids on Discord asking for fuzzer lists not understanding the point of it at all.  
It does actually have use in a Red Team Engagement.  

# Disclaimer
I am *absolutely* not responsible if you get in trouble for tampering with a reader. (Yes, fuzzing is tampering).  

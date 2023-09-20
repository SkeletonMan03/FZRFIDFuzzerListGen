# FZRFIDFuzzerListGen
Simple RFID Fuzzer List Generator for Flipper Zero

## How to use
1) Simply run `python FuzzerListGen.py`.  
2) You enter all but the last octet of a known RFID card then either pick a range of hex values to use for the last octet or just let it do all possible hex values for the last octet.  
3) Throw the generated list into your Flipper Zero's RFID Fuzzer Folder.  

## Why?
I keep seeing skids on Discord asking for fuzzer lists not understanding the point of it at all.  
It does actually have use in a Red Team Engagement.  

## Need a better explanation?
Trying the default codes in the Flipper Zero RFID Fuzzer app generally won't work as the default codes are typically removed by the time the reader is installed.  
Without a known card value it's basically useless trying to use the RFID Fuzzer app. With all possible values, you'll spend an extremely long time standing at the reader and most likely won't get anywhere before you set off tamper detection or someone sees you holding your Flipper to it.  
To stress that point, let's use H10301 as an example because it's only 26-bit. The preamble (which tells the reader the type), then 3 octets of 8-bit values (0 - 255) so 256 possible values per octet.  
So 256^3=16,777,216  
Lets assume you're running 1 per second, that's 4,660.3377777778 hours to exhaust or 194.1807407407 days or approximately 6.472691358 months.  

## Why this script then?
Instead of all that, you can use a known card, omit the last octet, and instead generate a list of hex values for the last octet for different card numbers.  
Since it's only 26-bit, I'll use H10301 again as an example.  
As already stated, it's the preamble, then three 8-bit octets.  
So it could be something like 24:45:2A for example.  
24 being the Facility code which is 36 in decimal, and 45:2A being the card number, which in this case would be 17706 in decimal.  
So, with this in mind, lets say the tag doesn't work, but you want to try some card numbers before it. Lets say, 20 of them, since it's hex, you'd put 15 as the last octet and have it end at 29 so you'd be trying card numbers 17685 through 17705.  


# Disclaimer
I am *absolutely* not responsible if you get in trouble for tampering with a reader. (Yes, fuzzing is tampering).  

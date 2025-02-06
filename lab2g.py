#!/usr/bin/env python3

# Author: Aashis Kharel
# Author ID: akharel2
# Date Created: 2025/02/06

import sys
if len(sys.argv) == 1:
    timer = 3
elif len(sys.argv) != 1:
    timer = int(sys.argv[1])
while timer != 0:
    print (timer)
    timer = timer -1
print ('blast off!')

"""I preferes this way beacouse is better for my
Of course you can set way how you feel better"""


import time

#you import file with calculations
from git.timerPRO import timer as end

#begining code
input()

#start count time
starttime = time.time()

#end your code
input()

#ending count time
endtime = time.time()
#calclations your code time
timelaps = endtime - starttime

end.timer(timelaps)


#if your program doesn't need to be clicked for the program to start counting then do it like this

"""
starttime = time.time()

#code

endtime = time.time()
timelaps = endtime - starttime
end.timer(timelaps)
"""

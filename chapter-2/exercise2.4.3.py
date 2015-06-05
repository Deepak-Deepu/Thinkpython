start = (6*60+52) * 60
easy = (8*60+15)*2
fast = (7*60+12)*3
finishhour = (start + easy + fast)/(60*60.0)
finishfloored =(start + easy +fast)/(60*60)
finishminute = (finishhour - finishfloored)*60
print 'Finish time was %d:%d' % (finishhour,finishminute)

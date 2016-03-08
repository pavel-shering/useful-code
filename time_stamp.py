import time
t = time.localtime()
# yyyy-mm-dd hh:mm:ss
print '%d-%02d-%02d %02d:%02d:%02d' % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
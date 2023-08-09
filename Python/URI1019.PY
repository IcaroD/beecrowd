seg = int(input())

hour = seg // 3600
seg = seg % 3600
minute = seg // 60
seg = seg % 60

print("%d:%d:%d" %(hour, minute, seg))
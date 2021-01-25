```
Create a Time class and initialize it with hours and minutes.
Create a method addTime which should take two Time objects and add them.
```

class Time:

    def __init__(self,hours,minutes):
        self.hours = hrs
        self.minutes = mins
    
    def addTime(t1,t2):
        hr = t1.hrs + t2.hrs 
        min = t1.mins + t2.mins
        if min > 60:
            extra_hr = min//60
        hr = hr + extra_hr
        min = min % 60
        total_time = Time(hr,min)
        return total_time


time1 = Time(5,50)
time2 = Time(6,60)
addtime = Time.addTime(time1,time2)

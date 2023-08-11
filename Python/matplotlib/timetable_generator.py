import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.collections import PolyCollection

label_colors = ("C0", "C2")
labels = ("Person 1", "Person 2")
label_minutes = (0, 20, 40)

start_time = mdates.date2num(dt.datetime(2000, 1, 1, 17, 00))
end_time = mdates.date2num(dt.datetime(2000, 1, 2, 9, 00))

p1_data =  [
                (dt.datetime(2000, 1, 1, 18, 40), dt.datetime(2000, 1, 1, 19, 00)),
           ]
p2_data =  [    
                (dt.datetime(2000, 1, 1, 18, 30), dt.datetime(2000, 1, 1, 18, 50)),
           ]

data_list = (p1_data, p2_data)

verts = []
colors = []
for i, data in enumerate(data_list):
    for d in data:
        y_center = i + 1
        v =  [
                (mdates.date2num(d[0]), y_center - 0.4),
                (mdates.date2num(d[0]), y_center + 0.4),
                (mdates.date2num(d[1]), y_center + 0.4),
                (mdates.date2num(d[1]), y_center - 0.4),
                (mdates.date2num(d[0]), y_center - 0.4)
            ]
        verts.append(v)
        colors.append(label_colors[i])

bars = PolyCollection(verts, facecolors=colors, edgecolors='black')

fig, ax = plt.subplots()
ax.add_collection(bars)
ax.set_xlim(start_time, end_time)
major_loc=mdates.HourLocator()
ax.xaxis.set_major_locator(major_loc)
minute_fmt = mdates.DateFormatter('%H')  
ax.xaxis.set_major_formatter(minute_fmt)
major_loc = mdates.MinuteLocator(byminute=label_minutes)
ax.xaxis.set_minor_locator(major_loc)

ax.set_yticks([i+1 for i, _ in enumerate(labels)])
ax.set_yticklabels(labels)
plt.show()

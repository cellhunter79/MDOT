# Python code for measure reacation time in human subject
# with computer monitor and keyboard

import matplotlib.pyplot as plt 
import numpy as np 
import time
from matplotlib.widgets import Button

Z = np.random.uniform(1,100,100).reshape((10, 10))
fig, ax1 = plt.subplots(figsize = (10,10))
 

dot_num = 1000
x = np.random.random(dot_num)
y= np.random.random(dot_num)
x0 = np.zeros(dot_num)
y0 = np.zeros(dot_num)
print(x)
print(y)
chance = 3
rand_choice = round(np.random.random()*100)%chance
time_display=0
time_interval = []
t_press = 0
delay = 1

plt.ion()

class controls(object):
    def iseeit(self,event):
        t_press = time.time()
        if t_press - time_display < delay:
            time_interval.append(t_press-time_display)
            print(t_press)
            print(time_display)
            print(time_display-t_press)
            print(time_interval)

control_event=controls()


plt.show(block=False)

im = plt.imshow(Z,cmap='gray')
time_init = time.time()

fig_result = plt.figure()
ax_result = plt.subplot(111)
line1, = ax_result.plot(np.arange(len(time_interval)),time_interval)
ax_result.set_ylim([-delay,delay])
ax_result.set_xlim([0,40])

def on_press(event):
    print('you pressed', event.button, event.xdata, event.ydata)
    t_press = time.time()
    if t_press - time_display < delay:
        time_interval.append(t_press-time_display)
        print(t_press)
        print(time_display)
        print(time_display-t_press)
        print(time_interval)

cid = fig.canvas.mpl_connect('button_press_event', on_press)


for i in range(1,100,1):
    m =0
    if rand_choice == 0:
        # display a figure at random time
        for m in range(1,100,1):
            Z = np.random.uniform(1,100,100).reshape((10, 10))
            im.set_data(Z)
            plt.pause(0.1)
        #plt.show(block=False)
        #fig.canvas.flush_events()
        time_display = time.time()
        #go_display = input("GO!! ")
        #t_press = time.time()
        #time_interval.append(t_press-time_display)
        line1.set_xdata(np.arange(len(time_interval)))
        line1.set_ydata(time_interval)
        print(time_interval)
        print(np.average(time_interval))
        plt.pause(delay)

    else: 
        
        #fig.canvas.flush_events()
        #dots1.set_ydata(y0)
        #plt.show(block=False)
        #line1.set_ydata(time_interval)
        line1.set_xdata(np.arange(len(time_interval)))
        line1.set_ydata(time_interval)
        plt.pause(delay)
        print(rand_choice)
        print(np.average(time_interval))


    rand_choice = round(np.random.random()*100)%chance

print(np.average(time_interval))

plt.pause(30)


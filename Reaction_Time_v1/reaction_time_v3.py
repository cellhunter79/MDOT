# Python code for measure reacation time in human subject
# with computer monitor and keyboard

import matplotlib.pyplot as plt 
import numpy as np 
import time
from matplotlib.widgets import Button

#Z = np.random.uniform(1,100,100).reshape((10, 10))

nrows, ncols = 10,10
image = np.random.uniform(0,1,nrows*ncols*3)

# Reshape things into a 9x9 grid.
image = image.reshape((nrows, ncols,3))
fig, ax1 = plt.subplots(figsize = (10,10))

dot_num = 1000
x = np.random.random(dot_num)
y= np.random.random(dot_num)
x0 = np.zeros(dot_num)
y0 = np.zeros(dot_num)
#print(x)
#print(y)
chance = 3
rand_choice = round(np.random.random()*100)%chance
time_display=0
time_interval = []
t_press = 0
delay = 1

plt.ion()
plt.show(block=False)


#im = plt.imshow(Z,cmap='gray')
im = plt.imshow(image)
#im = plt.matshow(image)

time_init = time.time()

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

fig_result = plt.figure()
ax_result = plt.subplot(111)
line1, = ax_result.plot(np.arange(len(time_interval)),time_interval)
ax_result.set_ylim([-delay,delay])
ax_result.set_xlim([0,40])



for i in range(1,100,1):
    
    m =0
    if rand_choice == 0:
        # display a figure at random time
        start_p = np.random.choice(5)
        end_p = np.random.choice(5)
        Signal_start_point = (start_p,(5-start_p))
        Signal_end_point = (end_p,(5-end_p))
        for m in range(1,10,1):
            Red = np.full((25),1)
            Green = np.full((25),1)
            Blue = np.random.uniform(0,1,25)

            print(Signal_start_point,Signal_end_point)
            Z_signal = np.concatenate((Red,Green,Blue),axis=0)
            Z_signal = Z_signal.reshape((3,5,5))
            Z_signal = np.transpose(Z_signal, (2,1,0))
            Z_signal = np.pad(Z_signal,(Signal_start_point,Signal_end_point,(0,0)),'constant',constant_values=(0,0))
            Z_mask = np.zeros(75).reshape((3,5,5))
            Z_mask = np.transpose(Z_mask, (2,1,0))
            Z_mask = np.pad(Z_mask,(Signal_start_point,Signal_end_point,(0,0)),'constant',constant_values=(1,1))
            Z_new = image*Z_mask + Z_signal
            im.set_data(Z_new)
            plt.pause(0.25)
        #plt.show(block=False)
        #fig.canvas.flush_events()
            time_display = time.time()
            image = np.random.uniform(0,1,nrows*ncols*3)
            image = image.reshape((nrows, ncols, 3))
            im.set_data(image)
        #Z = np.random.uniform(1,100,100).reshape((10, 10))
           
        #go_display = input("GO!! ")
        #t_press = time.time()
        #time_interval.append(t_press-time_display)
        #line1.set_xdata(np.arange(len(time_interval)))
        #line1.set_ydata(time_interval)
        print(time_interval)
        print(np.average(time_interval))
        
        #plt.pause(delay)

    else: 
        
        #fig.canvas.flush_events()
        #dots1.set_ydata(y0)
        #plt.show(block=False)
        #line1.set_ydata(time_interval)
        line1.set_xdata(np.arange(len(time_interval)))
        line1.set_ydata(time_interval)
        #plt.pause(delay)
        #print(rand_choice)
        #print(np.average(time_interval))
        image = np.random.uniform(0,1,nrows*ncols*3)
        image = image.reshape((nrows, ncols,3))
        im.set_data(image)
        plt.pause(0.25)

    rand_choice = round(np.random.random()*100)%chance

print(np.average(time_interval))



plt.pause(30)


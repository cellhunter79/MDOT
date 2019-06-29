# Python code for measure reacation time in human subject
# with computer monitor and keyboard

import matplotlib.pyplot as plt 
import numpy as np 
import time
from matplotlib.widgets import Button
from PIL import Image
#Z = np.random.uniform(1,100,100).reshape((10, 10))
road_im = Image.open("road2.png")  
image_raw = np.array(road_im)
x_res = 1046
y_res = 1857
stim_x_size=100
stim_y_size=100
x_ram_loc = np.random.randint(0,high=x_res-stim_x_size)
y_ram_loc = np.random.randint(0,high=y_res-stim_y_size)
#idx_x = np.random.randint(500, size =10)
#idx_y = np.random.randint(500, size =10)
#nrows, ncols = 10,10
image_shuffle = image_raw.reshape(x_res*y_res,3)
print("here")
np.random.shuffle(image_shuffle)
print(image_shuffle.shape)
image_shuffle = image_shuffle.reshape((x_res,y_res,3))
image = image_shuffle[x_ram_loc:(x_ram_loc+stim_x_size),y_ram_loc:(y_ram_loc+stim_y_size),:]
print(image.shape, image_shuffle.shape)
#image = image.reshape((10,10))
#image = road_im.reshape[(idx_x,idx_y),:]
#image = image[:,idx_y,:]
#image = np.random.uniform(0,1,nrows*ncols*3)
# Reshape things into a 9x9 grid.
#image = image.reshape((nrows, ncols,3))
fig, ax1 = plt.subplots(figsize = (10,10))

chance = 5
rand_choice = round(np.random.random()*100)%chance
time_display=0
time_interval = []
t_press = 0
delay = 1
reaction_time=0

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
        time_interval.append(t_press-time_display-0.1)
        print(t_press)
        print(time_display)
        print(time_display-t_press)
        print(time_interval)

cid = fig.canvas.mpl_connect('button_press_event', on_press)

class controls(object):
    def iseeit(self,event):
        t_press = time.time()
        if t_press - time_display < delay:
            time_interval.append(t_press-time_display-0.1)
            print(t_press)
            print(time_display)
            print(time_display-t_press)
            print(time_interval)

control_event=controls()

fig_result = plt.figure()
ax_result = plt.subplot(111)
line1, = ax_result.plot(np.arange(len(time_interval)),time_interval)
#text1  = plt.text(0.5,0.5,"")
ax_result.set_ylim([0,delay+0.5])
ax_result.set_xlim([0,40])

signal_x_size = 8
signal_y_size = 2

for i in range(1,300,1):
    
    m =0
    if rand_choice == 0:
        # display a figure at random time
        start_p = np.random.choice(stim_x_size-signal_x_size)
        end_p = np.random.choice(stim_y_size-signal_y_size)
        Signal_start_point = (start_p,(stim_x_size-start_p))
        Signal_end_point = (end_p,(stim_y_size-end_p))

        row_pad = (start_p,(stim_x_size-start_p-signal_x_size))
        column_pad =(end_p,(stim_y_size-end_p-signal_y_size))

        x_ram_loc = np.random.randint(0,high=x_res-stim_x_size)
        y_ram_loc = np.random.randint(0,high=y_res-stim_y_size)
        
        image = image_shuffle[x_ram_loc:(x_ram_loc+stim_x_size),y_ram_loc:(y_ram_loc+stim_y_size),:]
        print(image.shape, image_shuffle.shape)
        time_display = time.time()
        for m in range(1,10,1):
            Red = np.random.uniform(0,1,signal_x_size*signal_y_size)
            Green = np.full((signal_x_size*signal_y_size),0)
            Blue = np.full((signal_x_size*signal_y_size),0)

            print(Signal_start_point,Signal_end_point)
            Z_signal = np.concatenate((Red,Green,Blue),axis=0)
            Z_signal = Z_signal.reshape((3,signal_x_size,signal_y_size))
            Z_signal = np.transpose(Z_signal, (2,1,0))
            Z_signal = np.pad(Z_signal,(column_pad,row_pad,(0,0)),'constant',constant_values=(0,0))
            Z_mask = np.zeros(signal_x_size*signal_y_size*3).reshape((3,signal_x_size,signal_y_size))
            Z_mask = np.transpose(Z_mask, (2,1,0))
            Z_mask = np.pad(Z_mask,(column_pad,row_pad,(0,0)),'constant',constant_values=(1,1))
            Z_new = image*Z_mask/255 + Z_signal
            im.set_data(Z_new)
            plt.pause(0.25)
        #plt.show(block=False)
        #fig.canvas.flush_events()
            
            x_ram_loc = np.random.randint(0,high=x_res-stim_x_size)
            y_ram_loc = np.random.randint(0,high=y_res-stim_y_size)
            image = image_shuffle[x_ram_loc:(x_ram_loc+stim_x_size),y_ram_loc:(y_ram_loc+stim_y_size),:]         
            im.set_data(image)
        
        #Z = np.random.uniform(1,100,100).reshape((10, 10))
           
        #go_display = input("GO!! ")
        #t_press = time.time()
        #time_interval.append(t_press-time_display)
        #line1.set_xdata(np.arange(len(time_interval)))
        #line1.set_ydata(time_interval)
        print(time_interval)
        print(np.average(time_interval))
        
        print(reaction_time)
        line1.set_xdata(np.arange(len(time_interval)))
        line1.set_ydata(time_interval)
       

        
        #plt.pause(delay)

    else:         
        #fig.canvas.flush_events()
        #dots1.set_ydata(y0)
        #plt.show(block=False)
        #line1.set_ydata(time_interval)
            #line1.set_xdata(np.arange(len(time_interval)))
            #line1.set_ydata(time_interval)
        plt.pause(0.25)
        #plt.pause(delay)
        #print(rand_choice)
        #print(np.average(time_interval))

        

        x_ram_loc = np.random.randint(0,high=x_res-stim_x_size)
        y_ram_loc = np.random.randint(0,high=y_res-stim_y_size)
        image = image_shuffle[x_ram_loc:(x_ram_loc+stim_x_size),y_ram_loc:(y_ram_loc+stim_y_size),:]
        print(image.shape)
        im.set_data(image)
        plt.pause(0.25)

    rand_choice = round(np.random.random()*100)%chance


print(np.average(time_interval))

reaction_time = "Reaction Time: " + str(np.average(time_interval))
plt.text(0,-1,reaction_time,color = "red", fontsize = 18)

plt.pause(30)


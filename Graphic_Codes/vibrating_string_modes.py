import matplotlib.pyplot as plt
import numpy as np

# Function to generate a vibrating string mode (sine wave)
def string_modes(x, mode, L):
    return np.sin(mode * np.pi * x / L)

### Parameters ###
# String Length 
L = 1  
# Number of modes
modes = 4  

# String Array 
x = np.linspace(0, L, 1000)

fig,ax = plt.subplots(1,figsize=(10, 6))

for i in range(1, modes + 1):
    modes = string_modes(x, i, L)
    ax.plot(x, modes + 5/2*i, label=f'n = {i}', color=(0.2 + i/5, 0.4, 0.8)) 
    ax.plot(x, -modes +5/2*i,color=(0.2 + i/5, 0.4, 0.8))
    a1 = np.sin(i* np.pi*0.275)
    a2 = -np.sin(i* np.pi*0.275)
    b1 = np.sin(i* np.pi*0.075)
    b2 = -np.sin(i* np.pi*0.075)
    ax.plot(([0.275,0.275]),([a1 + 5/2*i,a2 + 5/2*i]),'k',linestyle = '--') #Neck Pickup Line
    ax.plot(([0.075,0.075]),([b1 + 5/2*i,b2 + 5/2*i]),'k',linestyle = '--') #Bidge Pickup Line

ax.scatter(0.275,1,marker="^",color='b',s=130, zorder=2,label = 'Neck Pickup') # Neck pick-up
ax.scatter(0.075,1,marker="^",color='r',s=130, zorder=2,label = 'Bridge Pickup') # Neck pick-up

ax.set_title('Individual Vibrating String Modes')
ax.set_xlabel('String')
ax.set_ylabel('Amplitude')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

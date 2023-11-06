import numpy as np 
import matplotlib.pyplot as plt 
from scipy.fft import fft,fftfreq

def get_frequency(signal,sr):
    """
    Obtains the frequency values for a given signal and sample rate

    Parameters:
        signal (array-like): The input signal.
        sampling_rate (float): The sampling rate of the signal.

    Notes:
        Performs well for arrays of shape ~300 

    Credit:
        https://docs.scipy.org/doc/scipy/tutorial/fft.html#fast-fourier-transforms
    """

    N = len(signal)
    T = 1.0 / sr
    y = signal[:N]
    yf = fft(y)
    xf = fftfreq(N, T)[:N//2]    
    m = 2.0 / N * np.abs(yf[:N // 2])
    return xf, m        


def plucked_string(x,t,L,p,c,a,n): 

    """
    Returns a fourier representation of the wave equation 
    
    Parameters:
        x (array-like): Array to plot wave coefficients against 
        t (int): Time at which the string is plucked 
        L (int): Length of the string 
        v (Float): Location of where the string is plucked 
        c (int): wave speed 
        a (int): Amplitude of initial pluck 
        n (int): Wave node 
    """

    A = (2*a*(L**2))*np.sin(n*np.pi*p/L)/((n**2) * (np.pi**2) * p*(L-p))
    return A*np.sin((np.pi*n*x)/L)*np.cos((n*np.pi*c*t)/L)

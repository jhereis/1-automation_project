import pyautogui as py
import time


site = 'globo.com'
ge = 'C:\\RoboGlobo\\ge.png'
coockie = 'C:\\RoboGlobo\\prosseguir.png'
times = 'C:\\RoboGlobo\\times.png'
palmeiras = 'C:\\RoboGlobo\\palmeiras.png'

py.hotkey('win','r')
time.sleep(1)
py.hotkey('chrome.exe')
time.sleep(1)
py.hotkey('enter')
time.sleep(8)
print("escrevendo site")
py.write(site)
time.sleep(1)
py.hotkey('enter')
time.sleep(2)

cont=0 
while cont < 5:
    if(py.locateCenterOnScreen(ge)is None) == False:
        ge = py.locateCenterOnScreen(ge)
        py.click(ge)
        print("ge clicked")
        cont=5
    else:
        cont=cont+1
        print("loading ge")
        
time.sleep(2)

cont=0 
while cont < 5:
    if(py.locateCenterOnScreen(times)is None) == False:
        timesVar = py.locateCenterOnScreen(times)
        py.click(timesVar)
        print("times clicked")
        cont=5
    else:
        cont=cont+1
        print("loading times")
        
time.sleep(2)

cont=0 
while cont < 5:
    if(py.locateCenterOnScreen(coockie)is None) == False:
        coockieVar = py.locateCenterOnScreen(coockie)
        py.click(coockieVar)
        print("coockie clicked")
        cont=5
    else:
        cont=cont+1
        print("loading coockie")
        
time.sleep(2)

cont=0 
while cont < 5:
    if(py.locateCenterOnScreen(palmeiras)is None) == False:
        palmeirasVar = py.locateCenterOnScreen(palmeiras)
        py.click(palmeirasVar)
        print("palmeiras clicked")
        cont=5
    else:
        cont=cont+1
        print("loading palmeiras")
        
time.sleep(2)
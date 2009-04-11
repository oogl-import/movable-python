#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/stop_16_h.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhEAAQAPf/AP8A/4kBAKMKA7IRBrEPBaAHAYgBAL8dD/NbPv6Ha/+M'
            'cv57XvtbOesxErUPAYQBAI8DAeZFKv+pk/+7q/6PdfxpSftYNvxTMfxGI/cs'
            'CcsYAYsDAOZDKf+3pfyahPtBI/ojA/ofAfceAO4bAeUfAuIhAb8YAbwbDP+a'
            'gf6Lcvo0EftWNPomBfocAPQcAO0gAu1TM9olBtAdAcsgAqENAe9PMf+Qdvot'
            'D/tUM/////6lkfMeAucXAPOLc+BlR8IWAL0fArIcAogCAKAIAvtiQfxRL/oe'
            'APolB/6givajjvKRee60o8YpDLgbAbQdArIfApMHAKwOBP5NKfswDfccAO4c'
            'AfShju62psIgBbYYALEdArUgApgLAaoMAv4uCvsjA/YfAescAOEYAPCPeOqn'
            'lrUbAq8ZAJkMAZoGAPggAekdAOEfA+6Lc+2xoOelk+KkkbQjCLAbAbQfApUI'
            'AYcBANwcAe0gAdwXAOJVNu20pLsgBbIZAeGei89qTqwUALIeArAcAokDAKcM'
            'AeAhAdMcAcwmB9dmSbwoC7AYALQiBs5mSrcrDbUfAp8PAYMBALsYAcwgAr8c'
            'AbQVALAaAbAcAa0VAKwaAocCAIoDALIYAbcfArEeAqwZAo4EAIYBAJ0NAa8c'
            'ApMIAZkLAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAAFAAAP8CPAAA/zxQAAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfKR//QAAAAAA'
            'AAACAKwAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAj5AAEIFBhAwAAC'
            'BQwMXAggwAEECRQsYNDAwQOGECJImEChgoULGDJo2DAwAIcOHj6ACBFCxAgS'
            'JUxcBHACRQoVK1i0cPECRgwZM2g0rGHjBo4cOnbw6JHDxw8gQYQMIVLEyBEk'
            'OZIoybGESRMnT6BEkTIlBJUqVnLkuIIlixYtW7h08fIFTBgxY9SSKWPm7ZYz'
            'aNKAUbOGTY42bnK8gRNHi5w5dOrYuYMnRx49e/jk6OPnD6BAAAQNIlTI0CFE'
            'ZhIpWhSHUSOBjh5BiiRp0ltKleLIsXRpIKZMmja9fftHDqdODD19AiWHEaMn'
            +'gBr1ZihQSChRZ0KBXhgQACH+ADs=')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

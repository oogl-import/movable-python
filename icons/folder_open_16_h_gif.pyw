#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/folder_open_16_h.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhEAAQAPdIAP8A/6x0Av7+/v/+j//6if76if74iv76iv74if/6iqdv'
            'A/7yg/7zgvzyg/7zg/zzgv7revzrerV/CvvjcO/RXLeEEf///vz0uPz0uv70'
            'uv70uN7Jg/7+4/bvxfvaaNGkK9exSvvrlvvldPzldM+pM+/ruvrTXreBC+/V'
            'gvvgefrcavvcafvcavrcafvdas+mL7R+CfjKV/vimfrRXvrRX/jRXs6hLOCq'
            'M8SSI/rZifjHVPfHVPjHU/fHU86dJ8SKE+G2VvjLave/S/e/Sva/SvfAS8yY'
            'I7qBDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAANn8AAAAEgAAAJEFyCCYfMgAFQAS2pEFURN4fG0AFXyRBQAAAAQ9AAB8'
            'kQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAAAAIAP8CMgAA/zIACAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLJ//QAAAAAA'
            'AAACALoAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAihAAEIHEiwoMGD'
            'CBMqXBigYQCGAgZIdOiQYAABBAoUMHAAwYEEBBIoGBhgAQMGDRwwWPDAJIOR'
            'AgNAiCCBok2KEyhUsHABA4YMGjBo2MChQ0MPH0CEECFixIimIkiUKNHQxAkU'
            'KVSsWMFiRQsXL0rAABAgRgAZM9KmpVGjhg2qZG/gyKFjB48dOvL28AE3wA8g'
            +'QYQMGUxkCJEiRo6QvGlzYEAAIf4AOw==')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

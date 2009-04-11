#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/folder_open_16.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhEAAQAPdjAP8A/76NB/7+/v/+pf/7oP77oP76of77of76oP/7obqJ'
            'Cf71m/72mv31m/72m/32mv7wk/3wk8WXFvzqivPcd8ecIf///v33yP33yf73'
            'yf73yObVm/7+6vjz0vzjgty3Q+DCZfzwq/zrjf3rjdq7TPPwyfvdeceZGPPf'
            'mvznkvvkhPzkg/zkhPvkg/zlhNq5SMSWFPrWcvzprvvcefvcevrcedm1ROe8'
            'TNGoOfvioPrUb/nUb/rUbvnUbtmxPtGhJejGcfrXhPnNZvnNZfjNZfnOZtit'
            'OsmZGQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAANn8AAAAEgAAAJEFyCCYfMgAFQAS2pEFURN4fG0AFXyRBQAAAAQ9AAB8'
            'kQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAABEAAP8CNwAA/zcRAAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfK5//QAAAAAA'
            'AAACALYAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
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

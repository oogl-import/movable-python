#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/arrowright_green_16_h.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhEAAQAPf/AP8A/zWkHSOZEyqME7XhmNTuvcTnp7HgkJ/ZeHnHST2d'
            'G4jMauP00LbhmnrHUGe9OF26LGC7MF28L0+8IzCjEQ9iBnPFVtjwxYzPZlK0'
            'IFS1I8DmqrHelkixGTysEzSqEi2wDx+ZCgprA8Xnqo7QaEivFkyxG2i/Off8'
            '9P///57ZhDKqESmnDiCkCxyvCQ54Bmm9TKfdg1W2Ik6yHFS1In/KVen24Z3Z'
            'iC+rECemDBanBgqMAwNGAXrFVHTGRH3HUoHKV4DKVnPFSZLVefr++qXdlzOt'
            'GhilBwydAxJ0CGm9Ply6Kvz+/LDjqgygAwyfAwVSAg1oBlGxIVG3Hs/tv8bq'
            'usLpt8XquMLptcHpt/f89u/67l7FVARKAQZXA0GjF0q1GDSrERGgBgyeAw2f'
            'BH3QdPT780i8PgyhAwqWAwNCASOCDUG2Fy2pDhOgBRGgB4nVgvb89Eq8QAyl'
            'Awh7AwlPBDCsECirDRykCQ+eAyCqFtjy1er46VLASAynAwRMAhFrBh+rChWk'
            'Bw2eBAqdAgqdAwZqAglPAwllAw2jBAymAwugAwqeAgZpAgI0AQNFAQh4Awuc'
            'Awl+AgRNAQIwAQNBAQRRAgNDAQIzAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAADd8AP8CMgAA/zI3fAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLx//QAAAAAA'
            'AAACAMQAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAj1AAEIFBhAgEEB'
            'AwYqBGCQQAEDBxAkUKBgoYAFDBo4eAAhgoQJFCoMFGDhAoYMGjZw6ODhA4gQ'
            'IgQKGEGihIkTKFKoWMGihYuYL2DEkDGDBo0aNlLcwJFDxw4eL3r4+AEkCBAh'
            'Q4ikKGLkCBIeSZQsSUG2LBOyTZw8gRJFyhQqVaxcwZJFS4otXNR28fIFTBgx'
            'Y8iMKcPEzJkxaNKo8bKGTRs3ZN7ASRFHzpgxc+ioAVDHzh08efTs4dPn8hM/'
            'fwTWARRI0CBChS6PceLHUGqBhxAlUrSI0RMncxQ1crTw0SNIkZ48QSJp0qSF'
            'AylVsmTpEqaFAQEAIf4AOw==')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

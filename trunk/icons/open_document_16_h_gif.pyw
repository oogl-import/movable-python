#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/open_document_16_h.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhEAAQAPf/AP8A/wtrBCKhESukFzCnGax0AkrCKP7+/v/+j6NzAtGk'
            'K17TNTqnIP/6if76if74iv76imrYPFO/Lv7yg/7zgvzyg/7zg1HALW7cP27Y'
            'PnvlRkqwKP7revzrerV/CmXOOH/nR0q0KfvjcO/RXLaEEf///P70uP70ukKq'
            'Jfr31PfzyvvaaNeySvzrl/vldPzldM+pM/f0o9e7UvrTXreBC+/Vgvrgefrc'
            'avvcafvcavrcafvdas+mL/fwn/jKV/vjmfrRXvrRX/jRXs6hLPftmeCqM8SS'
            'I/rZifjHVPfHVPjHU/fHU86dJ+XLasSKE+C3V/jLa/e/S/e/Sva/SvfAS8yY'
            'IwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAANn8AAAAEgAAAJEFyCCYfMgAFQAS2pEFURN4fG0AFXyRBQAAAAQ9AAB8'
            'kQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAAO+kAP8COwAA/zvvpAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLZ//QAAAAAA'
            'AAACAL4AAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAi8AAEIFBigYICB'
            'CBMSNKiwIYAAAg46RBhgAAGJAwtoLEDRAEYABQ4gGJlAgckACxhIDNnAgYMH'
            'EAwGiCDBYIEJFChUsEBhQoALGDJo2HCwAIcOHjZqDPABRIgAG0WMIFHCxImr'
            'JgKgCJBChcYVCli0cOHixYuyAWDEkKFxBo0aNm7gwJEDh44dPHpwLOCjwA8g'
            'gAEHESJkCJG9RYwcQZJESRIkkJcwabLXyRMoUaRoniJlCpUqHAUqHa1UYEAA'
            +'If4AOw==')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

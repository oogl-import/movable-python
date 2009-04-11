#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/properties_doc_16_h.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhEAAQAPf/AP8A/46QscLe/5emurfA1cbh//D2+svj/87P3s/m/36L'
            'nPofAdTp/5OhtZKgspGfsdnr/wAegQcedrgfEd3t//7+/vtcPOLv/v7j3P7X'
            'zvyXgD8fSeby/vtZOPoqCfy6qv7u6vouDPtXNQEef+v0/v7UyvtNK/tLKPog'
            'AfD3/v76+PuAZPtfP/T6/vyOdfy2pfr7/mwAYQBcAGkAZwBmADEAXAA2AHAA'
            'XAByAHAAbwBlAHQAcgBpAHMAZQBfAG8AZABjADEAXwA2AGgAXwAuAGkAZwBm'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAANn8AAAAEgAAAJEFyCCYfMgAFQAS2pEFURN4fG0AFXyRBQAAAAQ9AAB8'
            'kQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAAH54AP8CPAAA/zx+eAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLh//QAAAAAA'
            'AAACAMAAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgACFNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAifAAEACECwIEGB'
            'CBEGEMCQ4QACARIqLECR4gADECUOPMCR40UDCCImDJCgpEkFKBUEWKCQgcuX'
            'DRw8WEBTIYQIOHNKmLBApMAAFCJUGDrUwgIKPgdeiIAhw1ANCzZcSBqAQ4QO'
            'Hj6ACCFiBAeqJCKUMLHgBIoMEUhQTSFUxYoFLCpESEG1hdChLl7IbUEVRs6/'
            +'EWD0hUG4cGGqBhMfBBAQACH+ADs=')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/properties_doc_16.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhEAAQAPeTAP8A/6SmwtDm/6y5ycfO39Po//T4+9fq/9na5trs/5ai'
            'sPs1A97u/6m1xai0w6ezwuLw/wAzmREzj8g1IuXx//7+/vx3Vunz/v7q5P7g'
            '2f2smFk0ZOz1/vx0UvtCFP3JvP7y7/tHGvxyTwQzl/D3/v7e1vxoQ/xmQPs2'
            'BPT5/v77+vyYfvx6Wff7/v2kjv3GuPv8/mwAYQBcAGkAZwBmADEAXAA2AHAA'
            'XAByAHAAbwBlAHQAcgBpAHMAZQBfAG8AZABjADEAXwA2AGcALgBpAAAAZgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAANn8AAAAEgAAAJEFyCCYfMgAFQAS2pEFURN4fG0AFXyRBQAAAAQ9AAB8'
            'kQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAANJ4AP8COwAA/zvSeAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLR//QAAAAAA'
            'AAACALwAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAifAAEACECwIEGB'
            'CBEGEMCQ4QACARIqLECR4gADECUOPMCR40UDCCImDJCgpEkFKBUEWKCQgcuX'
            'DRw8WEBTIYQIOHNKmLBApMAAFCJUGDrUwgIKPgdeiIAhw1ANCzZcSBqAQ4QO'
            'Hj6ACCFiBAeqJCKUMLHgBIoMEUhQTSFUxYoFLCpESEG1hdChLl7IbUEVRs6/'
            +'EWD0hUG4cGGqBhMfBBAQACH+ADs=')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

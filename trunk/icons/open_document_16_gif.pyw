#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/open_document_16.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhEAAQAPf/AP8A/xiFDDi1IUO3Kkm6Lb6NB2XQQP7+/v/+pbaMB9y3'
            'Q3ndTlS6Nv/7oP77oP76of77oYThVm7NR/71m/72mv31m/72m2zORojkWYjh'
            'WJTrYWXBQP7wk/3wk8WXFn/ZUpftYmXEQfzqivPcd8acIv///f73yP73yV28'
            'PPv53vn21vzjguDDZf3wrPzrjf3rjdq7TPn3tuDKbfvdeceZGPPfmvvnkvvk'
            'hPzkg/zkhPvkg/zlhNq5SPn0s/rWcvzqrvvcefvcevrcedm1RPnxrue8TNGo'
            'OfvioPrUb/nUb/rUbvnUbtmxPuvXhNGhJefHcvrXhfnNZvnNZfjNZfnOZtit'
            'OQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAANn8AAAAEgAAAJEFyCCYfMgAFQAS2pEFURN4fG0AFXyRBQAAAAQ9AAB8'
            'kQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAAI4gAP8COwAA/zuOIAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLJ//QAAAAAA'
            'AAACALoAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAi8AAEIFBigYICB'
            'CBMSNKiwIYAAAg46RBhgAAGJAwtoLEDRAEYABQ4gGJlAgckACxhIDNnAgYMH'
            'EAwGiCDBYIEJFChUsEBhQoALGDJo2HCwAIcOHjZqDPABRIgAG0WMIFHCxImr'
            'JgKgCJBChcYVCli0cOHixYuyAWDEkKFxBo0aNm7gwJEDh44dPHpwLOCjwA8g'
            'gAEHESJkCJG9RYwcQZJESRIkkJcwabLXyRMoUaRoniJlCpUqHAUqHa1UYEAA'
            'If4AOw==')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

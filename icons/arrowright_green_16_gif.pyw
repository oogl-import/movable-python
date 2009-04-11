#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/arrowright_green_16.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhEAAQAPenAP8A/063MjmuJUKjJMXord7yzNHtusLnprPikZLUZFex'
            'L5/YhOr328bor5PUa4HMUnjJRHvKSXjLSGrLOUm2IR98D4zSceH00qPagG3E'
            'Nm/FOc7svMLmq2PCLVa+JE28I0bBHzSuFheFCtLtvKTbgmPAKGfCL4LNU/n9'
            '9////7LinEu8IkG6HTa3GDDAFB2RD4PMZ7rlm3DGOGnDMG/FOJfWcO746LHi'
            'n0i9ID65Gim6EBejCAphBZPSb43TX5XUbZnWcpjWcYzSZKjfkvv++7jlrEy/'
            'Liu4ERmxCCONE4PMWHfJQv3+/cHqvBq0ChmzCQ1tBhyCD2zCN2zHM9rxzdPv'
            'ydDux9LvyNDuxc/ux/n9+PP78nnSbxm0CAtlBRByCFu2KmXFLE29IiK0Dxqy'
            'ChyzDBmyCpXbjff89mPLWBmyCRq1CRerCAldBDqaG1vGKkW7HSW0DhuzCyG0'
            'EaDfmvj992XLWhq4CROUCBVqC0m+IEC9GzC3FB+yCja8KOH13+/67m3OYxq6'
            'CQxnBiKFDzS9Fie3ERyyCxaxBxexCBm0CRCEBxVqChV/Chy2Cxq5CRi0CBay'
            'BxCDBwZNBAlgBRORCBiwCRqzCRmxCRSWBwxoBQZJBAlbBQxsBgpeBQZMBAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAAAGgAP8COQAA/zkBoAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLh//QAAAAAA'
            'AAACAMAAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAj2AAEIFBhAgEEB'
            'AwYqBGCQQAEDBxAkUKBgoYAFDBo4eAAhgoQJFCoMFGDhAoYMGjZw6ODhA4gQ'
            'IgQKGEGihIkTKFKoWMGihYuYL2DEkDGDBo0aNlLcwJFDxw4eL3r4+AEkCBAh'
            'Q4ikKGLkCBIeSZQsSUG2LBOyTZw8gRJFyhQqVaxcwZJFS4otXLo88fIFTBgx'
            'Y8iUMXOGCZo0atawafPFzRs4ceTMoZOijh01au7gaQMgj549fPr4+QMoEOYn'
            'ggYJzEOokKFDiBJhVqNI0CLVAhk1cvQIUqQniu48kjRpISVKlSxdeoIpkyZN'
            'Cwdu4tSpk6dPCwMCACH+ADs=')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

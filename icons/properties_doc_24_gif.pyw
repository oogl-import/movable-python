#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/properties_doc_24.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhGAAYAPe3AP8A/6msyqiryaeqyaapyaWoyKWox6SnxqOmxaKlxair'
            +'ys/m/87l/snh+sDa8bbR6KrH3aPB1dfh8KuvzYeKstHn/9Dm/9Dm/s/m/svi'
            +'+sPb87jT6azJ3sLW5efw+rG41KeqyNPo/9Ln/9Ln/s7k+8bd87vV6q/K3/H2'
            +'+u72/r7G39Xp/9To/tHm+8nf9L7X6+Pt9Pz9/vD3/szV6qSox9jq/9fq/9fp'
            +'/tTn/Mzh9eTu9/7+/v3+/vL4/tbg8qOnxtrs/9rr/9nr/tfp/M/j9sTa7bjQ'
            +'4qvG17TL2cjAyc5gVPs1A9zt/9vs/tnq/dLl9sfc7bvS49V+bfU+EPo2BKGk'
            +'xN/u/97u/97t/tzs/dXm98ve7vs2BPg7C95MMJ+jxOHv/wAzmS8zfes1DPk8'
            +'Dd2JeYuLsJ6hwuPw//7x7vxbMvZYMuekmdHi8Jygweby//x0Uubl7uTw/t7s'
            +'+YaIsZuewOjz/v2yoOfy/ebx/YSHr5qdv+r0/v3Yz/tCE/yZgOnz/YKFr5ib'
            +'ve31/vtOIv2/r+z1/uz0/YGErZaZve/2/vyNcYCDrZWYu/H4/n+Cq5OXu/T5'
            +'/n2AqpKUufb6/v7l33x/qpCTuPj7/np+qY6St/v8/nl9qYyPtXh7p4uOtXd6'
            +'p4qNtIiKsoeKsYWIsYSHsIOGr4KFroGErn+Bq3yAqnt/qXp9qXl8qHZ5pgAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            +'7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            +'/wAAAJEEPdtAfHUAEnyBCwAAAAvEAP8CYQAA/2ELxAAYAgAAAAAAABLbKABA'
            +'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLR//QAAAAAA'
            +'AAACALwAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            +'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAYABgAAAj+AAEACCBAwAAC'
            +'BQwcQJAAgUOBECMKVLCgIgMGDRw8gBBBwgQKEiUKqEDSwgUMGTRs4NDBwweQ'
            +'IQWCCEEzhIgRI0iUMHECRQoVMEMaWEG0KAsWLVy8gBFDxoygEWnUmErVxo0b'
            +'OHLo2MGjhw+oAn8AGUsWSBAhQoYQKWLkCJIkSpYsgZiAid27d5s0cfIEShQp'
            +'U6jIhVjFiuHDh69gwZJFyxYuXbxI/AKmcpjLmDGLGbOETBkzEs+gGR1mh+nT'
            +'O9KoWbKGTRuwbt7ILo3aNJwlY+LImUNHYh07wGmjviNXDB48efRI3MOneZg7'
            +'avqYTuNnyZ8wfAABCiRR0KDvYQiULfFTaMefJYR2hBlk6BAiiYkUyQ+jWu6i'
            +'6uXDyFfESGIjRwDStohc6JkWBoCOPCIRJJE0KFwh1d1hYIORSCLRJJRkKNwO'
            +'laiRhoEZUmKJRJdgYmJmKF5mIiaZSKTJJjDGKOOMMHIiUSc85Kjjjjzm6IlE'
            +'n9QmpJCgSBSKKKOQUoopp6DCSCqSqLIKK6144gkorkAUEAAh/gA7')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

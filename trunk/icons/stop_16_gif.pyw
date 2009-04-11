#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/stop_16.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhEAAQAPf/AP8A/6AEALYXCcMiEMIfDbQRA58FAc0yHvZ2WP6ehf+j'
            'i/6Uefx2U/BKI8UeBZwEAaUJA+xgQv+7qf/Kvf6ljv2DZPxzUP1uSv1hOflE'
            'FNcsBKIJAexeQf/HuP2vnPxcOvs6Cvs1A/kzAfIvBes1Buk3Bc0sBZwEAMsv'
            'Gv+vmf6ii/tNIfxxTfs9DvswAPcxAPE2BvFuTOM8ENsyBNc2BrUcBKADAPNq'
            'Sv+mj/tGH/xvTP////64p/YzB+0qAPaijOd/YtAoAMw0B8MwB58GALQTBvx8'
            'W/1sSPszAfs8Ef60ofi2pPWnkvLEttNBGsgvBMQyB8M0B6kSAr4dC/5oQfxJ'
            'HPkxAPIxBfe1pPLGudA2DcYsAMIyB8U2B60YBLwZBv5HF/w6Cfg1BPAxAegr'
            'APSlke+6q8UvBsAtAq4ZBK8PAvo2A/g1A+4yAug1CvKijPHCtO24qem3p8Q6'
            'E8EvBcQ0B6oTA54EAeQwBPE2BOQqAOlwUPHEt8o2DcMtBOiyotqEab4mAMMz'
            'B8ExB6AIAboaA+c3Bd0xA9g9EuCAZMtAGMEsAMQ4D9mAZcdDG8U1B7MfBZsE'
            'AcorBdg2Bs0xBMQnAMEuA8EwBL8nAMEvBMQ1B74uB54GAaEJAcMrBcc1B8Iz'
            'B74tBqQMAp0EAbEcBMAwB7MfBJ8HAakTA64YBAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAAMB8AP8CPQAA/z3AfAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfKB//QAAAAAA'
            'AAACAKgAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAj6AAEIFBhAwAAC'
            'BQwMXAggwAEECRQsYNDAwQOGECJImEChgoULGDJo2DAwAIcOHj6ACBFCxAgS'
            'JUycEIgihYoVLFq4eAEjhowZNGoAsHEDRw4dO3j08PFjB5AgQoYQKWLkCJIk'
            'SnYsYbKjiZMnUKJImUKlSggrV7Ds2JFFyxYuXLp4+QImjJgxZMqsNXMGDdwu'
            'adSsYdPGzZsdcOLskDOHDpc6du7gyaNnzw4+ffz82QEokKBBhAAUMnQIUSJF'
            'i9AwauSIziNIAiNJmkSpkiW4lzBl0rSJ08BOnj6BggtXkKZQohiOIlWqzqNH'
            +'UQaZ8s1Q4ClUqdKgCr0wIAAh/gA7')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

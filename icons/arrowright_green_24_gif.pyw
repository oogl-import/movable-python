#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/arrowright_green_24.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhGAAYAPf/AP8A/xmyCVy+P33KW5DSbJXUcJDSaX/KWGS6P0GiJByC'
            +'DxmDD27FT6fchsbor9PuwtXuxc/svcfpsbrjn6ndhpLVZXLEQj6cH0GzK5bV'
            +'dMvqtuHz1tzxz8jptLThl6TbgpzXd5nWc5PUaoHOUmvJOEitIEKzLKPagdjv'
            +'ycPnrJ3YeIPNVHXIQW/FOG3ENW7FN23GO2fFOFvBLVTDJkGxHQxlCJjVddbv'
            +'x9nwyqvejILNUoDMUXzLTnjLS3TJSF/BK1e/J069I0e7IETAHjCkFXLFUcjp'
            +'sX/MUJzYev///6Tcilm/KFO/JUq9IUC6HTm5GTW+FhqFDAdQBKfbhdHsv6nd'
            +'iHfJQ3vLTbrko73nrUu8IUS7Hjy6GjK3Fiu4EiKuDmO8Q7vkn7jjnX/MT37M'
            +'UHfKSoXQX+f24bjlqja4Fy22EyK0DR24Cw97BoDKWrfim5XVbYHNUX7NUHrL'
            +'TXbKSXHJRmvHQm3IRsnrvLnnrkC8JDm6HxyyChm2CRSXCIvQYqTbgX7LTZHT'
            +'Z57Ze5vXeZjXd5XWdJDVcYzUbn7QYXrPXbDjoM3uxz+8KRqyCRmzCRipCYbO'
            +'WI7SYnHGO/f89Pb89Ob24tfx03nJR33LSmzDNnDGOGnDMMrrutvx0Nnxz9jw'
            +'ztbwzdXvzNPvy9Lvys/uyOT24XXQaRiuCWK7LWnEMWLCLWnGQGLEPFzDN1bB'
            +'M0/AL0m+KkO9JlrFQ5Xah3XRaRq1CRafCEqlIWXGLljAKU++JFrBMFXBMk/A'
            +'Lki+KkK9JVfFQcTrve3566jiohq4CRGFB1vEKVG+JVO+KVfAKFG/LEi9KUG8'
            +'JVrFRNny1P3+/UOqHk3BIkO7HT26G0C7HTG3FTq6IJrcjhOTCEK9HTS3Fh+z'
            +'DDO5G1XFQ/L68KvipBm1CSCDDjW9Fy24Eya0Dw1yBhmDCyW4Dx62DBq3CRmx'
            +'CQ52BhelCRWdCBitCRSZCKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            +'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAYABgAAAj+AAEIHCgwgMGD'
            +'BgkqVGhQwAACBQwcQJBAwYKFBA0yaODgAYQIEiZQqGDhggIFGANgyKBhA4cO'
            +'Hj6ACBFCxAgSJSwyNHECxYYUKlawaOHCxQsYMWTMoKGgRkYbN3Dk0EFVxw4e'
            +'PXz8ABJEyBAiTgsWMQLhRFUdR5AkSaJkCZMmTp5AiSKl4BQqVaxUPXIFy9ok'
            +'WbRs4dLFy5e6AcCEETOmKpkrZcyc+YuGSxo1a9i0kRLAzRs4VOPImUOnjp07'
            +'eP7m0bOHTx8/nP8AChRI0CBChQwdQpRI0aK/jBo5egSJcyRJkyZR+su8kiXm'
            +'lw5yxpSpKPPr2A0+4qxpEydOnTzBfQIVStQoUqVMMT9lEBXnVKpWyWfVytUr'
            +'WLFkzaL1t5ZBW7dwhksuuhS4Cy+9+PILMMEIM8xaxBxUjDF1LXAMMloko4wu'
            +'yzDTjDPPQAPhQY8EUBcAC0QjzTTTUFONNXpcg81fEUqYzYkoasPFNtz0yE03'
            +'3nyTBDgIheMeQQuIMw455fiIEEKPPGIOjgItcA466Tz5pDrrsEPlQDXU0I46'
            +'6kRp5iNkBvilQjVI4Q4qj4QTziPvwCPFmhgBcOeee+YZEAAh/gA7')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

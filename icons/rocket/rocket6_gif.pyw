#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/rocket/rocket6.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODlhFAAUAPeWAP7+/vz8/MYAAKurq+np6aioqPDw8Pv6+v/+/vHZ2vLv'
            '770AAL0DA7VtbdPPzfj4+MC+vsC8vPHv7+vV1eDExLgAAMc4ONq0tEVCQqkB'
            'AX19fdzFxdm3tv38/OS2tpeksero5/v4+J88PV5nZ8Z0dEGHvX5JSqKiosx6'
            'ej92mDdviv7//wWAxdPS0t7Z1pYAAObS0XoAAGgWFuPj4+jV1QCD09vCwtnc'
            '3KuqqlFQUJWZmZWVlcBiYuCsrCkzMjQRENnZ2RkjInolJs0AAN28u/X19c3L'
            'yZxgYOHDw3tDQs2Ehb1WV81XV1wYGJkAAIVERM0LC8kMDFoUFIhTU/n5+fLy'
            '8sU8PP39/aMKC9PT06AdHagVFbVBQWwAAHpBQHFvbnx/gjlGTswSEri4u5We'
            'qbirqytPX+nk5ZycnfPz8/3//21qZx0REkx2lt3V1UkJCMjIyNfX1/37+5GL'
            'iX9bXL8AAE5GQcvIxtDQ0L5ERffk5U1daPDp6rnCw/Pp6c9pbDyDt7IfIOPE'
            'xUgICP78/NTU03l5eYAKC5GMi8EAAN3d3YiJiu7Fxfz7+9Wxsdzb2/z5+b2O'
            'jc7OzvHj5M/Pz////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAACH5BAEAAJYALAAAAAAUABQAAAjsAC0JHEiwYIAq'
            'WSgVXEjwwQw8BQYwXAjAgCQgcXbAmUjwiiIjIAgM0FCEo0AAj8Z8IHPCUIFK'
            'JisRcNCmBKA9a9JMlFOpkoRCLlLUYBHmDkyCCPwIUkIiUoQbEMCoMIMIQMED'
            'PSxAGbJARJ8yi77YmUOl4CQmAgTUSbRFR4MnI3LgCFCQBhcrf/JgcULniAwf'
            'GFocJXhhAiRLIZCYSNIkyA8pZ0wKDDDlDZtBXQ65kVyJiBc0QmK80KLAJAAb'
            'jgxY8pChAo8VJg9sICRQjxgGMDgjGJggyhI1kgsyCsQnOMFKKCgMNt6BQyOT'
            +'AQEAOw==')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

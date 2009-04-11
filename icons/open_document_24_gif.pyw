#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/open_document_24.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhGAAYAPf/AP8A/xiFDBeWDBqZDSSkFDGuHM+aAUG7KD6xJv//7P//'
            +'vP//wPv1nUW3K1jJOPDgpP/9oP/8iv/8kP/9mfXohmSGBEezLGbRQVS8Nv//'
            +'x//1gv/1j//1jv/0jf//t///r///rvT5pvj7pfr8o3ewTE+3MnDWSHLTSv/2'
            +'q//tfv/shf/shP/sgP/sfP/sff/sfmPHQHraT4PfVf/vp//ldv/lfP/lff/j'
            +'ffvdctK4QEetLXLUSnvZUIPeVYjhWYvjWlGvM8OXAf/pn//ccP7ddv7cdf7c'
            +'dP7cc/7bc/bOYdmoHNWlHNfOjGbFQozmW4nhWY/nXWC9Pu/x2//imf/TZ/7U'
            +'bf7UbP7RafvOZPnNYfXJW+u+SNWjF924S/v33//86N3nsXPOSpXrYWTBQfD2'
            +'1vXprf/bi//NX/7NZOOvLNOfDdOgD9OgENOjF+zXjv794v/6w//4pf/4o8/d'
            +'hFe1OOvzq/38tfzVd/vIXOm4PtWnIPPmtvr00Pr10fr20vz51f77uf/4m//2'
            +'j//2kf/2kv/3k7fQa+Dqi///pOLBQ/jRafPEVdenH+fLc//8xf/zif/yif/y'
            +'i//zjvPeav/4lf/6mPXPZeW3PtisKfjuv//vjf/thf/thv/th//uifPZZf/1'
            +'lu/KYNioH+LBXv70u/7nff7ogv7ogf7phPHTXv/ujefCUtWnHfPirf/oj/7i'
            +'fP7jfP7kff7jffPRXtyxMd63Sfvuvf7dcf7ed/7edv/feP/hfPjSZdapH+vT'
            +'j//kl/7Zb/7Zcf7ac//cdv/fe//eev/ceP/cd9mvNPjpvP/Ybv7Yb/7YcP/Y'
            +'cf/bdP/def/Zc/XMXN2sItCcBuXIdv7pqf/Ybf/bdf/bd/nRY+OzMNCbAtGf'
            +'De7Ui/jTa+3AReCwKAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLJ//QAAAAAA'
            +'AAACALoAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            +'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAYABgAAAj+AAEIHEgQQICD'
            +'BwsqXDjwoIABARhKJBiAQIGICw1o3LgwwAEEGAkaSKCg5AIGBhQGaOAgpEAD'
            +'DyBEkEBzAoWNGytYuIDBpYEMGjYI5dABgocPIEKIGEGihIkTPlGkUEFVxQoW'
            +'LVy8QBgARgwZXAEYmEGjhtkaNtLewJEjgI4dPHr4+AEkQBCxQoYQ2VvEyBEk'
            +'SZQsYRKgiZMnUKIEkJLSwBQqVaxcwZJFyxYuXbx8ARMgjJgxAciUaWzmDJo0'
            +'atawYdPGzRs4ceTMCUAnQB07KcXewZNHzx4+ffz8ARRI0CBChQwFOIQoUW4D'
            +'ihYxauSoUCFCHR5BisQ9kqRJlCqT5RZr6RKmTJo2qd/EqX37Tp4+gRovNpSo'
            +'UaRKmTrFvz9/U6ikogp9BqzCSiuuvALLggwyGIsss9AnFi212HILLhhmiEsu'
            +'HOqyCy8SGtCLL78AE8yJKAozDDHFGHOMhGIhk4wyyzDDTDPOFPMMNNFIw5FC'
            +'01BTjTXXHINNNtpsg9NE3HTjzTfgLDlRQVJOaeWVBAUEACH+ADs=')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

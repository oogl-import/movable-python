#Embedded image created from D:/Python Projects/modules in progress/movpy/icons/stop_24.gif
#Done with imageEmbedder 1.0 utility img2pytk.py from
#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk

import Tkinter as tk
root = tk.Tk()

img00 = tk.PhotoImage(format='gif',data=
             'R0lGODdhGAAYAPdYAO6IbfKJbvSFafWAYvV8XvN5WfF0VPBvTfBqR/BnQ+9k'
            +'QPFhPPJgOvNeN/RaMvRVLvNQKPFMI/NHHfRGG/VEGfZCFvc/E/Y8D/Y5C/Y3'
            +'CPc1Bfg1BPc0A/Y0A/MyA/AzA+wyA+oyA+gyBOYxBOUxBeMxBeEyB90zCNsz'
            +'CNkyCNcxCdQxCNIxB9AxBc8wBc0wBMswBMkyB8czB8YyB8UwBcQwBsMxBsMx'
            +'BsIxBsIxBsExBsExBsExBsExBsExBsEwBcEuBcEsBMApA8AnAr4mA70lA7sj'
            +'A7cfA7MbA7AXA60SAqoQAqcNAaQLAaEIAZ8GAJ4EAJ0DAJwCAJwCAJsBAJoA'
            +'AJoAAJoAAJoAAJoBAJkDApgFBJUKCY4UE4QlJHc5OHBFRWtQUGhWVmZcXGRk'
            +'ZGVlZWZmZmdnZ2hoaGlpaWpqamtra2xsbG1tbW5ubm9vb3BwcHFxcXJycnNz'
            +'c3R0dHV1dXZ2dnd3d3h4eHl5eXp6ent7e3x8fH19fX5+fn9/f4CAgIGBgYKC'
            +'goODg4SEhIWFhYaGhoeHh4iIiImJiYqKiouLi4yMjI2NjY6Ojo+Pj5CQkJGR'
            +'kZKSkpOTk5SUlJWVlZaWlpeXl5iYmJmZmZqampubm5ycnJ2dnZ6enp+fn6Cg'
            +'oKGhoaKioqOjo6SkpKWlpaampqenp6ioqKmpqaqqqqurq6ysrK2tra6urq+v'
            +'r7CwsLGxsbKysrOzs7S0tLW1tba2tre3t7i4uLm5ubq6uru7u7y8vL29vb6+'
            +'vr+/v8PDw8vLy9XV1d3c3OXk5PDv7/f29vv6+v38/P79/f7+/v7+/v7+/v7+'
            +'/v7+/v7+/v79/f79/P78+/77+v76+f76+f75+P749/329f318/3y7/3w7P3u'
            +'6v3r5/3k3f3f1/3a0fzWzP3Ow/3Ft/y+r/24p/21o/2zoP2wnv2tm/2nmf2e'
            +'m/2Uov2Kp/19rv1tt/1Vx/4x3f4Y7v4C/f4A/v4A/v4A/v4A/v4A/v4A/v4A'
            +'/v4A/v4A/v4A/v4A/v4A/iH5BAkAAPgALAAAAAAYABgAAAj+APEJHCgQC5Yn'
            +'SphEMUiwYUMsSVA8YKCAwYMKLJhgcUgQCxMJBtadI1cu3boBDCqkcLLRIUQH'
            +'68SFG2cywIABBh5cGLGk5UCIDNSBGxcAAQQKFixUmDDhgogTPQkyeaAuXDoE'
            +'FDJs2LqBwwcQIkiccPHk54QA4tY9yACBA4etHT5EEFHiRIoVRFoqQVBO3QMN'
            +'6rINcKsBhIJu5eyyaBGjCT4sKgRcxRBhGjNkAzwY5saMWQIWL2LMOGJQQgAB'
            +'FLoSqHa5QAPOzACwiBHjRg4gWKJAEKBAq9vVzLBp6wzgBYwZtnPkiKIkAoII'
            +'XOMa2NbZWvHjyrM3YWJBwoWtHj6ojHhdncCQ5NlzNImSIYMGryBGKOAMDRmz'
            +'aQKGpFe+UMSGuPHNR5wBrCEjQBDp4YYFDACOEMFwsQkxBHDMKJAeafgwAUII'
            +'JJhwAjnOACAEDTkQsVo4MqTn2GMviIXCCisgQAOJygmxgAwIKpfXQE+o8CJj'
            +'yO23HxBl/bREC0AKKWRUHS1BwwxKJsjkQ08QEaWOT/jEERZNHAFEgkc0oSVH'
            +'P+XWxHoMcRQQACH+ADs=')

newButton = tk.Button(root,image=img00)
t = str(img00.width()) + ' wide x ' + str(img00.height()) + ' high'
newButton.pack()
tk.Label(root,text='The image is\n'+t).pack()
root.mainloop()    #comment this out to run from IDLE

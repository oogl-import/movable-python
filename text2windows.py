from pathutils import walkfiles
import os

#thedir = r'../Webstuff Python/Voidspace FTP Changes'
thedir = r'.'
fileending = ['.py', '.txt', '.ini', '.html', '.css']

for member in walkfiles(thedir):
    if '.svn' in member:
        continue
    ext = os.path.splitext(member)[1]
    if ext in fileending:
        #print 'Reading : "%s"' % member
        a = open(member).read()
        print 'Writing : "%s"' % member
        open(member, 'w').write(a)


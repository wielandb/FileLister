def FileList(path, ext=None):
    import os
    filelist = []
    for a,b,c in os.walk(path):
        for f in c:
            if ext:
                if "."+ext in f:
                    filelist.append(os.path.join(a, f))
            else:
                filelist.append(os.path.join(a, f))
    return filelist
            

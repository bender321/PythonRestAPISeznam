import  os
import time



def file_size(path):
    file_stats = os.stat(path)
    return file_stats.st_size / (1024 * 1024)

def directory_size(path):
   print(sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)))



def get_whole_list(path):
    dic ={}
    try:
        dir = os.listdir(path)
        for f in dir:
            fullpath = str(path + '/' + f)
            if os.path.isfile(fullpath):
                data = get_info(fullpath)
                name = str(data[0])
                info = [str(data[1]), str(data[2]), str(data[3])]
                dic[name] = info

            else:

                info = ["Folder"]
                dic[f] = info

        return dic
    except OSError as e:
        return "Error: %s : %s" % (path, e.strerror)




def delete_by_path(path):
    if os.path.isdir(path):
        try:
            dir = os.listdir(path)
            if len(dir) == 0:
                os.rmdir(path)
                info = "Folder deleted"
                return info
            else:
                info = "Folder is full, can not be deleted"
                return info
        except OSError as e:
            info = "Error: %s : %s" % (path, e.strerror)
            return info
    else:
        try:
            os.remove(path)
            info = "File deleted"
            return info
        except OSError as e:
            info = "Error: %s : %s" % (path, e.strerror)
            return info



def create_file_by_path(path):
    try:
        if os.path.exists(path):
            info = "File already exists in this directory!"
            return info
        else:
            with open(path, 'w') as wfile:
                pass
            wfile.close()
            name = path.split('/')[-1]

        info = "File called " + name + " was created!"
        return info
    except OSError as e:
        info = "Error: %s : %s" % (path, e.strerror)
        return info


def get_info(path):
    try:
        if os.path.isdir(path):
            info = ["Nejedná se o soubor!"]
            return info
        else:

            ctime = time.ctime(os.path.getctime(path))
            sinceEpoch = os.path.getmtime(path)
            mtime = time.strftime('%d %m %H:%M:%S %Y', time.localtime(sinceEpoch))
            size = file_size(path)
            name = path.split('/')[-1]

            info = [name, "Date of creation: " + ctime, "Date of modification: " + mtime, "Size of file: " + str(size) + " MB"]
            return info
    except OSError as e:
        info = ["This file does not exist :-( "]
        return info







#if __name__ == '__main__':
    #path = 'D:/test'
    #print(fullpath1)
    #print(get_whole_list(path))
    #print(delete_by_path(path))
    #create_file_by_path(path)
    #get_info(path)
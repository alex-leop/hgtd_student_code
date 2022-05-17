import os

## list the input files
path = '/eos/user/a/aleopold/project10/data_with_jets'

def createTextFile(list, extension):
    f = open("input_list_{ext}.txt".format(ext=extension), "w")
    for element in list:
        f.write(os.path.join(path,element) + '\n')
    f.close()

if __name__ == '__main__':

    fileslist = os.listdir(path)

    ## write the file paths into text files, split into N paths per file
    n_files = 20
    chunks = [fileslist[x:x+n_files] for x in range(0, len(fileslist), n_files)]

    for i, chunk in enumerate(chunks):
        createTextFile(chunk, i)

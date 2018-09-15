import os, sys
import hashlib

file_sizes = []

def findDup(parentFolder):
    # Duplicates in format {hash:[names]} 
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            
            #Check how many times the file is found in file_sizes list
            
            
            # Ignore symbolic links
            if os.path.islink(path):
                continue
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups
 
 
# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]
 
#Returns hash of filename
def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    bufr = afile.read(blocksize)
    while len(bufr) > 0:
        hasher.update(bufr)
        bufr = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
 
 
def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates files are grouped together below. Files with different content are separated by ### header')
        for result in results:
            group = []
            for subresult in result:
                group.append(subresult)
            print(group)
            print('###')
 
    else:
        print('No duplicate files found.')

def create_byte_list(parentFolder):
    print("Generating byte list")
    for dirName, subdirs, fileList in os.walk(parentFolder):
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            
            # Ignore symbolic links
            if os.path.islink(path):
                continue
            
            # Calculate file sizes
            file_sizes.append(os.path.getsize(path))
    print(file_sizes)
    return
    
 
if __name__ == '__main__':
    if len(sys.argv) == 2:
        dups = {}
        folder = sys.argv[1:]
        
        #This for loop creates a global list called file_sizes
        for i in folder:
            # Iterate the folders given
            if os.path.exists(i):
                create_byte_list(i)
            else:
                print('%s is not a valid path, please verify' % i)
                sys.exit()
        
        #This for loop finds the duplicates
        for i in folder:
            #Find the duplicated files and append them to the dups
            joinDicts(dups, findDup(i))
            
        printResults(dups)
    else:
        print('Instructions: python findduplicates.py folder')
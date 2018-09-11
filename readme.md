This python 3 script receives a path as argument 1 and returns a list of all paths & files that have duplicate content. os.walk crawls the directory and sub-directory and takes the hash of every file and stores them in a dictionary in format: {hash:[names]} . The keys are compared and duplicate hashes have the value dumped to a list.

Example usage: 
"python findduplicates.py /home/ec2-user/environment"
"python  /home/ec2-user/scripts/findduplicates.py /home/ec2-user/environment"
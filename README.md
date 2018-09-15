This python 3 script receives a path as argument 1 and returns a list of all paths & files that have duplicate content. os.walk crawls the directory and subdirectories and first makes a list of all file sizes. It then runs another loop of every file, gets the current file size, and evaluates if there is more than 1 occurence of the file size in the file size list. If there is more than one occurence it takes the hash and stores them in a dictionary in format: {hash:[names]} . The keys are compared and duplicate hashes have the value dumped to a list and then printed to the screen.

Example usage: 
"python findduplicates.py /home/ec2-user/environment"

"python  /home/ec2-user/scripts/findduplicates.py /home/ec2-user/environment"


Example output:
Generating byte list
Scanning /home/ec2-user/environment/clc/toolbox/.git/logs...
Duplicates files are grouped together below. Files with different content are separated by ### header
['/home/ec2-user/environment/clc/toolbox/ARCHIVE/CalendarAutomation/Microsoft.Exchange.WebServices.xml', '/home/ec2-user/environment/clc/toolbox/ARCHIVE/OofBot/LocalModule/Microsoft.Exchange.WebServices.xml']
###
['/home/ec2-user/environment/clc/toolbox/.git/logs/HEAD', '/home/ec2-user/environment/clc/toolbox/.git/logs/refs/remotes/origin/HEAD', '/home/ec2-user/environment/clc/toolbox/.git/logs/refs/heads/master']
###
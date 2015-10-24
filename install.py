#Social Engineering Toolkit installer.
#by John Grindal.

import os, sys

#exit program if not root user
if not os.geteuid()==0:
  sys.exit("Please run this script as root")

def install():
  os.system("clear")
  print "Installing Git if needed..."

  os.system("sudo apt-get install git")

  print "installing"

  
  os.system("git clone https://github.com/trustedsec/social-engineer-toolkit/")
  os.system("chmod +x redirect.sh")
  os.system("./redirect.sh")



yes = set(['yes','y', 'ye', 'Y'])
no = set(['no','n'])

choice = raw_input("Would you like to install Social Engineering Toolkit y/n:").lower()
if choice in yes:
   install()
elif choice in no:
   sys.exit("Okay...")
else:
   sys.exit("Answer yes or no.")

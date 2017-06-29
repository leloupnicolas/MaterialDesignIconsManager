import sys, getopt, os, subprocess

CWD = "/Users/nicolasleloup/scripts/mdim"
VENDORS_DIR = CWD + "/vendors"

MDI_REPO_URL = "https://github.com/google/material-design-icons.git"
MDI_VENDOR_DIR = VENDORS_DIR + '/material-design-icons'

def usage():
  print 'usage: help should be displayed here'

def execCommand(cmd):
  process = os.popen(cmd,"r")
  logProcess(process)

def handleColorization(color):
  print 'to be defined'

def cloneMDIRepo():
  print 'Creating material-design-icons local copy'
  execCommand('git clone ' + MDI_REPO_URL + ' ' + MDI_VENDOR_DIR)

def updateMDIRepo():
  print 'Updating material-design-icons local copy'
  execCommand('cd ' + MDI_VENDOR_DIR + ';git pull origin master')

def logProcess(p):
  while 1:
    line = p.readline()
    if not line: break
    print line 

def ensureGithubRepoIsAvailable():
  if os.path.exists(VENDORS_DIR):
    if os.path.isdir(VENDORS_DIR):
      if os.path.exists(VENDORS_DIR + '/material-design-icons'):
        updateMDIRepo()
      else:
        cloneMDIRepo()
    else:
      print 'vendors is not a directory'
  else:
    print 'Creating vendors directory'
    execCommand('mkdir ' + VENDORS_DIR)
    cloneMDIRepo()

def main(argv):
  group = ""
  iconName = ""
  projectSrc = "application"
  assetsCatalogName = "Assets"
  newName = None
  try:
    opts, args = getopt.getopt(argv, "-h-g:-i:-p:-a:-r", ["help", "group=", "icon-name=", 'project-src=', 'assets-catalog-name=', "rename-with="])
  except getopt.GetoptError as err:
    print(err)
    usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
    elif opt in ("-g", "--group"):
      group = arg
    elif opt in ("-i", "--icon-name"):
      iconName = arg
    elif opt in ("-p", "--project-src"):
      projectSrc = arg
    elif opt in ("-a", "--assets-catalog-name"):
      assetsCatalogName = arg
    elif opt in ("-r", "--rename-with"):
      newName = arg
    else:
      usage()
      sys.exit(2)

  ensureGithubRepoIsAvailable()

  copyCommand = 'cp -r ' + MDI_VENDOR_DIR + '/' + group + '/ios/ic_' + iconName +'.imageset $PWD/' + projectSrc + '/' + assetsCatalogName + '.xcassets/'

  if newName is not None:
    copyCommand += newName
    
  execCommand(copyCommand)

if __name__ == "__main__":
  main(sys.argv[1:])

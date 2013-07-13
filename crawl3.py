import os, argparse, string, cPickle as pickle
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

"""
usage: deecrawl2.py [-h] [-d] url

crawls a url passed as command line argument for job listings matching the
provided criteria.

positional arguments:
  url -- url to start crawl from

optional arguments:
  -h, --help  show this help message and exit
  -d, --dump  dumps and replaces existing dictionaries
"""

parser = argparse.ArgumentParser(
        description='crawls a url passed as command line argument for job \
        listings matching the provided criteria.', fromfile_prefix_chars="@" )
parser.add_argument('-d', '--dump', 
	 help='dumps and replaces existing dictionaries', action="store_true")
parser.add_argument('url', help='url to start crawl from', action='store')
args = parser.parse_args()

if args.dump: dump = True           # dump; will override any existing
else: dump = False                  # dictionaries and drop existing tables

# ---------------------------------------------------------------------------- #
#   function - pickleDump
#   saves "files" and "extensions" dict to a file
# ---------------------------------------------------------------------------- #
def pickleDump():
  global matchedJobs
  print 'pickling...'
  pickle.dump( matchedJobs, open( "filesdict.p", "wb" ) )


# ---------------------------------------------------------------------------- #
#   function - pickleLoad
#   loads "files" and "extensions" dict from a file
# ---------------------------------------------------------------------------- #
def pickleLoad():
  global matchedJobs
  cwd = os.getcwd()
  fileDictPickle = str(cwd) + '/filesdict.p'
  print 'Loading files...'
  matchedJobs = pickle.load( open( fileDictPickle, "rb" ) )



# ---------------------------------------------------------------------------- #
#   function - pickleTry
#   checks if pickled files already exist
# ---------------------------------------------------------------------------- #
def pickleTry():
  cwd = os.getcwd()
  try:
    with open(cwd+'/filesdict.p') as f:
        pass
        print 'pickle found'
        return True
  except IOError as e:
    print 'pickle not found'
    return False

# dictionary selection
#  - if dump flag; replace existing dictionaries
#  - if pickle's found, use; else start new dictionaries
if not dump:
  if pickleTry():
      pickleLoad()
      print 'Using existing dictionary...\n'
  else:
      print 'Starting new dictionary...'
else:
  if pickleTry():
      'Replacing existing dictionaries.'


def main():

	site = args.url
	print site
	soup = BeautifulSoup(urlopen(site))
	print soup

	if soup.find('span', attrs={'title' : 'Show/Hide Courses for Subject'}):
		spanTitle = soup.find('span', attrs={'title' : 'Show/Hide Courses for Subject'})
		print spanTitle

if __name__ == '__main__':
	main()

# sierra-isbn2bibnum
A python script to make SQL queries for ISBN's against a Sierra postgres database and return any matching bib numbers. 

To use this:

* Clone this repo onto your local machine which has Python3 installed on it. You'll also need psycopg2, a python library for connecting to Postgres databases. You should be able to get it by running "pip install psycopg2".
* Edit the file repeater.py. Make sure the shebang line (the first line in the file) points to your Python3 executable. Then find the section "params" and replace "sierra-db.dartmouth.edu" with the hostname of your institution's Sierra database server.
* Replace the contents of "inputfile.txt" with a set of ISBN's, either 10- or 13-digit, one ISBN per line
* Create a file in the parent directory of this repository, with your Sierra login on the first line and your Sierra password on the second line. (I'm keeping this file outside of the repository to try to prevent anyone from accidentally pushing their credentials up into Github.)
* From the directory of this repository, run ./repeater.py.
* Note that this can take some time - it took several minutes for my test case of about 80k ISBN's, and there's no indicator that things are working during that time. If you need to quit early you should be able to CTRL-C out of it (though sometimes I've had to hit CTRL-C multiple times.
* When the process finishes, you should have a pile of bib record numbers in outputfile.txt (assuming that some of the ISBN's from inputfile.txt matched on some of your Sierra records).

Note that this script *does not* make any attempt to cross-check 10-digit ISBN's with 13-digit ISBN's. It's looking for ISBN's in Sierra that exactly match those you put in "inputfile.txt". 

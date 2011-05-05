# Copyright (c) 2011
# Jann Kleen jann@pocketvillage.com
# Thomas Maier thomas@thomas-maier.net
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import os
from operator import itemgetter

#numpy is needed to run the function numpyMatrix_from_list(listData,conversionMap)
#from numpy import zeros

#use psyco for the module if you want.
#import psyco
#psyco.full()

DOWNLOAD_DIR = "/home/thomas/Downloads"
OUTPUT_DIR = "/home/thomas/Desktop"
OUTPUT_FILENAME = "codejam.out"

"""
this function scans the folder DOWNLOAD_DIR for files ending with ".in" or "in.txt" (Safari on OSX extends the file with "txt") and asks the user wich file shall be opened. a suggestion, pointing on the newest file, helps to choose the rigth one.
arguments: none
returns: a list with lines from the chosen file
"""
def get_file():
	filenames = filter(lambda x: x[-3:] == ".in" or x[-7:] == ".in.txt", os.listdir(DOWNLOAD_DIR))
	fileinfo = map(lambda fname: (fname, os.path.getmtime(os.path.join(DOWNLOAD_DIR, fname))), filenames)
	if len(fileinfo) > 0:
		print "[CodeJamHelper] %d files with extension *.in or *.in.txt found in %s" % (len(fileinfo),DOWNLOAD_DIR)
		for idx in enumerate(fileinfo):
			print "[CodeJamHelper] %s) %s" % (idx[0], idx[1][0])
		while(True):
			try:
				suggestion = fileinfo.index(sorted(fileinfo, key=itemgetter(1), reverse=True)[0])
				choice = raw_input("[CodeJamHelper] choice (%s):" % suggestion)
				if choice == "":
					choice = suggestion
				else:
					choice = int(choice)
			except ValueError:
				pass
			else:
				filename = fileinfo[choice]
				break
		print "[CodeJamHelper] opening %s" % filename[0]
		with open(os.path.join(DOWNLOAD_DIR, filename[0])) as fp:
			lines = map(lambda x: str.rstrip(x, "\n"), fp.readlines())
		return lines
	else:
		print "[CodeJamHelper] no files in %s with extension *.in or *.in.txt found" % DOWNLOAD_DIR

"""
this function writes a list with strings (solutions) to the file OUTPUT_DIR/OUTPUT_FILENAME in "google code jam format".
example: ["solution1","solution2"] -> "Case #1: solution1\nCase #2: solution2"
arguments: a list with solutions
returns: none
"""
def put_file(lines):
	for idx, line in enumerate(lines):
		lines[idx] = "Case #%s: %s\n" % (idx+1, line)
	print "[CodeJamHelper] writing %s lines to %s/%s" % (idx+1, OUTPUT_DIR, OUTPUT_FILENAME)
	with open(os.path.join(OUTPUT_DIR, OUTPUT_FILENAME), 'w') as fp:
		fp.writelines(lines)

"""
you can use this function to get the number of cases. it simply returns the first line (striped) from the input file.
arguments: list of strings, provided by function get_file()
returns: number of cases in the input file
"""
def get_case_count(inputList):
	return int(inputList[0].strip())

"""
you can use this function to get the cases from the input file without the first line (number of cases).
arguments: list of strings, provided by function get_file()
returns: list with cases
"""
def get_case_list(inputList):
	return inputList[1:]

"""
if the length of the cases (number of lines for each case) is for each case equal, you can use this function, to get a list with tuples for the cases. for the conversion, a description for the tuples is needed.
example:
	inputList: ["2","3","A B C","5","A B C D E"]
	tupleDesc: [int,str]
	returns: [(3,"A B C"),(5,"A B C D E")]
arguments: a list of strings, provided by function get_file() and the description for the tuples
returns: a list with tuples containing the cases
"""
def get_case_tuples(inputList,tupleDesc):
	inputTuples = []
	for listPos in xrange(1,len(inputList),len(tupleDesc)):
		tmp = []
		for tuplePos in xrange(0,len(tupleDesc)):
			tmp.append(tupleDesc[tuplePos](inputList[listPos+tuplePos]))
		inputTuples.append(tuple(tmp))
	return inputTuples

"""
this function transforms a list with tho dimensions (also a list with strings - the chars are the second dimension) in a numpy matrix. for transformation, a dictionary is needed, which describes the conversion rules for the list contents.
requires: numpy module
example:
	listData: ["R.R","..R","BR."]
	conversionMap: {"R":1,".":0,"B":-1}
	returns:
		[[ 1.  0.  1.]
		[ 0.  0.  1.]
		[-1.  1.  0.]]
arguments: list with data for the matrix and a dictionary with the conversion rules
returns: the new numpy matrix
"""
"""
def numpyMatrix_from_list(listData,conversionMap):
	m,n = len(listData),len(listData[0])
	A = zeros((m,n))
	for mx in xrange(m):
		for nx in xrange(n):
			A[mx][nx] = conversionMap[listData[mx][nx]]
	return A
"""

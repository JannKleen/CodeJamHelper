# Copyright (c) 2011 Jann Kleen jann@pocketvillage.com
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

# Local includes
from settings import DOWNLOAD_DIR

# System includes
import os
from datetime import datetime
from operator import itemgetter
from functools import partial

def get_file(file_name = None):
    if not file_name:
        expanded_download_dir = os.path.expanduser(DOWNLOAD_DIR) 
        files = filter(lambda x: x[-3:] == '.in' or x[-7:] == '.in.txt', os.listdir(expanded_download_dir))
        max_name_len = max(map(len, files) + [32])
        files = map(lambda fname: (fname, os.path.getmtime(os.path.join(expanded_download_dir, fname))), files)
        if len(files) > 1:
            for idx, (fname, mtime) in enumerate(files):
                print "%s) %s %s" % (idx, fname.ljust(max_name_len), datetime.fromtimestamp(mtime).isoformat())
            done = False
            while (not done):
                try:
                    suggestion = files.index(sorted(files, key=itemgetter(1), reverse=True)[0])
                    choice = raw_input("choice (%s):" % suggestion)
                    if choice == '':
                        choice = suggestion
                    else:
                        choice = int(choice)
                except ValueError:
                    pass
                else:
                    done = True
                    fname = files[choice]
        elif len(files) > 0:
            fname = files[0]
        else:
            print "ERROR: no file found in %s" % expanded_download_dir
    else:
        fname = file_name

    print "Opening %s ..." % fname    
    with open(os.path.join(expanded_download_dir, fname[0])) as fp:
        lines = map(lambda x: str.rstrip(x, '\n'), fp.readlines())
        
    return lines

def put_file(lines, fname='codejam.out'):
    for idx, line in enumerate(lines):
        lines[idx] = "Case #%s: %s\n" % (idx, line)
    print "Writing %s lines to %s ..." % (idx, fname)
    with open(fname, 'w') as fp:
        fp.writelines(lines)
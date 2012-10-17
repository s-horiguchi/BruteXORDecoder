#!/usr/bin/env python
#-*- coding:utf-8 -*-

from subprocess import Popen, PIPE
import os, os.path

def file_check(path):
    p = Popen("file %s" % path, shell=True, stdout=PIPE, close_fds=True)
    p.wait()
    output = p.stdout.read()
    filetype = output.split(": ")[1].strip()
    if filetype != "data":
        print "Bingo!"
        print "File type is", filetype
        return True
    else:
        return False

def xor_file(code, path):
    fd = open(path, "rb")
    content = fd.read()
    fd.close()
    content = "".join([chr(ord(c) ^ code) for c in content])
    fd = open(path, "wb")
    fd.write(content)
    fd.close()
    return

def main(path, if_overwrite=False, savedir=None):
    if not savedir:
        savedir = "xor_%s" % os.path.basename(path)
    
    for code in range(0x100):
        print "[*] Trying to XOR with 0x%02x" % code
        if if_overwrite:
            xor_file(code, path)
            file_check(path)
            xor_file(code, path)
        else:
            copy_path = os.path.join(os.path.dirname(path), savedir, "0x%02x_%s" % (code, os.path.basename(path)))
            os.system("cp %s %s" % (path, copy_path))

            xor_file(code, copy_path)
            if file_check(copy_path):
                print "[*] Copied to", copy_path
            else:
                os.system("rm %s" % copy_path)                
                
    return

if __name__ == "__main__":
    from optparse import OptionParser

    parser = OptionParser("Usage: ./%prog [options] FILE_PATH")
    parser.add_option("-s", "--single-mode", dest="code",
                      action="store", type="int", default=None, metavar="CODE",
                      help="not-bruteforce mode. just XOR the file with the number<CODE>.")
    parser.add_option("-o", "--overwrite", dest="overwrite",
                      action="store_true", default=False,
                      help="not save XORed file.(finally original file will be restored)")
    parser.add_option("-d", "--save-directory", dest="savedir", 
                      action="store", default=None, metavar="SAVEDIR",
                      help="set the directory where xor-ed/checked file will be saved.(default is 'xor_<FILENAME>')")
    (options, args) = parser.parse_args()

    if len(args) == 1:
        if options.repair_code:
            print "<SingleXORMode>"
            print "[*] Trying to XOR with 0x%02x" % options.repair_code
            xor_file(options.repair_code, args[0])
            print "finished!"
        else:
            main(args[0], if_overwrite=options.overwrite, savedir=options.savedir)
    else:
        parser.print_help()

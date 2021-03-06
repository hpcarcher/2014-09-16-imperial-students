import os
import os.path

def file_exists(filename):
  if (os.path.isfile(filename)):
    print "OK ", filename, "exists"
  else:
    print "FAIL ", filename, "does not exist"

def file_not_exists(filename):
  if (os.path.isfile(filename)):
    print "FAIL ", filename, "exists"
  else:
    print "OK ", filename, "does not exist"

def files_equal(file1,file2):
  cmd = "diff -q " + file1 + " " + file2
  result = os.system(cmd)
  if (result == 0):
    print "OK ", file1, "equals", file2
  else:
    print "FAIL ", file1, "does not equal", file2

for f in os.listdir("."):
  if f.endswith(".dat"):
    os.remove(f)

for f in os.listdir("configs"):
  if f.endswith(".cfg"):
    name = os.path.splitext(f)[0]
    cfg = os.path.join("configs",f)
    dat = name + ".dat"
    cmd = "python cfd.py " + cfg + " " + dat + " quiet"
    os.system(cmd)
    file_exists(dat)
    expected = os.path.join("expected", dat)
    files_equal(dat,expected)

print "Test none"
os.system("python cfd.py configs/none.cfg none.dat")
file_not_exists("none.dat")

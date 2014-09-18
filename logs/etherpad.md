Setup
=====

https://github.com/swcarpentry/bc/wiki/Configuration-Problems-and-Solutions

Editors
======= 

vi
--
 
To start,

$ vi file.txt

When vi starts it is in Command mode.  
To enter Write mode from Command mode, press i.

In Write mode:

 * Type and delete text.
 * To move the cursor, use the arrow keys.
 * To switch to Command mode, press Esc.

In Command mode:

 * To delete a character, press x.
 * To delete a line, press dd.
 * To move the cursor, use the arrow keys.
 * To switch to Write mode, press i.
 * To switch to Command prompt mode, press :.

In Command prompt mode:

 * To save the file, type w.
 * To quit, type q.
 * To save the file and quit, type wq.

nano
----

To start,

    $ nano file.txt

To move the cursor,

 * Left, CTRL-B
 * Right, CTRL-F
 * Up a line, CTRL-P
 * Down a line, CTRL-N
 * To the start of the line, CTRL-A
 * To the end of the line, CTRL-E

To delete and undelete a line,

 * Delete the current line, CTRL-K
 * Undelete the recently deleted lines, CTRL-U

To save a file, CTRL-O. You will be given the opportunity to edit the file name to save the file under a different name.
To quit, CTRL-X. If the file has unsaved changes you'll be given the chance to save them now.

emacs
-----

To start,

    $ emacs file.txt

Emacs typically opens up a new window. To start, and continue to use the current shell:

    $ emacs file.txt &

To prevent Emacs opening a new window (-nw – no window):

    $ emacs -nw file.txt

To move the cursor,

 * Left, CTRL-B
 * Right, CTRL-F
 * Up a line, CTRL-P
 * Down a line, CTRL-N
 * To the start of the line, CTRL-A
 * To the end of the line, CTRL-E

To delete and undelete a line,

 * Delete the current line, CTRL-K
 * Undelete the recently deleted lines, CTRL-Y

To save a file, CTRL-X,CTRL-S.

To quit, CTRL-X, CTRL-C. If the file has unsaved changes you'll be given the chance to save them now.I
 
Prompts and exits
----------------

http://hpcarcher.github.io/2014-09-16-imperial/novice/ref/05-prompts-exits.html
 
Shell
=====

http://xkcd.com/1168/

Is it worth the time: http://www.xkcd.org/1205/

Git and version control
=======================

Try to avoid this: http://www.xkcd.org/1296/

Useful Git resources:

* http://git-scm.com
* http://ftp.newartisans.com/pub/git.from.bottom.up.pdf
* http://gitready.com

Python and Good Programming Practice
====================================

Asserts are used for "defensive" programming.They assume that mistakes will happen, that a developer might put invalid arguments into a function, so if they do asserts just terminate program execution at this point. 

Assertions can check that:

* the preconditions of a function are true in order for it to work correctly
* the postconditions are true, that the function has worked correctly,
* that invariants are true, conditions that must always be true are indeed true

A user should never see an assertion-related error as they should not fail because a developer should be testing for such failures and if they do error-handling code should catch it!

    $ ipython --pylab

The numpy library is called "numpy". "np" is an alias for "numpy" that is used by convention.

Ways of creating arrays:

    np.array()
    np.zeros()
    np.ones()
    np.identity()

Timing our own dot product implementation with lists versus Numpy's dot product function with arrays:

First create large arrays:

    m = np.random.random(1000000)
    n = np.random.random(1000000)

Then replicate these as lists

    mlist = m.tolist()
    nlist = n.tolist()

Analysing patient data:

    patients = np.loadtxt('patients.csv', delimiter=',')

Visualising the entire trial:

    pyplot.imshow(patients)

Plotting average infection over time:

    avg_infection = np.mean(patients, 0)
    pyplot.figure()
    pyplot.plot(avg_infection)

Excellent Python Scientific Programming resources:

* https://github.com/jrjohansson/scientific-python-lectures/blob/master/README.md
* http://scipy-lectures.github.io/intro/index.html

Automation and Make Exercises
=============================

Exercise 1 - add a rule 
-----------------------

Add in a rule for `methane.pdb.data`, based on the rules for
`cubane.pdb.data` and `ethane.pdb.dat`.

Be sure to use a single tab when indenting the actions, not spaces!

`touch` all the *.pdb files.

Re-run `make` and all the `.pdb.data` files should be rebuilt.

Exercise 2 - simplify a rule 
----------------------------

Simplify the `awk` rule using automatic variables:

* `$@` is the target of the current rule.
* `$^` is the dependencies of the current rule.

Using `$@` and `$^` in the right places would seem to work.

Try this, re-run `make` and observe the results.

Exercise 3 - gzip the files
---------------------------

Add a rule to package up and compress each `.pdb.data` file into 
its own `gz` file (e.g. cubane.`pdb.data.gz`).

The syntax of `gz` is:

    gzip -c <file to gzip> <gzipped file>

Change the `PDBAnalysis.tar.gz` rule to package up the `gz` files.

Try running it without creating the `gz` files manually first.

You'll need to remove a `*.pdb.data.gz` file

    rm \*.pdb.data.gz

Create the gzip files manually, by running make each time, 
then re-run `make` to make `PDBAnalysis.tar.gz`.

Exercise 4 - create a macro
---------------------------

Add a new macro to make the name of the file `PDBAnalysis.tar.gz`
configurable.

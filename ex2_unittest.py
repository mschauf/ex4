"""
Author -- Michael Widrich
Contact -- widrich@ml.jku.at
Date -- 01.10.2020

###############################################################################

The following copyright statement applies to all code within this file.

Copyright statement:
This  material,  no  matter  whether  in  printed  or  electronic  form,
may  be  used  for personal  and non-commercial educational use only.
Any reproduction of this manuscript, no matter whether as a whole or in parts,
no matter whether in printed or in electronic form, requires explicit prior
acceptance of the authors.

###############################################################################
"""

import sys
import subprocess

ex_file = 'ex2.py'
points = 2.5
python = sys.executable
feedback = ''

with subprocess.Popen([f'{python}', ex_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
    try:
        outs, errs = proc.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
    outs = outs.decode("utf-8").replace('\r', '')
    errs = errs.decode("utf-8").replace('\r', '')

if not outs == "4\nI also completed exercise 2!\n":
    points = 0

if len(errs):
    points = 0

print(f"Unittest for: {ex_file}")
print(f"Error messages:\n---\n{errs}\n---\n")
print(f"Output was:\n---\n{outs}\n---\n")
print(f"Estimated points upon submission: {points}")
print(f"This is only an estimate, see Instructions for submitting homework in moodle for common mistakes "
      f"that can still lead to 0 points.")

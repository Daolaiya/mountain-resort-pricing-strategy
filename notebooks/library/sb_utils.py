import os
import pickle

import pandas as pd

# This utility was created because students were getting confused when they ran
# their notebooks twice, the previous write-to-file code would do nothing and say
# nothing. The students thought the file was over-written when in fact, it was not -
# generating hidden bugs in subsequent notebooks.


def save_file(data, fname, dname, overwrite=False):
    """
    Save a datafile (data) to a specific location (dname) and filename (fname).
    Currently valid formats are limited to CSV or PKL.

    Parameters
    ----------
    overwrite : bool
        If True, replace an existing file without prompting.
        If False, prompt interactively when the file already exists.
    """
    if not os.path.exists(dname):
        os.mkdir(dname)
        print(f'Directory {dname} was created.')

    fpath = os.path.join(dname, fname)

    if os.path.exists(fpath):
        if overwrite:
            print(f'Overwriting file. "{fpath}"')
            _save_file(data, fpath)
            return

        print("A file already exists with this name.\n")

        yesno = None
        while yesno != "Y" and yesno != "N":
            response = input('Do you want to overwrite? (Y/N)').strip()
            yesno = response[0].capitalize() if response else ''
            if yesno == "Y":
                print(f'Writing file. "{fpath}"')
                _save_file(data, fpath)
                break
            elif yesno == "N":
                print('\nPlease re-run this cell with a new filename.')
                break
            else:
                print('\nUnknown input, please enter "Y" or "N".')
    else:
        print(f'Writing file.  "{fpath}"')
        _save_file(data, fpath)


def _save_file(data, fpath):
    valid_ftypes = ['.csv', '.pkl']

    assert (fpath[-4:] in valid_ftypes), "Invalid file type.  Use '.csv' or '.pkl'"

    if fpath.endswith('.csv'):
        data.to_csv(fpath, index=False)
    elif fpath.endswith('.pkl'):
        with open(fpath, 'wb') as f:
            pickle.dump(data, f)

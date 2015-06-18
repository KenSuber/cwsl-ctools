""" Class to read in the COD file date strings. """

import datetime as dt

import numpy as np


class CodFile(object):
    
    def __init__(self, filename):
        
        self.filename = filename
        self._raw_data = None

    def __repr__(self):
        return "<CodFile; filename = {}>".format(self.filename)

    @property
    def base_dates(self):
        if self._raw_data is None:
            self.read_data()

        return [self.convert_date(datestring)
                for datestring in self._raw_data[0]]

    @property
    def projected_dates(self):
        if self._raw_data is None:
            self.read_data()

        return [self.convert_date(datestring)
                for datestring in self._raw_data[1]]

    def read_data(self):
        """ Read in the raw data from the COD file."""

        with open(self.filename, "r") as open_codfile:
            # Throw away the first line.
            open_codfile.readline()
            
            raw_vals = [tuple(line.split())
                        for line in open_codfile]

        self._raw_data = np.array(zip(*raw_vals))

    def convert_date(self, datestring):
        """ Convert the string date to a python date object. """
        
        date_part = int(datestring[-2:])
        month_part = int(datestring[-4:-2])
        year_part = int(datestring[:-4]) + 1900

        return(dt.date(year_part, month_part, date_part))

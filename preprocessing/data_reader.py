# data_reading/data_reader.py
from Readers.i2gResRead import ReadI2GRes
from FileLogging.simple_logger import SimpleLogger
import pandas as pd

class DataReader:
    def __init__(self, logger = None):
        self.logger = logger
        
    def _log(self, message):
        if self.logger:
            self.logger.write_log(message)
        else:
            pass

    def read_res_file(self, filepath, columns):
        try:
            self.logger.write_log(f"Reading file: {filepath}")
            df = ReadI2GRes(filepath).get_fix_s_data()
            df = df[['epoch', 'sys', 'num', *columns]]
            self.logger.write_log(f"Successfully read and filtered data from {filepath}")
            return df
        except Exception as e:
            self.logger.write_log(f"Error reading file {filepath}: {e}")
            raise

import os
import pandas as pd
class Data_searcher:
    def __init__(self, path):
        self.path = path

    def search(self):
        first_file = os.listdir(self.path)[0]
        if first_file != None:
            # a logger that file has been found
            return first_file
        else:
            # a logger should be added here that
            pass

    def move_file(self, file, destination):
        """
        Move new found data to folder that has been looked at 
        """
        source = self.path
        src_path = os.path.join(source, file)
        dst_path = os.path.join(destination, file)
        os.rename(src_path, dst_path)
    
import logging
class Log:
    def __init__(self, directory, file_name) -> None:
        logging.basicConfig(filename=f"{directory}/{file_name}.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    def write_to_logger(self, text):
        self.logger.info(text)
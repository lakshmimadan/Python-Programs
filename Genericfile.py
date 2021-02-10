import glob
import logging
import yaml
#glob module used to retrive the files/pathnames matching a specified pattern

logging.basicConfig(filename='genericfilelog.log', level=logging.INFO,
       format='%(asctime)s:%(levelname)s:%(message)s')

class Numberoffiles():
    def __init__(self):
        self.destination=""

    def load_config_file(self):
            with open(r'genericfileconfig') as file:
                # scalar values to Python the dictionary format
                config_list = yaml.load(file, Loader=yaml.FullLoader)
                self.destination=config_list['destination']

    def multiplefiles(self):
        try:
            sourcefile = glob.glob('*.txt')
            logging.info("retrieve all the files")
            try:
                with open('E:\\Users\\Lakshmi\\PycharmProjects\\pythonproject1\\{}'.format(self.destination), 'w') as destfile:
                    logging.info("destination file is opened")
                    try:
                        for fname in sourcefile:
                            with open(fname, 'r') as readfile:
                                logging.info("source files are opened")
                                try:
                                    infile = readfile.read()
                                    for line in infile:
                                        destfile.write(line)
                                    destfile.write("\n")
                                    logging.info("all the files copied to the destination")

                                except Exception as e:
                                    logging.error("something went wrong while iterating the file")
                    except Exception as e:
                        logging.error("something went wrong in reading a file {}".format(fname))
                    finally:
                        fname.close()
                        logging.info("all the files are successfully clsoed")

            except Exception as e:
                logging.error("something went wrong while opening a destination file")
        except Exception as e:
            logging.error("something went wrong in retrieving a file")


nofiles_obj=Numberoffiles()
nofiles_obj.load_config_file()
nofiles_obj.multiplefiles()
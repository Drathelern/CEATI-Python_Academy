#Import Modules
import os
import pathlib
import configparser

#Set APP Path
APP_PATH  = pathlib.Path(__file__).parents[1].absolute()


#Define the several functions.

def err_handling_decorator(func):
    '''
    This decorator is to set error handling to all the methods in which it is required and to indicate which was the specific error.
    '''
    def error_handling(*args):
        try:
            return func(*args)
        except Exception as e:
            error        = e.args[0]
            func_name    = func.__name__
            print('''\n\nError:
                The {} function had the following error: {}'''.format(func_name, error))
            exit()

    return error_handling

@err_handling_decorator
def get_config_file_data(config_file):
    '''
    This function read config files and returns the file data\n
    Arguments:
        config_file: name of the configuration file to read the content.
    ''' 
    #Set Config File path and read the file
    config_path = os.path.join(APP_PATH, "config", config_file)
    config_data  = configparser.ConfigParser()
    config_data.read(config_path)

    #Convert object to Dictionary
    config_dict = {}
    for stanza in config_data.sections():
        config_dict[stanza] = dict(config_data.items(stanza))
    
    return config_dict

@err_handling_decorator
def write_config_file(config_file, stanza, object_data):
    '''
    This function write data to config files\n
    Arguments:
        config_file: name of the configuration file to write the new data.
        stanza: stanza where the attribute will be stored
        object_data: object with the data to be stored
            Example:
                {
                    "url": "https://api.test.com/",
                    "endpoint": "/v1/test/api"
                }
    '''
    #Set Config File path and read the current file
    config_path     = os.path.join(APP_PATH, config_file)

    #Validate if not existe and create Config Path.
    if not os.path.isdir(config_path):
        os.makedirs(config_path)

    #Read current Config File and save it on Config Parser obj
    config          = get_config_file_data(config_path)
    config[stanza]  = object_data

    #Write the new config on the config file
    with open(config_file, 'w') as configfile:
        config.write(configfile)



    
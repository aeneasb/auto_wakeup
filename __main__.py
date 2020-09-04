import time
import json
from sys import exit
import argparse
from Move import Move

#Main program
def main():
    '''
    The main function for controlling the electro motor
    '''
    def load(configFile):
        with open(configFile,'r') as fp:
            return json.loads(fp.read()) 
    parser = argparse.ArgumentParser()
    parser.add_argument("--configFile", help="Specify the path of the configFile")
    parser.add_argument("--mode", help="Possible modes of wakeup: chill, normal, rush.")
    args = parser.parse_args()
    configFile = load(args.configFile)
    try:
        move = Move(configFile, args.mode)
    except Exception as anError:
        print('Unexpected error at start up')
        raise anError
        exit(0)
    try:
        try:
            move.trigger()
        except Exception as anError:
            print ('Error during move' + str (anError))
            raise anError
    finally:
        move.cleanup()
if __name__ == '__main__':
    main()

'''
Script to find prime factors of an integer value

by

Vitek Urbanec, 2019
'''

import sys
import time
import json
import argparse

PARSER = argparse.ArgumentParser(
    usage="Enter the integer number to find prime factors \
and archive JSON file to store performed computations, -h for help"
    )
PARSER.add_argument('-n',
                    type=str,
                    help="integer number",
                    required=True,
                    dest="number"
                    )
PARSER.add_argument('-a',
                    type=str,
                    help="archive JSON file",
                    default="archive.json",
                    dest="archive_file"
                    )

ARGUMENTS = PARSER.parse_args()

ARCHIVE_FILE = ARGUMENTS.archive_file

try:
    NUMBER = int(ARGUMENTS.number)
except ValueError:
    print('Error: not a valid integer')
    sys.exit(1)

def init_archive():
    '''Initialise the archive file in case it's missing or corrupted'''
    with open(ARCHIVE_FILE, 'w') as archive_file:
        pass

def load_archive():
    '''function to load the archive file to memory as a dictionary'''
    with open(ARCHIVE_FILE, 'r') as archive_file:
        try:
            archive_dict = json.load(archive_file)
        except json.JSONDecodeError:
            print('Error: archive JSON cannot be decoded')
            sys.exit(1)
    return archive_dict

def get_prime_factors(number):
    '''function to find prime factors of an integer'''
    start_time = time.time()
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return number, factors, time.time() - start_time

def record_result(number, factors, record_dict):
    '''record the result into the archive.json file'''
    record_dict[number] = factors
    with open(ARCHIVE_FILE, 'w') as archive_file:
        json.dump(record_dict, archive_file)


if __name__ == "__main__":

    try:
        RECORD_DICT = load_archive()
    except FileNotFoundError:
    # except:
        init_archive()
        RECORD_DICT = {}
    if str(NUMBER) in RECORD_DICT.keys():
        PRIME_FACTORS = RECORD_DICT[str(NUMBER)]
        COMPUTE_TIME = 0
    else:
        _, PRIME_FACTORS, COMPUTE_TIME = get_prime_factors(NUMBER)
        record_result(NUMBER, PRIME_FACTORS, RECORD_DICT)


    print("prime factors of %d are %s - found in: %f sec" %
          (
              NUMBER,
              ', '.join(str(x) for x in PRIME_FACTORS),
              COMPUTE_TIME
          )
          )

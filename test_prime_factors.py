import subprocess
import json
import os
import pytest

from prime_factors import validate_number, get_prime_factors

def test_validate_number():
    with pytest.raises(Exception, match="not a valid integer"):
        validate_number('perkele')
    with pytest.raises(Exception, match="not a natural number"):
        validate_number(-666)

def test_get_prime_factors():

    def check_multiply(list_integers):
        output = 1
        for item in list_integers:
            output *= item
        return output

    tested_numbers = [
        166335,
        688996,
        17,
        58653,
        49966633
    ]
    for item in tested_numbers:
        _, prime_factors, _ = get_prime_factors(item)
        assert item == check_multiply(prime_factors)

def test_prime_factors_output():
    child = subprocess.Popen(['python3', 'prime_factors.py','-n','13195','-t', '-a', 'test_archive.json'], stdout=subprocess.PIPE)
    out, err = child.communicate()
    exitcode = child.returncode
    out_dict = json.loads(out.strip())
    assert exitcode == 0
    assert out_dict['13195'] == [5, 7, 13, 29]

def test_archive_retrieve():
    child = subprocess.Popen(['python3', 'prime_factors.py','-n','13195','-t', '-a', 'test_archive.json'], stdout=subprocess.PIPE)
    out, err = child.communicate()
    exitcode = child.returncode
    out_dict = json.loads(out.strip())
    assert exitcode == 0
    assert out_dict['compute_time'] == 0
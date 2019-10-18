import subprocess
import json
import os

from prime_factors import get_prime_factors



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
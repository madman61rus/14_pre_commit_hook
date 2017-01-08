import argparse
import subprocess

def run_tests(file_with_tests):
    command = '/usr/bin/python {}'.format(file_with_tests)
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               shell=True)
    process.wait()
    return process.returncode


if __name__ == '__main__' :

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tests", required=True, help="path to a file with tests")
    parser.add_argument("-f", "--file", help="path to a testing file")
    args = parser.parse_args()

    if run_tests(args.tests) == 0 :
        print('Тесты прошли удачно')
    else:
        print('Тесты выявили ошибку')

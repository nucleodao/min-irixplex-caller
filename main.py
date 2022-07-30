#!/usr/bin/env python3.10

'''
main.py: script to call irixplex binary on demand
'''

import argparse
import subprocess
import sys

# parse arguments
def parse_args():
    parser = argparse.ArgumentParser(description='irixplex arguments')
    parser.add_argument("-u", '--url', action='store')
    return parser.parse_args()

def check_docker_installation():
  docker_installed = subprocess.check_output('docker -v', shell=True).decode("utf-8").strip().startswith('Docker')
  if docker_installed == False:
    print('Sorry our demo requires docker installed. (docker is just required for demo purpose)')
    answer = str(input('Do you want us to install docker on your system? (Y/N)')).lower()
    if answer == 'y' or answer == "yes":
      print('we are installing docker for you ...')
      print(subprocess.check_output('pip install docker', shell=True).decode("utf-8").strip())
      print('docker installed. proceeding ...')
    else:
      print('aborted, bye')
      sys.exit(0)
    
def main():  
  check_docker_installation()

  args = parse_args()
  url = args.url
  if url is None:
    url = 'https://drive.google.com/file/d/1lNDKC7nNfXVW-To4PibKh08GFp8jzrrE/view?usp=sharing' # this is our test genome file
      
  cmd = 'docker run ilovelili/min-irisplex-binary:latest analyze --url={}'.format(url)
  answer = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()

  print('analyze result:', answer)

if __name__ == '__main__':
    main()

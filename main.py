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

def check_docker_installation() -> bool:
  return subprocess.check_output('docker -v', shell=True).decode("utf-8").strip().startswith('Docker')

def main():  
  if check_docker_installation() == False:
    print('sorry our demo requires docker installed. (docker is just required for demo purpose)')
    sys.exit(1)

  args = parse_args()
  url = args.url
  if url is None:
    url = 'https://drive.google.com/file/d/1lNDKC7nNfXVW-To4PibKh08GFp8jzrrE/view?usp=sharing' # this is our test genome file
      
  cmd = 'docker run ilovelili/min-irisplex-binary:latest analyze --url={}'.format(url)
  answer = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()

  print('analyze result:', answer)
  
if __name__ == '__main__':
    main()

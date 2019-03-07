import os
import playsound
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='the audio parser')
    parser.add_argument('uid', type=str,
                        help='A required integer positional argument')
    args = parser.parse_args()
    playsound.playsound(os.path.join(os.getcwd(), 'majortempaud', args.uid + '.wav'),True)

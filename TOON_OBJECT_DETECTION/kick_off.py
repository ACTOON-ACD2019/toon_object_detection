"""
This Project is SBD(Speech Bubble Detection) based paper(Faster RCNN).
Future Science Technology Internship
Ajou Univ.
Writer: Han Kim
"""

import argparse
#import train
import test
import config

'''PROJECT KICK OFF'''

parser = argparse.ArgumentParser(description='Speech Bubble Localization(Detection)')

#parser.add_argument('--train', default=False, type=bool, help='train flag')
parser.add_argument('--test', default=False, type=bool, help='test flag')
parser.add_argument('--txt', default=True, type=bool, help='visualization txt')
parser.add_argument('--bub', default=True, type=bool, help='visualization bub')
parser.add_argument('--cut', default=True, type=bool, help='visualization cut')
parser.add_argument('--bg', default='white', type=str, help='bg')
args = parser.parse_args()

config.DRAWBUB = args.bub
config.DRAWTXT = args.txt
config.DRAWCUT = args.cut
config.BACKGROUND = args.bg

'''This is training part'''
#if args.train: train.train()

'''This is testing part'''
if args.test: test.test()

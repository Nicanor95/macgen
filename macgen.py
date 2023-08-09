### Generador de MAC Adress ###
### Author: Vrs-            ###

import argparse
import random

tplink = (('F4', 'F2', '6D'), ('30', 'B4', '9E'), ('00', '25', '86'), ('10', 'FE', 'ED'), ('18', 'A6', 'F7'), ('18', 'D6', 'C7'), ('34', 'E8', '94'), ('44', 'B3', '2D'))
cisco = (('00', '08', '20'), ('F8', '6B', 'D9'), ('F8', '7B', '20'), ('F8', '0F', '6F'), ('F0', '9E', '63'), ('FC', 'FB', 'FB'), ('F4', 'BD', '9E'), ('F8', 'B7', 'E2'))
linksys = ('00', '23', '69')
kozumi = ('00', '26', 'CE')

valid_chars='ABCDEF1234567890'

parser = argparse.ArgumentParser()
parser.add_argument('--all', default=False, action='store_true', help='Generates MAC Adress for all of the known manufacturers OUIs')
parser.add_argument('--hyphen', default=False, action='store_true', help='Use hyphens as separators instead of colons.')
parser.add_argument('-cs', '--cisco', action='store_true', help='Generates cisco MAC Adress.')
parser.add_argument('-tp', '--tplink', action='store_true', help='Generates TP-Link MAC Adress.')
parser.add_argument('-ls', '--linksys', action='store_true', help='Generates Linksys MAC Adress.')
parser.add_argument('-kz', '--kozumi', action='store_true', help='Generates Kozumi MAC Adress.')
parser.add_argument('-a', '--amount', type=int, default=1, help='Amount of MACs to generate per manufacturer.')
args = parser.parse_args()

separator = '-' if args.hyphen else ':'

def gentail(sep):
    def genoctet():
        return random.choice(valid_chars) + random.choice(valid_chars)
    return sep + genoctet() + sep + genoctet() + sep + genoctet()

if args.amount >= 1:
    if args.cisco or args.all:
        print('CISCO:')
        for _ in range(args.amount):
            print(separator.join(random.choice(cisco)) + gentail(separator))
    if args.tplink or args.all:
        print('TP-LINK:')
        for _ in range(args.amount):
            print(separator.join(random.choice(tplink)) + gentail(separator))
    if args.linksys or args.all:
        print('LINKSYS:')
        for _ in range(args.amount):
            print(separator.join(linksys) + gentail(separator))
    if args.kozumi or args.all:
        print('KOZUMI:')
        for _ in range(args.amount):
            print(separator.join(kozumi) + gentail(separator))
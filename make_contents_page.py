# -*- coding: utf-8 -*-
"""
Make index page of all md files
"""

import glob


def make_link(filename):
    if filename!='README.md':
        return '['+filename.split('.')[0]+']('+filename.split('.')[0]+')'
    else:
        return '[README](/choice-engine-text/)'


def pad(item):
    return '\n'+item+'\n'

filenames=sorted(glob.glob('*.md'))



with open('contents.md', 'w') as outfile:
    outfile.write('# Contents\n\n')
    for filename in filenames:
        outfile.write(pad(make_link(filename)))
        

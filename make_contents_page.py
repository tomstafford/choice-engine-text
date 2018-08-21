# -*- coding: utf-8 -*-
"""
Make index page of all md files
"""

import glob


def make_link(filename):
    return '<a href="'+filename.split('.')[0]+'">'+filename.split('.')[0]+'</a>'

def pad(item):
    return '<br>\n'+item+'\n<br>\n'

filenames=sorted(glob.glob('*.md'))



with open('contents.html', 'w') as outfile:

    for filename in filenames:
        outfile.write(pad(make_link(filename)))
        

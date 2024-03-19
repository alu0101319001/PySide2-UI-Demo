# -*- coding: utf-8 -*-
#!/usr/bin/python
import os

def check_icons_folder():
    icons_folder = os.path.join(os.path.dirname(__file__),'icons_tfg')
    if os.path.exists(icons_folder):
        # print('The icons folder exists in {}.'.format(icons_folder))
        return icons_folder
    else:
        print('The icons folder does not exist.')
        return None
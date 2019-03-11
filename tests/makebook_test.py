#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Bookmaker test for the collection of notebooks in this directory
'''

from context import jupyterbookmaker as jbm

if __name__ == '__main__':

# Add contents, book info, and navigation bars
    jbm.make_book(toc_nb_name = '00.00-Front_Page.ipynb',
                  header = 'Test 3 for the jupyterbookmaker module',
                  core_navigators=['00.00-Front_Page.ipynb', 
                    'BA.00-References.ipynb'],                  
                  directory='notebooks',
                  show_full_entry=True)

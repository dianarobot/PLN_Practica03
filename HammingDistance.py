#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Diana Rocha Botello
"""

class HammingDistance():

	def __init__(self):
		pass

	def hamdistance(self, str1, str2):
        diffs = 0
        if len(str1) == len(str2):
        	for ch1, ch2 in zip(str1, str2):
                if ch1 != ch2:
                    diffs += 1
        else:
        	diffs = -1
        return diffs
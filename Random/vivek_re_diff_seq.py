#!/usr/bin/python

import re

SYN_SEQ = '4444'
result = 'Connection seen is Syn#:4444'
syn_dif_seq = re.findall('(?<=Syn#:)(\d+)', str(result))
print syn_dif_seq
#if SYN_SEQ == syn_dif_seq:
#	print "Match found"
#else:
#	print "No match found"

assert (SYN_SEQ not in syn_dif_seq[-1]), \
            "Connection does not have different sequence"

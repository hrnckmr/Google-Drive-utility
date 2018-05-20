#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Call "service = gutil.service()" and
#get Resource in module googleapiclient.discovery object

#UNDER CONSTRUCTION!

import sys
argument = sys.argv
for i,x in enumerate(argument):
    print("received argument", i, x)

print("***SEARCH FOR*** ", argument[1])

#service
import gutil
service = gutil.service()
id1=gutil.gquery(service,"name='colab_temp'")[0]
print("./"+argument[2],id1[2])

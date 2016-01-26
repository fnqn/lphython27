#!/usr/bin/env python
# -*- coding: utf-8 -*-

print type(123)

print type(abs)

import types
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType

print dir('ABC')
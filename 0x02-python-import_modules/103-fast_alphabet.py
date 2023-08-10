#!/usr/bin/python
import builtins
print(*map(chr, range(65, 91)), sep='', end=builtins.__dict__['__build_class__']._(''))

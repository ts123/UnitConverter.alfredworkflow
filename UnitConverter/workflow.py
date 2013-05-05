#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import subprocess

import alfred

def main(query):
    args = query.split()
    try:
        args[0] = str(eval(args[0]))
    except NameError:
        pass
    from_unit = ' '.join(args[:2])
    to_units = args[1:]

    suggested_items = []
    uid = uid_generator()
    for to_unit in to_units:
        stdout_ = subprocess.Popen(['units', from_unit, to_unit], stdout=subprocess.PIPE).communicate()[0]
        result = '{0} {1}'.format((stdout_.splitlines()[0]).split()[1], to_unit)
        suggested_items.append(alfred.Item(
            attributes = { 'uid': uid.next(), 'arg': result }, 
            title = result, 
            subtitle = 'Copy to Clipboard', 
            icon = 'icon.png'))
    alfred.write(alfred.xml(suggested_items))

def uid_generator():
    import time
    uid = time.time()
    while True:
        uid += 1
        yield uid

if __name__ == '__main__':
    import sys
    main(' '.join(sys.argv[1:]))


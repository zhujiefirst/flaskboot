#!/usr/bin/env python
# -*- coding: utf-8 -*
'''
主入口
'''

from sample import create_app

app = create_app()

if __name__ == '__main__':
    app.run()

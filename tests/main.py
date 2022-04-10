#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy <wxnacy@gmail.com>
# Description:


from multitasker import (
    FileSystemTasker,
    SubTaskModel
        )


if __name__ == "__main__":
    import time
    import os
    tasker = FileSystemTasker(action = 'copy',
        from_file = os.path.expanduser('~/Downloads/dltest'),
        to_file = '/tmp/test'
    )
    tasker.build()
    b = time.time()
    tasker.run()
    print(time.time() - b)



#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy <wxnacy@gmail.com>
# Description: multitasker 单元测试

import os
import json
from typing import List
from pydantic import BaseModel

from multitasker import MultiTasker, SubTaskModel

class DownloadTask(BaseModel):
    download_url: str
    download_path: str

def find_sub_tasks(task_id):
    dirname = f'/Users/wxnacy/.lfsdb/data/download/sub_task-{task_id}'
    items = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        with open(path) as f:
            data = json.loads(''.join(f.readlines()))
            items.append(data)
    return items

class M3u8Tasker(MultiTasker):

    class Config:
        task_type = 'm3u8'

    def build_task(self) -> dict:

        return {}

    def build_sub_tasks(self) -> List[SubTaskModel]:
        sub_tasks = find_sub_tasks('20097')
        res = []
        for detail in sub_tasks[:10]:
            print(detail)
            res.append(SubTaskModel(task_type = 'download_ts', detail = detail))
        return res

tasker = M3u8Tasker()

@tasker.trigger_sub_task('download_ts')
def sub_task_download_ts(sub_task) -> bool:
    pass


if __name__ == "__main__":
    tasker.build().run()

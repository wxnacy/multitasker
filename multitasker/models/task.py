#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy <wxnacy@gmail.com>
# Description: task model

import json

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DATETIME, Enum, TEXT

from multitasker.models.base import Base, BaseDB
from multitasker.models.enums import TaskStatusEnum

class BaseTaskModel(object):

    id = Column(String(32), primary_key=True)
    task_type = Column(String(64))
    status = Column(String(16), default=TaskStatusEnum.INIT.value)
    progress = Column(Float(), default=0)
    is_delete = Column(Integer(), default=0)
    detail = Column(TEXT(), default='{}')
    create_time = Column(DATETIME(), default=datetime.now)
    update_time = Column(DATETIME(), default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_detail(self.detail)

    def get_detail(self):
        return json.loads(self.detail)

    def set_detail(self, detail):
        if isinstance(detail, dict) or isinstance(detail, list):
            detail = json.dumps(detail)
        self.detail = detail


class TaskModel(BaseTaskModel, BaseDB, Base):
    __tablename__ = 'task'


class SubTaskModel(BaseTaskModel, BaseDB, Base):
    __tablename__ = 'sub_task'

    task_id = Column(String(32), index=True)

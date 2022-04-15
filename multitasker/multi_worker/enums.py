#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xiaoning.wen(xiaoning.wen@yiducloud.cn)
# Description: 枚举模块

from wpy.base import BaseEnum


class WorkRunTypeEnum(BaseEnum):
    GEVENT = 'gevent'
    PROCESS = 'process'
    THREAD = 'thread'

    @classmethod
    def default(cls):
        """
        """
        return cls.GEVENT



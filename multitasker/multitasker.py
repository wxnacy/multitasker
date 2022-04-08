#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy <wxnacy@gmail.com>
# Description: 


import abc

from multitasker.models.task import TaskModel, SubTaskModel


class MultiTasker(metaclass=abc.ABCMeta):

    class Config:
        task_type: str

    @abc.abstractmethod
    def build_task_detail(self) -> dict:
        """
        构建任务
        """
        pass

    @abc.abstractmethod
    def build_sub_tasks(self) -> list[SubTaskModel]:
        """
        构建任务
        """
        pass


    def build(self):

        task_detail = self.build_task_detail()
        task = TaskModel(detail = task_detail)
        task.save()

        for sub_task in self.build_sub_tasks():
            sub_task.task_id = task.id
            sub_task.save()

    def run(self):
        pass



from typing import List
from multitasker.base import MultiTasker
from multitasker.models.task import SubTaskModel


class TestTasker(MultiTasker):

    class Config:
        task_type: str = 'test'


    def build_task(self) -> dict:
        return {}

    def build_sub_tasks(self) -> List[SubTaskModel]:

        items = []
        for i in range(10):
            items.append(SubTaskModel(task_type = 'test'))
        return items



def test_get_subtasks():
    print('test get subtasks')
    tasker = TestTasker()
    tasker.build()

    subtasks = tasker.get_subtasks()
    assert len(subtasks) == 10

def setup_module():
    print('\nsetup_module 执行')

def teardown_module():
    print('\nteardown_module 执行')

def setup_function():
    """函数方法（类外）初始化"""
    print('setup_function 执行')

def teardown_function():
    """函数方法（类外）初始化"""
    print('\nteardown_function 执行')

def test_in_class():
    """类（套件）外的测试用例"""
    print('类外测试用例')


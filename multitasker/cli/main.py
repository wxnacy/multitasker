#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy <wxnacy@gmail.com>
# Description:

#  from multitasker.models import task
from multitasker.models.base import Base, engine
from multitasker.filesystem import FileSystemTasker

import typer

app = typer.Typer()

@app.command()
def init():
    """
    初始化数据库等信息
    """
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

@app.command()
def copy(from_path: str, to_path: str):
    """复制文件"""
    tasker = FileSystemTasker(action = 'copy',
        from_file = from_path,
        to_file = to_path
    )
    tasker.build()
    tasker.run()


if __name__ == "__main__":
    app()

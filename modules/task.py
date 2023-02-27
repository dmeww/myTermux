# 条件关系映射
from modules.task_map import conditions


class Task(object):

    def __init__(self, condition) -> None:
        self.check = conditions[condition]['check']
        self.task = conditions[condition]['action']


    def doTask(self):
        self.task()

    def doCheck(self):
        self.check()

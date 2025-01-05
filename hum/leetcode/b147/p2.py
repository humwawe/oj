import heapq
from typing import List


class TaskManager:

  def __init__(self, tasks: List[List[int]]):
    self.tasks = dict()
    self.all_tasks_pri = []
    for u, t, p in tasks:
      self.add(u, t, p)

  def add(self, userId: int, taskId: int, priority: int) -> None:
    self.tasks[taskId] = [userId, priority]
    heapq.heappush(self.all_tasks_pri, (-priority, -taskId))

  def edit(self, taskId: int, newPriority: int) -> None:
    if newPriority > self.tasks[taskId][1]:
      heapq.heappush(self.all_tasks_pri, (-newPriority, -taskId))
    self.tasks[taskId][1] = newPriority

  def rmv(self, taskId: int) -> None:
    self.tasks.pop(taskId)

  def execTop(self) -> int:
    while True:
      if len(self.all_tasks_pri) == 0:
        return -1
      priority, taskId = heapq.heappop(self.all_tasks_pri)
      priority = -priority
      taskId = -taskId
      if taskId in self.tasks:
        u, p = self.tasks.pop(taskId)
        if priority == p:
          return u
        else:
          self.tasks[taskId] = [u, p]
          heapq.heappush(self.all_tasks_pri, (-p, -taskId))


s = TaskManager([[0, 14, 1]])
print(s.execTop())

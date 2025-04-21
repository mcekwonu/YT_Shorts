#
# www.youtube.com/@mersthub_mentors
#

class TodoList:
    def __init__(self, tasks=[]):
        self.tasks = tasks

    def add_task(self, task):
        self.tasks.append(task)


sun = TodoList()
mon = TodoList()
sun.add_task("Work on Python exercise")

print(sun.tasks)
print(mon.tasks)


initial_tasks = ["Watch Python podcast", "Brush my teeth"]
tue = TodoList(initial_tasks)
wed = TodoList(initial_tasks)
tue.add_task("Work on Python exercise")

print(tue.tasks)
print(wed.tasks)


# fix
class TodoListFixed:
    def __init__(self, tasks=None):
        self.tasks = [] if tasks is None else tasks.copy()

    def add_task(self, task):
        self.tasks.append(task)


initial_tasks = ["Watch Python podcast", "Brush my teeth"]
thur = TodoListFixed(initial_tasks)
fri = TodoListFixed(initial_tasks)

thur.add_task("Work on Python exercise")

print("\nAfter fix:")
print(thur.tasks)
print(fri.tasks)


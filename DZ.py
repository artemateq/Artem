class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = False

    def mark_as_done(self):
        self.status = True


class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def remove_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]
    def mark_task_as_done(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.mark_as_done()
    def list_tasks(self):
        for task in self.tasks:
            print(f"Назва: {task.title}, Опис: {task.description}, Дедлайн: {task.deadline}, Виконано: {task.status}")



task_manager = TaskManager()

task1 = Task("Вивчити Python", "Пройти курс та зробити проєкт", "2024-11-30")
task2 = Task("Прочитати книгу", "Прочитати 'Війна і мир'", "2024-12-15")

task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.mark_task_as_done("Вивчити Python")
task_manager.list_tasks()
task_manager.remove_task("Прочитати книгу")
task_manager.list_tasks()

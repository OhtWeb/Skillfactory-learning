class TaskList:
    def __init__(self):
        self.__task_list = []

    def __is_task_in_list(self, task):
        if task in self.__task_list:
            return True
        else:
            return False
    def add_task(self, task):
        if task in self.__task_list:
            print(f'Задача "{task}" уже есть в списке')
        else:
            self.__task_list.append(task)
            print(f'Задача "{task}" добавлена в список')
    def remove_task(self, task_name):
        if task_name in self.__task_list:
            self.__task_list.remove(task_name)
            print(f'Задача "{task_name}" удалена из списка')
        else:
            print(f'Задачи "{task_name}" нет в списке')
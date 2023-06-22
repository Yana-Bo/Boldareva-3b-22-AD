class ToDoHome:
    def __init__(self, fl_name):
        file = open(fl_name, 'r')
        self.lst = [i.replace('\n', '') for i in file.readlines()]
        self.file_name = fl_name
        file.close()
    def app_elem(self, elem):
        self.lst.append(elem)
        file = open(self.file_name, 'a')
        file.write(elem + '\n')
        file.close()
    def del_elem(self, elem):
        self.lst.remove(elem)
    def print_lst(self):
        print(self.lst)
td = ToDoHome('test_f.txt')
td.print_lst()
td.app_elem('Помыть посуду')
td.print_lst()
td.app_elem('Протереть пыль')
td.print_lst()
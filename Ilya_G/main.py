import tkinter as tk
import tkinter.ttk as ttk
import os
import datetime
from idlelib.tooltip import Hovertip
import shutil

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Набор цветов
        self.mycolor_1 = '#%02x%02x%02x' % (194, 221, 229)  # Фон
        self.mycolor_2 = '#%02x%02x%02x' % (169, 176, 198)  # Панель инструментов
        self.mycolor_3 = '#%02x%02x%02x' % (253, 253, 254)  # Белый
        self.mycolor_4 = '#%02x%02x%02x' % (87, 53, 114)  # Темно фиалетовый
        self.network_path = r"C:\Cетевая папка"  # Указываем путь проекта
        self.path_project = r"C:\LearnPyton\file manager\Cетевая папка"
        self.ful_path_tree_dict = {}
        self.create_main_window()
        self.create_buttons()
        self.create_right_tree()
        self.create_left_tree()

    # Главное окно
    def create_main_window(self):
        self.title("File manager")  # меняем заголов программы
        w = self.winfo_screenwidth()  # определяем ширину монитора
        h = self.winfo_screenheight()  # определяем высоту монитора
        w = w // 2  # середина экрана
        h = h // 2
        w = w - 600  # смещение от середины, иначе в центре экрана окажется верхний левый угол окна, а не его середина
        h = h - 363
        self.geometry('1200x725+{}+{}'.format(w, h))  # пределяем геометрию и положение основного окна программы
        self.resizable(False, False)  # запретит изменение размеров основного окна

        self.configure(bg=self.mycolor_1)  # меняем фон программы
        # Меняем иконку у программы
        path_icon = os.path.abspath("icon.ico")
        self.iconbitmap(path_icon)

        # Создаем группы
        self.group_toolbar = tk.LabelFrame(self, height=80, width=1180, bg=self.mycolor_2)
        self.group_toolbar.place(x=10, y=10)

        self.group_1 = tk.LabelFrame(self, height=590, width=540, bg=self.mycolor_3)
        self.group_1.place(x=10, y=100)

        self.group_2 = tk.LabelFrame(self, height = 590, width = 540, bg=self.mycolor_3)
        self.group_2.place(x = 650, y = 100)

    # Создаем кнопки
    def create_buttons(self):
        # Создаем кнопки со стрелками впарво и влево
        self.img_right = tk.PhotoImage(file="right.png")
        self.btn_right = tk.Button(self, height=40, width=50, bg=self.mycolor_1, image=self.img_right,
                                   command=self.Add_All_files_to_tree)

        self.btn_right.place(x=575, y=220)
        self.img_right_litle = tk.PhotoImage(file="right_litle.png")
        self.btn_right_litle = tk.Button(self, height=40, width=50, bg=self.mycolor_1, image=self.img_right_litle,
                                         command=self.Add_files_to_tree)
        self.btn_right_litle.place(x=575, y=280)


        self.img_left = tk.PhotoImage(file="left.png")
        self.btn_left = tk.Button(self, height=40, width=50,bg=self.mycolor_1, image=self.img_left,
                                  command=self.del_func_all_data)
        self.btn_left.place(x = 575, y =400)
        self.img_left_litle = tk.PhotoImage(file="left litle.png")
        self.btn_left_litle = tk.Button(self, height=40, width=50, bg=self.mycolor_1, image=self.img_left_litle,
                                        command=self.del_func)
        self.btn_left_litle.place(x=575, y=460)

        # Создаем кнопку загрузки данных в Майкромайн

        self.img_Download = tk.PhotoImage(file="download.png")
        self.btn_Download = tk.Button(self.group_toolbar, height=60, width=70, bg=self.mycolor_1, image=self.img_Download,
                                      command=self.copy_files_to_project)
        self.btn_Download.place(x=1090, y=5)
        Hovertip(self.btn_Download, "Функция загрузки данных в Майкромайн.", hover_delay=300)

        # Создаем кнопку загрузки данных в Майкромайн

        self.img_download_BM = tk.PhotoImage(file="download_BM.png")
        self.btn_download_BM = tk.Button(self.group_toolbar, height=60, width=70, bg=self.mycolor_1,
                                      image=self.img_download_BM, text = "Загрузка БМ")
        self.btn_download_BM.place(x=10, y=5)
        Hovertip(self.btn_download_BM, "Функция загрузки БМ в сеть.", hover_delay=300)

    # Создаем дерево таблицу
    def create_right_tree(self):
        columns = ("#1", "#2", "#3")
        self.tree = ttk.Treeview(self.group_2, show="headings", columns=columns,height = 28)
        self.tree.place(x=0, y=0)

        style = ttk.Style()
        style.configure("Treeview", font=(None, 8)) # Изменяем размер текста в Treeview
        style.configure("Treeview.Heading", font= ('Calibri', 9,'bold'))  # Изменяем размер текста в заголовке

        self.tree.heading("#1", text="Имя")
        self.tree.column("#1", minwidth=342, width=342)

        self.tree.heading("#2", text="Дата изм.")
        self.tree.column("#2", minwidth=86, width=86)

        self.tree.heading("#3", text="Размер")
        self.tree.column("#3", minwidth=80, stretch=0, width=80, anchor="e")

        # Добовляем скроллдаун
        self.ysb = ttk.Scrollbar(self.group_2, orient=tk.VERTICAL, command=self.tree.yview)

        self.tree.configure(yscroll=self.ysb.set)  # Присоединяем скроллдаун к дереву файлов

        self.ysb.place(x=515, y=0, relheight=1)

        # Добовляем чеббокс копирования данных

        self.var = tk.IntVar()
        self.cb_copyfile = tk.Checkbutton(self, text="Скопировать данные в локальный проект",
                                          variable=self.var, bg=self.mycolor_1)
        self.cb_copyfile.place(x=660, y=695)

    # Создаем Иерархическую структуру папок

    def create_left_tree(self):

        self.abspath = os.path.abspath(self.network_path) # Создаём переменную, которая возвращает нормализованный абсолютный путь
        self.nodes = {} # Создаём словарь
        self.tree_left = ttk.Treeview(self.group_1, height=28) # Указываем высоту окна, в котором будут папки и файлы
        self.tree_left.place(x=0, y=0) # Задаём точку отсчёта для местоположения таблицы
        self.tree_left.heading("#0", text=self.abspath, anchor=tk.W) # Задаём местоположение заголовка, по умолчанию указывается путь
        self.tree_left.column("#0", width=510) # Указываем ширину окна, в котором будут папки и файлы

        self.tree_left.bind("<<TreeviewOpen>>", self.open_node) # Вызываем функцию, которая позволяет после нажатия плюсика определить вложеные данные
        self.populate_node("", self.abspath) # Вызываем функцию, которая определяет какие папки находятся в первоначальном пути

        # Добавляем скроллдаун
        self.ysb_left = ttk.Scrollbar(self.group_1, orient=tk.VERTICAL, command=self.tree_left.yview) # Указываем, что используется вертикальный скролл

        self.tree_left.configure(yscroll=self.ysb_left.set)  # Присоединяем скроллдаун к дереву файлов

        self.ysb_left.place(x=515, y=0, relheight=1) # Задаём расположение скролла
        self.tree_left.bind("<Double-1>",lambda event: self.OnDoubleClick_tree_left())

    # Функция, которая изначально заполняет дерево записями из указанной директории
    def populate_node(self, parent, abspath):
        for entry in os.listdir(abspath): # Отображаются все названия директорий внутри первоначальной папки
            entry_path = os.path.join(abspath, entry) # Задаётся абсолютный путь
            node = self.tree_left.insert(parent, tk.END, text=entry, open=False) # Задаём переменную, которая настраивает, чтобы папки были закрыты (отображался плюсик для раскрытия)
            if os.path.isdir(entry_path): # Проверяется, является ли путь директорией
                self.nodes[node] = entry_path # Если абсолютный путь записи указывает на директорию, то добавляется связь для узла и пути в атрибут
                self.tree_left.insert(node, tk.END)

    # Функция, которая обрабатывает раскрывающиеся вложенные директории
    def open_node(self, event):
        item = self.tree_left.focus() # Метод, который раскрывает выбранную директорию
        self.abspath = self.nodes.pop(item, False) # Возвращаем параметр, в качестве значения по умолчанию, если узел не существует, чтобы не возникала ошибка KeyError
        if self.abspath:
            children = self.tree_left.get_children(item) # Если записи являются директориями, то раскрываются поддиректории
            self.tree_left.delete(children) # Удаляем пустые записи
            self.populate_node(item, self.abspath) # Добавляем существующие вложенные файлы

    def OnDoubleClick_tree_left(self):
        item_iid = self.tree_left.selection()[0]
        parent_iid = self.tree_left.parent(item_iid)
        paren_iid_2 = self.tree_left.parent(parent_iid)
        self.micromine_path = os.path.join(self.network_path, self.tree_left.item(paren_iid_2)['text'], self.tree_left.item(parent_iid)['text'], self.tree_left.item(item_iid)['text'])
        self.read_files_attributes(self.micromine_path)

    def read_files_attributes(self, path_file):
        self.list_tree = []
        self.path_file = path_file
        filename, file_extension = os.path.splitext(self.path_file) # Находим расширение файл
        if file_extension in [".STR", ".DAT", ".tridb"]:
            time_stats = os.stat(self.path_file).st_mtime  # Получаем статистику по каждому файлу (дата)
            timestamp_date = datetime.datetime.fromtimestamp(time_stats).strftime('%Y-%m-%d')  # Преобразуем дату в нужный формат
            size_stats = os.stat(self.path_file).st_size  # Получаем статистику по каждому файлу (размер)
            size_file = str(round(size_stats / 1000)) + " КБ"  # Преобразуем размер в килобайт
            self.ful_path_tree_dict[self.path_file.split("\\")[-1]] = self.path_file # Добавляем в словарь путь(ключ) и имя файла(значение)
            for item in self.tree.get_children(""):
                file_tree = self.tree.set(item, "#1")
                self.list_tree.append(file_tree)
            for key in self.ful_path_tree_dict:
                if key not in self.list_tree:
                    self.tree.insert("", tk.END, values=(key, timestamp_date, size_file))   # Записываем атрибуты в Treeview
                else:
                    print("Файл уже добавлен")

        self.treeview_sort_column()

    # Функция, которая добавляет выбранные данные в список на копирование
    def Add_files_to_tree(self):
        for item_iid in self.tree_left.selection():
            parent_iid = self.tree_left.parent(item_iid)
            paren_iid_2 = self.tree_left.parent(parent_iid)
            self.micromine_path = os.path.join(self.network_path, self.tree_left.item(paren_iid_2)['text'],
                                               self.tree_left.item(parent_iid)['text'],
                                               self.tree_left.item(item_iid)['text'])
            self.read_files_attributes(self.micromine_path)

    # Функция, которая добавляет все данные в список на копирование
    def Add_All_files_to_tree(self):
        for item_iid_1 in self.tree_left.get_children():  # получаем элементы 1 уровня
            item_iid_2 = self.tree_left.get_children(item_iid_1)  # получаем элементы 2 уровня
            item_iid_3 = self.tree_left.get_children(item_iid_2)  # получаем элементы 3 уровня
            item_tup = (item_iid_1,)
            item_tup_2 = item_tup + item_iid_2 + item_iid_3  # получаем кортеж из всех элементов дерева
            for item_iid in item_tup_2:
                parent_iid = self.tree_left.parent(item_iid)
                paren_iid_2 = self.tree_left.parent(parent_iid)
                self.micromine_path = os.path.join(self.network_path, self.tree_left.item(paren_iid_2)['text'],
                                                   self.tree_left.item(parent_iid)['text'],
                                                   self.tree_left.item(item_iid)['text'])
                self.read_files_attributes(self.micromine_path)

    #Функция сортировки Treeview по расширению
    def treeview_sort_column(self):
        rows = [(self.tree.set(item, "#1"), item) for item in self.tree.get_children('')]
        i = sorted(rows, key=lambda x: x[0].split(".")[-1])
        for index, (values, item) in enumerate(i):
            self.tree.move(item, '', index)

    # Функция полной очистки Treeview
    def del_func_all_data(self):
        self.ful_path_tree_dict = {}
        for item in self.tree.get_children():
            self.tree.delete(item)

    # Функция удаления по выбору
    def del_func(self):
        for item in self.tree.selection():
            file_del = self.tree.set(item, "#1")
            self.ful_path_tree_dict.pop(file_del)
            print(self.ful_path_tree_dict)
            self.tree.delete(item)




    # Функция копирования данных из сети
    def copy_files_to_project(self):
        if self.var.get() == 1:
            shutil.rmtree(self.path_project)  # Удаляем всю директорию из проекта
            shutil.copytree(self.network_path, self.path_project,
                            ignore=shutil.ignore_patterns(".*"), dirs_exist_ok=True)
            for values in self.ful_path_tree_dict.values():

                x = self.path_project
                print(self.network_path)
                print(self.path_project)
                #print(os.path.join(self.path_project,))
                #shutil.copy(values,)
            print("Данные успешно скопированы!")
        else:
            print("Данные не загружены!")

    def ignor_copy(self):
        all_files_network = []

        all_files_tree = []
        for root, dirs, files in os.walk(self.network_path, topdown=False):
            for name in files:
                all_files_network.append((os.path.join(root, name)))

        for volumes in self.ful_path_tree_dict.values():
            all_files_tree.append(volumes)

        ignored_names = set(all_files_network).difference(all_files_tree)

        

        return ignored_names






if __name__ == "__main__":
    app = App()
    app.mainloop()
    app.ignor_copy()



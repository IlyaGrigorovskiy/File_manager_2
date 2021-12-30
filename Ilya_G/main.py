import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import os, sys
from pathlib import Path # библиотек
# Создание переменной root_path типа Path,
# в которой содержится абсолютный путь до папки с main.py
root_path = Path(os.path.dirname(os.path.realpath(__file__)))
# Добавляем созданную нами папку в список библиотечных папок
sys.path.insert(0, str(root_path))
import datetime
from idlelib.tooltip import Hovertip
import shutil
import MMpy
from copy_data_to_project import *
from widgets_click import get_form_info
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Набор цветов
        self.mycolor_1 = '#%02x%02x%02x' % (194, 221, 229)  # Фон
        self.mycolor_2 = '#%02x%02x%02x' % (169, 176, 198)  # Панель инструментов
        self.mycolor_3 = '#%02x%02x%02x' % (253, 253, 254)  # Белый
        self.mycolor_4 = '#%02x%02x%02x' % (87, 53, 114)  # Темно фиалетовый
        self.network_path = r"C:\Cетевая папка"  # Указываем путь к сетевой папке
        self.path_project = MMpy.Project.path()
        self.ful_path_tree_dict = {}
        self.create_main_window()
        self.create_buttons()
        self.create_right_tree()
        self.create_left_tree()

        get_form_info(507)




    # Главное окно
    def create_main_window(self):
        self.title("File manager")  # меняем заголов программы
        w = self.winfo_screenwidth()  # определяем ширину монитора
        h = self.winfo_screenheight()  # определяем высоту монитора
        w = w // 2  # середина экрана
        h = h // 2
        w = w - 800  # смещение от середины, иначе в центре экрана окажется верхний левый угол окна, а не его середина
        h = h - 363
        self.geometry('1400x725+{}+{}'.format(w, h))  # пределяем геометрию и положение основного окна программы
        self.resizable(False, False)  # запретит изменение размеров основного окна

        self.configure(bg=self.mycolor_1)  # меняем фон программы
        # Меняем иконку у программы
        path_icon = str(root_path / "icon.ico")
        self.iconbitmap(path_icon)

        # Создаем группы
        self.group_toolbar = tk.LabelFrame(self, height=80, width=1380, bg=self.mycolor_2)
        self.group_toolbar.place(x=10, y=10)

        self.group_1 = tk.LabelFrame(self, height=590, width=540, bg=self.mycolor_3)
        self.group_1.place(x=10, y=100)

        self.group_2 = tk.LabelFrame(self, height = 590, width = 540, bg=self.mycolor_3)
        self.group_2.place(x = 650, y = 100)

    # Создаем кнопки
    def create_buttons(self):
        # Создаем кнопки со стрелками впарво и влево
        self.img_right = tk.PhotoImage(file=str(root_path /"right.png"))
        self.btn_right = tk.Button(self, height=40, width=50, bg=self.mycolor_1, image=self.img_right,
                                   command=self.Add_All_files_to_tree)

        self.btn_right.place(x=575, y=220)
        self.img_right_litle = tk.PhotoImage(file=str(root_path /"right_litle.png"))
        self.btn_right_litle = tk.Button(self, height=40, width=50, bg=self.mycolor_1, image=self.img_right_litle,
                                         command=self.Add_files_to_tree)
        self.btn_right_litle.place(x=575, y=280)


        self.img_left = tk.PhotoImage(file=str(root_path /"left.png"))
        self.btn_left = tk.Button(self, height=40, width=50,bg=self.mycolor_1, image=self.img_left,
                                  command=self.del_func_all_data)
        self.btn_left.place(x = 575, y =400)
        self.img_left_litle = tk.PhotoImage(file=str(root_path /"left litle.png"))
        self.btn_left_litle = tk.Button(self, height=40, width=50, bg=self.mycolor_1, image=self.img_left_litle,
                                        command=self.del_func)
        self.btn_left_litle.place(x=575, y=460)

        # Создаем кнопку загрузки данных в Майкромайн

        self.img_Download = tk.PhotoImage(file=str(root_path /"download.png"))
        self.btn_Download = tk.Button(self.group_toolbar, height=60, width=70, bg=self.mycolor_1, image=self.img_Download,
                                      command=self.copy_files_to_project)
        self.btn_Download.place(x=1290, y=5)
        Hovertip(self.btn_Download, "Функция загрузки данных в Майкромайн.", hover_delay=300)

        # Создаем кнопу выбора сетевой папки

        #кнопка
        self.img_folder = tk.PhotoImage(file=str(root_path /"folder.png"))
        self.img_folder_small = self.img_folder.subsample(2,2)

        self.btn_network_path = tk.Button(self, text = " Выбрать...", width = 80, bg="white",bd = 0, height= 15, image= self.img_folder_small, compound= "left", command=self.select_network_folder)
        # меняем цвет кнопки при наведении курсора мыши
        self.btn_network_path.bind("<Enter>", lambda e: self.btn_network_path.config(bg='#ADD8E6'))
        self.btn_network_path.bind("<Leave>", lambda e: self.btn_network_path.config(bg="white"))
        self.btn_network_path.place(x=434, y=105)

        #Меню выбора форм для загрузки по умолчанию
        self.label_head = tk.Label(self,text="Выбор форм для загрузки данных", bg=self.mycolor_1,font= ('Calibri', 9,'bold'))
        self.label_head.place(x=1200, y=100)

        self.label_BM = tk.Label(self,text="Блочные модели:", bg=self.mycolor_1)
        self.label_BM.place(x=1200, y=120)
        self.combobox_BM = ttk.Combobox(self,width=25, values = get_form_info(507))
        self.combobox_BM.current(0)
        self.combobox_BM.place(x=1200, y=140)

        self.label_point = tk.Label(self,text="Точки:", bg=self.mycolor_1)
        self.label_point.place(x=1200, y=161)
        self.combobox_point = ttk.Combobox(self,width=25, values = get_form_info(437))
        self.combobox_point.current(0)
        self.combobox_point.place(x=1200, y=180)

        self.label_line = tk.Label(self,text="Линии:", bg=self.mycolor_1)
        self.label_line.place(x=1200, y=201)
        self.combobox_line = ttk.Combobox(self,width=25, values = get_form_info(486))
        self.combobox_line.current(0)
        self.combobox_line.place(x=1200, y=220)

        self.label_wr = tk.Label(self,text="Каркасы:", bg=self.mycolor_1)
        self.label_wr.place(x=1200, y=241)
        self.combobox_wr = ttk.Combobox(self,width=25, values = get_form_info(506))
        self.combobox_wr.current(0)
        self.combobox_wr.place(x=1200, y=260)

    #Выбираем сетевую папку
    def select_network_folder(self):
        #Открываем окно выбора папки
        self.folder = filedialog.askdirectory()
        if self.folder != "":
            self.network_path = self.folder
            #Очищаем дерево
            for item in self.tree_left.get_children():
                self.tree_left.delete(item)
            #Создаем и заполняем дерево заново
            self.create_left_tree()


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

        self.abspath = self.network_path #Создаём переменную, которая возвращает нормализованный абсолютный путь
        self.nodes = {} # Создаём словарь
        self.tree_left = ttk.Treeview(self.group_1, height=28) # Указываем высоту окна, в котором будут папки и файлы
        self.tree_left.place(x=0, y=0) # Задаём точку отсчёта для местоположения таблицы


        self.tree_left.heading("#0", text=self.abspath, anchor=tk.W, command=self.select_network_folder) # Задаём местоположение заголовка, по умолчанию указывается путь
        
        
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
            extension = entry_path.split('.')[-1]
            if extension in ["STR", "DAT", "tridb"]:
                node = self.tree_left.insert(parent, tk.END, text=entry, open=False) # Задаём переменную, которая настраивает, чтобы папки были закрыты (отображался плюсик для раскрытия)

            if os.path.isdir(entry_path): # Проверяется, является ли путь директорией
                node = self.tree_left.insert(parent, tk.END, text=entry,open=False)  # Задаём переменную, которая настраивает, чтобы папки были закрыты (отображался плюсик для раскрытия)
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

        self.treeview_sort_column()

    # Функция, которая добавляет выбранные данные в список на копирование
    def Add_files_to_tree(self):
        files = [] # список файлов для добавления
        slct_files =[] # список всех выбранных файлов
        for item_iid in self.tree_left.selection():
         value = self.tree_left.item(item_iid)
         slct_files.append (value['text']) # записываем имена выделенных файлов в список
           # r=корень, d=папки, f = файлы
           # если выделен файл
         for r, d, f in os.walk(self.network_path):
              for file in f:
                  if file in slct_files: # выбираем только выделенные файлы
                     files.append(os.path.join(r, file))# записываем пути всех файлов в сетевой папке в список
                     for f in files:
                        self.read_files_attributes(f)
            # если выделена папка
              for folder in d:
                  if folder in slct_files: # выбираем только выделенную папку
                      fpath = os.path.join(r, folder) #  путь к выделенной папке
                      for r, d, f in os.walk(fpath):
                          for file in f:
                                files.append(os.path.join(r, file))# записываем пути всех файлов в сетевой папке в список
                                for f in files:
                                  self.read_files_attributes(f)

    # Функция, которая добавляет все данные в список на копирование
    def Add_All_files_to_tree(self):
        files = [] # список всех файлов
        # r=корень, d=папки, f = файлы
        for r, d, f in os.walk(self.network_path):
          for file in f:
             files.append(os.path.join(r, file)) # записываем пути всех файлов в сетевой папке в список
        for f in files:
          self.read_files_attributes(f)

    # Функция сортировки Treeview по расширению
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

            self.tree.delete(item)




    # Функция копирования и загрузки данных  из сети
    def copy_files_to_project(self):
        copy_data_to_project(self.path_project + "Сетевая папка",self.network_path, bool(self.var.get()), self.ignor_copy())
        #for key in self.ful_path_tree_dict:
            #downloаd_data_to_мм(self.ful_path_tree_dict[key])

    #Функция игнора файлов
    def ignor_copy(self):
        def _ignore(folder, files):
            ignored_names = []
            for file in files:
                full_path = os.path.join(folder, file)
                if not os.path.isdir(full_path):
                    if file not in self.ful_path_tree_dict.keys():
                        ignored_names.append(file)
            return ignored_names
        return _ignore



app = App()
app.mainloop()
app.ignor_copy()



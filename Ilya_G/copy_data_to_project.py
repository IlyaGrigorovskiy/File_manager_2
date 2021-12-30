import os
import shutil
import MMpy

def copy_data_to_project(path_project,network_path,var,ignored_names):
    # Создаем папку Сетевая папка в проете Майкромайн
    if not os.path.isdir(path_project):
        os.mkdir(path_project)

    if var:
        shutil.rmtree(path_project)
        shutil.copytree(network_path, path_project,
                        ignore=ignored_names, dirs_exist_ok=True)

        files_project = []  # список всех файлов
        # r=корень, d=папки, f = файлы
        for r, d, f in os.walk(path_project):
            for file in f:
                files_project.append(os.path.join(r, file))  # записываем пути всех файлов d ghjtrnt в сетевой папке в список
        for path in files_project:
            downloаd_data_to_мм(path)


    else:
        print("FDFDFDF")


def downloаd_data_to_мм(path_bm):
    MMpy.set_api_version(1, 0, 0)  # Set MMpy API version for compatibility
    hatch0 = MMpy.Hatch(MMpy.Colour(255, 255, 255), MMpy.Colour(255, 255, 255), MMpy.Colour(0, 0, 0), False, MMpy.LineType.solid, 13, 1, 'MM Hatch Patterns 1')
    datagrid0 = MMpy.DataGrid(3, 1)  # GRID
    datagrid0.set_column_info(0, 1, -1)  # Значение, type:value
    datagrid0.set_column_info(1, 2, 1)  # Значение2, type:colour
    datagrid0.set_column_info(2, 3, -1)  # Метка, type:value
    datagrid0.set_row(0, ['', MMpy.Colour(171, 171, 171), ' < 0.4'])
    datagrid0.set_row(1, ['0.4', MMpy.Colour(0, 255, 64), '0.4 до 0.8'])
    datagrid0.set_row(2, ['0.75', MMpy.Colour(0, 255, 255), '0.8 до 1.5'])
    datagrid0.set_row(3, ['1.5', MMpy.Colour(255, 0, 0), ' >= 1.5'])
    nestedformset2 = MMpy.FormSet(284, '22.0.439.2')  # NUMERIC_COLSET - Числовой набор цветов [COLRANGE]: Создать и изменить набор цветов, основанный на диапазонах
    nestedformset2.set_field(161, 1)  # RANGES, type:choice
    nestedformset2.set_field(162, 0)  # SPECTRUM, type:choice
    nestedformset2.set_field(1501, datagrid0)  # GRID, type:grid
    nestedformset2.set_field(1505, True)  # UPDATE, type:boolean
    datagrid1 = MMpy.DataGrid(10, 1)  # LABELS_GRID
    datagrid1.set_column_info(0, 0, 14)  # Вкл., type:boolean
    datagrid1.set_column_info(1, 1, 4)  # Поле текста, type:value
    datagrid1.set_column_info(2, 2, -1)  # Десятичные, type:value
    datagrid1.set_column_info(3, 3, 17)  # Набор цветов, type:formset
    datagrid1.set_column_info(4, 4, 1)  # Цвет по умолчанию, type:colour
    datagrid1.set_column_info(5, 5, -1)  # Размещение, type:value
    datagrid1.set_column_info(6, 7, -1)  # Смещение по X, type:value
    datagrid1.set_column_info(7, 8, -1)  # Смещение по Y, type:value
    datagrid1.set_column_info(8, 9, -1)  # Угол, type:value
    datagrid1.set_column_info(9, 6, -1)  # Текст, type:value
    datagrid1.set_row(0, ['1', '', '', '', '', '', '', '', '', ''])
    datagrid2 = MMpy.DataGrid(6, 1)  # FILTER_GRID
    datagrid2.set_column_info(0, 1, 14)  # Вкл., type:boolean
    datagrid2.set_column_info(1, 2, 4)  # Атрибут, type:value
    datagrid2.set_column_info(2, 3, 14)  # Вкл.2, type:boolean
    datagrid2.set_column_info(3, 4, -1)  # Значение, type:value
    datagrid2.set_column_info(4, 5, 14)  # Вкл.3, type:boolean
    datagrid2.set_column_info(5, 6, -1)  # Значение2, type:value
    datagrid2.set_row(0, ['0', '', '0', '', '0', ''])
    formset0 = MMpy.FormSet(507, '22.0.439.2')  # WS_LOAD_BLOCK_MODEL - Блочная модель [VXBLOCKS]: Показать блочные модели, созданные MM
    formset0.set_field(7, path_bm)  # WSBLK_FILE, type:filename
    formset0.set_field(8, 0)  # TYPE, type:choice
    formset0.set_field(9, False)  # WSBLK_FILTER, type:boolean
    formset0.set_field(10, '')  # FLTNO, type:formset
    formset0.set_field(11, 'X')  # X_VARB, type:field
    formset0.set_field(12, 'Y')  # Y_VARB, type:field
    formset0.set_field(13, 'Z')  # Z_VARB, type:field
    formset0.set_field(15, '')  # THICK_VARB, type:field
    formset0.set_field(19, False)  # FIELD_BOOL, type:boolean
    formset0.set_field(20, '')  # HATCH_VARB, type:field
    formset0.set_field(21, '')  # HATCH_FILE, type:formset
    formset0.set_field(22, hatch0)  # HATCH, type:hatch
    formset0.set_field(23, True)  # FOREGROUND_BOOL, type:boolean
    formset0.set_field(25, False)  # BACKGRND_BOOL, type:boolean
    formset0.set_field(29, 'AU')  # HATCH_COL_VARB, type:field
    formset0.set_field(30, nestedformset2)  # HATCH_COL_FILE, type:formset
    formset0.set_field(31, MMpy.Colour(0, 0, 100))  # HATCH_COL, type:colour
    formset0.set_field(34, '')  # HATCLRBACK_VARB, type:field
    formset0.set_field(35, '')  # SET, type:formset
    formset0.set_field(36, MMpy.Colour(0, 0, 100))  # DEF, type:colour
    formset0.set_field(37, 0)  # F3DSHADE, type:choice
    formset0.set_field(38, 0)  # F2DSLICE, type:choice
    formset0.set_field(39, 0)  # F3DLINES, type:choice
    formset0.set_field(40, 0)  # F3DPOINTS, type:choice
    formset0.set_field(41, '')  # FLD, type:field
    formset0.set_field(42, False)  # USE, type:boolean
    formset0.set_field(43, 1)  # CONST, type:choice
    formset0.set_field(44, 0)  # FIELD, type:choice
    formset0.set_field(46, False)  # XY, type:boolean
    formset0.set_field(50, '')  # CENTRE_COL_VARB, type:field
    formset0.set_field(51, '')  # CENTRE_COL_FILE, type:formset
    formset0.set_field(52, MMpy.Colour(0, 0, 100))  # CENTRE_COL, type:colour
    formset0.set_field(53, False)  # CENTRE_BOOL, type:boolean
    formset0.set_field(54, False)  # LABELS_BOOL, type:boolean
    formset0.set_field(104, '0')  # SLIDER
    formset0.set_field(107, 0)  # F3DSHADE_SHADER, type:choice
    formset0.set_field(108, 0)  # F3DLINES_SHADER, type:choice
    formset0.set_field(111, True)  # EDGES, type:boolean
    formset0.set_field(112, MMpy.Colour(0, 0, 100))  # COLOUR, type:colour
    formset0.set_field(113, 0)  # WIDTH, type:choice
    formset0.set_field(116, False)  # GRADE_FILTER, type:boolean
    formset0.set_field(123, 1)  # AUTO, type:choice
    formset0.set_field(124, datagrid1)  # LABELS_GRID, type:grid
    formset0.set_field(125, datagrid2)  # FILTER_GRID, type:grid
    name = os.path.basename(path_bm)
    formset0.save(name)
    formset0.run()
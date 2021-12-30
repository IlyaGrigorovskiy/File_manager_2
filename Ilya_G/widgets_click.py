
import MMpy
import os, sqlite3



def get_form_info(command_id):
    form_bd = MMpy.Project.path()
    mm_version = int(MMpy.Micromine.version().split('.')[0])
    for file in os.listdir(form_bd):
        if file.startswith("FLDVAL") and file.endswith(".BDB"):
            if int(file[6:-5]) == mm_version:
                form_bd += file
                break
    con = sqlite3.connect(form_bd)
    cursor = con.cursor()
    cursor.execute(f"select title, setId from PRMSETS where cmdId = {command_id}")
    names_and_ids = cursor.fetchall()
    forms = ["По умолчанию"]
    for name, id_ in names_and_ids:
        forms.append(name)
    con.close()
    return list(filter(None, forms))



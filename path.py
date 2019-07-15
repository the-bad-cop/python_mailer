import os
import datetime


class pathClass:
    path = "templates\\template.txt"

    def pathMeth():
        pwd = os.getcwd()
        # filename="template.txt"
        f_path = os.path.join(pwd, pathClass.path)
        # if not os.path.isfile(f_path):
        # raise Exception("Template file not found!")
        return f_path

    def getTemplate():
        file_path = pathClass.pathMeth()
        return open(file_path).read()

    """
    def formatTemplate(tempText, dataItems):
        return(tempText.format(**dataItems))

    
    date_tdy = datetime.date.today()
    path = "templates\\template.txt"
    dataItems = {
        "name":
        "date":
        "total":

    print(formatTemplate(getTemplate(path), dataItems))
    """

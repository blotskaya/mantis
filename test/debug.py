from model.project import Project

def test_debug(app):
    result = app.soap.get_project_list("administrator", "root")
    print(result)


from model.project import Project

def test_add_project(app):
    project = Project(name="TestAuto2")
    #app.session.login("administrator", "root")
    #assert app.session.is_logged_in_as("administrator")
    app.project.open_project_list()
    old_project_list = app.project.get_project_list()
    app.project.create(project)
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) + 1 == len(new_project_list)
    old_project_list.append(project)
    assert sorted(str(old_project_list)) == sorted(str(new_project_list))

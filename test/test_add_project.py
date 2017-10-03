from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    #old_project_list = app.project.get_project_list()
    app.project.create(Project(name="TestAuto1"))
    #new_project_list = old_project_list + 1
    #assert len(old_project_list) == len(new_project_list)

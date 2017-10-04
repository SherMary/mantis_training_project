from model.project import Project


def test_delete_first_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    app.project.open_project_list()

    if app.project.count() == 0:
        app.project.create(Project(name="New Project"))
    old_projects_list = app.project.get_project_list()
    app.project.delete_first_project()
    new_project_list = app.project.get_project_list()
    assert len(old_projects_list) - 1 == len(new_project_list)
    old_projects_list[0:1] = []
    assert sorted(str(old_projects_list)) == sorted(str(new_project_list))

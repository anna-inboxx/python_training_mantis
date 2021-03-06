from model.project import Project

def test_add_project(app):

    project = Project(name="test1122255")
    old_projects_list = app.soap.get_projects_list(app.username, app.password)
    app.project.create_project(project)
    assert len(old_projects_list) + 1 == app.project.count()
    new_projects_list = app.soap.get_projects_list(app.username, app.password)
    old_projects_list.append(project)
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)

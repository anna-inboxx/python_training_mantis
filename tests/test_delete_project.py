from model.project import Project
import random

def test_delete_some_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(name="test123456"))
    old_projects = app.soap.get_projects_list(app.username, app.password)
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    assert len(old_projects) - 1 == app.project.count()
    new_projects = app.soap.get_projects_list(app.username, app.password)
    old_projects.remove(project)
    assert old_projects == new_projects



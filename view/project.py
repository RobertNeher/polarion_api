import flet as ft

from utilities.configuration import Configuration
from model.project import Project

class ProjectView():
    def __init__(self) -> None:
        self.widgets = []
        _projects = Project()
        self.projects = _projects.projects

        for _project in self.projects:
            config = Configuration()
            projectDetail = _projects.getDetails(projectID=_project["id"])
            print(projectDetail["description"])
            self.widgets.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(controls= [
                                ft.ListTile(
                                    leading=ft.Icon(ft.icons.ALBUM),

                                    title=ft.Text(f"{projectDetail['name']} (ID: {projectDetail['id']}",
                                        style=config.headerStyle
                                    ),
                                    subtitle=ft.Text(
                                        projectDetail["description"]["value"],
                                        style=config.normalStyle
                                    ),
                                ),
                                ft.Row(
                                    controls=[ft.TextButton("Open")],
                                    alignment=ft.MainAxisAlignment.END,
                                )
                            ]
                        )
                    ),
                    width=400,
                )
            )

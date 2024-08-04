import flet as ft

from utilities.configuration import Configuration
from model.project import Project

class ProjectView():
    def __init__(self, callback) -> None:
        config = Configuration()
        self.widgets = []
        _projects = Project()
        projects = _projects.projects

        for _project in projects:
            projectDetail = _projects.getDetails(projectID=_project["id"])

            if "description" in projectDetail.keys():
                description = projectDetail["description"]["value"]
            else:
                description = "<empty>"

            self.widgets.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(controls= [
                                ft.ListTile(
                                    leading=ft.Icon(ft.icons.ALBUM),

                                    title=ft.Text(f"{projectDetail['name']} (ID: {projectDetail['id']})",
                                        style=config.headerStyle
                                    ),
                                    subtitle=ft.Text(
                                        description,
                                        style=config.normalStyle
                                    ),
                                ),
                                ft.Row(
                                    controls=[ft.TextButton(
                                        "Open",
                                        on_click=callback,
                                        data=_project["id"])
                                    ],
                                    alignment=ft.MainAxisAlignment.END,
                                )
                            ]
                        )
                    ),
                    width=400,
                    height=150,
                    color=ft.colors.BLUE_GREY_100,
                )
            )

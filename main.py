import flet as ft

from utilities.configuration import Configuration
from view.project import ProjectView

def main(page: ft.Page):
    def openProject(e):
        print(f"callback: {e.control.data}")

    config = Configuration()
    projectView = ProjectView(callback=openProject)
    projectCards = projectView.widgets

    page.add(ft.Column(controls=[
            ft.Text(f"Projects on {config.schema}://{config.polarionHost}",
                    text_align = ft.TextAlign.CENTER,
                    size=30,
                    style=config.headerStyle
            ),
            ft.Container(bgcolor=ft.colors.DEEP_ORANGE_400),
            ft.Column(controls=projectCards,
                expand=0,
                spacing=10,
            )
        ])
    )
    page.update()



ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)

import flet as ft
from chat_vox import Config
from settings import SettingsView
from top import TopView


def main(page: ft.Page):
    def route_change(e: ft.RouteChangeEvent):
        troute = ft.TemplateRoute(e.route)
        if troute.match("/"):
            page.views.clear()
            page.views.append(TopView(page))
        elif troute.match("/settings"):
            page.views.append(SettingsView(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    config = Config("config.ini")
    is_setup = config.read_config()

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.title = "ChatVox"

    page.go("/")
    if not is_setup:
        page.go("/settings")


if __name__ == "__main__":
    ft.app(target=main)

import flet as ft
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

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.title = "ChatVox"

    page.views.clear()
    page.go("/")


if __name__ == "__main__":
    ft.app(target=main)

import flet as ft

appbar = ft.AppBar(
    title=ft.Text("ChatVox"),
    bgcolor=ft.colors.SURFACE_VARIANT,
    actions=[
        ft.IconButton(ft.icons.SETTINGS, on_click=lambda e: e.page.go("/settings"))
    ],
)

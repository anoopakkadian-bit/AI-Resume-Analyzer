import flet as ft

def main(page: ft.Page):
    page.title = "SaaSva Mobile"
    page.window_width = 380
    page.window_height = 700
    page.bgcolor = "#F0F2F5" # കുറച്ചുകൂടി പ്രീമിയം വൈറ്റ്
    page.horizontal_alignment = "center"

    # Top Search (UMANG Style)
    search_bar = ft.Container(
        content=ft.TextField(
            hint_text="Search for services...",
            prefix_icon=ft.icons.SEARCH,
            border_radius=25,
            bgcolor="white",
            border_color="transparent",
            height=50,
        ),
        padding=ft.padding.only(top=20, bottom=10)
    )

    # Grid for Services
    def make_box(name, icon, color):
        return ft.Container(
            content=ft.Column([
                ft.Icon(icon, color=color, size=35),
                ft.Text(name, size=12, weight="bold", color="black54")
            ], alignment="center", horizontal_alignment="center"),
            bgcolor="white",
            width=100, height=100,
            border_radius=20,
            shadow=ft.BoxShadow(blur_radius=10, color="black12"),
            on_click=lambda _: print(f"{name} clicked")
        )

    services_grid = ft.Row([
        make_box("Token", ft.icons.TICKET, "red"),
        make_box("MVD", ft.icons.CAR_RENTAL, "blue"),
        make_box("Bills", ft.icons.ELECTRICAL_SERVICES, "orange"),
        make_box("PSC", ft.icons.HISTORY_EDU, "green"),
        make_box("Health", ft.icons.LOCAL_HOSPITAL, "pink"),
        make_box("Ration", ft.icons.GRAIN, "brown"),
    ], wrap=True, alignment="center")

    # Bottom Nav
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationDestination(icon=ft.icons.CHAT_BUBBLE_OUTLINE, label="SaaSva Bot"),
            ft.NavigationDestination(icon=ft.icons.PERSON_OUTLINE, label="Profile"),
        ]
    )

    page.add(
        ft.Text("🌊 SaaSva", size=28, weight="bold", color="blue700"),
        search_bar,
        ft.Text("Quick Services", size=16, weight="w600"),
        services_grid
    )

ft.app(target=main)
import flet as ft


class Landing(ft.View):
    def __init__(self ,page: ft.Page) -> None:
        super(Landing,self).__init__(
            route="/",horizontal_alignment='center',
            vertical_alignment='center'
        )

        self.page = page
        self.cart_logo = ft.Icon(name=ft.icons.SHOPPING_CART_CHECKOUT_OUTLINED,size=64)
        self.title = ft.Text('MINHA LOJA'.upper(),size=28, weight='bold')
        self.subtitle = ft.Text('Desenvolvido com Flet', size=11)
        self.controls = [
            self.cart_logo,
            ft.Divider(height=25,color="transparent"),
            self.title,
            self.subtitle,
            ft.Divider(height=10,color="transparent"),
        ]

def main(page:ft.Page) -> None:
    def router(route) -> None:
        page.views.clear()

        if page.route == '/':
            landing = Landing(page)
            page.views.append(landing)

        page.update()

    page.on_route_change = router
    page.go('/')

ft.app(main)

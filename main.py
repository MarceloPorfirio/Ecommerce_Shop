import flet as ft


class Landing(ft.view):
    def __init__(self,page:ft.Page) -> None:
        super(Landing,self).__init__(
            route="/",horizontal_alignment='center',
            vertical_alignment='center'
        )

        self.page = page
        self.cart_logo = ft.Icon(name=ft.icons.SHOPPING_CART_CHECKOUT_OUTLINED,size=64)
        self.controls = [
            self.cart_logo
        ]

def main(page:ft.Page) -> None:
    page.add(ft.SafeArea(ft.Text('Hello, Flet')))


ft.app(main)

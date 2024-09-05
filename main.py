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
        self.product_page_btn = ft.IconButton(
            "arrow_forward",
            width=54,
            height=54,
            style=ft.ButtonStyle(
                bgcolor={"":"#202020"},
                shape={"": ft.RoundedRectangleBorder(radius=8)},
                side={"": ft.BorderSide(2,"white54")}
            ),
            on_click= lambda e: self.page.go("/products")
        )
        self.controls = [
            self.cart_logo,
            ft.Divider(height=25,color="transparent"),
            self.title,
            self.subtitle,
            ft.Divider(height=10,color="transparent"),
            self.product_page_btn
        ]

# Definir o Model, onde guardar os dados
class Model(object):
    products: dict = {
        0:{
            "id": "111",
            "img_src": "phone1.png",
            "name": "Product 1",
            "description": " ajsioajsoiajsioajsoiajsioajsjaosjaoaoijsioajeioajeoiajeioajeioajeioajeioajeioajdoiasuifnsuodjiajdia",
            "price": "R$ 1200,00"
        },
        1:{
            "id": "111",
            "img_src": "phone1.png",
            "name": "Product 1",
            "description": " ajsioajsoiajsioajsoiajsioajsjaosjaoaoijsioajeioajeoiajeioajeioajeioajeioajeioajdoiasuifnsuodjiajdia",
            "price": "R$ 1200,00"
        },
        2:{
            "id": "111",
            "img_src": "phone1.png",
            "name": "Product 1",
            "description": " ajsioajsoiajsioajsoiajsioajsjaosjaoaoijsioajeioajeoiajeioajeioajeioajeioajeioajdoiasuifnsuodjiajdia",
            "price": "R$ 1200,00"
        },
        3:{
            "id": "111",
            "img_src": "phone1.png",
            "name": "Product 1",
            "description": " ajsioajsoiajsioajsoiajsioajsjaosjaoaoijsioajeioajeoiajeioajeioajeioajeioajeioajdoiasuifnsuodjiajdia",
            "price": "R$ 1200,00"
        },


    }

    cart = dict = {}

    @staticmethod
    def get_products():
        return Model.products
    
    def get_cart():
        return Model.cart

# Definir a página produtos
class Product(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super(Product, self).__init__(route="/products")
        self.page = page

    def create_products(self, products: dict =Model.get_products()) -> None:
        # loop pelos dados, extrair a informação baseada nas chaves
        for _ ,value in products.items():
            for key, value, in value.items():
                if key == "img_src":
                    ...
                elif key == "name":
                    ...
                elif key == "description":
                    ...
                elif key == "id":
                    ...
                elif key == "price":
                    ...

    # Definir metodo para image UI
    def create_product_image(self, img_path: str):
        return ft.Container(image_src=img_path, image_fit="fill",
                            border_radius=6, padding=10)

    # Definir o metodo para o texto UI (nome + descrição)
    def create_product_text(self, name: str, description: str):
        return ft.Column([ft.Text(name, size=18), ft.Text(description, size=11)])
    
    # Definir o metodo para o preço e botão de adicionar ao carrinho
    def create_product_event(self, price: str, idd: str):
        return ft.Row(
            [
                ft.Text(price, size=14),
                ft.IconButton("add", data=idd, on_click=self.add_to_cart)
            ],
            alignment="spaceBetween"
        )
    # Metodo para pegar o produto dentro do container
    def create_product_container(self, expand: bool, control: ft.control):
        return ft.Container(content=control,expand=expand, padding=5)


def main(page:ft.Page) -> None:
    def router(route) -> None:
        page.views.clear()

        if page.route == '/':
            landing = Landing(page)
            page.views.append(landing)

        if page.route == '/products':
            products = Product(page)
            page.views.append(products)

        page.update()

    page.on_route_change = router
    page.go('/')

ft.app(main)

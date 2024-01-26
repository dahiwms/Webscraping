from bs4 import BeautifulSoup
import requests

page = 1
url = f"https://supermercado.laanonimaonline.com/almacen/n1_1/pag/{page}/"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")

product_list = soup.find_all('div', class_='producto item text_center centrar_img fijar cuadro clearfix')
product_special = soup.find_all('div', class_='producto especial item text_center centrar_img fijar cuadro clearfix ')

for product in product_list:
    product_name = product.find('div', class_='titulo02 aux1 titulo_puntos clearfix').text.strip()
    product_after = product.find('div', class_='precio anterior codigo').text.strip()
    product_price_plus = product.find('div', class_='precio semibold aux1').text.strip()

    print(f'''
        Product Name: {product_name}
        Previous Price: {product_after}
        Current Price: {product_price_plus}
    ''')

for product in product_special:
    product_name = product.find('div', class_='titulo02 aux1 titulo_puntos clearfix').text.strip()
    product_after = product.find('div', class_='precio anterior codigo').text.strip()
    product_price_plus = product.find('div', class_='precio semibold aux1').text.strip()

    print(f'''
        Product Name: {product_name}
        Previous Price: {product_after}
        Current Price: {product_price_plus}
    ''')



from bs4 import BeautifulSoup
import requests

for i in range(1, 2):
    url = f"https://supermercado.laanonimaonline.com/almacen/n1_1/pag/{i}/"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")

    product_special = soup.find_all('div', class_='producto especial item text_center centrar_img fijar cuadro clearfix')

    print("------------------productos especiales------------")

    for Sproduct in product_special:
        product_name_element = Sproduct.find('div', class_='titulo02 aux1 titulo_puntos clearfix')
        product_after_element = Sproduct.find('div', class_='precio anterior codigo')
        product_price_plus_element = Sproduct.find('div', class_='precio semibold aux1')
        promo_element = Sproduct.find('span', class_='position position-left-top icono promocion')

        # Check if the elements are found before accessing their text attributes
        product_name = product_name_element.text.strip() if product_name_element else "N/A"
        product_after = product_after_element.text.strip() if product_after_element else "N/A"
        product_price_plus = product_price_plus_element.text.strip() if product_price_plus_element else "N/A"

        # Check if the promo element is found and evaluate the promotion type
        promo = "No Promotion"
        if promo_element:
            promo_content = promo_element.text.strip()
            if 'promocion2x1' in promo_content:
                promo = "Promocion 2x1"
            elif 'promocion20-off' in promo_content:
                promo = "Promocion 20% Off"
            elif 'promocion15-off' in promo_content:
                promo = "Promocion 15% Off"
            else:
                promo = "Unknown Promotion"

        print(f'''
            Product Name: {product_name}
            Previous Price: {product_after}
            Current Price: {product_price_plus}
            Promo: {promo}
        ''')





    print("------------------PAGINA", i, "------------")
    
    for product in product_list:
        product_name_element = product.find('div', class_='titulo02 aux1 titulo_puntos clearfix')
        product_after_element = product.find('div', class_='precio anterior codigo')
        product_price_plus_element = product.find('div', class_='precio semibold aux1')

        # Check if the elements are found before accessing their text attributes
        product_name = product_name_element.text.strip() if product_name_element else "N/A"
        product_after = product_after_element.text.strip() if product_after_element else "N/A"
        product_price_plus = product_price_plus_element.text.strip() if product_price_plus_element else "N/A"

        print(f'''
            Product Name: {product_name}
            Previous Price: {product_after}
            Current Price: {product_price_plus}
        ''')



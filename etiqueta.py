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
        after_price_element = Sproduct.find('div', class_='precio anterior codigo')
        current_price_element = Sproduct.find('div', class_='precio semibold aux1')

        # Obtener el tipo de promoción
        promo_text = ""
        
        promo_element_2x1 = Sproduct.find('span', class_='position position-left-top icono promocion promocion2x1')
        promo_element_2da_70 = Sproduct.find('span', class_='position position-left-top icono promocion promocion2da-al-70')
        promo_element_25_off = Sproduct.find('span', class_='position position-left-top icono promocion promocion25-off')
        promo_element_30_off = Sproduct.find('span', class_='position position-left-top icono promocion promocion30-off')
        promo_element_20_off = Sproduct.find('span', class_='position position-left-top icono promocion promocion20-off')
        promo_element_15_off = Sproduct.find('span', class_='position position-left-top icono promocion promocion15-off')
        promo_element_50_off = Sproduct.find('span', class_='position position-left-top icono promocion promocion50-off')

        if promo_element_2x1:
            promo_text = f"Promocion 2x1 Pagas {product_price_plus} C/U"
        elif promo_element_2da_70:
            promo_text = "2da unidad al 70%"
        elif promo_element_25_off:
            promo_text = "25% OFF"
        elif promo_element_20_off:
            promo_text = "20% OFF"
        elif promo_element_15_off:
            promo_text = "15% OFF"
        elif promo_element_50_off:
            promo_text = "50% OFF"
        elif promo_element_30_off:
            promo_text = "30% OFF"
            

        # Check if the elements are found before accessing their text attributes
        product_name = product_name_element.text.strip() if product_name_element else "N/A"
        after_price = after_price_element.text.strip() if after_price_element else "N/A"
        current_price = current_price_element.text.strip() if current_price_element else "N/A"

        print(f'''
            Product Name: {product_name}
            Previous Price: {after_price}
            Current Price: {current_price}
            Promo: {promo_text}
        ''')


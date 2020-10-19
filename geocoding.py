import sys
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GeoCode:
    def __init__(self):
        url = 'https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/utils/geocoder'

        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument('log-level=3')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def address_to_coords(self, address):
        search_bar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="query-input"]'))
        )

        # self.driver.find_element(By.ID, 'show-options-link').click()
        # self.driver.find_element(By.ID, 'bias-viewport-checkbox').click()

        search_bar.clear()
        search_bar.send_keys(address)

        geocode_button = self.driver.find_element(By.XPATH, '//*[@id="geocode-button"]')
        geocode_button.click()

        texto = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="result-0"]/table/tbody/tr/td[2]/p[@class="result-location"]'))
        )

        coord_regex = re.compile(r'\W?\d{1,2}.\d{1,6},\W?\d{1,2}.\d{1,6}')

        coords = coord_regex.findall(texto.text)[0].split(',')
        latitude = float(coords[0])
        longitude = float(coords[1])

        js_string = """
                        function getElementByXpath(path) {
                            return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                        }
                        var element = getElementByXpath('//*[@id="result-0"]/table/tbody/tr/td[2]/p[@class="result-location"]');
                        element.remove();
                    """

        self.driver.execute_script(js_string)

        return {'latitude': latitude, 'longitude': longitude}

    def address_list_to_coords(self, addresses_list):
        coord_list = []
        for index, addr in enumerate(addresses_list):
            coord = self.address_to_coords(addr)
            coord_list.append(coord)
            print(coord)
            if index % 5 == 0:
                time.sleep(2)

        return coord_list


if __name__ == '__main__':
    geocode = GeoCode()

    coord = geocode.address_to_coords(sys.argv[1])
    print(coord)
    geocode.quit()

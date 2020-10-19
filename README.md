# web scraping geocode

O código usa a api de Geocoding do Google por meio de web scraping para receber um endereço escrito e retornar sua latitude e longitude.

Use para instalar os requisitos.
```
pip install -r requirements.txt
```


## Exemplos de uso:
### Terminal:
```
python geocoding.py "Av. Alm. Barroso, 123 , Rio de Janeiro"
```

### Import:
```python
from geocoding import Geocode

geocode = GeoCode()

# passando por string
coord = geocode.address_to_coords("Av. Alm. Barroso, 123 , Rio de Janeiro")
print(coord)

# passando por lista
lista_de_enderecos = ["Av. Alm. Barroso, 123 , Rio de Janeiro", "Rua da Quitanda 123 RJ"]
coord_list = geocode.address_list_to_coords(lista_de_enderecos)
```

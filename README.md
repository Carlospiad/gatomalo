#gatomalo

##Dependencies
Before you can use Gatomalo you need Python3.4 with virtualenv:


##Installation Instructions
1. Make sure you have pyvenv installed
2. First, go to directory and activate the pyvenv
```
source venv/bin/activate
```
3. install the Dependencies
```
pip install -r requirement.txt
```
4. Create db in Mac OSX
```
createdb gatomalo
```
5. Setup the db
```
export gatomalo_development='postgresql:///gatomalo'
```
6. Run the app
```
python3 app.py
```

##Usage Instructions
### Manual commands

1. To send a Factura JSON:
  ```
  curl http://localhost:5000/facturas --data     @fact.json -H 'Content-Type: application/json'
  ```

2. To print Reporte X y Z
  got to `cd /gatomalo` and run
  ```
  sudo ./tfunilx SendCmd I0X
  sudo ./tfunilx SendCmd I0Z
  ```
3. to create a Nota de Credito (devolucion)
  ```
  curl http://192.168.1.3:5000/nota --data     @dev.json -H 'Content-Type: application/json'
  ```
4. dev.json default format:
  factura_id: es el número que se encuentra en localhost:5000/facturas
  legacy_id: es el número impreso en la factura fiscal
  ```json
  {"nota": {
  "factura_id":104,
  "legacy_id":140
  }}
  ```
5. reporte con rango de fechas de facturas impresas
  ```
  fecha de inicio YYYMMDD
  fecha de fin yyymmdd
  RfYYYMMDDyyymmdd
  ejemplo (del 1ero de enero de 2014 hasta el 1ero de diciembre de 2014.
  sudo ./tfunilx SendCmd Rf01401010150401
  ```

## Improvement
If you want to install new dependencies please:

1. activate the pyvenv first
2. install the dependency you need
3. Add the dependencies to the requierement list (only run the next code):
  ```
  pip freeze > requirement.txt
  ```
##Credits

Special thanks to:
- Cat designed by <a href="http://www.thenounproject.com/misirlou">misirlou</a> from the <a href="http://www.thenounproject.com">Noun Project</a>

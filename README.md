#gatomalo

##Dependencies
Before you can use Gatomalo you need Python3.4 with virtualenv:


##Installation Instructions


1. Make sure you have pyvenv installed
1. First, go to directory and activate the pyvenv
```
source venv/bin/activate
```
2. install the Dependencies
```
pip install -r requirement.txt
```
3. Create db in Mac OSX
```
createdb gatomalo
```
3. Setup the db
```
export gatomalo_development='postgresql:///gatomalo'
```
3. Run the app
```
python3 app.py
```

##Usage Instructions
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

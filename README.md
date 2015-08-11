#gatomalo

##Dependencies
Before you can use gatomalo you need Python3 with virtualenv:


##Installation Instructions


1. First, activate the pyvenv
```
source venv/bin/activate
```
2. install the Dependencies
```
pip install -r requirement.txt
```
3. Setup the db
```
createdb gatomalo
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

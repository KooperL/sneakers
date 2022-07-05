#Installation
`pip install virtualenv` to download the module to create a virtual environment.

Create a new venv with `virtualenv flask` and then `source flask/bin/activate` to activate it.

You can then `pip install Flask` or `pip install -r requirements.txt` to download any other modules.

#Navigation
Enter the app at `app.py`.
Find html files in `templates/`. Note that html files apart from `index.html` are build on top of `base.html` which is used as a header/navbar.
Python scripts, used to help build webpages are in the `scripts/` folder. To keep things organised, more subfolders are used along with `__init__.py` files to keep the imports simple and readable.

#Example
In this example, `test1` is used as the placeholder name. The site path `http://localhost/test1/`, the template being called `test1.html` and the 'product id' name 'test1' don't have to share the same name. 
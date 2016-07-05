import os

# ----- TORNADO SETTINGS -----

ABSOLUT_PATH = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = ABSOLUT_PATH(ROOT, 'static')

TORNADO_SETTINGS = {
    'static_path': STATIC_ROOT  # The path of the static files (such as html, javascript, images, etc.) to send to front end
}
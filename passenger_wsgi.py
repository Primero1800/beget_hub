import sys
import os

INTERP = os.path.join(os.path.dirname(__file__), 'venv', 'bin', 'python3')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hub_config.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

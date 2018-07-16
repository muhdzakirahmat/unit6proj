"""
python import.py export.zip challenges,teams,both,metadata
"""
from Unit6 import create_app
from Unit6.utils import import_ctf

import sys

app = create_app()
with app.app_context():
    if len(sys.argv) == 3:
        segments = sys.argv[2].split(',')
    else:
        segments = None

    import_ctf(sys.argv[1], segments=segments)

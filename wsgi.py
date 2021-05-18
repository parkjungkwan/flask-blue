
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from app import create_app

app = application = create_app()

if __name__ == "__main__":
    app.run(debug=True)

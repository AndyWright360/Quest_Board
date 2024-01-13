import os
from quest_board import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        post=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
from flaskr import create_app

if __name__ == "__main__":
    app = create_app("config.py")
    app.run()
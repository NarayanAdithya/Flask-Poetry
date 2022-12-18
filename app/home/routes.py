from app.home import home


@home.route('/', methods=["GET"])
def home_():
    return "Home of Application With Poetry"


@home.route('/<string:name>', methods=['GET'])
def returnname(name):
    return f"{name} was passed in the URL"

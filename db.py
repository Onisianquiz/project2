import mongoengine

host = 'mongodb://admin:admin@cluster0-shard-00-00.od2d3.mongodb.net:27017,cluster0-shard-00-01.od2d3.mongodb.net:27017,cluster0-shard-00-02.od2d3.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-r3o1z2-shard-0&authSource=admin&retryWrites=true&w=majority'
db_name = "project2"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(
        db_name, 
        host='mongodb+srv://admin:admin@cluster0.od2d3.mongodb.net/project2?retryWrites=true&w=majority',
        username='admin',
        password='admin'
    )
    
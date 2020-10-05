from flask import Flask , request
from  flask_restful import Resource, Api
from flask_jwt import JWT , jwt_required
from appJwt import authenticate, identity
app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app,authenticate,identity) # /auth


#in mempry databases
items = []

# need and create

#get(item is demanded by the server)
class Item(Resource):
    @jwt_required()
    def get(self,name):
        item = next((filter(lambda x: x['name'] == name,items )),None)

        return {'item':item},200 if item  else 404

    # post(item is delivered to the server to store in database)
    def post(self,name):
        if(next((filter(lambda x: x['name'] == name, items)), None)):
            return {'message':"An item with name '{}' already exists.".format(name)},400


        #Json Payload from the request

        data= request.get_json()

        item = {"name":name, "price":data['price']}
        items.append(item)
        return item , 201


class ItemList(Resource):
    def get(self):
        return {'items':items}


api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList,'/items')
app.run(port = 5000, debug=True)




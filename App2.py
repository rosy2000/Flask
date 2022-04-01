from flask import Flask,request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = [
    {
        'name' : 'Top',
        'price': 20,
        'discount':2
    }
]
class Item(Resource):
    def get(self,name):
        for item in items:
            if(item['name'] == name):
                return item
        return 404
            
    def post(self,name):
        data = request.get_json()
        for item in items:
            if(item['name'] == name):
                return "Item already exists!" 
        new_item = {'name':name,'price':data['price'],'discount':data['discount']}
        items.append(new_item)
        return new_item,201
        
    def put(self,name):
        data = request.get_json()
        for item in items:
            if(item['name'] == name):
                item['price'] = data['price']
                item['discount'] = data['discount']
                return item,201
        return 404
    
    def delete(self,name):
        for item in items:
            if(item['name'] == name):
                items.remove(item)
                return f'Successful deleted {name}'
        return 404
            
class CompleteItem(Resource):
    def get(self):
        return items
    

api.add_resource(Item,'/item/<string:name>')
api.add_resource(CompleteItem,'/items')

app.run(port=1234)

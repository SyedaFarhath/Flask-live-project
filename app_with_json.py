
from flask import Flask, jsonify,request
import json,uuid

app = Flask(__name__)

# getter for all books
@app.route('/books',methods=['GET'])
def get_books():
    with open('data.json') as f:
        return json.loads(f.read())
    
#  getting only a particular book
@app.route("/books/<int:bookid>",methods=['Get'])   
def get_onebook(bookid):
    with open('data.json') as f:
        current_books = json.loads(f.read())
    for i in current_books:
        if i["id"] == bookid:
            # return i["title"]
            return jsonify(i)
    else:
        return jsonify({"message": "Book not found"}),404
    
class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)
        return super().default(obj)
  
# inputting new data  
@app.route('/books',methods=['POST'])
def create_book():
    with open('data.json') as f:
        current_books = json.loads(f.read())
    data = request.get_json()
    current_books.append({"id":uuid.uuid4(),"title":data["title"]})
    with open('data.json','w') as f:
        json.dump(current_books,f,cls=UUIDEncoder)
    return jsonify({"message": "succcesfully added"}),201

# updating data  
@app.route('/books/<string:bookid>',methods=['PUT'])
def update_book(bookid):
    with open('data.json') as f:
        current_books = json.loads(f.read())
    data = request.get_json()
    for i in current_books:
        if i['id']== bookid:
           i['title'] = data['title']
    with open('data.json','w') as f:
        json.dump(current_books,f,cls=UUIDEncoder)       
    return jsonify({"message": "Book successfully update"}), 201

# deleting book
@app.route('/books', methods=['DELETE'])
def delete_book():
    with open('data.json') as f:
        current_books = json.loads(f.read())
    data = request.get_json()
    for i in current_books:
      if i['title']==data['title']:
        current_books.remove(i)
    with open('data.json','w') as f:
        json.dump(current_books,f,cls=UUIDEncoder)
    return jsonify({"message": "Book successfully deleted"}), 201

            
if __name__ == "__main__":  
    app.run(debug=False, host="172.18.214.34")

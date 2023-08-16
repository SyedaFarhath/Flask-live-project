# from flask import Flask, jsonify,request

# app = Flask(__name__)

# books=[{"id":1,"title":"Book 1"},
#        {"id":2,"title":"Book 2"},
#        {"id":3,"title":"Book 3"},
#        {"id":4,"title":"Book 4"}
#        ]

# @app.route("/books",methods=['Get'])
# def get_books():
#     return books

# @app.route("/books/<int:bookid>",methods=['Get'])
# def get_book(bookid):
#     for i in books:
#         if i["id"] == bookid:
#             # return i["title"]
#             return jsonify(i)
#     else:
#         return jsonify({"message": "Book not found"}),404
    
# @app.route('/books',methods=['Post'])
# def create_book():
#     data = request.get_json()
#     books.append({"id":len(books)+1, 'title':data['title']})
#     return jsonify({"message": "Book sucesfully added"}), 201
        
# # @app.route('/books',methods=['Delete'])
# # def delete_book():
# #     data = request.get_json()
# #     for i in books:
# #         if i['title']==data['title']:
# #             books.remove(i)
# #     return jsonify({"message": "Book sucesfully deleted"}), 201  # here you have to give body in postman

# @app.route('/books/<string:title>',methods=['DELETE'])
# def delete_book(title):
#     for i in books:
#         if i['title']==title:
#             books.remove(i)
#             return jsonify({"message": "Book sucesfully deleted"}), 201  # this is the param approach
#     else:
#             return jsonify({"message": "Book not found"}),404
        
# if __name__ == "__main__":
#     app.run(debug=False,host="172.18.210.163")

from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "Book 1"},
    {"id": 2, "title": "Book 2"},
    {"id": 3, "title": "Book 3"},
    {"id": 4, "title": "Book 4"}
]

@app.route("/books", methods=['GET'])
def get_books():
    return jsonify(books)

@app.route("/books/<int:bookid>", methods=['GET'])
def get_book(bookid):
    for i in books:
        if i["id"] == bookid:
            return jsonify(i)
    return jsonify({"message": "Book not found"}), 404

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    books.append({"id": len(books) + 1, 'title': data['title']})
    return jsonify({"message": "Book successfully added"}), 201

@app.route('/books/<string:title>', methods=['DELETE'])
def delete_book(title):
    for i in books:
        if i['title'] == title:
            books.remove(i)
            return jsonify({"message": "Book successfully deleted"}), 201
    return jsonify({"message": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="172.18.210.163")

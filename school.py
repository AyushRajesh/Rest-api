from flask import Flask, request, jsonify
import pymysql
import json

app=Flask(__name__)

def db_connection():
    conn=None
    try:
        conn=pymysql.connect(
            host= 'localhost',
            database= 'test',
            user= 'root',
            password= '',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    except pymysql.Error as e:
        print(e)
    return conn

# books_list=[
#     {
#         "id":0,
#         "author":"Chinua Achebe",
#         "language":"English",
#         "title":"Things Fall Apart",
#     },
#     {
#         "id":1,
#         "author":"Hans Christian Andersen",
#         "language":"Danish",
#         "title":"Fairy tales",
#     },
#     {
#         "id":2,
#         "author":"xyz",
#         "language":"Hindi",
#         "title":"ABC",
#     },
#     {
#         "id":3,
#         "author":"Chetan Baghat",
#         "language":"Hindi",
#         "title":"Two States",
#     }
# ]

@app.route('/books', methods=['GET','POST'])
def books():
    conn=db_connection()
    cursor=conn.cursor()

    if request.method=='GET':
        cursor.execute("SELECT * FROM book")
        books=[
            dict(id=row['id'], author=row['author'], language=row['language'], title=row['title'])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
         # if len(books_list)>0:
            # return jsonify(books_list)
        # else:
            # 'Nothing Found', 404
    if request.method=='POST':
        new_author=request.form['author']
        new_lang=request.form['language']
        new_title=request.form['title']
        # iD=books_list[-1]['id']+1
        # sql= f"INSERT INTO book(author, language, title)) VALUES(%s, %s, %s)"
        cursor.execute("INSERT INTO book (author, language, title) VALUES(%s, %s, %s)", (new_author, new_lang, new_title,))
        conn.commit()
        return "Book details created successfully"

    # new_obj={
    #     'id':iD,
        # 'author':new_author,
        # 'language':new_lang,
        # 'title':new_title
    # }
    # books_list.append(new_obj)
    # return jsonify(books_list),201
@app.route('/book/<int:id>', methods=['GET','PUT','DELETE'])
def single_book(id):
    conn=db_connection()
    cursor=conn.cursor()
    book=None
    if request.method=='GET':
        # for book in books_list:
        #     if book['id']== id:
                # return jsonify(book)
            # pass
       cursor.execute("SELECT * FROM book WHERE id=%s",(id,))
       rows=cursor.fetchall()
       for r in rows:
           book=r
       if book is not None:
           return jsonify(book), 200
       else:
           return "No Book record for this id.", 404

    if request.method=='PUT':
        try:
            # if book['id']==id:
            author=request.form['author']
            language=request.form['language']
            title=request.form['title']

            # sql = f"UPDATE book SET author=%s, language=%s, title=%s WHERE id=%s"
            cursor.execute("UPDATE book SET author=%s, language=%s, title=%s WHERE id=%s",(author, language, title, id,))
            conn.commit()
            updated_book = {
                'id': id,
                'author': book['author'],
                'language': book['language'],
                'title': book['title']
            }
        except:
            return "Book with id {} has been updated successfully".format(id)
            return jsonify(updated_book)
    if request.method=='DELETE':
        sql="""DELETE FROM book WHERE id=%s"""
        cursor.execute(sql,(id))
        conn.commit()
        return "The book with id: {} has been deleted.".format(id), 200
        # for index, book in enumerate(books_list):
        #     if book['id']==id:
                # books_list.pop(index)
                # return jsonify(books_list)

if __name__=='__main__':
    app.run(debug=True)
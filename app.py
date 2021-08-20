from flask import Flask, request

app = Flask(__name__)

from users import users

# Testing Route
@app.route('/test', methods=['GET'])
def test():
    return {"message": "test running"}

#Get Data Route
@app.route('/users', methods=['GET'])
def getUsers():
    return {"usuarios": users}

#Get Data for ID Route
@app.route('/users/<int:id>', methods=['GET'])
def getUserId(id):
    print(id)
    return 'received ID'

#Get Data for Name Route
#@app.route('/users/<string:userName>', methods=['GET'])
#def getUserName(userName):
  #  print(userName)
  #  return 'received Name'

#Get Data userFound Route (Find User by Name)
@app.route('/users/<string:userName>', methods=['GET'])
def getUser(userName):
    userFound = [user for user in users if user['name']== userName]
    if (len(userFound)>0):
        return {"user": userFound[0]}
    return {"message": "User not found"}

#POST test
@app.route('/test', methods=['POST'])
def addTest():
    print(request.json)
    return 'received'

#POST Data to users (Create User)
@app.route('/users', methods=['POST'])
def addUser():
    new_user = {
        "name": request.json["name"],
        "lastName": request.json["lastName"],
        "age": request.json["age"]
    }
    users.append(new_user)
    return {"message": "User added succesfully", "users": users}

#PUT Edit user by user name
@app.route('/users/<string:user_name>', methods=['PUT'])
def editUser(user_name):
    userFound = [user for user in users if user["name"] == user_name ]
    if (len(userFound) >0):
        userFound[0]["name"] = request.json["name"]
        userFound[0]["lasName"] = request.json["lastName"]
        userFound[0]["age"] = request.json["age"]
        return {
            "message": "User Updated",
            "user": userFound[0]
        }
    return {
        "message": "Product Not Found"
    }

#DELETE Delete user by user name
@app.route('/users/<string:user_name>', methods=['DELETE'])
def deleteUser(user_name):
    userFound = [user for user in users if user["name"] == user_name ]
    if (len(userFound) >0):
        users.remove(userFound[0])
        return {
            "message": "User Deleted",
            "user": users
        }
    return {
    "message": "User Not Found"
    }

if __name__== '__main__':
    app.run(debug=True, port=4000)

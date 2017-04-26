from flask import jsonify, request
from model import Users
from common import Common

def init_api(app):
    @app.route('/')
    def index():
        return jsonify(Common.trueReturn(Common, 'Hello Flask!'))

    @app.route('/user', methods=['GET'])
    def getUsers():
        users = Users.getAll(Users)
        output = []
        for user in users:
            output.append(Users.output(Users, user))
        return jsonify(Common.trueReturn(Common, output))


    @app.route('/user/<int:userId>', methods=['GET'])
    def getUser(userId):
        user = Users.get(Users, userId)
        if user is None:
            return jsonify(Common.falseReturn(Common, None, '找不到数据'))
        else:
            return jsonify(Common.trueReturn(Common, Users.output(Users, user)))


    @app.route('/user', methods=['POST'])
    def addUser():
        user_name = request.form.get('user_name')
        user_password = request.form.get('user_password')
        user_nickname = request.form.get('user_nickname')
        user_email = request.form.get('user_email')
        user = Users(user_name=user_name, user_password=user_password, user_nickname=user_nickname, user_email=user_email)
        result = Users.add(Users, user)
        if user.user_id:
            return getUser(user.user_id)
        else:
            return jsonify(Common.falseReturn(Common, None, result))


    @app.route('/user/<int:userId>', methods=['PUT'])
    def updateUser(userId):
        user = Users.get(Users, userId)
        if user is None:
            return jsonify(Common.falseReturn(Common, None, '找不到要修改的数据'))
        else:
            user_name = request.form.get('user_name')
            user_password = request.form.get('user_password')
            user_nickname = request.form.get('user_nickname')
            user_email = request.form.get('user_email')

            user.user_name = user_name
            user.user_password = user_password
            user.user_nickname = user_nickname
            user.user_email = user_email

            result = Users.update(Users)
            return getUser(user.user_id)


    @app.route('/user/<int:userId>', methods=['DELETE'])
    def deleteUser(userId):
        user = Users.get(Users, userId)
        if user is None:
            return jsonify(Common.falseReturn(Common, None, '找不到要删除的数据'))
        else:
            deleteRow = Users.delete(Users, userId)
            user = Users.get(Users, userId)
            if user is None:
                return getUsers()
            else:
                return jsonify(Common.falseReturn(Common, None, '删除失败'))

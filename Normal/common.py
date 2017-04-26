class Common:
    def trueReturn(self, data, msg="请求成功"):
        return {
            "status": 1,
            "data": data,
            "msg": msg
        }

    def falseReturn(self, data, msg="请求失败"):
        return {
            "status": 0,
            "data": data,
            "msg": msg
        }

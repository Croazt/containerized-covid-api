import json
class CustomResponse:
    def success_response(self, res, data, message, code_status=200):
        res.status_code = code_status
        response = {'ok': True, 'data': data, 'message': message}
        return response

    def error_response(self, res, data, message, code_status=404):
        res.status_code = code_status
        response = {'ok': False, 'data': data, 'message': message}
        return response

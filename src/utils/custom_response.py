import json

class CustomResponse:
    def success_response(self, data, message, code_status=200):
        response = {'ok' : True, 'data' : data, 'message' : message}
        return json.dumps(response), code_status, {'ContentType':'application/json'}

    def error_response(self, data, message, code_status=404):
        response = {'ok' : False, 'data' : data, 'message' : message}
        return json.dumps(response), code_status, {'ContentType':'application/json'}
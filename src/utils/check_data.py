import json

from src.utils.custom_response import CustomResponse
def check_if_data_result_is_null(is_type, response, repository, since, upto, individual :bool = False):

    data = repository.get_data(since, upto)
    if len(data.values) < 1:
        return CustomResponse().error_response(response, {}, "No data found!", 400)

    if individual:
        return CustomResponse().success_response(response, data.values[0], "Data for specific "+is_type+" found!",)

    return CustomResponse().success_response(response, data.values, "Data periodically per "+is_type+" found!",)

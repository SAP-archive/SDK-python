from recastai import utils
from recastai import errors
from recastai import response

class Client(object):
  def __init__(self, token=None):
    self.token = token

  def text_request(self, text, **options):
    token = options.get('token') or self.token
    if token is None:
      raise RecastError('Token is missing')

    response = requests.post("{url}/request".format(url=self.url),
        params={'text': text},
        headers={'Authorization': 'Token ' + token}
        )
    if response.status_code != 200:
      raise RecastError(response.message)

    return Response(response.body)

  def file_request(self, file, **options):
    token = options.get('token') or self.token
    if token == None:
      raise RecastError('Token is missing')

    file = open(file, 'rb') if (type(file) is str) else file

    response = requests.post("{url}/request".format(url=self.url),
        files={'voice':file},
        headers={'Authorization': 'Token ' + token}
        )
    if response.status_code != 200:
      raise RecastError(response.message)

    return Response(response.body)

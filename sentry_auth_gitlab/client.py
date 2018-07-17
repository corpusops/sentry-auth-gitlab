from __future__ import absolute_import

from requests.exceptions import RequestException
from sentry import http
from sentry.utils import json

from .constants import API_BASE_URL


class GitLabApiError(Exception):
    def __init__(self, message='', status=None):
        super(GitLabApiError, self).__init__(message)
        self.status = status


class GitLabClient(object):
    def _request(self, path, access_token):
        session = http.build_session()
        headers = {'Authorization': 'Bearer {0}'.format(access_token)}
        url = '{0}/{1}'.format(API_BASE_URL, path.lstrip('/'))

        try:
            req = session.get(url, headers=headers)
        except RequestException as e:
            raise GitLabApiError(unicode(e), status=getattr(e, 'status_code', None))
        return json.loads(req.content)

    def get_user(self, access_token):
        return self._request('user', access_token)

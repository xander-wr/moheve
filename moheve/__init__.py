# noinspection PyUnresolvedReferences
from flask import request
from eve.auth import HMACAuth
from mohawk import Receiver


class MohawkAuth(HMACAuth):
    nonce = True

    def check_auth(self, *args, **kwargs):
        pass

    def seen_nonce(self, sender, nonce, timestamp):
        if not self.nonce:
            return False

        raise NotImplementedError("Please implement the seen_nonce method or set 'nonce' to False.")

    def authorized(self, allowed_roles, resource, method):
        res = True
        # noinspection PyBroadException
        try:
            Receiver(self.check_auth,
                     request.headers.get('Authorization'),
                     request.url,
                     request.method,
                     content=request.get_data(),
                     content_type=request.headers.get('Content-Type'),
                     seen_nonce=self.seen_nonce)
        except NotImplementedError as e:
            raise e
        except Exception:
            res = False

        return res

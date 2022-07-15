from functools import wraps
from typing import Any, Callable, Tuple, Union

from flask import request
from twootfeed import param


def require_token(f: Callable) -> Callable:
    @wraps(f)
    def decorated_function(
        *args: Any, **kwargs: Any
    ) -> Union[Callable, Tuple[str, int]]:
        token = request.args.get('token')
        if not token:
            return 'missing token', 401
        if token != param['feed']['token']:
            return 'invalid token', 403

        return f(*args, **kwargs)

    return decorated_function

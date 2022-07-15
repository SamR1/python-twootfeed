from functools import wraps
from typing import Any, Callable, Tuple, Union

from flask import current_app, request


def require_token(f: Callable) -> Callable:
    @wraps(f)
    def decorated_function(
        *args: Any, **kwargs: Any
    ) -> Union[Callable, Tuple[str, int]]:
        token = request.args.get('token')
        if not token:
            return 'missing token', 401
        if token != current_app.config['FEED_CONFIG']['token']:
            return 'invalid token', 403

        return f(*args, **kwargs)

    return decorated_function

# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from werkzeug.contrib.securecookie import SecureCookie
from flask.sessions import SessionInterface


class SessionMixin(object):
    """Expands a basic dictionary with an accessors that are expected
    by Flask extensions and users for the session.
    """
    new = False
    modified = True

    # permanent
    def _get_permanent(self):
        return self.get('_permanent', False)

    def _set_permanent(self, value):
        self['_permanent'] = bool(value)

    permanent = property(_get_permanent, _set_permanent)
    del _get_permanent, _set_permanent

    # expire
    def setExpire(self, td):
        self._expire_td = timedelta(seconds=td)

    def getExpire(self):
        if not hasattr(self, '_expire_td'):
            self._expire_td = timedelta(days=7)
        return self._expire_td


class SecureCookieSession(SecureCookie, SessionMixin):
    """Expands the session with support for switching between permanent
    and non-permanent sessions.
    """
    pass


class SecureCookieSessionInterface(SessionInterface):
    """The cookie session interface that uses the Werkzeug securecookie
    as client side session backend.
    """
    session_class = SecureCookieSession

    def open_session(self, app, request):
        key = app.secret_key
        if key is not None:
            return self.session_class.load_cookie(request,
                                                  app.session_cookie_name,
                                                  secret_key=key)

    def get_expiration_time(self, app, session):
        if session.permanent:
            return None
        else:
            return datetime.utcnow() + session.getExpire()

    def save_session(self, app, session, response):
        expires = self.get_expiration_time(app, session)
        domain = self.get_cookie_domain(app)
        path = self.get_cookie_path(app)
        httponly = self.get_cookie_httponly(app)
        secure = self.get_cookie_secure(app)
        if session.modified and not session:
            response.delete_cookie(app.session_cookie_name, path=path,
                                   domain=domain)
        else:
            session.save_cookie(response, app.session_cookie_name, path=path,
                                expires=expires, httponly=httponly,
                                secure=secure, domain=domain)



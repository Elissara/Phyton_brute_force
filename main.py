import generators
import queries
import logics

logics.first_password_then_login_logic(
    login_generator=generators.ListGenerator(['admin', 'jack', 'cat']),
    password_generator=generators.BadPasswordGenerator(),
    query=queries.local_server
)

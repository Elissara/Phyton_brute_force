

def simple_logic(login_generator, password_generator, query):
    login = login_generator.next()
    if login is None:
        return

    while True:
        password = password_generator.next()
        if password is None:
            break

        if query(login, password):
            print ('SUCCESS', login, password)
            return

# def first_login_then_password_logic(login_generator, password_generator, query, limit=1000):
#     while True:
#         login = login_generator.next()
#         if login is None:
#             return
#         password_generator.reset()
#
#         for step in range(limit):
#             password = password_generator.next()
#             if password is None:
#                 break
#
#             if query(login, password):
#                 print ('SUCCESS', login, password)
#                 break

def first_password_then_login_logic(login_generator, password_generator, query, limit=1000):
    finished_logins = set()

    while True:
        password = password_generator.next()
        if password is None:
            return

        login_generator.reset()
        for step in range(limit):
            login = login_generator.next()
            if login in finished_logins:
                continue
            if login is None:
                break

            if query(login, password):
                finished_logins.add(login)
                print('SUCCESS', login, password)
                break
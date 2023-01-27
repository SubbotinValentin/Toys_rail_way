menu = [{'title': 'Авторизация', 'url_name': 'login'},
        {'title': 'Регистрация', 'url_name': 'register'},
]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        return context
"""
my_app Django application initialization.
"""

from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'full_python_path.my_app'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'my_app',
                'regex': '^api/my_app/',
                'relative_path': 'api.urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'production': { 'relative_path': 'settings.production' },
                'common': { 'relative_path': 'settings.common' },
            }
        },
        'signals_config': {
            'lms.djangoapp': {
                'relative_path': 'my_signals',
                'receivers': [{
                    'receiver_func_name': 'on_signal_x',
                    'signal_path': 'full_path_to_signal_x_module.SignalX',
                    'dispatch_uid': 'my_app.my_signals.on_signal_x',
                    'sender_path': 'full_path_to_sender_app.ModelZ',
                }],
            }
        },
        'view_context_config': {
            'lms.djangoapp': {
                'course_dashboard': 'my_app.context_api.get_dashboard_context'
            }
        }
    }

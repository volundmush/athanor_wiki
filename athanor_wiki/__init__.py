import os

def init(settings, plugins):

    THIS_DIR = os.path.dirname(os.path.abspath(__file__))

    settings.INSTALLED_APPS.extend([
        'django.contrib.humanize.apps.HumanizeConfig',
        'django_nyt.apps.DjangoNytConfig',
        'mptt',
        'sorl.thumbnail',
        'wiki.apps.WikiConfig',
        'wiki.plugins.attachments.apps.AttachmentsConfig',
        'wiki.plugins.notifications.apps.NotificationsConfig',
        'wiki.plugins.images.apps.ImagesConfig',
        'wiki.plugins.macros.apps.MacrosConfig'
    ])

    settings.WIKI_ACCOUNT_HANDLING = False
    settings.WIKI_ACCOUNT_SIGNUP_ALLOWED = False

    settings.URL_INCLUDES.extend([
        ("notifications/", "django_nyt.urls"),
        ("wiki/", "wiki.urls")
    ])

    settings.TEMPLATES[0]["DIRS"].append(os.path.join(THIS_DIR, "web", "templates"))

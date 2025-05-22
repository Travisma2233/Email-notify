# email_notifier/__init__.py

from .sender import (
    send_notification,
    quick_send_my_notification,
    send_my_default_status_update,
    notify_program_done
)

__version__ = '0.5.0' # 更新版本号以反映修改
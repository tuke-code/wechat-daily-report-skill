import os
from pathlib import Path


HOME_OVERRIDE_ENV = "WECHAT_DAILY_REPORT_HOME"


def get_workspace_root():
    return Path(__file__).resolve().parent.parent


def get_runtime_root():
    override = os.environ.get(HOME_OVERRIDE_ENV)
    if override:
        return Path(override).expanduser().resolve()
    return get_workspace_root()


def get_vendor_dir():
    return get_runtime_root() / "vendor"


def get_decryptor_dir():
    return get_vendor_dir() / "wechat-decrypt"


def get_decrypted_dir():
    return get_decryptor_dir() / "decrypted"


def get_data_dir():
    return get_runtime_root()


def get_reports_dir():
    return get_runtime_root()


def get_default_stats_path():
    return get_runtime_root() / "stats.json"


def get_default_text_path():
    return get_runtime_root() / "simplified_chat.txt"


def get_default_report_path():
    return get_runtime_root() / "report.png"


def ensure_runtime_dirs():
    for path in (get_runtime_root(), get_vendor_dir()):
        path.mkdir(parents=True, exist_ok=True)

import os
import tempfile
import unittest
from importlib import import_module
from pathlib import Path
from unittest.mock import patch


class RuntimePathsTests(unittest.TestCase):
    def test_runtime_paths_default_to_workspace_root(self):
        runtime_paths = import_module("scripts.runtime_paths")
        runtime_root = runtime_paths.get_runtime_root()
        workspace_root = runtime_paths.get_workspace_root()
        self.assertEqual(runtime_root, workspace_root)
        self.assertEqual(runtime_paths.get_decryptor_dir(), workspace_root / "vendor" / "wechat-decrypt")
        self.assertEqual(runtime_paths.get_decrypted_dir(), workspace_root / "vendor" / "wechat-decrypt" / "decrypted")
        self.assertEqual(runtime_paths.get_default_stats_path(), workspace_root / "stats.json")
        self.assertEqual(runtime_paths.get_default_text_path(), workspace_root / "simplified_chat.txt")
        self.assertEqual(runtime_paths.get_default_report_path(), workspace_root / "report.png")

    def test_runtime_paths_follow_home_override(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch.dict(os.environ, {"WECHAT_DAILY_REPORT_HOME": tmpdir}, clear=False):
                runtime_paths = import_module("scripts.runtime_paths")

                runtime_root = runtime_paths.get_runtime_root()
                self.assertEqual(runtime_root, Path(tmpdir).resolve())
                self.assertEqual(runtime_paths.get_decryptor_dir(), runtime_root / "vendor" / "wechat-decrypt")
                self.assertEqual(runtime_paths.get_decrypted_dir(), runtime_root / "vendor" / "wechat-decrypt" / "decrypted")
                self.assertEqual(runtime_paths.get_default_stats_path(), runtime_root / "stats.json")
                self.assertEqual(runtime_paths.get_default_text_path(), runtime_root / "simplified_chat.txt")
                self.assertEqual(runtime_paths.get_default_report_path(), runtime_root / "report.png")


if __name__ == "__main__":
    unittest.main()

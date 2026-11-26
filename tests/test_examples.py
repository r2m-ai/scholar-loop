"""The free example scripts listed in the README must keep running: no model key, no optional engine."""
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
FREE = ["quickstart.py", "ideation_demo.py", "governed_campaign.py", "writing_demo.py"]

pytestmark = pytest.mark.skipif(not EXAMPLES.is_dir(), reason="no examples in this copy")


@pytest.mark.parametrize("script", FREE)
def test_free_example_runs_to_the_end(script):
    done = subprocess.run([sys.executable, str(EXAMPLES / script)], cwd=ROOT, capture_output=True,
                          text=True, encoding="utf-8", errors="replace", timeout=300)
    assert done.returncode == 0, (done.stdout + done.stderr)[-2000:]
    assert done.stdout.strip()

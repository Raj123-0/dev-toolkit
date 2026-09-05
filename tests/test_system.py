from toolkit.system import get_system_summary

def test_system_summary():
    summary = get_system_summary()
    assert "platform" in summary
    assert "python_version" in summary
    assert summary["cpu_count"] >= 1

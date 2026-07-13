from rviz_mcp.backend import get_backend
from rviz_mcp.backend.mock import MockBackend
from rviz_mcp.config import set_mode


def test_seed_and_displays():
    b = MockBackend()
    s = b.seed_demo()
    assert s["ok"] is True
    displays = b.list_displays()
    assert any(d["name"] == "Grid" for d in displays)
    assert b.doctor()["ok"] is True


def test_add_frame_view_shot():
    b = MockBackend()
    b.seed_demo()
    add = b.add_display("PointCloud", "rviz_default_plugins/PointCloud2", "/points")
    assert add["ok"] is True
    assert b.set_fixed_frame("base_link")["fixed_frame"] == "base_link"
    assert b.set_view(distance=5.0)["ok"] is True
    shot = b.screenshot("out.png")
    assert shot["path"] == "out.png"
    assert b.remove_display("PointCloud")["ok"] is True


def test_get_backend_mock():
    set_mode("mock")
    assert get_backend().name == "mock"

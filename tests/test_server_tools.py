from rviz_mcp import server as srv


def test_tools_registered():
    assert callable(srv.rviz_doctor)
    assert callable(srv.rviz_add_display)
    assert "mock" in srv.rviz_mode()

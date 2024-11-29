def pytest_collection_modifyitems(session, config, items):
    for item in items:
        for marker in item.iter_markers(name="testsuite_id"):
            testsuite_id = marker.args[0]
            item.user_properties.append(("testsuite_id", testsuite_id))
from check_site_linux import site_is_not_vulnerable


def test_site_vulnerability(site):
    assert site_is_not_vulnerable(site), f'Site {site} is vulnerable'
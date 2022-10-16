# -*- coding: utf-8 -*-
def pkg_is_installed(host):
    package = host.package('nginx')

    assert package.is_installed


def test_service_is_running(host):
    service = host.service('nginx')

    assert service.is_running
    assert service.is_enabled

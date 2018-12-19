import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_redis_local_port(host):
    local_port = host.socket("tcp://127.0.0.1:6379")
    assert local_port.is_listening


def test_prometheus_config(host):
    config = host.run("redis-cli -p 6379 ping")
    assert config.rc == 0

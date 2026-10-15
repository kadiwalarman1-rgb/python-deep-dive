import pytest

from devops_ai.monitoring.docker_monitor import DockerMonitor


def test_docker_monitor_rejects_unbounded_container_count():
    with pytest.raises(ValueError, match="max_containers"):
        DockerMonitor().list_statuses(max_containers=1000)

from unittest.mock import MagicMock

from siteprobe.config import TOPIC_AVAILABILITY, TOPIC_CONTENT
from siteprobe.probe import process


def test_process_empty_list():
    """Test process() with an empty list of targets."""
    producer = MagicMock()
    process(producer, [])
    producer.send.assert_not_called()


def test_process_availability_single_target(mocker):
    """Test process() with a single availability target."""
    producer = MagicMock()
    targets = [{"url": "https://example.com"}]
    mocker.patch("siteprobe.probe.check_site", return_value=(0.0, 200, True))
    process(producer, targets)
    producer.send.assert_called_once_with(
        TOPIC_AVAILABILITY, b"https://example.com,0.0,200"
    )


def test_process_content_single_target(mocker):
    """Test process() with a single content target."""
    producer = MagicMock()
    targets = [{"url": "https://example.com", "regex pattern": "Example Domain"}]
    mocker.patch("siteprobe.probe.check_site", return_value=(0.0, 200, True))
    process(producer, targets)
    producer.send.assert_called_with(TOPIC_CONTENT, b"https://example.com,True")

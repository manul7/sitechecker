from unittest.mock import MagicMock

from siteprobe.config import ARG_AVAIL, ARG_CONTENT
from siteprobe.keeper import process


def test_process_empty_message():
    conn = MagicMock()
    consumer = MagicMock()
    message = MagicMock()
    message[0].value.decode.return_value = ""
    consumer.poll.return_value.values.return_value = [message]
    process(conn, consumer, ARG_AVAIL)
    conn.cursor().execute.assert_not_called()


def test_process_new_format():
    """Validate handling unsupported messages"""
    conn = MagicMock()
    consumer = MagicMock()
    message = MagicMock()
    message[0].value.decode.return_value = "1,2,3,4,5"
    consumer.poll.return_value.values.return_value = [message]
    process(conn, consumer, ARG_AVAIL)
    conn.cursor().execute.assert_not_called()


def test_process_avail_message():
    """Validate happy path for availability messages"""
    conn = MagicMock()
    consumer = MagicMock()
    message = MagicMock()
    message[0].value.decode.return_value = "1,2,3"
    consumer.poll.return_value.values.return_value = [message]
    process(conn, consumer, ARG_AVAIL)
    conn.commit.assert_called_once()


def test_process_content_message():
    """Validate happy path for content messages"""
    conn = MagicMock()
    consumer = MagicMock()
    message = MagicMock()
    message[0].value.decode.return_value = "1,2"
    consumer.poll.return_value.values.return_value = [message]
    process(conn, consumer, ARG_CONTENT)
    conn.commit.assert_called_once()

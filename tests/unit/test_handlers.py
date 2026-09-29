# -*- coding: utf-8 -*-

import logging

import pytest

from logging_loki.handlers import LokiHandler

handler_url: str = "https://example.net/loki/api/v1/push"


def create_record() -> logging.LogRecord:
    """Create test logging record."""
    log = logging.Logger(__name__)
    return log.makeRecord(
        name="test",
        level=logging.WARNING,
        fn="",
        lno="",
        msg="Test",
        args=None,
        exc_info=None,
    )


def test_handle_error_reraises_by_default(monkeypatch):
    """Without suppress_errors, the standard logging error handling still runs."""
    handler = LokiHandler(url=handler_url, version="1")
    handler.emitter = object.__new__(type(handler.emitter))
    handler.emitter.close = lambda: None

    calls = []
    monkeypatch.setattr(logging.Handler, "handleError", lambda _self, record: calls.append(record))

    record = create_record()
    handler.handleError(record)

    assert calls == [record]


def test_handle_error_suppressed_skips_default_error_reporting(monkeypatch):
    """With suppress_errors=True, the noisy '--- Logging error ---' dump is skipped."""
    handler = LokiHandler(url=handler_url, version="1", suppress_errors=True)
    closed = []
    handler.emitter.close = lambda: closed.append(True)

    calls = []
    monkeypatch.setattr(logging.Handler, "handleError", lambda _self, record: calls.append(record))

    record = create_record()
    handler.handleError(record)

    assert closed == [True]
    assert calls == []


def test_emit_failure_does_not_raise_when_suppressed():
    """emit() swallows delivery failures without raising when suppress_errors=True."""
    handler = LokiHandler(url=handler_url, version="1", suppress_errors=True)

    def boom(record, line):
        msg = "Unexpected Loki API response status code: 405"
        raise ValueError(msg)

    handler.emitter = boom
    handler.emitter.close = lambda: None

    record = create_record()
    # Should not raise and should not print to stderr.
    handler.emit(record)


def test_suppress_errors_defaults_to_false():
    handler = LokiHandler(url=handler_url, version="1")
    assert handler.suppress_errors is False


@pytest.mark.parametrize("suppress_errors", [True, False])
def test_suppress_errors_stored_on_handler(suppress_errors):
    handler = LokiHandler(url=handler_url, version="1", suppress_errors=suppress_errors)
    assert handler.suppress_errors is suppress_errors

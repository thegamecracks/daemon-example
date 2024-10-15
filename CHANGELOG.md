# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- `thedaemon.daemonize()`
  - Allow passing any sequence to `win_args=`
  - On Unix, make `win_args=` an optional argument
  - On Windows, raise `ValueError` if `win_args` is empty

### Fixed

- Ensure that selector is closed when daemon exits

## [1.1.0] - 2024-10-15

### Added

- `start --no-daemon` flag to skip daemonization

### Fixed

- (Windows) Long timeouts on commands when daemon was offline
  - This was due to Windows taking a while to refuse connections.
    On Windows, client connection attempts will now timeout after 100ms.
- Actually close sockets on server
  - This resulted in high CPU usage from polling sockets that were shut down
    by their clients.

## [1.0.0] - 2024-10-15

This is the first release, implementing an installable Python package with
three commands, `thedaemon start`, `thedaemon ping`, and `thedaemon stop`.

The daemon serves a socket server on port 21365 to both allow IPC and prevent
multiple daemon processes from serving at the same time.

Daemonization is implemented with double-forking on Unix, and detached processes
on Windows.

[Unreleased]: https://github.com/thegamecracks/theticketbot/compare/v1.1.0...main
[1.1.0]: https://github.com/thegamecracks/theticketbot/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/thegamecracks/theticketbot/releases/tag/v1.0.0

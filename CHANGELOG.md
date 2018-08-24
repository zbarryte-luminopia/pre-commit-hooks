# Changelog

## v0.0.9

Case-insensitive checks on license names for `--explicit-packages`.

## v0.0.8

Ignore utf-8 decode errors in `enforce-action-comments` to allow non-utf-8 files (e.g. images) to pass the check.

## v0.0.5

Make `enforce-action-comments` configurable and make defaults more sensible.

Remove undocumented, and incorrectly implemented, `list-action-comments` hook.

## v0.0.4

Fix `yarn-licenses` file reading issue for large yarn.lock files

Trim option segments for `explicit-packages` command line argument

## v0.0.3

Add hook for checking node packages against a whitelist (`yarn-licenses`)

## v0.0.2

Add hook for ensuring large binary files are LFSed (`lfs-large-files`)

## v0.0.1

Add hook for enforcing action commits (`enforce-action-comments`)

# Luminopia's pre-commit-hooks

Repository storing various hooks to be used with the Yelp [pre-commit](https://pre-commit.com) framework.

## Hooks

### LFS Large Files

`lfs-large-files`

This hook detects binary files over a certain size threshold and ensures that the are being tracked by LFS. This will only apply to binary files, as detected using an algorithm similar to Git's binary detection (looking for null bytes within the first 8 KiB into a file).

| Argument              | Default | Description |
|-----------------------|---------|-------------|
| --maximum-binary-size | 524288  | What is the size threshold at which files must be tracked by LFS |

NOTE: this currently relies on porcelain commands from git-lfs to operate and may be prone to breakages.

### Yarn Licenses

`yarn-licenses`

This hook analyzes the licenses of all the node packages managed by the yarn.lock file to ensure that they are compliant with a list of approved licenses. This hook also provides extra arguments for explicitly whitelisting certain package's license with optional version lock.

| Argument            | Default                                  | Description |
|---------------------|------------------------------------------|-------------|
| --approved-licenses | MIT,BSD-3-Clause,Public Domain,Unlicense | A comma delimited list of whitelisted SPDX licenses |
| --explicit-packages | None                                     | A comma delimited list of packages and their approved license (and an optional version), in the form PACKAGE_NAME::SPDX_LICENSE::VERSION, such as left-pad::CC-BY-3 |

## WIP Hooks

### Enforce Action Comments

`enforce-action-comments`

This hook ensures that there are no comments that demand immediate action. Currently, this hook looks for `TODO NOW` entries in the source code and fails a commit if any exist.

## Other Resources

* https://github.com/pre-commit/pre-commit-hooks
* https://github.com/detailyang/pre-commit-shell

## Changelog

*v0.0.4*

Fix `yarn-licenses` file reading issue for large yarn.lock files

Trim option segments for `explicit-packages` command line argument

*v0.0.3*

Add hook for checking node packages against a whitelist (`yarn-licenses`)

*v0.0.2*

Add hook for ensuring large binary files are LFSed (`lfs-large-files`)

*v0.0.1*

Add hook for enforcing action commits (`enforce-action-comments`)

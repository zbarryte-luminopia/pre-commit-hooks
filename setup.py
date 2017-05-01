from setuptools import find_packages
from setuptools import setup


setup(
    name='luminopa_pre_commit_hooks',
    description='Some custom pre-commit-hooks used by Luminopia',
    url='https://github.com/luminopia/pre-commit-hooks',
    version='0.0.4',

    author='Alex Wendland',
    author_email='alex@luminopia.com',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[ ],
    entry_points={
        'console_scripts': [
            'enforce-action-comments = pre_commit_hooks.enforce_action_comments:main',
            'lfs-large-files = pre_commit_hooks.lfs_large_files:main',
            'list-action-comments = pre_commit_hooks.list_action_comments:main',
            'yarn-licenses = pre_commit_hooks.yarn_licenses:main'
        ],
    },
)

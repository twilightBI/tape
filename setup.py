# -*- coding: utf-8 -*-
from setuptools import setup


with open('README.md', 'r') as rf:
    README = rf.read()

with open('LICENSE', 'r') as lf:
    LICENSE = lf.read()

setup(
    name='tape_proteins',
    version='0.1',
    description="Repostory of Protein Benchmarking and Modeling",
    author="Roshan Rao, Nick Bhattacharya, Neil Thomas",
    author_email='roshan_rao@berkeley.edu, nickbhat@berkeley.edu, nthomas@berkeley.edu',
    url='https://github.com/rmrao/tape-pytorch',
    license=LICENSE,
    keywords=['Proteins', 'Deep Learning', 'Pytorch', 'TAPE'],
    install_requires=[
        'torch>=1.0',
        'tqdm',
        'tensorboardX',
        'scipy',
        'lmdb',
    ],
    entry_points={
        'console_scripts': [
            'tape-train = tape.main:run_train',
            'tape-train-distributed = tape.main:run_train_distributed',
            'tape-eval = tape.main:run_eval',
            'tape-embed = tape.main:run_embed',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
)

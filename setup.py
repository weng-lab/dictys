#!/usr/bin/python3

pkgname="dictys"
pkgnamefull="Dictys"
version=[0,1,0]
url="https://github.com/pinellolab/"+pkgname
author="Lingfei Wang, Nikolaos Trasanidis, Luca Pinello"
author_email="Lingfei.Wang.github@outlook.com, ntrasanidis@mgh.harvard.edu, lpinello@mgh.harvard.edu"
packages=['docstring2argparse','dictys','dictys.net','dictys.utils','dictys.plot']

def pkg_setup():
	from setuptools import setup
	from os import path
	pkgnameu=pkgname[0].upper()+pkgname[1:].lower()
	with open(path.join(path.abspath(path.dirname(__file__)),'README.rst'),encoding='utf-8') as f:
		long_description=f.read()
	setup(name=pkgname,
		version='.'.join(map(str,version)),
		author=author,
		author_email=author_email,
		description=pkgnamefull,
		long_description=long_description,
		long_description_content_type='text/x-rst',
		url=url,
		scripts=['bin/dictys','bin/dictys_helper'],
		install_requires=['numpy','pandas','docutils','h5py','pyro-ppl==1.6.0','scipy','networkx','pybedtools','pyDNase','threadpoolctl','joblib','torch','matplotlib','adjustText','jupyter'],
		classifiers=[
			'Development Status :: 4 - Beta ',
			'Environment :: Console',
			'Environment :: GPU :: NVIDIA CUDA',
			'Framework :: Jupyter',
			'Framework :: Matplotlib',
			'Intended Audience :: Developers',
			'Intended Audience :: End Users/Desktop',
			'Intended Audience :: Science/Research',
			'License :: OSI Approved :: GNU Affero General Public License v3',
			'Operating System :: OS Independent',
			'Programming Language :: Python :: 3.9',
			'Topic :: Scientific/Engineering :: Bio-Informatics',
			'Topic :: Scientific/Engineering :: Visualization',
		],
		python_requires='>=3.9',
		packages=packages,
		package_dir={x:path.join('src',*x.split('.')) for x in packages},
		package_data={
			'dictys':
				['scripts/*.'+x for x in 'sh,py'.split(',')]+
				['scripts/helper/*.'+x for x in 'sh,py'.split(',')]+
				['scripts/makefiles/*.'+x for x in 'mk'.split(',')],
		}
	)

pkg_setup()

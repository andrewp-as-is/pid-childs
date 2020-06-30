import setuptools

setuptools.setup(
    name='pid-childs',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/pid-childs']
)

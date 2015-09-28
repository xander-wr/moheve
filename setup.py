from setuptools import setup

setup(name="moheve",
      version="0.1",
      description="Mohawk authentication for Eve APIs",
      keywords="python-eve mohawk moheve",
      url="https://github.com/xander-wr/moheve/",
      author="https://github.com/xander-wr/",
      author_email="hello@xander.frl",
      license="MIT",
      packages=['moheve'],
      install_requires=['mohawk'],
      classifiers=[
          'Framework :: Flask'
      ],
      include_package_data=True,
      zip_safe=False)

import distutils.core

try:
    # to enable "python setup.py develop"
    import setuptools
except ImportError:
    pass

distutils.core.setup(
    name="stormed-amqp",
    version='0.1.1',
    url='http://github.com/paolo-losi/stormed-amqp'
    packages = ["stormed", "stormed.method", "stormed.method.codegen"],
    author="Paolo Losi",
    author_email="paolo.losi@gmail.com",
    license="http://www.opensource.org/licenses/mit-license.html",
    description="native tornadoweb amqp 0-9-1 client implementation",
)

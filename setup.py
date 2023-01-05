from distutils.core import setup, Extension

module1 = Extension('phys',
                    sources = ['col_phys.cpp'])

setup (name = 'phys',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
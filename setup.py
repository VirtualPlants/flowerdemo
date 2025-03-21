# -*- coding: utf-8 -*-
__revision__ = "$Id: setup.py 2456 2010-05-19 13:10:10Z pradal $"

# This Setup script has been commented to ease the writing of your own file. 

# A setup script mainly consist of a call to the setup function of setuptool, 
# that allows to create a distribution archive of a set of python modules 
# grouped in packages (i.e. in directories with an __init__.py file).

# In the context of OpenAlea, this function has been extended by the 
# openalea.deploy module to ease the simultaneaous distribution of binaries
# and libraries.


# In order adapt this script for your package, you have to change the content 
# of metainfo.ini file that is read in the setup.py and to adapt the variables
# defined before the call to setup function, and comment out unused options 
# in the call of the function

import sys
import os

from setuptools import setup, find_packages

# Reads the metainfo file
version = '1.3.0'
release = '1.3'
name = 'VPlants.FlowerDemo'
package = 'flowerdemo'
description= 'Flower Demo for Science Festival.'
long_description= 'Demo to manipulate flowers architecture and genes'
authors= 'Frederic Boudon'
authors_email = 'frederic.boudon@cirad.fr'
url = 'https://github.com/fredboudon/flowerdemo'
license = 'Cecill-C'


#The metainfo files must contains
# version, release, project, name, namespace, pkg_name,
# description, long_description,
# authors, authors_email, url and license
# * note that authors and authors_email have an s even though there is only one author
# * version is 0.7.0 and release 0.7
# * project must be in [openalea, vplants, alinea]
# * name is the full name (e.g., OpenAlea.Starter) whereas pkg_name is only 'starter'

# name will determine the name of the egg, as well as the name of 
# the pakage directory under Python/lib/site-packages). It is also 
# the one to use in setup script of other packages to declare a dependency to this package)
# (The version number is used by deploy to detect UPDATES)


# Packages list, namespace and root directory of packages

# (this will determine the archive content and the names of your modules)
# (with the loop used bellow,all packages,ie all directories with a __init__.py, under pkg_root_dir will be recursively detected and named according to the directory hirearchy)
# (namespace allows you to choose a prefix for package names (eg alinea, openalea,...). 
# (This functionality needs deploy to be installed)
# (if you want more control on what to put in your distribution, you can manually edit the' packages' list 
# (the 'package_dir' dictionary must content the pkg_rootdir and all top-level pakages under it)

pkg_root_dir = 'src'
pkgs = [ pkg for pkg in find_packages(pkg_root_dir) ]
top_pkgs = [pkg for pkg in pkgs if  len(pkg.split('.')) < 2]
packages = pkgs 
package_dir = dict( [('',pkg_root_dir)] + [( pkg, pkg_root_dir + "/" + pkg) for pkg in top_pkgs] )

# List of top level wralea packages (directories with __wralea__.py) 
# (to be kept only if you have visual components)
#wralea_entry_points = ['%s = %s'%(pkg,namespace + '.' + pkg) for pkg in top_pkgs]

# dependencies to other eggs
# (This is used by deploy to automatically downloads eggs during the installation of your package)
# (allows 'one click' installation for windows user)
# (linux users generally want to void this behaviour and will use the dependance list of your documentation)
# (dependance to deploy is mandatory for runing this script)

# scons build-prefix 
#(to be kept only if you contruct C/C++ binaries)




# setup function call
#
setup(
    # Meta data (no edition needed if you correctly defined the variables above)
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    author=authors,
    author_email=authors_email,
    url=url,
    license=license,
    keywords = '',	
    # package installation
    packages= packages,	
    package_dir= package_dir,
    # tell setup not  tocreate a zip file but install the egg as a directory (recomended to be set to False)
    zip_safe= False,


    # Binary installation (if necessary)
    # Define what to execute with scons	
    #scons_scripts=['SConstruct'],
    # Tell deploy where to find libs, includes and bins generated by scons.
    #lib_dirs = {'lib' : build_prefix+'/lib' },
    #inc_dirs = { 'include' : build_prefix+'/include' },
    #bin_dirs = { 'bin' : build_prefix+'/bin' },
    share_dirs = {  'data' : 'data'},

    # Eventually include data in your package
    # (flowing is to include all versioned files other than .py)
    include_package_data = True,
    # (you can provide an exclusion dictionary named exclude_package_data to remove parasites).
    # alternatively to global inclusion, list the file to include   
    #package_data = {'' : ['*.pyd', '*.so'],},
    py_modules = ['fd_gui_postinstall'],

    postinstall_scripts = ['fd_gui_postinstall',],

    # Declare scripts and wralea as entry_points (extensions) of your package 
    entry_points = { 
        #'console_scripts': [
        #       'fake_script = openalea.fakepackage.amodule:console_script', ],
        'gui_scripts': [
              'flowerdemo = flowerdemo.main:main',
              'flowerdemo3 = flowerdemo.main3:main3',],
        #	'wralea': wralea_entry_points
        },
    )



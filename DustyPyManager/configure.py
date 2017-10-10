"""
Handles all configuration of DustyPyManager
"""

import pkg_resources
import configparser

def get_config_resource(resource_pkg, resource_name):
    """Gets Configuration object for resource requested

    Args:
        - resource_pkg (str): The name of the resource sub-package
        - resource_name (str): The name of the ini file (with extension)

    Returns:
        configparser object
    """
        
    resource_pkg = resource_pkg.strip()

    #Check the pkg exists in resources
    if resource_pkg not in ['stream',
                            'wsn',
                            'tests']:
        raise FileNotFoundError("Pkg Resource %s does not exist" % resource_pkg)        
    
    pkg_full = 'DustyPyManager.resources.%s' % resource_pkg
    ini_path = pkg_resources.resource_string(pkg_full,
                                             resource_name)
    # TODO: Handle exception if resource is not found
    # TODO: Handle missing extension

    config = configparser.ConfigParser()
    config.read_string(ini_path.decode('ascii'))

    return config
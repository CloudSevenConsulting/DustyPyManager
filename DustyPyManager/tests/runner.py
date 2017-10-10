"""
Runs all unit tests specified in pkg_resource tests.runner
"""

import sys
import unittest
import importlib
from StringIO import StringIO

from DustyPyManager import configure
from DustyPyManager.cli_tools import cli_stdout, cli_hline

def test_class_loader():
    """
    Loads all the unit test based on package resources
    """

    conf = configure.get_config_resource('tests', 'runner.ini')

    all_test_objs = {}

    for mod in conf.sections():
        module_name = conf[mod]['module']
        kls_name = conf[mod]['kls']

        all_test_objs[kls_name] = importlib.import_module(module_name)

    return all_test_objs

def report_test_failure(fail_item):
    
    traceback = fail_item[1].strip().split('\n')
    msg = ["Test Failure",
           "%s" % fail_item[0],
    ]
    for t in traceback:
        msg.append("\t%s" % t)
    cli_stdout('err', msg)

def main():
    
    cli_hline()

    test_objs = test_class_loader()
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)

    all_errs = []
    all_fails = []
    test_cntr = 0

    for kls, mod in test_objs.iteritems():
        
        cli_stdout("info", "Running unit tests for %s" % kls)

        obj = getattr(mod, kls)
        result = runner.run(unittest.makeSuite(obj))

        test_cntr += 1

        all_errs.extend(result.errors)
        all_fails.extend(result.failures)
        if len(all_errs) + len(all_fails) == 0:
            cli_stdout("good", "%s passed" % kls)
        else:
            cli_stdout("warn", "%s failed" % kls)
        stream.seek(0)
        #print 'Test output\n', stream.read()

    print
    print
    cli_hline()
    cli_hline()
    cli_stdout("info", "TEST RESULTS")
    cli_stdout("debug", "%d Test run" % test_cntr)

    passed = True

    if len(all_errs) > 0:
        passed = False
        cli_stdout("err", "Test errors")
        print all_errs

    if len(all_fails) > 0:
        passed = False
        for fail in all_fails:
            report_test_failure(fail)
    
    if (passed):
        cli_stdout("good", "ALL TESTS SUCCESSFUL")

if __name__ == '__main__':
    main()
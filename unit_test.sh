#!/usr/bin/env bash

# Get full path to the directory that this scripts is in
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# By changing to the directory that this script is in means you no longer need to be in
# the directory to run these tests
cd $DIR
mkdir -p test-reports
pip3 -V

# Some of these tests don't run on integration, because no valid response is returned
# from the mock. Only run the working tests in this script.  All the tests run locally.
# See https://github.com/pallets/werkzeug/issues/618

py.test unit_tests/test_calls.py::TestCalls::test_error_logged unit_tests/test_logging.py::TestLogging::test_error_logged unit_tests/test_calls.py::TestCalls::test_post_json unit_tests/test_general.py::TestGeneral::test_health unit_tests/test_general.py::TestGeneral::test_health_service_check --junitxml=test-reports/TEST-UNIT-flask-app-medium.xml --cov-report term-missing --cov-report=html --cov application

#!/usr/bin/env bash

#env_dir="$JENKINS_HOME/virtualenv/${JOB_NAME// /_}"
env_dir="${WORKSPACE}/virtualenv"
#create and activate a virtualenv
python3 -m venv $env_dir
source $env_dir/bin/activate
#install requirements
echo '**** WHAT IS ALREADY INSTALLED? ****'
#pip freeze
${env_dir}/bin/pip install -r requirements.txt
echo '**** RUNNING UNIT TESTS ****'
${WORKSPACE}/unit_test.sh
echo '**** COMPLETED UNIT TESTS ****'
python_linting=$?
coverage xml
coverage -rm
e_code=$((unit_test_pass + python_linting))
rm -rf $env_dir
exit $e_code
# Set the base image to the base image
FROM lr_base_python_flask:2

# ----
# Put your app-specific stuff here (extra yum installs etc).
# Any unique environment variables your config.py needs should also be added as ENV entries here

ENV APP_NAME transactions-api
ENV TRANSACTION_ADAPTER_URI 'http://transactions-adapter:8080'
ENV TEST_TITLE GR515570
ENV TEST_APPLICATION E991YPW
ENV LOG_LEVEL DEBUG

# Get the python environment ready
# Have this at the end so if the files change, all the other steps
# don't need to be rerun. Same reason why _test is first.
# This ensures the container always has just what is in the requirements files as it will
# rerun this in a clean image.
ADD requirements_test.txt requirements_test.txt
ADD requirements.txt requirements.txt
RUN pip3 install -q -r requirements.txt && \
  pip3 install -q -r requirements_test.txt

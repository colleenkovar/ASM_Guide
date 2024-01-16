In order to create the virtual environment, run the command:
python -m venv /path/to/new/virtual/environment
where venv is the name of the environment

To enable the virtual environment and run the application:
source venv/bin/activate (deactivate - to deactivate)

To install the requirements.txt (Flask) run
pip install -r /path/to/requirements.txt
Or install Flask using 
pip install Flask

Once the virtual environment is running you can run the following to see traces:
DD_SERVICE="testing" DD_ENV=“prod” DD_LOGS_INJECTION=true DD_APPSEC_ENABLED=true ddtrace-run python main.py

Since this script sets the environment variables, you can just run:
ddtrace-run python main.py

Go to http://127.0.0.1:8080/ to view site and collect traces

Once the web-app is running you can run the attack file by running the following in a new terminal:
./attack.sh

What the attack file does is run the following CURL commands to test the endpoints and it will trigger the security rule Security Scanner Detected: https://docs.datadoghq.com/security/default_rules/security-scan-detected/
curl http://127.0.0.1:8080/test -A'dd-test-scanner-log'; 
curl http://127.0.0.1:8080/tests -A'dd-test-scanner-log'; 


Enable APM and ASM docs:
https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-host/?tab=pip
https://docs.datadoghq.com/security/application_security/getting_started/python?tab=dockercli
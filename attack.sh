for ((i=1;i<=200;i++)); 
do
# Target existing service’s routes
curl http://127.0.0.1:8080/test -A dd-test-scanner-log;
# Target non existing service’s routes
curl http://127.0.0.1:8080/tests -A dd-test-scanner-log;
done
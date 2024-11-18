ip=`cat server-ip`

scp -i ~/priv/albino.pem server/serve_input_requests.py ubuntu@$ip:~/

# scp -i ~/priv/albino.pem server/html/* ubuntu@$ip:~/to_html/ && \
# ssh -i ~/priv/albino.pem ubuntu@$ip 'sudo mv to_html/* /var/www/html'
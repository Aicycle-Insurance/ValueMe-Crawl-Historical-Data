ansible-playbook -i inventories/instance.yml --private-key ~/.ssh/id_rsa proxy.yml


ssh -i ~/seta/manhtd6932/crawl-data.pem -n -f ubuntu@13.251.127.34 '/home/ubuntu/.local/bin/proxy --hostname 0.0.0.0 --port 8888 --enable-web-server --plugins proxy.plugin.RedirectToCustomServerPlugin > /dev/null 2>&1 &'
ssh -i ~/seta/manhtd6932/crawl-data.pem -n -f ubuntu@13.250.204.172 '/home/ubuntu/.local/bin/proxy --hostname 0.0.0.0 --port 8888 --enable-web-server --plugins proxy.plugin.RedirectToCustomServerPlugin > /dev/null 2>&1 &'
ssh -i ~/seta/manhtd6932/crawl-data.pem -n -f ubuntu@13.250.42.59 '/home/ubuntu/.local/bin/proxy --hostname 0.0.0.0 --port 8888 --enable-web-server --plugins proxy.plugin.RedirectToCustomServerPlugin > /dev/null 2>&1 &'
ssh -i ~/seta/manhtd6932/crawl-data.pem -n -f ubuntu@54.169.220.42 '/home/ubuntu/.local/bin/proxy --hostname 0.0.0.0 --port 8888 --enable-web-server --plugins proxy.plugin.RedirectToCustomServerPlugin > /dev/null 2>&1 &'

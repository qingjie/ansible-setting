http://codebeautify.org/yaml-validator

brew uninstall ansible
pip install ansible

./ec2.py --list

ansible webservers -m ping

sudo ansible -i ec2.py -u ec2-user us-west-2 -a "pwd"

ansible-playbook upload_to_s3.yaml

ansible -i ec2.py -u ec2-user tag_Environment_staging -m ping


# install apache2 on tag_Environment_production
#ansible-playbook -i ec2.py -u ec2-user webserver.yaml --extra-var="value=production"

#upload and deploy
#ansible-playbook -i ec2.py -u ec2-user upload_and_deploy.yaml --extra-var="value=production"

ansible-playbook new_server.yaml

export ANSIBLE_LIBRARY='/etc/ansible'
ansible -i ec2.py us-west-2 -u ec2-user -m demo -a showname=yes




ansible -i ec2.py -u ec2-user tag_Environment_staging -m ping

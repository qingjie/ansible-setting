#!/usr/bin/python

from ansible.module_utils.basic import *
import os
import socket

def main():
    #Helper to handle grabbing arguments
    module = AnsibleModule(
        argument_spec = dict(
            showname = dict(required=False,type='bool')
        )
    )
    #Grab our ipaddress,albeit not our public one.
    ipaddress=socket.gethostbyname(socket.gethostname())

    #The show name is specified as a bool above. So it' ll handle YES|NO TRUE|FALSE
    if module.params.get('showname'):
        module.exit_json(changed=True, name=os.name, ipaddress=ipaddress)
    else:
        module.exit_json(changed=True, ipaddress=ipaddress)

if __name__ == "__main__":
    main()
    

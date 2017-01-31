# DreamHost.Python.passanger
My DreamHost template for creating a new python sight using the passanger apache module.

## Using this template with DreamHost
1. Setup the subdomain in the DreamHost Control Panel
  * [enable passanger](https://help.dreamhost.com/hc/en-us/articles/216385637-How-do-I-enable-Passenger-on-my-domain-)
  * [Setup ssh into the account (ssh overview)](https://help.dreamhost.com/hc/en-us/articles/216041267-SSH-overview)
2. SSH into the account to compleate the rest of the steps
3. Checkout this repository into a directory matching the subdomain you are setting up
4. Edit `scripts/init_env.sh` (lines 6 to end of file) to install the python modules you application will need
5. Run the script `scripts/init_env.sh` to setup the environment and install the python modules.
  * This can be done anytime to refresh the environment and clean out anything you may have tested
  * [DreamHost python virtualenv and module install](https://help.dreamhost.com/hc/en-us/articles/215489338-Installing-virtualenv-and-custom-modules-in-Python)
6. Test that everything works as it is checked out
7. Remove the myAppModule directory. You will replace this with your own application
8. Add in your own application module
9. Edit `passenger_wsgi.py`
  * [Python WSGI with passanger](https://help.dreamhost.com/hc/en-us/articles/215769548-Passenger-and-Python-WSGI)
10. Change line 49 to include your application module
11. Change line 63 to reflect you application entrypoint
12. Try out your application

## Troubleshooting
* [DreamHost passanger troubleshooting](https://help.dreamhost.com/hc/en-us/articles/216635268-Passenger-troubleshooting)
* Change line 6 of `passenger_wsgi.py` to enable DEBUG. This will output more information to the logfiles `logs/passanger/passenger_wsgi.log`

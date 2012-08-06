healthQuery
===========

A crowdsourced health query service.


Setup Instructions
==================

- `pip install -r requirements.txt`
- `cp healthquery/settings/local.py-dist healthquery/settings/local.py`
- Edit `healthquery/settings/local.py` to set database details
- `./manage.py syncdb`
- `./manage.py migrate`

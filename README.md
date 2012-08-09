healthQuery
===========

A crowdsourced health query service.


Setup Instructions
==================

### Setup `Solr` search engine
- cd /opt/
- Download Solr: `curl -O http://apache.mirrors.tds.net/lucene/solr/3.6.1/apache-solr-3.6.1.tgz`
- Untar download file: `tar xvfz apache-solr-3.6.1.tgz`
- `cd apache-solr-3.6.1/solr/`
- Build Solr example: `ant example`
- Add DRIVE JDBC for PostgreSQL to use Solr DataImportHandler
  - `cd /opt/apache-solr-3.6.1/solr/example/lib/`
  - `wget http://jdbc.postgresql.org/download/postgresql-9.1-901.jdbc4.jar`
  - `cd ..`
- Run Solr: `java -jar start.jar`
- Open `http://127.0.0.1:8983/solr/` in browser, if you see the welcome page, then congratulations.
  You have successfully run Solr.

### Setup `healthQuery`
- `pip install -r requirements.txt`
- `cp healthquery/settings/local.py-dist healthquery/settings/local.py`
- Edit `healthquery/settings/local.py` to set database details
- `./manage.py syncdb`
- `./manage.py migrate`
- Load fixtures: `./manage.py loaddata healthquery/common/fixtures/*.json`
- Build Solr schema and place it in Solr directory:
  `./manage.py build_solr_schema > /opt/apache-solr-3.6.1/solr/example/solr/conf/schema.xml`
- Restart `Solr`
- Build Solr index: `./manage.py rebuild_index`
- Run healthQuery server: `./manage.py runserver 0.0.0.0:8000`

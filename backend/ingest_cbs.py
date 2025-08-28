# backend/ingest_cbs.py
import cbsodata
from models import get_session, SES, Healthcare


def ingest_table_to_db(table_id, year, kind='ses'):
print("Fetching", table_id)
rows = cbsodata.get_data(table_id)
session = get_session()


for r in rows:
pc = r.get('Postcode6') or r.get('Postcode')
if not pc:
continue


if kind == 'ses':
obj = SES(postcode=pc, year=year, data=r)
else:
obj = Healthcare(postcode=pc, year=year, data=r)


session.merge(obj)


session.commit()
session.close()
print("Done")


if __name__ == "__main__":
ingest_table_to_db("83765NED", 2023, kind="ses")
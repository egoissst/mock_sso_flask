Commands to start the server - 
python3.8 -m venv .env
.env/bin/pip install -r pip_req.txt
.env/bin/python hello.py

Flask Application - APIs - 
Add user - 
curl --location --request POST 'http://127.0.0.1:5000/add_user' \
--header 'Content-Type: application/json' \
--data-raw '{"_id":619972072,"uid":"7iorb8tkbhtzqc4on6fu493mn","sso":"7iorb8tkbhtzqc4on6fu493mn@indiatimes.com","GID":792060453888,"F_N":"Priyanka","L_N":"Kansal","F_C":0,"FE_C":0,"GN_C":0}'

Get user - 
http://127.0.0.1:5000/get_user?uid=8df58boq1ekf0x90ja63zjuy3

WebHook Related-
Add-
curl --location --request POST 'http://127.0.0.1:5000/add_forwebHook' \
--header 'Content-Type: application/json' \
--data-raw '{"A_ID": {"$numberLong": "248819"}, "C_D": "1611178479474", "A_K": "C1_stgtestclientid2", "F_ADD": "VU865255@webbamail.com", "A_N": "Commented", "A_D_N": "test user", "C_T": "new2345 oneeee", "A_U_I": "2494918", "tet": "test  article 1", "tesyn": "test article", "teu": "http://timesofindia.indiatimes.com/testing1/articleshow/61450807.cms", "msid": "61450807"}'

Get where id matched-
http://127.0.0.1:5000/get_forwebHook?id=2494918
Get all doc
http://127.0.0.1:5000/getall_forwebHook

TinyDB - 
https://tinydb.readthedocs.io/en/latest/
https://tinydb.readthedocs.io/en/stable/usage.html

Common TinyDB commands - 
db.insert({'type': 'peach', 'count': 3})
db.truncate()
db.all()

import sqlite3

conn =sqlite3.connect('database2.db')
c=conn.cursor()
data=open("testdata.txt","r")
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS database2(question TEXT,option1 TEXT,option2 TEXT,option3 TEXT,answer TEXT)")
def db_entry(q,o1,o2,o3,a):
    c.execute("INSERT INTO database2 (question,option1,option2,option3,answer) VALUES(?,?,?,?,?)",(q,o1,o2,o3,a))
    conn.commit()
def read_from_db():
    c.execute('SELECT * FROM database2')
    ex=c.fetchall()
    for i in ex:
        print(i[0])
        print('1).',i[1])
        print('2).',i[2])
        print('3).',i[3])
        print('answer =',i[4])
create_table()
while(True):

    question=data.readline()
    if question=='':
        break
    option1=data.readline()
    option2=data.readline()
    option3=data.readline()
    anwser=data.readline()
    db_entry(question,option1,option2,option3,anwser)
#print('dfdasfdssssssssssssssssssssssssssssssssssssss')
read_from_db()


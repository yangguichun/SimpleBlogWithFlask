import  unittest
import uuid
from app import db
from app.models import User, Post
from datetime import datetime

class TestModel(unittest.TestCase):
    def test_user_tostring(self):
        username = '那专拍'
        u = User(username='那专拍', email='yang@163.com')
        self.assertEqual(str(u), '<用户名:{}>'.format(username))

    def test_add_specify_name_user(self):
        uid = uuid.uuid1()
        username = 'lisi'.format(uid)
        email = 'lisi@163.com'.format(uid)
        u = User(username=username, email=email)
        u.set_password('123456')
        db.session.add(u)
        db.session.commit()


    def test_add_user(self):
        uid = uuid.uuid1()
        username = '张三{}'.format(uid)
        email = '张三{}@163.com'.format(uid)
        u = User(username=username, email=email)
        db.session.add(u)
        db.session.commit()

    def test_query_user(self):
        print('')
        print('test_query_user')
        users = User.query.all()
        for user in users:
            print(user.id, user.username, user.email)

    def test_add_post(self):
        print('')
        u = User.query.get(10)
        uid = uuid.uuid1()
        p = Post(body='hello，{}， 这里是  {}'.format(datetime.now(), uuid.uuid1()), author=u)
        db.session.add(p)
        db.session.commit()

    def test_query_post_of_specific_user(self):
        print('')
        print('test_query_post_of_specific_user')
        u = User.query.get(1)
        posts = u.posts.all()
        for post in posts:
            print(post.id, post.body, post.timestamp)


    def test_del_all_posts(self):
        posts = Post.query.all()
        for post in posts:
            db.session.delete(post)
        db.session.commit()

    def test_user_password(self):
        u = User(username='zhangsan', email='zhangsan@163.com')
        u.set_password('123456')
        self.assertTrue(u.check_password('123456'))
        self.assertFalse(u.check_password('567890'))

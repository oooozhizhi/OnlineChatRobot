# OnlineChatRobot

## Requirements

* python2.7
* django1.10

## How to Start
1. Set the password of root user in mysql server "abc123".
2. Create a database named "db1".
3. Migrate tables defined in the applications to MySQL server.
```bash
python manage.py makemigrations
python manage.py migrate
```
4. Add some records to the tables.
    * Enter shell environment
    ```bash
    python manage.py shell
    ```
    
    * Add Tag record
    ```python
    from blog.models import Category, Tag, Post
    import datetime
    c = Category(name='category test')
    c.save()
    t = Tag(name='tag test')
    t.save()
    p = Post(title="title test", body="body test", category=c, abstract="abstract test", create_time=datetime.datetime.now(), modified_time=datetime.datetime.now())
    p.save()
    p.tags.add(t)

    ```
5. Run server
```bash
python manage.py runserver
```

6. Open chrome and try to access the urls defined in the app. 
    For example, `http://127.0.0.1:8000/blogs`. 
    Then you can see your posts. 
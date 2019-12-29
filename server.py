from flask import Flask, render_template, request, redirect, escape, url_for, session, Response
import sqlite3
import pyzbar.pyzbar as pyzbar
import cv2
import numpy
obj=[]
app = Flask(__name__)
app.secret_key = 'swalla'

@app.route('/')
def hello_world():
    return render_template('signin.html')

def get_frame():
    global obj
    camera_port=0
    camera=cv2.VideoCapture(camera_port) #this makes a web cam object
    while True:
        retval, im = camera.read()
        imgencode=cv2.imencode('.jpg',im)[1]
        stringData=imgencode.tostring()
        obj=pyzbar.decode(im)
        if len(obj)!=0:
            print(obj)
            break
        else:
            yield (b'--frame\r\n'
                b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
    del(camera)
    
@app.route('/calc')
def calc():
    return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/signup')
def sign_up():
    return render_template('signup.html')

data_base = sqlite3.connect('products.sqlite')
cursor = data_base.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER,
        name TEXT,
        description TEXT,
        price INTEGER,
        offer INTEGER
    )
''')
sql = ("INSERT INTO products(id, name, description, price, offer) VALUES(?, ?, ?, ?, ?)")
val = (1, 'Onions', '''Onions belong to the Allium family of plants, which also includes chives, garlic, and leeks. These vegetables have characteristic pungent flavors and some medicinal properties. It is common knowledge that chopping onions causes watery eyes. However, onions may also provide potential health benefits. These may include reducing the risk of several types of cancer, improving mood, and maintaining skin and hair health.
''', 50, 100)
val1 = (2, 'Lemons', '''Lemons give flavor to baked goods, sauces, salad dressings, marinades, drinks, and desserts, and they are also a good source of vitamin C. One 58 gram (g) lemon can provide over 30 milligrams (mg) of vitamin C. Vitamin C is essential for health, and a deficiency can lead to health problems. The early explorers knew this and took lemons on their long voyages to help prevent or treat scurvy, a life threatening condition that was common among sailors''', 50, 100 )
val2 = (3, 'Cotton', '''Cotton, one of the world’s leading agricultural crops, is plentiful and economically produced, making cotton products relatively inexpensive. The fibres can be made into a wide variety of fabrics ranging from lightweight voiles and laces to heavy sailcloths and thick-piled velveteens, suitable for a great variety of wearing apparel, home furnishings, and industrial uses. Cotton fabrics can be extremely durable and resistant to abrasion. Cotton accepts many dyes, is usually washable, and can be ironed at relatively high temperatures. It is comfortable to wear because it absorbs and releases moisture quickly. When warmth is desired, it can be napped, a process giving the fabric a downy surface. ''', 50, 100 )
val3 = (4, 'Corn', '''Also known as maize (Zea mays), corn is one of the world’s most popular cereal grains. It’s the seed of a plant in the grass family, native to Central America but grown in countless varieties worldwide. Popcorn and sweet corn are popular varieties, but refined corn products are also widely consumed, frequently as ingredients in processed food. Whole-grain corn is as healthy as any cereal grain, as it’s rich in fiber and many vitamins, minerals, and antioxidants.''', 50, 100)
val4 = (5, 'Tomatoes', '''Tomato, (Solanum lycopersicum), flowering plant of the nightshade family (Solanaceae), cultivated extensively for its edible fruits. Labelled as a vegetable for nutritional purposes, tomatoes are a good source of vitamin C and the phytochemical lycopene. The fruits are commonly eaten raw in salads, served as a cooked vegetable, used as an ingredient of various prepared dishes, and pickled. Additionally, a large percentage of the world’s tomato crop is used for processing; products include canned tomatoes, tomato juice, ketchup, puree, paste, and “sun-dried” tomatoes or dehydrated pulp.''', 50, 100 )
val5 = (6, 'Potatoes', '''Potatoes are edible tubers, available worldwide and all year long. They are relatively cheap to grow, rich in nutrients, and they can make a delicious treat. The fiber, vitamins, minerals, and phytochemicals it provides can help ward off disease and benefit human health.''', 50, 100)
val6 = (7, 'Apples', '''As one of the most cultivated and consumed fruits in the world, apples are continuously being praised as a "miracle food". In fact, apples were ranked first in Medical News Today's featured article about the top 10 healthy foods. Apples are extremely rich in important antioxidants, flavanoids, and dietary fiber. The phytonutrients and antioxidants in apples may help reduce the risk of developing cancer, hypertension, diabetes, and heart disease.''', 50, 100)
val7 = (8, 'Mangoes', '''Mangoes are sweet, creamy fruits that have a range of possible health benefits. They are highly popular around the world. The mango is a member of the drupe family. This is a type of plant food with a fleshy outer section that surrounds a shell, or pit. This pit contains a seed. Olives, dates, and coconuts are also part of this family. There are many different kinds of mango. They vary in color, shape, flavor, and seed size. Although mango skin can be green, red, yellow, or orange, its inner flesh is mostly golden yellow.''', 50, 100)
val8 = (9, 'Grapes', '''The nutrients in grapes may help protect against cancer, eye problems, cardiovascular disease, and other health conditions. Resveratrol is a key nutrient in grapes that may offer health benefits. Grapes are a good source of fiber, potassium, and a range of vitamins and other minerals. Grapes are suitable for people with diabetes, as long as they are accounted for in the diet plan.''', 50, 100)
val9 = (10, 'Bananas', '''Bananas are rich in potassium and fiber. They may help prevent asthma, cancer, high blood pressure, diabetes, cardiovascular disease, and digestive problems. Ripen bananas at room temperature and add them to cereal for a tasty breakfast. People who use beta blockers should not suddenly increase their intake of bananas.''', 50, 100)
val10 = (11, 'Carrots', '''Carrots are rich in vitamins, minerals, and fiber. They are also a good source of antioxidants. Antioxidants are nutrients present in plant-based foods. They help the body remove free radicals, unstable molecules that can cause cell damage if too many accumulate in the body. Free radicals result from natural processes and environmental pressures. The body can eliminate many free radicals naturally, but dietary antioxidants can help, especially when the oxidant load is high''', 50, 100)
val11 = (12, 'Oranges', '''In addition to vitamin C, oranges contain fiber, potassium and choline, all of which are good for your heart. Potassium, an electrolyte mineral, is vital for the healthy functioning of the nervous system, and a lack of potassium can lead to arrhythmia (an irregular heartbeat), increased blood pressure and a depletion of calcium in bones.''', 50, 100)
cursor.execute(sql, val)
cursor.execute(sql, val1)
cursor.execute(sql, val2)
cursor.execute(sql, val3)
cursor.execute(sql, val4)
cursor.execute(sql, val5)
cursor.execute(sql, val6)
cursor.execute(sql, val7)
cursor.execute(sql, val8)
cursor.execute(sql, val9)
cursor.execute(sql, val10)
cursor.execute(sql, val11)
data_base.commit()
cursor.close()
data_base.close()

@app.route('/profileu', methods = ['GET', 'POST'])
def profileu():
    if request.method == 'POST':
        data = request.form.to_dict()
        if len(data) == 5:
            session['username'] = data['username']
            data_base = sqlite3.connect('users.sqlite')
            cursor = data_base.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    username TEXT,
                    email TEXT,
                    dob TEXT,
                    password TEXT
                )
            ''')
            sql = ("INSERT INTO users(username, email, dob, password) VALUES(? ,? ,?, ?)")
            val = (data['username'], data['email'], data['dob'], data['password'])
            cursor.execute(sql, val)
            data_base.commit()
            cursor.close()
            data_base.close()
            return render_template('profileu.html', data = data)
        session['username'] == data['username']
        data_base = sqlite3.connect('users.sqlite')
        cursor = data_base.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (session['username'], ))
        result = cursor.fetchone()
        if result is None:
            return render_template('signin.html')
        if data['password'] == result[3]:
            data = {'username': result[0], 'email': result[1], 'dob': result[2], 'password': result[3]}
            return render_template('profileu.html', data=data)
    data_base = sqlite3.connect('users.sqlite')
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (session['username'], ))    
    result = cursor.fetchone()
    data = {'username': result[0], 'email': result[1], 'dob': result[2], 'password': result[3]}
    return render_template('profileu.html', data= data)

@app.route('/profilef')
def profilef():
    global obj
    if(obj!=0):
        spl=str(obj[0].data).split('\\')
        name=spl[3][spl[3].index('nFN:')+4:]
        add=spl[6][spl[6].index('nADR')+7:]
        mob=spl[8][spl[8].index('CELL:')+5:]
        spl=add.split(';')
        dob=spl.pop()
        add=','.join(spl)
        data_base = sqlite3.connect('farmers.sqlite')
        cursor = data_base.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                name TEXT,
                dob TEXT,
                mob TEXT,
                address TEXT
            )
        ''')
        sql = ("INSERT INTO users(name, dob, mob, address) VALUES(? ,? ,?, ?)")
        val = (name, dob, mob, add)
        cursor.execute(sql, val)
        data_base.commit()
        cursor.close()
        data_base.close()
        data = [name, dob, mob, add]
        return render_template('profilef.html', data = data)
    return render_template('./farmerlog.html') 

def qr(obj):
    str(obj[0].data)


@app.route('/index', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()
        session['username'] = data['username']
        return render_template('index.html')
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('signin.html')


@app.route('/cart', methods = ['POST', 'GET'])
def cart():
    if request.method == 'POST':    
        data = request.form.to_dict()
        data_base = sqlite3.connect('products.sqlite')
        cursor = data_base.cursor()
        cursor.execute("SELECT * FROM products WHERE name = ?", (data['product'], ))
        result = cursor.fetchone()
        cursor.close()
        data_base.close()
        data_base = sqlite3.connect('carts.sqlite')
        cursor = data_base.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS carts(
                username TEXT,
                product TEXT,
                id INTEGER,
                quantity INTEGER,
                price INTEGER
            )
        ''')
        sql = ("INSERT INTO carts(username, product, id, quantity, price) VALUES(?, ?, ?, ?, ?)")
        val = (session['username'], result[1], result[0], data['quantity'], result[3])
        cursor.execute(sql, val)
        data_base.commit()
        cursor.close()
        data_base.close()
        data_base = sqlite3.connect('carts.sqlite')
        cursor = data_base.cursor()
        cursor.execute("SELECT * FROM carts WHERE username = ?", (session['username'], ))
        result = cursor.fetchall()
        cursor.close()
        data_base.close()
        data = result
        return render_template('/cart.html', data = data)
    data_base = sqlite3.connect('carts.sqlite')
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM carts WHERE username = ?", (session['username'], ))
    result = cursor.fetchall()
    cursor.close()
    data_base.close()
    data = result
    return render_template('/cart.html', data = data)


@app.route('/single-product')
def singlep():
    data = [11, 'Carrots', "These are orange vegetables", 50, 100]
    return render_template('single-product.html', data = data)

@app.route('/single-product1')
def singlet():
    data = [11, 'Carrots', "These are orange vegetables", 50, 100]
    return render_template('single-product1.html', data = data)

@app.route('/single-product-<int:id>') 
def single_product(id):
    data_base = sqlite3.connect('products.sqlite')
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (id, ))
    result = cursor.fetchone()
    values = [result[0], result[1], result[2], result[3], result[4]]
    return render_template('single-product.html', data= values)

@app.route('/single-product1-<int:id>') 
def single_product1(id):
    data_base = sqlite3.connect('products.sqlite')
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (id, ))
    result = cursor.fetchone()
    values = [result[0], result[1], result[2], result[3], result[4]]
    return render_template('single-product1.html', data= values)


@app.route('/checkout', methods = ["POST", "GET"])
def checkout():
    data_base = sqlite3.connect('carts.sqlite')
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM carts WHERE username = ?", (session['username'], ))
    result = cursor.fetchall()
    s =0
    for i in result:
        s += (int(i[3])*int(i[4]))
    data = [result, s]
    cursor.close()
    data_base.close()
    return render_template('/checkout.html', data= data)



@app.route('/<string:page_name>')
def render(page_name):
    return render_template(page_name)


 # filename: app.py
from aiohttp import web
import json


class User:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    async def withdraw(self, amount):
        self.balance = self.balance - amount

    async def deposit(self, amount):
        self.balance = self.balance + amount


new_user1 = User('Aman', 101010, 1000)


async def handle(request):
    response_obj = {'status': 'success'}
    return web.Response(text=json.dumps(response_obj))


async def check_balance(request):
    try:
        response_obj = (str(new_user1.acc_no) + " account of " +
                        new_user1.name + " has balance " + str(new_user1.balance))
        return web.Response(text=json.dumps(response_obj))
    except Exception as e:
        # Bad path where name is not set
        response_obj = {'status': 'failed', 'reason': str(e)}
        # return failed with a status code of 500 i.e. 'Server Error'
        return web.Response(text=json.dumps(response_obj), status=500)


async def withdraw_amount(request):
    try:
        amt = int(request.query['amt'])
        if(new_user1.balance > 0 and amt <= new_user1.balance):
            await new_user1.withdraw(amt)
            response_obj = ("Updated Balance " + str(new_user1.balance))
            return web.Response(text=json.dumps(response_obj))
        else:
            response_obj = {'status': 'failed', 'reason': 'Current Balance:'+str(
                new_user1.balance)+'  Your available balance is less then the amount you have entered'}
           # return failed with a status code of 500 i.e. 'Server Error'
            return web.Response(text=json.dumps(response_obj), status=500)
    except Exception as e:
        # Bad path where name is not set
        response_obj = {'status': 'failed', 'reason': str(e)}
        # return failed with a status code of 500 i.e. 'Server Error'
        return web.Response(text=json.dumps(response_obj), status=500)


async def deposit_amount(request):
    try:
        amt = int(request.query['amt'])
        if(amt>0):
            await new_user1.deposit(amt)
            response_obj = ("Updated Balance " + str(new_user1.balance))
            return web.Response(text=json.dumps(response_obj))
        else:
            response_obj = {'status': 'failed', 'reason': 'amount:'+str(
           amt)+' Amount to be deposited in positive numbers.'}
           # return failed with a status code of 500 i.e. 'Server Error'
            return web.Response(text=json.dumps(response_obj), status=500)    
        
    except Exception as e:
        # Bad path where name is not set
        response_obj = {'status': 'failed', 'reason': str(e)}
        # return failed with a status code of 500 i.e. 'Server Error'
        return web.Response(text=json.dumps(response_obj), status=500)


async def new_user(request):
    try:
        # happy path where name is set
        user = request.query['name']
        acc_no = request.query['acc_no']
        balance = int(request.query['balance'])
        if(balance > 0):
        # Process our new user or update the existing user if new created !  
            new_user1.name=user
            new_user1.acc_no=acc_no
            new_user1.balance=balance
            response_obj = (str(new_user1.acc_no) + " account of " +
            new_user1.name + " has balance " + str(new_user1.balance))
            return web.Response(text=json.dumps(response_obj))
        else:
            response_obj = {'status': 'failed', 'reason': 'Balance:'+str(
            balance)+'  Your Can Atleast have Zero account balance'}
           # return failed with a status code of 500 i.e. 'Server Error'
            return web.Response(text=json.dumps(response_obj), status=500)    
     
        print("Creating new user with name: ", user)
        response_obj = {'status': 'success'}
        # return a success json response with status code 200 i.e. 'OK'
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        # Bad path where name is not set
        response_obj = {'status': 'failed', 'reason': str(e)}
        # return failed with a status code of 500 i.e. 'Server Error'
        return web.Response(text=json.dumps(response_obj), status=500)


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/user/checkBalance', check_balance)
app.router.add_post('/user/withdraw', withdraw_amount)
app.router.add_put('/user/deposit', deposit_amount)
app.router.add_post('/user', new_user)

web.run_app(app)

import sys
import json
from random import uniform
from functools import wraps
from datetime import datetime

class Logs:
    def __init__(self, file_path):
        self.file_path = file_path
    def add_row(self, row):
        try:
            with open( self.file_path, "a" ) as file:
                file.write( row )
        except:
            print( "[logs] Something going bad" )
    def log(method):
        @wraps(method)
        def _impl(self, *method_args, **method_kwargs):
            output = method(self, *method_args, **method_kwargs)
            args_formated = " ".join( list(map(str, method_args)) )
            time = datetime.now().isoformat()
            self.logs.add_row( f"[{time}] {method.__name__} {args_formated}\n" )
            return output
        return _impl

class UserStory:
    def __init__(self):
        self.logs = Logs("log.txt")

        self.course = None
        self.UAH = None
        self.USD = None
        self.delta = None
        self.load_from_config()

    def load_from_config(self):
        try:
            with open("config.json", "r") as file:
                data = json.loads(file.read())
                self.course = data["current_data"]["course"]
                self.UAH = data["current_data"]["UAH"]
                self.USD = data["current_data"]["USD"]
                self.delta = data["current_data"]["delta"]
        except FileNotFoundError:
            print( "Check to see if the file" )

    @Logs.log
    def restart(self):
        try:
            data = None
            with open("config.json", "r") as file:
                data = json.loads(file.read())
            with open("config.json", "w") as file:
                data["current_data"]["course"] = data["default_data"]["course"]
                data["current_data"]["UAH"] = data["default_data"]["UAH"]
                data["current_data"]["USD"] = data["default_data"]["USD"]
                data["current_data"]["delta"] = data["default_data"]["delta"]
                file.write( json.dumps(data) )
        except FileNotFoundError:
            print( "Check to see if the file" )
        self.load_from_config()
    
    def save(self):
        try:
            data = None
            with open("config.json", "r") as file:
                data = json.loads(file.read())
            with open("config.json", "w") as file:
                data["current_data"]["course"] = self.course
                data["current_data"]["UAH"] = self.UAH
                data["current_data"]["USD"] = self.USD
                data["current_data"]["delta"] = self.delta
                file.write( json.dumps(data) )
        except FileNotFoundError:
            print( "Check to see if the file" )

    @Logs.log
    def rate(self):
        return round(self.course, 2)
    
    @Logs.log
    def available(self):
        return f"USD {self.USD} UAH {self.UAH}"
    
    @Logs.log
    def buy(self, count):
        if self.UAH < count*self.course:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {count*self.course}, AVAILABLE {self.UAH}")
            return
        
        self.UAH -= count*self.course
        self.USD += count
        self.save()
    
    @Logs.log
    def sell(self, count):
        if self.USD < count:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {count}, AVAILABLE {self.USD}")
            return
        
        self.UAH += count*self.course
        self.USD -= count
        self.save()
    
    @Logs.log
    def buy_all(self):
        self.buy( self.UAH )
        self.save()
    
    @Logs.log
    def sell_all(self):
        self.sell( self.USD )
        self.save()
    
    @Logs.log
    def next(self):
        self.course += uniform(-self.delta, self.delta)
        self.save()

def parse_args():
    us = UserStory()

    args = sys.argv[1:]
    if len(args) == 0:
        print( """Enter an action from the list: 
RATE
AVAILABLE
BUY XXX
SELL XXX
BUY ALL
SELL ALL
NEXT
RESTART: """ )

    if args[0] == "RATE":
        print(us.rate())
    elif args[0] == "AVAILABLE":
        print( us.available() )
    elif args[0] == "BUY":
        if len(args) == 2:
            if args[1] == "ALL":
                us.buy_all()
                return
            elif args[1].isdigit():
                us.buy( float(args[1]) )
                return
        print( "Invalid user input" )
    elif args[0] == "SELL":
        if len(args) == 2:
            if args[1] == "ALL":
                us.sell_all()
                return
            elif args[1].isdigit():
                us.sell( float(args[1]) )
                return
        print( "Invalid user input" )
    elif args[0] == "NEXT":
        us.next()
    elif args[0] == "RESTART":
        us.restart()

parse_args()
bar = {
    "ycj" : {"name" : "정영철", "age" : 20}, 
    "lny" : {"name" : "이나영", "age" : 30}
}

foo = [ d for d in bar.values() ]

print(foo)
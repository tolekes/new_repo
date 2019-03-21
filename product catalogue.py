products = {
    "books":{
        "spiritual":{
            "book1":"spiritual diet",
            "book2":"know thy God",
            "book3":"he is the way"
        },
        "fiction":{
            "fiction1":"gangster men",
            "fiction2":"men of war",
            "fiction3":"tight fist"
        },
        "scientific":{
            "sci1":"smooth galaxy",
            "sci2":"milky way",
            "sci3":"truth about the earth"
        }
    },
    "car":{ 
      "  toyota":{ "toy1":"corolla", "toy2":"matrix"  },
        "rover":{   "rov1":"landrover","rov2":"range rover"},
        "BMW":{   "B1": "XX5",   "B2":"XX6" }
    },
    "phone":{
        "Iphone":{},
        "samsung":{},
        "huawei":{}
    }

}
# print(products["books"]["fiction"]["fiction1"])
print(products.keys())

sale = input("what do you want to buy?")
sale2 = input("which type do you want to buy?")
print(products[sale][sale2])

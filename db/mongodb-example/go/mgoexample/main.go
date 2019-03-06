package main

import (
	// "fmt"

	"github.com/globalsign/mgo"
	// "github.com/globalsign/mgo/bson"
)

var TEST_DB_URI = "127.0.0.1:27017"

type User struct {
	// OId  bson.ObjectId `bson:"_id,omitempty"`
	Id   string `bson:"_id,omitempty"`
	Name string
}

func main() {
	session, err := mgo.Dial(TEST_DB_URI)
	if err != nil {
		panic(err)
	}

	defer session.Close()

	c := session.DB("test").C("user")

	id := "16318114"

	// err = c.Insert(&User{OId: bson.ObjectId(id), Id: id, Name: "sfgov"})
	// panic: ObjectIDs must be exactly 12 bytes long (got 8)

	err = c.Insert(&User{Id: id, Name: "sfgov"})

	// run multiple times
	// panic: E11000 duplicate key error collection: test.user index: _id_ dup key: { : "16318114" }
	
	if err != nil {
		panic(err)
	}
}

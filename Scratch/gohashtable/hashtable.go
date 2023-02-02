package main

import (
	"fmt"
)

/*

1. array[MAX_LEN]
2. struct node
3. func hash
4. func search
5. func insert
6. func delete
7. func printTable

*/

func main() {

	t := &table{}
	t.init()

	t.insert("James")
	t.insert("Jane")
	t.insert("Camille")
	t.insert("Bisi")
	t.insert("Steven")
	t.insert("Sayaka")
	t.insert("Sayaka")

	t.delete("Bisi")

	printTable(t)
}

// Max array length
const MAX_LEN int = 10


type table struct {
	array [MAX_LEN]*node
}

// This is a node from our linked list
type node struct {
	k *string
	next *node
}

// toString return string representation of linked list
func (n *node) toString() string {
	tmp := n
	s := ""
	for tmp != nil {
		s += *tmp.k + " - "
		tmp = tmp.next
	}
	return s
}


// initHashTable initializes a new array [MAX_LEN]*node
func (t *table) init() {
	for i:=0; i < MAX_LEN; i+=1 {
		t.array[i] = nil
	}
}

// hash will take a string key and return an array index *int
func hash(key string) int {
	sum := 0
	l := len(key)
	for i:=0; i < l; i+=1 {
		sum += int(key[i])
	}

	return (sum * l) % MAX_LEN
}

// insert a key into our table
func (t *table) insert(k string) bool {
	i := hash(k)

	if t.search(&k) {
		// Key already exists
		fmt.Println("Entry: ", k, "-- already exists")
		return false
	}

	fmt.Println("Entry: ", k)
	t.array[i] = &node{k: &k, next: t.array[i]}
	
	return true
}

// delete removes a key from the table
func (t *table) delete(k string) bool {
	i := hash(k)
	var tmp, prev *node = t.array[i], nil

	for tmp != nil && *tmp.k != k {
		prev = tmp
		tmp = tmp.next
	}

	if tmp == nil {
		return false
	}

	fmt.Println("Delete: ", k)
	if prev == nil {
		t.array[i] = tmp.next
	} else {
		prev.next = tmp.next
	}

	return true
}

// search for a key in the table
func (t *table) search(k *string) bool {
	i := hash(*k)
	tmp := t.array[i]
	for tmp != nil && *tmp.k != *k {
		tmp = tmp.next
	}

	return tmp != nil 
}

// printTable does exactly that
func printTable(t *table) {
	for i:=0; i<MAX_LEN; i+=1 {
		fmt.Println(i, ": ", t.array[i].toString())
	}
}
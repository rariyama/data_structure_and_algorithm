package main

import "fmt"

/*
//hachioji, katakura, hashomoto, sagamihara, yabe, fuchinobe, kobuchi, machida
*/

type Node struct {
	value interface{}
	prev  *Node
	next  *Node
}

type List struct {
	head *Node
	tail *Node
}

func (L *List) Insert(value interface{}) {
	list := &Node{
		next:  L.head,
		value: value,
	}
	if L.head != nil {
		L.head.prev = list
	}
	L.head = list

	l := L.head
	for l.next != nil {
		l = l.next
	}
	L.tail = l
}

func (l *List) Display() {
	list := l.head
	for list != nil {
		fmt.Printf("%+v ->", list.value)
		list = list.next
	}
	fmt.Println()
}

func main() {
	input := [...]map[string]int{
		{"insert": 5},
		{"insert": 2},
		{"insert": 3},
		{"insert": 1},
		{"insert": 6},
	}
	link := List{}
	for _, value := range input {
		for k, v := range value {
			if k == "insert" {
				link.Insert(v)
			}
		}
	}
	//	fmt.Printf("Head: %v\n", link.head.value)
	//	fmt.Printf("Head: %v\n", link.tail.value)
	link.Display()
}

//	for _, station := range stations {
//		cell := &Cell{station, nil}
//		insert(cell, ans)
//		fmt.Println(*ans)
//	}

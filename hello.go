package main

import "fmt"

func add(a int, b int) int {
    return a + b
}

func main() {
    fmt.Println("Welcome to the go world!")
    fmt.Println(add(2, 3))
}
package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	answers := []string{"Yes", "Nope"}
	fmt.Println(answers[rand.Intn(len(answers))])
}
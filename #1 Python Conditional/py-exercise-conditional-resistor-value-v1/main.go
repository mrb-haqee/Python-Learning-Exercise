package main

import (
	"fmt"
	"strconv"
)

func resistorValue(bandColor1, bandColor2, bandColor3, bandColor4 string) string {
	color := map[string]string{
		"black":  "0",
		"brown":  "1",
		"red":    "2",
		"orange": "3",
		"yellow": "4",
		"green":  "5",
		"blue":   "6",
		"violet": "7",
		"grey":   "8",
		"white":  "9",
	}
	significantFigure := ""
	for k, v := range color {
		for k2, v2 := range color {
			if bandColor1 == k && bandColor2 == k2 {
				significantFigure = v + v2
			}
		}
	}
	mult := 1
	for k := range color {
		if bandColor3 == k {
			num, _ := strconv.Atoi(significantFigure)
			// fmt.Println(num)
			mult *= num
			// fmt.Println(mult)
			break
		}
		mult *= 10
	}
	if bandColor4 == "black" {
		return fmt.Sprintf("%d ohm ±20%%", mult)
	} else if bandColor4 == "brown" {
		return fmt.Sprintf("%d ohm ±1%%", mult)
	} else if bandColor4 == "red" {
		return fmt.Sprintf("%d ohm ±2%%", mult)
	} else if bandColor4 == "gold" {
		return fmt.Sprintf("%d ohm ±5%%", mult)
	} else {
		return fmt.Sprintf("%d ohm ±10%%", mult)
	}
}

func main() {
	fmt.Println(resistorValue("black", "brown", "red", "gold"))
	fmt.Println(resistorValue("red", "red", "red", "gold"))
	fmt.Println(resistorValue("yellow", "violet", "green", "silver"))
	fmt.Println(resistorValue("blue", "grey", "green", "silver"))
}

package aoc.Util

import scala.io.Source

def readFile(day: Int): String =
    Source
        .fromFile(
          s"/home/donal/Documents/advent_of_code_2021/scala/src/main/input/Day$day.txt"
        )
        .mkString

def formatResultOutput(input: Any, day: Int, part: Int): String =
    s"Day $day part $part: $input"

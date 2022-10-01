import aoc.Day1

@main def main: Unit =
    // DAY 1
    val output = Day1.part1(Day1.readInput())
    println(formatResultOutput(output, 1, 1))

def formatResultOutput(input: Any, day: Int, part: Int): String =
    s"Day $day part $part: $input"

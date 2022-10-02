import aoc.Util
import aoc.Day1
import aoc.Day2

@main def main: Unit =
    // DAY 1
    val d1p1 = Day1.part1(Util.readFile(1))
    println(Util.formatResultOutput(d1p1, 1, 1))
    val d1p2 = Day1.part2(Util.readFile(1))
    println(Util.formatResultOutput(d1p2, 1, 2))
    // DAY 2
    val d2p1 = Day2.part1(Util.readFile(2))
    println(Util.formatResultOutput(d2p1, 2, 1))
    val d2p2 = Day2.part2(Util.readFile(2))
    println(Util.formatResultOutput(d2p2, 2, 2))

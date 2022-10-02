package aoc.Day1

def part1(input: String): Int =
    val inList = splitInput(input)
    var depth = 0
    for (first, second) <- inList zip inList.slice(1, inList.length)
    do if second > first then depth += 1
    depth

def part2(input: String): Int =
    val inList = splitInput(input)
    var depth = 0
    for i <- 0 to inList.length
    do
        val first = inList.slice(i, i + 2).sum
        val second = inList.slice(i + 1, i + 3).sum
        if second > first then depth += 1

    depth

    // alternative soln
    val sums = inList.sliding(3).map(_.sum)
    val depthPairs = sums.sliding(2).map(arr => (arr(0), arr(1)))
    depthPairs.count((prev, next) => prev < next)

def splitInput(input: String): List[Int] =
    val strList = input.split("\n").toList

    strList.map(_.toInt)

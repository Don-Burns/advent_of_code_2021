// For more information on writing tests, see
// https://scalameta.org/munit/docs/getting-started.html

import aoc.Day3
class TestDay3 extends munit.FunSuite {
    def createInput(): String =
        """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

    test("Day 3 binarySeqToInt") {
        val input = Seq(1, 0, 1, 1, 0)
        val output = Day3.binarySeqToInt(input)
        val expected = 22
        assertEquals(output, expected)
    }
    test("Day 3 part 1") {
        val input = createInput()

        val output = Day3.part1(input)
        val expected = 198
        assertEquals(output, expected)
    }

    test("Day 3 part 2") {
        val input = createInput()

        val output = Day3.part2(input)
        val expected = 230
        assertEquals(output, expected)
    }
}

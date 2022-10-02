// For more information on writing tests, see
// https://scalameta.org/munit/docs/getting-started.html

import aoc.Day2
class TestDay2 extends munit.FunSuite {
    def createInput(): String =
        """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

    test("Day 2 part 1") {
        val input = createInput()

        val output = Day2.part1(input)
        val expected = 150
        assertEquals(output, expected)
    }

    test("Day 2 part 2") {
        val input = createInput()

        val output = Day2.part2(input)
        val expected = 900
        assertEquals(output, expected)
    }
}

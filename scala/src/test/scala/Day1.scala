// For more information on writing tests, see
// https://scalameta.org/munit/docs/getting-started.html

import aoc.Day1
class TestDay1 extends munit.FunSuite {
    def createInput(): String =
        """199
200
208
210
200
207
240
269
260
263"""

    test("Day 1 part 1") {
        val input = createInput()

        val output = Day1.part1(input)
        val expected = 7
        assertEquals(output, expected)
    }
    test("Day 1 part 2") {
        val input = createInput()

        val output = Day1.part2(input)
        val expected = 5
        assertEquals(output, expected)
    }
}

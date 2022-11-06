package aoc.Day4

def part1(input: String): Int =
    1

def part2(input: String): Int =
    1

def parseInput(input: String): (List[Int], List[Board]) =

    val sections = input.split("\n\n").toList

    val pulledNumbers = sections(0).split(",").map(_.toInt).toList

    val boardDefs = sections.slice(1, sections.length)

    val boards = boardDefs.map(Board.parse(_))

    (pulledNumbers, boards)

case class Board(lines: List[List[Int]]):
    ???

object Board:
    def parse(boardString: String): Board =
        val lines = boardString.linesIterator.map(parseLine(_)).toList

        Board(lines)

    private def parseLine(boardLine: String): List[Int] =
        val seperator = raw" "
        boardLine.split(seperator).toList.map(_.toInt)

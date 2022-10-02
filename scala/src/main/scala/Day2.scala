package aoc.Day2

def part1(input: String): Int =
    val pos = Position()
    val instructions = parseInput(input)
    val forward = "forward"
    val down = "down"
    val up = "up"
    for i <- instructions
    do
        if i.direction == forward then pos.horizontal += i.magnitude
        if i.direction == down then pos.depth += i.magnitude
        if i.direction == up then pos.depth -= i.magnitude

    pos.depth * pos.horizontal

def part2(input: String): Int =
    val pos = Position()
    val instructions = parseInput(input)
    val forward = "forward"
    val down = "down"
    val up = "up"
    for i <- instructions
    do
        if i.direction == forward then
            pos.horizontal += i.magnitude
            pos.depth += pos.aim * i.magnitude
        if i.direction == down then pos.aim += i.magnitude
        if i.direction == up then pos.aim -= i.magnitude

    pos.depth * pos.horizontal

def parseInput(input: String): List[Instruction] =
    val strList = input.split("\n").toList
    // first attempt
    // val instructions = strList
    //     .map(_.split(" ").toList)
    //     .collect(
    //       _ match
    //           case List(dir, mag, _*) =>
    //               Instruction(dir, mag.toInt)
    //           case List(_ @rest) =>
    //               throw new Exception(s"value $rest not valid")
    //     )
    val instructions = strList.collect(_ match
        case s"$dir $mag" if mag.toIntOption.isDefined =>
            Instruction(dir, mag.toInt)
        case s"$dir $mag" if mag.toIntOption.isDefined == false =>
            throw new Exception(s"$mag is not coverible to int")
        case _ @v => throw new Exception(s"$v is not valid")
    )

    instructions

class Position():
    var depth = 0
    var horizontal = 0
    var aim = 0

class Instruction(dir: String, mag: Int):
    val direction = dir
    val magnitude = mag

package aoc.Day3

type BitLine = IndexedSeq[Int]
type BitSums = IndexedSeq[Int]
type MostCommonBits = IndexedSeq[Int]

def part1(input: String): Int =
    val lines = parseInput(input)
    val sumOfBits: IndexedSeq[Int] = lines.reduceLeft((prevSum, line) =>
        for (prevBitSum, bit) <- prevSum.zip(line)
        yield prevBitSum + bit
    )
    val lineCount = lines.length
    val mostCommonBits = getMostCommonBit(sumOfBits, lineCount)
    val gamma = getGammaRate(mostCommonBits)
    val epsilon = getEpsilonRate(mostCommonBits)

    gamma * epsilon

def part2(input: String): Int =
    1
def parseInput(input: String): List[BitLine] =
    input.linesIterator.map(parseBitLine(_)).toList

def getGammaRate(mostCommonBits: MostCommonBits): Int =
    binarySeqToInt(mostCommonBits)

def getEpsilonRate(mostCommonBits: MostCommonBits): Int =
    binarySeqToInt(mostCommonBits.map(_ - 1).map(_.abs))

def getMostCommonBit(bitSums: BitSums, lineCount: Int): MostCommonBits =
    val threshold = lineCount / 2
    bitSums.map(bit => if bit > threshold then 1 else 0)

def binarySeqToInt(seq: Seq[Int]): Int =
    Integer.parseInt(seq.mkString, 2)

def parseBitLine(line: String): BitLine =
    line.map(b => b.toInt - '0'.toInt)

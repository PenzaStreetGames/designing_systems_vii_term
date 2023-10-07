package task_3.logic

class Task26: Computable, ITask<Pair<Int, List<Int>>, Int> {
    override fun calculate(message: String): String {
        return try {
            val decodedMessage = decode(message)
            val result = _calculate(decodedMessage)
            encode(result)
        } catch (exception: AssertionError) {
            exception.message!!
        }
    }

    override fun decode(message: String): Pair<Int, List<Int>> {
        val numbers = message.split(" ").map { it.toInt() }
        assert(numbers.isNotEmpty()) {"You should type at least 1 number"}
        assert(numbers[0] < numbers.size) {"Requested more items than presented"}
        return Pair(numbers[0], numbers.slice(1..<numbers.size))
    }

    override fun encode(result: Int): String {
        return result.toString()
    }

    override fun _calculate(params: Pair<Int, List<Int>>): Int {
        return params.second.slice(0..<params.first).sum()
    }
}
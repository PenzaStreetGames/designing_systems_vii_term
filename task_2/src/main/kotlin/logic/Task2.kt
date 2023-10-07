package task_3.logic

class Task2: Computable, ITask<List<List<Int>>, List<Int>> {
    override fun calculate(message: String): String {
        return try {
            val decodedMessage = decode(message)
            val result = _calculate(decodedMessage)
            encode(result)
        } catch (exception: AssertionError) {
            exception.message!!
        }
    }

    override fun decode(message: String): List<List<Int>> {
        return message
            .split(";")
            .map {
                array -> array.split(" ")
                    .filter { it.isNotEmpty() }
                    .map { elem -> elem.toInt() }
            }
    }

    override fun encode(result: List<Int>): String {
        return result.joinToString(" ")
    }

    override fun _calculate(params: List<List<Int>>): List<Int> {
        assert(params.size == 3) {"You should pass 3 arrays delimited by ';'"}
        return params.map { it.sum() }
    }
}
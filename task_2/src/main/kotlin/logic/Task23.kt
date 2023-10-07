package task_3.logic

import kotlin.math.sqrt

class Task23: Computable, ITask<List<Int>, List<String>> {
    override fun calculate(message: String): String {
        return try {
            val decodedMessage = decode(message)
            val result = _calculate(decodedMessage)
            encode(result)
        } catch (exception: AssertionError) {
            exception.message!!
        }
    }

    override fun decode(message: String): List<Int> {
        return message.split(" ").map { it.toInt() }
    }

    override fun encode(result: List<String>): String {
        return result.joinToString { it }
    }

    override fun _calculate(params: List<Int>): List<String> {
        assert(params.size == 10) { "You should type 10 numbers" }
        return params.map { isSimple(it) }.map {if (it) "Prime" else "Not prime"}
    }

    private fun isSimple(number: Int): Boolean {
        if (number == 0 || number == 1)
            return false
        for (i in 2..sqrt(number.toDouble()).toInt()) {
            if (number % i == 0)
                return false
        }
        return true
    }
}
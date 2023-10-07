package task_3.logic

import kotlin.math.sin

class Task5: Computable, ITask<Pair<Double, Double>, Double> {
    override fun calculate(message: String): String {
        return try {
            val decodedMessage = decode(message)
            val result = _calculate(decodedMessage)
            encode(result)
        } catch (exception: AssertionError) {
            exception.message!!
        }
    }

    override fun decode(message: String): Pair<Double, Double> {
        val numbers = message.split(" ").map { it.toDouble() }
        assert(numbers.size == 2) {"You should pass 2 numbers"}
        return Pair(numbers[0], numbers[1])
    }

    override fun encode(result: Double): String {
        return result.toString()
    }

    override fun _calculate(params: Pair<Double, Double>): Double {
        val s = params.first
        val t = params.second
        return g(1.0, sin(s)) + 2 * g(t * s, 24.0) - g(5.0, -s)
    }

    private fun g(a: Double, b: Double): Double {
        return (2 * a + b * b) / (2 * a * b + 5 * b)
    }
}
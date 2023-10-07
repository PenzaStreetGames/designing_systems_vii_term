package task_3.logic

class Task29: Computable, ITask<Double, Double> {
    override fun calculate(message: String): String {
        return try {
            val decodedMessage = decode(message)
            val result = _calculate(decodedMessage)
            encode(result)
        } catch (exception: AssertionError) {
            exception.message!!
        }
    }

    override fun decode(message: String): Double {
        return message.toDouble()
    }

    override fun encode(result: Double): String {
        return result.toString()
    }

    override fun _calculate(params: Double): Double {
        assert(params >= 0) {"Weight should not be negative"}
        return params / 1000.0
    }
}
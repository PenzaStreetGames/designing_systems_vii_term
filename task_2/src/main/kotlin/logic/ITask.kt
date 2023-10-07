package task_3.logic

interface ITask<T, R> {
    fun decode(message: String): T
    fun _calculate(params: T): R
    fun encode(result: R): String
}
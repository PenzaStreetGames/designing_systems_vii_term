package task_3

import task_3.logic.*
import java.io.BufferedReader
import java.io.IOException
import java.io.InputStreamReader
import java.io.PrintWriter
import java.net.ServerSocket
import java.net.Socket
import java.util.*
import kotlin.collections.ArrayList
import kotlin.collections.HashMap
import kotlin.concurrent.timerTask

class Server(var port: Int) {
    private var serverSocket: ServerSocket? = null
    var messages: MutableList<String> = ArrayList()
    private var connections: MutableList<ClientHandler> = ArrayList()
    private var timer: Timer = Timer()

    fun start() {
        serverSocket = ServerSocket(port)
        timer.schedule(timerTask { sendMessages() }, 0, 5000)
        println("Server is ready")
        while (true) {
            val connection = ClientHandler(serverSocket!!.accept(), this)
            connections.add(connection)
            connection.start()
        }
    }

    fun sendMessages() {
        if (messages.isEmpty())
            return
        for (message in messages) {
            for (connection in connections) {
                connection.outStream?.println(message)
            }
        }
        messages.clear()
    }
}

class ClientHandler(var socket: Socket, var server: Server) : Thread() {
    val tasks: HashMap<String, Computable> = hashMapOf(
        Pair("23", Task23()), Pair("26", Task26()), Pair("29", Task29()),
        Pair("2", Task2()), Pair("5", Task5())
    )
    var outStream: PrintWriter? = null
    var inStream: BufferedReader? = null

    override fun run() {
        outStream = PrintWriter(socket.getOutputStream(), true)
        inStream = BufferedReader(InputStreamReader(socket.getInputStream()))
        try {
            var message: String = inStream!!.readLine()
            while (true) {
                println("Message $message from ${socket.remoteSocketAddress}")
                val parts = message.split(": ")
                val response = if (parts.isNotEmpty()) {
                    val taskNumber = parts[0]
                    if (tasks.contains(taskNumber)) {
                        val args = parts[1]
                        val result = tasks[taskNumber]?.calculate(args)
                        result!!
                    } else {
                        "Task with number $taskNumber not implemented"
                    }
                } else {
                    "You should send message in format 'task_number: args'"
                }
                server.messages.add("${socket.remoteSocketAddress}: $response")
                message = inStream!!.readLine()
            }
        } catch (e: IOException) {
            inStream?.close()
            outStream?.close()
            socket.close()
        }
    }
}

fun main() {
    val server = Server(8080)
    server.start()
}
package task_3

import java.io.BufferedReader
import java.io.IOException
import java.io.InputStreamReader
import java.io.PrintWriter
import java.net.Socket
import java.util.Scanner

class Client(var ip: String, var port: Int) {
    private var socket: Socket? = null
    private var outStream: PrintWriter? = null
    private var inStream: BufferedReader? = null

    fun connect() {
        try {
            socket = Socket(ip, port)
            outStream = socket?.getOutputStream()
                ?.let { PrintWriter(it, true) }
            inStream = socket?.getInputStream()
                ?.let { InputStreamReader(it) }
                ?.let { BufferedReader(it) }
            println("Client is ready")
            Thread { getMessages() }.start()
            sendMessages()
        } catch (e: IOException) {
            disconnect()
        }
    }

    fun disconnect() {
        try {
            inStream?.close()
            outStream?.close()
            socket?.close()
        } catch (e: IOException) {
            e.printStackTrace()
        }
    }

    fun sendMessages() {
        println("Enter messages:")
        val scanner = Scanner(System.`in`)
        while (true) {
            val message = scanner.nextLine()
            sendMessage(message)
        }
    }

    fun sendMessage(message: String) {
        outStream?.println(message)
    }

    fun getMessages() {
        var message: String
        while (true) {
            message = getMessage() ?: ""
            println(message)
        }
    }

    @Throws(IOException::class)
    fun getMessage(): String? {
        return inStream?.readLine()
    }
}

fun main() {
    val client = Client("localhost", 8080)
    client.connect()
}

package at.htlhl.MulServerClient;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class MulServer {
    public MulServer() throws IOException {

        //BIND the IP address and TCP port number 4711 and
        //LISTEN for incoming date on this address and port
        //(ip address/host is a local one per default)
        ServerSocket server = new ServerSocket(6969);

        while (true) {
            //ACCEPT an incoming client connection
            Socket client = server.accept();

            //prepare in and out streams for read and write
            InputStream in = client.getInputStream();
            OutputStream out = client.getOutputStream();

            //READ data (factors)
            int start = in.read();
            int end = in.read();

            int result = start * end;

            //WRITE data (result of multiplication
            out.write(result);

            //CLOSE the socket connection to the client
            client.close();
        }
    }

    public static void main(String[] args) {
        try {
            new MulServer();
        } catch (IOException e) {
            System.err.println("A problem with the server occurred: " +
                    e.getMessage());
        }

    }
}

# cs361-sorting-service
Created for CS 361 Software Engineering 1

Use ZeroMQ listening on port 5559

Store data in a txt file in this format:

data1
data2
data3
data4

Send the microservice these two things:
1. Name of txt file
2. Mode: 'asc" for ascending sort and "desc" for descending sort

Use this python boilerplate code to send this information to the microservice:

    # Create ZeroMQ context
    context = zmq.Context()

    # Create REQ (request) socket
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5559")

    # Send login request
    socket.send_json({
        "filename": filename,
        "mode": mode
    })

The microservice will return the sorted data in this format:

{
    "filename": "name.txt",
    "mode": "mode",
    "sorted_data": "data1\ndata2\ndata3\ndata4"
}

To recieve the index from the microservice use this boilerplate python:

    # Receive response
    response = socket.recv_json()

    # Get the data from the response
    sorted_data = response["sorted_data"]
    
    #If there is an error print it
    if "error" in response:
        print("Error:", response["error"])

UML Diagram:

<img width="762" height="402" alt="Microservice - sorting UML drawio" src="https://github.com/user-attachments/assets/01df2bbd-abb6-4d19-aa55-29b8e3915420" />

import zmq

def main():
    # Create ZeroMQ context
    context = zmq.Context()

    # Create REQ (request) socket
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5559")

    # ---- CHANGE THESE FOR TESTING ----
    filename = "test_file.txt" #Name of the test file
    mode = "desc"               #Either "asc" or "desc"
    # ----------------------------------

    # Send login request
    socket.send_json({
        "filename": filename,
        "mode": mode
    })

    #Proccess errors and print the sorted data
    response = socket.recv_json()
    if "error" in response:
        print("Error:", response["error"])
    else:
        print("Sorted data received:")
        print(response["sorted_data"])

if __name__ == "__main__":
    main()
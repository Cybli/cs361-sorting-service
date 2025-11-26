import zmq
import os

def sort_data(data_lines, mode):
    #Remove the spaces and new lines from the data
    data_lines = [line.strip() for line in data_lines if line.strip()]

    # Try to sort numbers
    try:
        numbers = [float(line) for line in data_lines]
        sorted_data = sorted(numbers, reverse=(mode == 'desc'))

    # There are letters so sort letters
    except ValueError:
        sorted_data = sorted(data_lines, reverse=(mode == 'desc'))

    return sorted_data

def main():
    #Create zmq context
    context = zmq.Context()
    #Create a socket at port 5556
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5559")

    print("Sorting microservice running on port 5556...", flush=True)

    while True:
        #Recieve the message
        msg = socket.recv_json()
        filename = msg.get("filename")
        mode = msg.get("mode", "asc")
        
        #Validate the filename
        if not filename or not os.path.isfile(filename):
            socket.send_json({"error": f"File '{filename}' not found."})
            continue
        
        #Open the file and read the lines
        with open(filename, "r") as file:
            data_lines = file.readlines()

        sorted_data = sort_data(data_lines, mode)

        #Create the response
        response = {
            "filename": filename,
            "mode": mode,
            "sorted_data": "\n".join(map(str, sorted_data))
        }

        #Send the response to the client
        socket.send_json(response)


if __name__ == "__main__":
    main()
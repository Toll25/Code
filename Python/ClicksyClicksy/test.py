import dpkt

number = 0
with open("capture.pcap", "rb") as pcap_file:
    pcap = dpkt.pcap.Reader(pcap_file)
    skip_next = False
    for ts, buf in pcap:
        decoded_buf = buf.decode('utf-8', errors='ignore')
        if "FAILED" in decoded_buf:
            print("haha failed")
            skip_next = True
        else:
            if skip_next:
                skip_next = False
            else:
                index = decoded_buf.find("/maze?direction=")
                if index != -1:
                    start_index = index + len("/maze?direction=")
                    end_index = decoded_buf.find(" ", start_index)
                    direction = decoded_buf[start_index:end_index]
                    print(direction)
                    number += 1
print(number)

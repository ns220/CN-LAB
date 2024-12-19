storage = 0

no_of_ticks = int(input("Enter the number of ticks for which the buckets will be filled: "))  
bucket_size = int(input("Enter the bucket size: ")) 
input_pkt_size = int(input("Enter the number of packets that are inflowed per second: ")) 
output_pkt_size = int(input("Enter the outflow rate: "))  

print("Total bucket size is", bucket_size)

for i in range(no_of_ticks):
    print("\nAt time", i + 1)
    size_left = bucket_size - storage
    if input_pkt_size <= size_left:
        storage += input_pkt_size
        print("No packet loss.")
    else:
        dropped = input_pkt_size - size_left
        print(f"Packet loss = {dropped}")
        storage = bucket_size 
    
    print(f"Total packets in bucket = {storage} and remaining bucket capacity = {bucket_size - storage}")
    
    if storage >= output_pkt_size:
        storage -= output_pkt_size
    else:
        storage = 0 
    
    print(f"Packets remaining in bucket after outflow = {storage}")

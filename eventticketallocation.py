STADIUM_SECTION = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0]

PRIORITIZED_REQUESTS = [
    (4, "LoyalFan_A"),  
    (3, "LoyalFan_B"),  
    (5, "NewFan_C")     
]

print("Original Seat Map (0=Available, 1=Taken):", STADIUM_SECTION)

for seats_needed, customer_id in PRIORITIZED_REQUESTS:
    
    print(f"\n--- Checking Request for {seats_needed} seats by {customer_id} ---")

    current_start_index = -1
    consecutive_count = 0
    block_found = False
    
    for i in range(len(STADIUM_SECTION)):
        if STADIUM_SECTION[i] == 0:
            if consecutive_count == 0:
                current_start_index = i
                
            consecutive_count += 1
            
            if consecutive_count == seats_needed:
                
                for j in range(current_start_index, i + 1):
                    STADIUM_SECTION[j] = 1
                    
                print(f"    SUCCESS: Marked seats from index {current_start_index} to {i} as TAKEN.")
                block_found = True
                break 

        else:
            consecutive_count = 0
            current_start_index = -1

    
    if block_found == False:
        print(f"    FAILURE: Could not find {seats_needed} seats next to each other.")

    print("Map after attempt:", STADIUM_SECTION)

print("\n--- Allocation Complete ---")
#!/usr/bin/python3
def canUnlockAll(boxes):
    # Set to keep track of unlocked boxes
    unlocked_boxes = set([0])
    # List to simulate stack of keys to process
    keys = [0]  # Start with the first box being open (index 0)
    
    # Process keys until we have no more keys left to use
    while keys:
        current_key = keys.pop()  # Get the current key (box index)
        
        # Loop through all keys in the current box
        for key in boxes[current_key]:
            # If the box corresponding to this key is not unlocked yet
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.add(key)  # Unlock this box
                keys.append(key)  # Add its keys to the list of keys to process
    
    # If we've unlocked all boxes, return True, else return False
    return len(unlocked_boxes) == len(boxes)

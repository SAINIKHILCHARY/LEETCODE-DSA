class Solution2:
    def maximumUnits(self, boxTypes, truckSize):
        # Initialize the maximum number of units the truck can carry.
        max_units = 0

        # Sort the box types by the number of units per box in a non-increasing order.
        boxTypes.sort(key=lambda x: -x[1])

        # Iterate through the box types.
        for number_of_boxes, units_per_box in boxTypes:
            # Calculate the number of boxes the truck can load
            # by comparing what's left of the truck's capacity with the available boxes.
            boxes_to_load = min(truckSize, number_of_boxes)

            # Increment the maximum units by the units from the loaded boxes.
            max_units += units_per_box * boxes_to_load

            # Decrease the truckSize by the number of boxes loaded.
            truckSize -= boxes_to_load

            # If the truck is full, break out of the loop.
            if truckSize <= 0:
                break

        # Return the total maximum units the truck can carry.
        return max_units
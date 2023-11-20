from collections import deque


def manipulate_deque():
    """
    Manipulate a deque data structure containing names of movie stars.

    This function:
    - Instantiates a deque with names of movie stars.
    - Inserts new names into the middle, front, and end of the deque.
    - Removes specific names from the original list.
    - Removes names from both the front and the rear of the deque.
    - Prints the deque's state after each major operation.

    Returns:
    None
    """

    ## Instantiate a deque with five given names of movie stars.
    movieStars = deque(["Robert Lopez", "John Legend", "Andrew Lloyd Webber", "Tim Rice", "Alan Menken"])
    print("Original deque:")
    print(movieStars)

    ## Insert new names
    # Insert "Rita Moreno" in the middle of the deque. The middle position is determined using floor division.
    middleInsert = len(movieStars) // 2
    movieStars.insert(middleInsert, "Rita Moreno")
    # Insert "Whoopi Goldberg" at the front of the deque.
    movieStars.appendleft("Whoopi Goldberg")
    # Insert "Mel Brooks" at the rear of the deque.
    movieStars.append("Mel Brooks")
    print("\nAfter inserting names:")
    print(movieStars)
    # Remove two specific names: "Tim Rice" and "Alan Menken"
    movieStars.remove("Tim Rice")
    movieStars.remove("Alan Menken")
    print("\nAfter removing two names:")
    print(movieStars)
    # Remove the first name (front) and the last name (rear) from the deque.
    movieStars.popleft()
    movieStars.pop()
    print("\nAfter removing front and rear entries:")
    print(movieStars)


def main():
    """
    Main function that drives the script.

    It invokes manipulate_deque() to showcase various operations that can be performed on a deque.

    Returns:
    None
    """
    manipulate_deque()


# Entry point of the script.
if __name__ == "__main__":
    main()
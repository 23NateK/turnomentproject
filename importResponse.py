def importResponse(responseFile):
    # import a competitor's response from a file
    response = []

    # open the file & store lines in a list
    with open(responseFile) as file:
        lines = [line.rstrip() for line in file] # get the lines from the file, strip the '\n' from the end, and store them in a list

    response.append(lines[0]) # append the name to the response

    for i in range(2, 13, 2): # loop through the lines with answers
        response.append([item.strip().upper() for item in lines[i].split(',')]) # split the lines at the commas, strip the leading/trailing spaces, and make the letters uppercase, then store in a list

    return response

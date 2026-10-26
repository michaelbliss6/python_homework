import traceback

try:
   with open('diary.txt', 'a') as file:
        prompt = "What happened today?"
    
        while True:
            line = input(prompt)
            if line == "done for now":
                break
            file.write(line + "\n")
            prompt = "What else?"

except Exception as e:
    print(f"An exception occurred. {type(e).__name__}")
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
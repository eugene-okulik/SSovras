program_resp = input()
new_ind = program_resp.index(':')
print(int(program_resp[new_ind+2:]) + 10)

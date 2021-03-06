import os
dirname = os.path.dirname(__file__)
if dirname:
  os.chdir(dirname)

def get_count(answers):
  if len(answers) == 0:
    return 0
  if len(answers) == 1:
    len(answers[0])
  return len(set(answers[0]).intersection(*[set(x) for x in answers[1:]]))

def run():
  with open('../data/prob06.txt') as f:
    curr_group = []
    sum = 0
    for line in f.readlines():
      line = line.strip()
      if line:
        curr_group.append(line)
      else:
        sum += get_count(curr_group)
        curr_group = []
    sum += get_count(curr_group)
  return sum

if __name__ == '__main__':
  print(run())

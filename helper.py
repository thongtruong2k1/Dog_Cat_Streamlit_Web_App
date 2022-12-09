def check_id_exist(data, id):
  for value in data:
    if value[0] == id:
      return True
  return False

def print_value(data, id):
  check = False
  result = None
  for value in data:
    if value[0] == id:
      result = value
      check = True
  if check == True:
    print(result)
  else:
    print(f"No id {id} in array")

def sort_data(data):
  for i in range(len(data)):
    for j in range(i,len(data)):
      if data[i][0]>data[j][0]:
        temp = data[i]
        data[i] = data[j]
        data[j] = temp
  return True

def get_id_last(data):
  return data[-1][0]

def add_data(value, data):
  """
    Thêm dữ liệu vào array:
    - Create: data[id, value]
    - array.append(data)
  """
  # data[id,value]
  if check_id_exist(data, value[0]) == True:
    print("Error: Id have exist!!")
    return False
  else:
    data.append(value)
    return True

def get_id_max(data):
  max = data[0][0]
  for value in data:
    if value[0] > max:
      max = value[0]
  return max

def remove(data, id):
  for value in data:
    if value[0] == id:
      index = data.index(value)
      data.pop(index)
  return True
def last_layer(datas)
  datas.each do |data|
    p "i find #{data} " if data == 1
  end
end

datas = [5, 2, 4, 3, 8, 1]

p last_layer(datas)

def last_layer_recursion(datas)
  round = 0
  last_layer_recursion_helper(datas, round)
end

def last_layer_recursion_helper(datas, round)
  len = datas.length

  return if round >= len
  
  # step 1 
  last_layer_recursion_helper(datas, round + 1)
end

def group_anagrams(strs)
  result = {}
  strs.each do |str|
    p str
    p sort_str = str.split(//).sort.join('')
    p '--'
    if result["#{sort_str}"]
      result["#{sort_str}"] << str
    else
      result["#{sort_str}"] = [str]
    end
  end
  p result.values.sort_by(&:length)
end

strs = %w[eat tea tan ate nat bat]

group_anagrams(strs)

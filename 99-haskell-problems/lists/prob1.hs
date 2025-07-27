main :: IO ()

myLast xs = last xs

main = do
	let res = myLast [1, 2, 3, 4]
	print res
	let res = myLast ['x', 'y', 'z']
	print res

main :: IO ()

myButLast xs = last (init xs)

main = do
	let res = myButLast [1,2,3,4]
	print res
	let res = myButLast ['a'..'z']
	print res
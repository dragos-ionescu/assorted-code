main :: IO ()

elementAt xs n = xs !! (n - 1)

main = do
	let res = elementAt [1, 2, 3] 2
	print res
	let res = elementAt "haskell" 5
	print res
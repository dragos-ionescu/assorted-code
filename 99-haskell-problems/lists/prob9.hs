main :: IO()

pack [x] = [x]
pack (x:xs)
    | x == (head xs) = [x, (head xs)] ++ (pack (tail xs))
    | otherwise = x: (pack xs)


main = do
    print "Hello"

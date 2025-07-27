main :: IO()

compress [x] = [x]
compress (x:xs)
    | x /= (head xs) = x: compress xs
    | otherwise = compress xs


main = do
    let res = compress "aaaaabcbabcbddbbc"   -- "abcbabcbdbc"
    print res
    let res = compress "aaaaabcbabcbddbb"    -- "abcbabcbdb"
    print res
    let res = compress "aaaaabcbabcbddb"     -- "abcbabcbdb"
    print res

    let res = compress [1, 2, 2, 3, 3, 0, 1, 0, 1, 1, 0, 0] -- [1, 2, 3, 0, 1, 0, 1, 0]
    print res


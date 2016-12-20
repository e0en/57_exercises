import System.IO
import Data.Maybe
import Data.List


putStrF s = do
    putStr s
    hFlush stdout

ask q f = do
    putStrF (q ++ " ")
    f

getInteger = do
    hSetEcho stdin False
    hSetBuffering stdin NoBuffering
    n <- getIntegerRec ""
    hSetEcho stdin True
    return n

getIntegerRec s = do
    c <- getChar
    if c == '\n' || (c >= '0' && c <= '9')
    then do
        putChar c
        hFlush stdout
        if c == '\n' then return s else getIntegerRec (s ++ [c])
    else getIntegerRec s

promptInteger q = do
    nStr <- ask q getInteger
    return (read nStr :: Integer)

promptList :: String -> [String] -> IO String
promptList q l = do
    putStrF (q ++ " ")
    s <- getLine
    if isJust $ find ((==) s) l
    then
        return s
    else do
        putStr "Wrong input, "
        promptList q l


addUnit v u = (show v) ++ " " ++ u

area x y = fromIntegral $ x * y

sqMeterPerSqFeet = 0.09290304 :: Float

sqFeetToSqMeter sqf = (fromInteger sqf) * sqMeterPerSqFeet

main = do
    u <- promptList "Choose your unit (feet/meters)" ["feet", "meters"]
    l <- promptInteger $ "What is the length of the room in " ++ u ++ "?"
    w <- promptInteger $ "What is the width of the room in " ++ u ++ "?"
    let a = area l w
    putStrLn $ "You entered dimensions of " ++ (addUnit l u) ++ " by " ++ (addUnit w u)
    putStrLn "The area is"
    putStrLn $ (show a) ++ " square " ++ u
    if u == "meter" then
        putStrLn $ (show $ a / sqMeterPerSqFeet) ++ " square feet"
    else
        putStrLn $ (show $ a * sqMeterPerSqFeet) ++ " square meters"

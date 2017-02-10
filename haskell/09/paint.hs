import System.IO
import Text.Regex.Posix

putStrF s = do
    putStr s
    hFlush stdout

ask q f = do
    putStrF (q ++ " ")
    f

numPattern = "^[-+]?[0-9]+\\.?[0-9]*$"

getNum = do
    hSetBuffering stdin NoBuffering
    n <- getIntegerRec ""
    return n

bottlesPerSqMeter = 9.0
calcPaintBottleCount area = ceiling $ (fromIntegral area) / bottlesPerSqMeter

getIntegerRec s = do
    c <- getChar
    if c == '\n' || (c >= '0' && c <= '9')
    then do
        putChar c
        hFlush stdout
        if c == '\n' then return s else getIntegerRec (s ++ [c])
    else getIntegerRec s

promptInteger q = do
    nStr <- ask q getNum
    return (read nStr :: Integer)

main = do
    putStrLn "Hello, world!"

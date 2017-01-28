import System.IO
import Data.Maybe
import Data.List

data Unit = Meter | Feet
data Length = Length Float Unit
data Area = Area Float Unit

instance Show Unit where
    show Meter = "meter"
    show Feet = "feet"

instance Show Length where
    show (Length v u) = (show v) ++ " " ++ (show u)

instance Show Area where
    show (Area v u) = (show v) ++ " square " ++ (show u)

feetSqInMeterSq = 0.09290304 :: Float

convertArea :: Area -> Unit -> Area
convertArea (Area v Feet) Meter = Area (v * feetSqInMeterSq) Meter
convertArea (Area v Meter) Feet = Area (v / feetSqInMeterSq) Feet
convertArea a u = a

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

promptUnit :: String -> IO Unit
promptUnit q = do
    putStrF (q ++ " ")
    s <- getLine
    case s of
      "meter" -> return Meter
      "feet" -> return Feet
      _ -> do
        putStr "Wrong input, "
        promptUnit q

main = do
    u <- promptUnit "Choose your unit (feet/meter)"
    w <- promptInteger $ "What is the width of the room in " ++ (show u) ++ "?"
    h <- promptInteger $ "What is the height of the room in " ++ (show u) ++ "?"
    let lw = Length (fromInteger w) u
    let lh = Length (fromInteger h) u
    putStrLn $ "You entered dimensions of " ++ (show lw) ++ " by " ++ (show lh)
    let area = Area (fromInteger $ w * h) u
    putStrLn $ "The area is " 
    putStrLn $ (show $ convertArea area Meter)
    putStrLn $ (show $ convertArea area Feet)

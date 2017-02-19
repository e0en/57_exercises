import System.IO
import Text.Regex.Posix

putStrF s = do
    putStr s
    hFlush stdout

ask q = do
    putStrF (q ++ " ")
    getLine

natNumPattern = "^[0-9]+$"

bottlesPerSqMeter = 9.0
calcPaintBottleCount area = ceiling $ (fromIntegral area) / bottlesPerSqMeter

promptPattern :: String -> String -> IO String
promptPattern q p = do
    nStr <- ask q
    if nStr =~ p :: Bool
    then
        return nStr
    else
        do
            putStrLn "Wrong input"
            promptPattern q p

promptNatNum q = do
    s <- promptPattern q natNumPattern
    return (read s :: Integer)

main = do
    w <- promptNatNum "Width of your room in meters?"
    h <- promptNatNum "Height of your room in meters?"
    let area = w * h
    let bottles = calcPaintBottleCount area
    putStrLn $ "You will need to purchase " ++ (show bottles) ++ " liters of"
    putStrLn $ "paint to cover " ++ (show area) ++ " square meters."

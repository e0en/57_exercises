import System.IO
import Text.Regex.Posix

putStrF s = do
    putStr s
    hFlush stdout

ask q = do
    putStrF (q ++ " ")
    getLine

numPattern = "^-?[0-9]+\\.?[0-9]*$"

bottlesPerSqMeter = 9.0
calcPaintBottleCount area = ceiling $ (fromIntegral area) / bottlesPerSqMeter

promptPattern :: String -> String -> IO String
promptPattern q p = do
    nStr <- ask q
    if nStr =~ p :: Bool
    then
        return nStr
    else
        promptPattern q p

main = do
    i <- promptPattern "Number!" numPattern
    putStrLn $ show (read i :: Int)

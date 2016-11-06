import System.IO
import Data.Time

promptInt q = do
    putStr $ q ++ " "
    hFlush stdout
    x <- getLine
    return (read x :: Int)

getThisYear = do
    t <- getCurrentTime
    let (y, _, _) = toGregorian $ utctDay t
    return $ fromInteger y

yearLeftMessage y = "You have " ++ (show y) ++ " years left until you can retire."
retireYearMessage y dy = "It's " ++ (show y) ++ ", so you can retire in " ++ (show $ y + dy) ++ "."

main = do
    currentAge <- promptInt "What is your current age?"
    retireAge <- promptInt "At what age would you like to retire?"
    let yearsLeft = retireAge - currentAge
    y <- getThisYear
    putStrLn $ yearLeftMessage yearsLeft
    putStrLn $ retireYearMessage y yearsLeft

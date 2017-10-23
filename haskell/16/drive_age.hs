import System.IO
import Text.RE.TDFA.String

putStrF s = do
    putStr s
    hFlush stdout

ask q = do
    putStrF (q ++ " ")
    str <- Prelude.getLine
    return str

promptPattern :: String -> RE -> IO String
promptPattern q p = do
    nStr <- ask q
    if matched $ nStr ?=~ p :: Bool
    then
        return nStr
    else
        do
            putStrLn "Wrong input"
            promptPattern q p

agePattern :: RE
agePattern = [re|^[0-9]+$|]

promptAge q = do
    s <- promptPattern q agePattern
    return (read s :: Integer)

main = do
    age <- promptAge "What is your age?"    
    putStrLn $ age

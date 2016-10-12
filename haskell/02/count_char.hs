import System.IO

prompt :: String -> IO String
prompt q = do
    putStr (q ++ " ")
    hFlush stdout
    getLine

messageFor :: String -> String

messageFor "" = "Please input something"
messageFor s = s ++ " has " ++ (show . length $ s) ++ " characters"

main :: IO ()
main = fmap messageFor (prompt "What is the input String?") >>= putStrLn

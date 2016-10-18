import System.IO

prompt :: String -> IO String
prompt q = do
    putStr (q ++ " ")
    hFlush stdout
    getLine

message :: String -> String -> String
message quote name = name ++ " says, \"" ++ quote ++ "\""

main :: IO ()
main = do
    quote <- prompt "What is the quote?"
    name <- prompt "Who said it?"
    putStrLn $ message quote name

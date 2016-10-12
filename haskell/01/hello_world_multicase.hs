import System.IO

prompt = do
  putStr "What is your name? "
  hFlush stdout
  getLine

messageFor :: String -> String
messageFor "Bob" = "Hello, Bob, glad to meet you!"
messageFor n = "Hello, " ++ n ++ ", nice to meet you!"

main = fmap messageFor prompt >>= putStrLn

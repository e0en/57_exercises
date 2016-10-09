import System.IO

prompt = do
  putStr "What is your name? "
  hFlush stdout
  getLine

messageFor name = "Hello, " ++ name ++ ", nice to meet you!"

main = do
  name <- prompt
  putStrLn $ messageFor name
